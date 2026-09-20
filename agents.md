# THE MAST — for AI agents

THE MAST is a guard that refuses dangerous commands by a **constitution your past
self sealed** — even commands from your own future self.

Read `llms.txt` for the full index. The core idea:

```
human writes constitution of red lines
  → THE MAST seals it on an immutable SHA-256 + ECDSA ledger
  → every tool call is gated against it
  → violation → Deny (pinned to evidence) / OK → guardian quorum when risky
```

**To integrate**: subclass/instantiate `ConstitutionGate` (a Strands
`InterventionHandler`), load your red lines, and attach `before_tool_call` to your
agent loop. The gate is deterministic/model-free — it runs anywhere with zero
credentials.

Start here: `constitution_gate.py`, `the_mast_agent.py`, `ARCHITECTURE.md`.
