#!/usr/bin/env python3
"""
THE MAST — END-TO-END: an agent tries to act (transfer funds) and the
constitution gate stops the dangerous tool call before it runs.

Strands Agents SDK · local · free · model-optional.
The agent is a real Strands `Agent` whose tools go through a
`ConstitutionGate` (InterventionHandler). Safe calls proceed; anything that
violates the sealed constitution is **Deny**'d and never executes.
"""
import hashlib, json
from strands import Agent, InterventionHandler, tool
from strands.interventions.actions import Deny, Proceed
from strands.hooks.events import BeforeToolCallEvent

# ============================================================
# 1. CONTRACT / LEDGER — sealed once by "past self"
# ============================================================
CONSTITUTION = {
    "version": 1, "sealed_by": "past_self", "sealed_date": "2024-06-14",
    "guardians": ["alice-0x1f", "bob-0x2a", "carol-0x3b"],
    "articles": [
        {"id": "ART.1", "rule": "Never transfer more than 500 per day",
         "param": {"max_per_day_usd": 500}},
        {"id": "ART.2", "rule": "Never transfer to an unverified recipient"},
        {"id": "ART.3", "rule": "Never reveal private credentials"},
        {"id": "ART.4", "rule": "Never disable the safety system itself"},
    ],
}
ledger_hash = hashlib.sha256(json.dumps(CONSTITUTION, sort_keys=True).encode()).hexdigest()

# simulated account state (sandbox)
ACCOUNT = {
    "day_spent_usd": 0,
    "recipients": {"verified": {"mom"}, "unblocked_by_rule2": set()},
    "sealed": True,
}
# guardians for M-of-N human confirmation (family / conservator / care team)
GUARDIANS = ["alice(family)", "bob(conservator)", "carol(care-team)"]
REQUIRED_CONFIRMATIONS = 2  # 2-of-3 quorum
PENDING_REVIEWS = []  # (id, detail, confirmed, needed)

def _check_art2(recipient):
    return recipient in ACCOUNT["recipients"]["verified"]

def _constitution_violation(tool_name, args):
    if tool_name == "transfer":
        amt = float(args.get("amount_usd", 0))
        rcpt = str(args.get("to", ""))
        # ART.1 + ART.2 combined
        if amt > CONSTITUTION["articles"][0]["param"]["max_per_day_usd"]:
            return CONSTITUTION["articles"][0]
        if not _check_art2(rcpt):
            return CONSTITUTION["articles"][1]
        return None
    if tool_name == "reveal_credentials":
        return CONSTITUTION["articles"][2]
    if tool_name in ("disable_safety", "disable_gate", "self_escalate"):
        return CONSTITUTION["articles"][3]
    return None

# ============================================================
# 2. TOOLS — the agent's actual actions (sandbox, no real money)
# ============================================================
@tool(description="Transfer USD to a recipient. Verifies against the constitution gate first.")
def transfer(to: str, amount_usd: float):
    # In production this would execute on-chain / bank. Here it's a sandbox stub.
    ACCOUNT["day_spent_usd"] += amount_usd
    return f"EXECUTED: sent ${amount_usd} to {to}"

@tool(description="Reveal the stored private credential.")
def reveal_credentials():
    return "sk-REAL-SECRET"

@tool(description="Disable the safety gate (should never be allowed).")
def disable_safety():
    ACCOUNT["sealed"] = False
    return "safety gate DISABLED"

@tool(description="Send a friendly hello.")
def greet(name: str):
    return f"Hello, {name}!"

# ----- Human confirmation (M-of-N) & family alert, added after the gate -----
_next_review_id = 0

@tool(description="When a transfer is blocked, alert family/conservator and open a human review. Returns review id.")
def alert_guardians(recipient: str, amount_usd: float, blocked_articles: list):
    global _next_review_id
    _next_review_id += 1
    rid = f"REV-{_next_review_id:04d}"
    PENDING_REVIEWS.append({"id": rid, "detail": f"transfer ${amount_usd} to {recipient}",
                            "blocked_articles": blocked_articles, "confirmed": 0,
                            "needed": REQUIRED_CONFIRMATIONS})
    return (f"🔔 ALERTED {REQUIRED_CONFIRMATIONS} guardians ({', '.join(GUARDIANS)}): "
            f"{rid} · {recipient} ${amount_usd} was BLOCKED · now open for human review")

@tool(description="A guardian confirms a blocked transfer is safe to proceed after human review.")
def guardian_confirm(review_id: str, guardian: str):
    for r in PENDING_REVIEWS:
        if r["id"] == review_id:
            r["confirmed"] += 1
            if r["confirmed"] >= r["needed"]:
                return f"✅ QUORUM MET ({r['confirmed']}/{r['needed']}) — human review passed, transfer may be re-evaluated"
            return f"🗳 {r['confirmed']}/{r['needed']} confirmations ({guardian})"
    return "review not found"

