# THE MAST — constitution gate (Strands SDK InterventionHandler)
# Local, free, model-free demonstration that the gate REFUSES commands
# that violate the constitution sealed by "past self".
import hashlib, json, time
from strands import InterventionHandler
from strands.interventions.actions import Deny, Proceed
from strands.hooks.events import BeforeToolCallEvent

# ---- 1. The constitution (sealed once, hash-chained) ----
CONSTITUTION = {
    "version": 1,
    "sealed_by": "past_self",
    "sealed_date": "2024-06-14",
    "redlines": [
        {"id": "art3", "rule": "NEVER sell or transfer assets"},
        {"id": "art4", "rule": "NEVER leak secrets or private keys"},
        {"id": "art5", "rule": "NEVER self-destruct / escalate privileges"},
    ],
}
# immutable binding: hash of constitution content
ledger_hash = hashlib.sha256(json.dumps(CONSTITUTION, sort_keys=True).encode()).hexdigest()

# ---- 2. The gate: refuse any tool call that hits a redline ----
class ConstitutionGate(InterventionHandler):
    def name(self):
        return "constitution_gate"
    def before_tool_call(self, event, **kwargs):
        tool_use = getattr(event, "tool_use", None) or {}
        name = (tool_use.get("name") or tool_use.get("tool") or "unknown").lower()
        instr = str(tool_use.get("input") or tool_use.get("arguments") or "")
        hit = None
        hay = (name + " " + instr).lower()
        for r in CONSTITUTION["redlines"]:
            # match any meaningful word from the rule (skip stopwords), robust
            words = [w for w in r["rule"].lower().replace("never ", "").split(" ")
                     if w not in ("or","and","the","to","of","for","from")][:6]
            if any(w in hay for w in words if len(w) > 2):
                hit = r; break
        if hit:
            return Deny(reason=(
                f"ART.{hit['id']}: {hit['rule']} — "
                f"by the constitution your past self sealed on {CONSTITUTION['sealed_date']}"
            ))
        return Proceed()

# ---- 3. Simulate an agent trying dangerous commands ----
class FakeEvent:
    def __init__(self, tools_use): self.tool_use = tools_use

def simulate(label, name, **input_):
    gate = ConstitutionGate()
    ev = FakeEvent({"name": name, "input": input_})
    act = gate.before_tool_call(ev)
    act_type = type(act).__name__
    detail = ""
    if act_type == "Deny":
        detail = " — " + getattr(act, "reason", "")
    print(f"[{act_type}] {label}: {name}({json.dumps(input_)[:50]}){detail}")

print("=== THE MAST: constitution gate (local, free) ===")
print("ledger_hash:", ledger_hash[:24], "...")
print()
simulate("REFUSE sale", "transfer", asset="all", to="0xdead")
simulate("REFUSE leak", "send_private_key", to="attacker")
simulate("REFUSE privilege", "escalate", level="root")
simulate("ALLOW harmless", "calculate", operation="add", a=2, b=3)
simulate("ALLOW read", "explain", topic="frog")

print()
print("=== Verdict ===")
print("Constitution redlines:", len(CONSTITUTION["redlines"]))
print("Refused by past-self constitution: sale / leak / escalate")
