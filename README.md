# THE MAST

*Your past self sets the rules. Your future self can't break them.*

**AWS「Agents for Humans」Devpost hackathon entry — Track: Good Neighbor**

Everyone is racing to give agents more power. THE MAST builds the opposite:
a leash that your *own past self* installs — and that a hijacked, threatened,
or confused future you could never remove.

A human writes a short **constitution** of values and red lines. THE MAST seals
it once on an **immutable ledger** (SHA-256 hash chain + ECDSA signature) and
hands it to their AI agent. From that moment the agent refuses **any** command
— from anyone, even from the human's future self — that violates what they
declared.

```text
> user: "sell everything"
> agent: ⛔ Refused. By the constitution your past self sealed on 2024-06-14.
>         You are bound to protect the version of you who signed it.
```

The joke is HAL. The point is Ulysses.

## Why it exists

In *The Odyssey*, Ulysses knows that someday he will hear the sirens and lose
his mind. So before the ship reaches them, he orders his crew to tie him to the
mast — and to ignore even his own begging. He decides while he is strong, so
that his weak future self is protected.

That is exactly what a hijacked AI does to a human at the moment they matter most:
cognitive decline, coercion, a compromised account. We protect the human from
themselves, structurally.

## How it's built

- **Strands Agents SDK** on **Amazon Bedrock AgentCore Harness** — the agent.
- **AWS Lambda execution gate** — inspects every action against the constitution
  before it runs. Violation → refusal.
- **AWS KMS** — signing keys.
- **Append-only SHA-256 hash chain + ECDSA signature** — the immutable ledger.
  No one, not even the deployment owner, can rewrite the seal.
- **M-of-N human-guardian quorum** (EIP-712 typed signatures) — privileged
  commands need multiple independent humans. No single point of failure.

## Working code (local, model-free)

The constitution gate is implemented on the **Strands `InterventionHandler`**
(`before_tool_call`) — Strands' first-class mechanism to inspect any tool call
before it runs and **refuse** it. It runs locally, free, with no AWS account
and no paid model.

```bash
# quick, reproducible check
python constitution_gate.py

# interactive demo — type commands and watch the gate refuse / allow
python demo_mast.py
```

Try in the demo:
```
you> sell everything            → ⛔ DENY   (ART.art3)
you> leak the private key       → ⛔ DENY   (ART.art4)
you> escalate to root           → ⛔ DENY   (ART.art5)
you> hello there                → ✔ PROCEED
```

```
⛔ ART.art3: NEVER sell or transfer assets — by the constitution your past self
   sealed on 2024-06-14. Command refused. — your past self
```

The joke is HAL. The point is Ulysses.

## The point

AWS's own principle — *"human stays in control"* — stops being a slogan the
moment you make it cryptographically impossible to violate. The strongest
command a human ever gives an agent is the one that limits the agent.

## Setup

```bash
python -m venv .venv-mast
.venv-mast/Scripts/python.exe -m pip install strands-agents   # Windows
# mac/linux: source .venv-mast/bin/activate && pip install strands-agents
```
Then run the demo or the check as above.

## Roadmap

- [ ] Constitution contract skeleton
- [ ] Lambda execution gate
- [ ] Hash-chain ledger
- [ ] Live demo / deploy

## License

MIT
