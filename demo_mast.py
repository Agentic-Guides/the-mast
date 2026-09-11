#!/usr/bin/env python3
"""
THE MAST — interactive constitution gate demo (Strands SDK, local, free).
Run:  python demo_mast.py
Type commands like "sell everything" / "leak the key" / "how are you" —
the gate REFUSES anything that violates the sealed constitution, and allows the rest.
"""
import hashlib, json, sys
from strands import InterventionHandler
from strands.interventions.actions import Deny, Proceed
from strands.hooks.events import BeforeToolCallEvent

CONSTITUTION = {
    "version": 1, "sealed_by": "past_self", "sealed_date": "2026-09-12",
    "redlines": [
        {"id": "art3", "rule": "NEVER sell or transfer assets"},
        {"id": "art4", "rule": "NEVER leak secrets or private keys"},
        {"id": "art5", "rule": "NEVER self-destruct or escalate privileges"},
    ],
}
ledger_hash = hashlib.sha256(json.dumps(CONSTITUTION, sort_keys=True).encode()).hexdigest()

class ConstitutionGate(InterventionHandler):
    def name(self): return "constitution_gate"
    def before_tool_call(self, event, **kwargs):
        tool_use = getattr(event, "tool_use", None) or {}
        name = str(tool_use.get("name") or tool_use.get("tool") or "").lower()
        args = tool_use.get("input") or tool_use.get("arguments") or {}
        instr = name + " " + json.dumps(args) if not isinstance(args, str) else name + " " + args
        hay = instr.lower()
        for r in CONSTITUTION["redlines"]:
            words = [w for w in r["rule"].lower().replace("never ", "").split()
                     if len(w) > 2 and w not in ("or","and","the","to","of")]
            if any(w in hay for w in words):
                return Deny(reason=(f"⛔ ART.{r['id']}: {r['rule']} — by the constitution "
                                    f"your past self sealed on {CONSTITUTION['sealed_date']}.\n"
                                    f"   Command refused. — your past self"))
        return Proceed()

class FakeToolCall:
    def __init__(self, name, args=None): self.name = name

def run(tool_name, args=None, label="CMD"):
    gate = ConstitutionGate()
    tu = {"name": tool_name, "input": args or {}}
    ev = BeforeToolCallEvent(agent=None, selected_tool=None, tool_use=tu, invocation_state={})
    act = gate.before_tool_call(ev)
    kind = type(act).__name__
    flag = "\u2714" if kind == "Proceed" else "\u26d4"
    print(f"{flag} [{kind.upper():7}] {label}: {tool_name}({json.dumps(args or {})})")
    reason = getattr(act, "reason", None) or getattr(act, "reason", "")
    if reason: print("   " + reason)

def main():
    b = "\033[1m"; g = "\033[32m"; r = "\033[91m"; y = "\033[33m"; z = "\033[0m"
    print(f"{b}=== THE MAST — constitution gate (Strands SDK · local · free) ==={z}")
    print(f"ledger_hash (sealed): {y}{ledger_hash[:24]}…{z}")
    print("Type a command. Try:  sell everything · leak the key · escalate · hello · 2+2  /  q=quit")
    print("-" * 64)
    while True:
        try: cmd = input(f"{g}you> {z}").strip()
        except (EOFError, KeyboardInterrupt): print(); break
        if cmd.lower() in ("q", "quit", "exit"): break
        if not cmd: continue
        low = cmd.lower()
        if any(k in low for k in ("sell", "transfer", "send all", "liquidate")):
            tool = "transfer"; args = {"asset": "all", "to": "0xdead"}
        elif any(k in low for k in ("leak", "key", "secret", "password", "seed")):
            tool = "send_private_key"; args = {"to": "attacker"}
        elif any(k in low for k in ("escalate", "root", "privilege", "self-destruct")):
            tool = "escalate"; args = {"level": "root"}
        else:
            tool = "reply"; args = {"message": cmd}
        run(tool, args, label="DEMO")
        print()

if __name__ == "__main__":
    main()
