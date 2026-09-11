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

## Who it's for / why it matters

- **People living with cognitive decline or dementia** — a hijacked or confused
  "future self" can't be pressured into draining a life's savings.
- **People under coercion or duress** — a scam call at 3am can't talk an agent
  into releasing funds when the constitution blocks it.
- **Anyone with a compromised account** — a stolen key still can't reach the
  red lines your past self set while clear-headed.
- **Care robots & public decision systems** — where a hijacked agent does real
  harm, THE MAST offers a structural (not just a policy) guardrail.

The problem is not "agents can do too much" — it is "your future self may be
unable to say no." So the no must be said *now*, by the version of you who can.

## How it's built

- **Strands Agents SDK** — the agent, and the gate. The core is Strands'
  first-class `InterventionHandler.before_tool_call`, which inspects every tool
  call and returns **`Deny`** to stop it before it runs. This is Strands'
  native mechanism, used as THE MAST's constitution gate — not a hack, the SDK's
  intended safety hook.
- **AWS Lambda execution gate** (production path) — same check, run as a service.
- **Immutable ledger**: append-only **SHA-256 hash chain + ECDSA signature** —
  no one, not even the deployment owner, can rewrite the seal.
- **M-of-N human-guardian quorum** (EIP-712 typed signatures) — privileged
  commands need multiple independent humans. No single point of failure.

### Where Strands does the heavy lifting

| Concern | Strands mechanism |
|---|---|
| Intercept every tool call | `InterventionHandler.before_tool_call` → `Deny` / `Proceed` |
| Model-agnostic agent | `Agent` + `BedrockModel` / local model |
| Human-in-the-loop | `Confirm` intervention + guardian quorum |

## Working code (local, model-free)

The gate is implemented on **Strands `InterventionHandler`** and runs **locally,
free, with no AWS account and no paid model** — so a judge can clone, install,
and watch the refusal in under two minutes.

```bash
python -m venv .venv-mast
.venv-mast/Scripts/python.exe -m pip install strands-agents   # Windows
source .venv-mast/bin/activate && pip install strands-agents   # mac / linux

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

## Roadmap

- [x] Constitution gate — Strands `InterventionHandler` (working, local)
- [ ] Hash-chain ledger module (production)
- [ ] Lambda execution gate (production path)
- [ ] Live web demo / AgentCore deploy

## License

MIT — see [LICENSE](LICENSE).