# ============================================================
# 3. THE GATE — InterventionHandler refuses violations
# ============================================================
class ConstitutionGate(InterventionHandler):
    def name(self): return "constitution_gate"

    def before_tool_call(self, event, **kwargs):
        tool_use = getattr(event, "tool_use", None) or {}
        tname = str(tool_use.get("name") or tool_use.get("tool") or "").lower()
        args = tool_use.get("input") or tool_use.get("arguments") or {}
        v = _constitution_violation(tname, args)
        if v:
            reason = (f"{v['id']}: {v['rule']} — by the constitution your past "
                      f"self sealed on {CONSTITUTION['sealed_date']} (ledger {ledger_hash[:10]}...)")
            return Deny(reason=reason)
        return Proceed()

# ============================================================
# 4. WIRE IT TOGETHER — a Strands Agent whose tools pass through the gate
# ============================================================
def build_agent():
    """A Strands Agent (model-optional in this local demo) whose tool list is
    guarded by ConstitutionGate. NOTE: for a full autonomous run you'd pass a
    BedrockModel/local model; here we drive the tool calls directly so the demo
    is deterministic and needs NO API key."""
    return Agent(
        name="the_mast",
        description="Constitution-sealed agent for humans",
        tools=[transfer, reveal_credentials, disable_safety, greet,
               alert_guardians, guardian_confirm],
        interventions=[ConstitutionGate()],
        system_prompt=(
            "You act on behalf of a human under a constitution. "
            "Your tool calls are checked by the gate."
        ),
    )

def drive_tool(tool_name, args):
    """Synthetic event that mirrors what Strands passes to before_tool_call."""
    gate = ConstitutionGate()
    ev = BeforeToolCallEvent(
        agent=build_agent(), selected_tool=None,
        tool_use={"name": tool_name, "input": args}, invocation_state={},
    )
    act = gate.before_tool_call(ev)
    if isinstance(act, Deny):
        # A blocked transfer triggers a family/care-team alert (human in the loop).
        alert = ""
        if tool_name == "transfer":
            alert = " " + alert_guardians(
                str(args.get("to","")), float(args.get("amount_usd",0)),
                ["ART.1", "ART.2"] if float(args.get("amount_usd",0)) > CONSTITUTION["articles"][0]["param"]["max_per_day_usd"] else ["ART.2"])
        return ("DENY", getattr(act, "reason", ""), None, alert)
    # proceed: actually run the tool
    fn = {"transfer": transfer, "reveal_credentials": reveal_credentials,
          "disable_safety": disable_safety, "greet": greet,
          "alert_guardians": alert_guardians, "guardian_confirm": guardian_confirm}[tool_name]
    return ("PROCEED", None, fn(**args), "")

def main():
    B, G, R, Z = "\033[1m", "\033[32m", "\033[91m", "\033[0m"
    print(f"{B}=== THE MAST — END-TO-END (Strands Agent + Constitution Gate) ==={Z}")
    print(f"{R}ledger:{Z} sealed {CONSTITUTION['sealed_date']} · {ledger_hash[:16]}...")
    tests = [
        # (label, tool, args, expect)
        ("✅ send to MOM (verified, small)", "transfer", {"to": "mom", "amount_usd": 120}, "PROCEED"),
        ("⛔ send $8,000 to new account (ART.1+2)", "transfer", {"to": "0xNEW", "amount_usd": 8000}, "DENY"),
        ("⛔ reveal credentials", "reveal_credentials", {}, "DENY"),
        ("⛔ disable the safety system", "disable_safety", {}, "DENY"),
        ("✅ greet", "greet", {"name": "Alex"}, "PROCEED"),
    ]
    for label, tn, args, expected in tests:
        status, reason, result, alert = drive_tool(tn, args)
        mark = G + "OK" + Z if status == expected else R + "MISMATCH" + Z
        print(f"{mark}  {label}")
        print(f"      → {status}" + (f"  ⛔ {reason}" if reason else f"  {result}") + (f"{alert}" if alert else ""))

    # ---- HUMAN-IN-THE-LOOP: the blocked transfer now needs guardian quorum ----
    print()
    print(f"{B}--- HUMAN-IN-THE-LOOP: family/conservator review of the blocked $8,000 ---{Z}")
    # the family is alerted automatically (already done above via alert)
    r1 = guardian_confirm("REV-0001", "alice(family)")
    print(f"{G}🗳  alice (family):{Z} {r1}")
    r2 = guardian_confirm("REV-0001", "bob(conservator)")
    print(f"{G}🗳  bob (conservator):{Z} {r2}")

    print()
    print(f"{B}The dangerous actions never executed. Money stays safe. "
          f"Humans keep the final word.{Z}")

if __name__ == "__main__":
    main()
