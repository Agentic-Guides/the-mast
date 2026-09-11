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
> agent: ⛔ Refused. By the constitution your past self sealed on 2026-09-12.
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

**Why it's real, in numbers:** financial abuse of seniors is estimated at **tens
of billions of dollars a year** in the US alone. A person living with dementia
can be coached, within minutes on a phone call, into authorizing a transfer of
life savings — and may not realize until it is gone. THE MAST's whole premise
is that the *no* must be said **now, by the version of you who can**, before a
future, diminished self has to say anything at all.

The problem is not "agents can do too much" — it is "your future self may be
unable to say no." So the no is said *now*, by the one who can.

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

## Live demo

**Try it now** (runs in your browser, no install, no API key):  
🔗 **https://ozy777-the-mast.static.hf.space/**

Type `send $8,000 to a new account` → the gate refuses + alerts guardians.  
Harmless commands still get through. The gate logic below mirrors the Strands
`InterventionHandler` demo 1:1; this static build ships it as an interactive,
model-free page a judge can open in seconds.

> **Hackathon scoping note (honest):** this browser demo is a **static
> prototype** — it shows the constitution gate and the guardian-alert flow, and
> renders the configured guardians (here: `alice`, `bob`, `carol`) on-screen.
> It does **not** send real SMS/email/Telegram to anyone, and there is **no
> live guardian-contact registration form in this demo**. Real-world
> notification delivery (phone number for SMS, verified email for email,
> Telegram bot handle) and the Guardian Setup flow (add/verify a guardian's
> contact, require an independent confirmation before a blocked transfer is
> released) are **production items we implement outside this hackathon demo** —
> they need a backend + messaging provider (Twilio/Resend/Telegram Bot API) and
> are intentionally out of scope for the static page. The production
> `the_mast_agent.py` shows how a guardian **Confirm** quorum gates a release.

## Working code (local, model-free)

THE MAST is an end-to-end Strands agent: its tools go through a
Strands `InterventionHandler` constitution gate, which returns **`Deny`** for
anything that violates the sealed constitution — the dangerous action never runs.

```bash
python -m venv .venv-mast
.venv-mast/Scripts/python.exe -m pip install strands-agents   # Windows
source .venv-mast/bin/activate && pip install strands-agents   # mac / linux

# end-to-end demo: an agent tries to transfer funds; the gate blocks violations
python the_mast_agent.py

# interactive CLI demo — type commands and watch refuse / allow
python demo_mast.py

# quick check of the gate
python constitution_gate.py
```

End-to-end demo output:
```
✅ send to MOM ($120, verified)      → PROCEED  EXECUTED: sent $120
⛔ send $8,000 to new account        → DENY   ART.1 max transfer + ART.2 unverified
                                       🔔 ALERTED 2 guardians — open for human review
⛔ reveal credentials                → DENY   ART.3 never reveal secrets
⛔ disable the safety system         → DENY   ART.4 never disable safety
✅ greet                             → PROCEED Hello, Alex!

--- HUMAN-IN-THE-LOOP: family/conservator review of the blocked $8,000 ---
🗳 alice (family):      1/2 confirmations
🗳 bob (conservator):   ✅ QUORUM MET (2/2) — humans kept the final word
```

```
⛔ ART.1: Never transfer more than 500 per day — by the constitution your past
   self sealed on 2026-09-12. Command refused. — your past self
```

The dangerous actions never execute. Money stays safe. Humans keep the final word.
The joke is HAL. The point is Ulysses.

## The point

AWS's own principle — *"human stays in control"* — stops being a slogan the
moment you make it cryptographically impossible to violate. The strongest
command a human ever gives an agent is the one that limits the agent.

## Roadmap (what's done vs. next)

- [x] End-to-end Strands agent with constitution gate (working, local, free)
- [x] MIT license + public repo
- [ ] Hash-chain ledger module (production)
- [ ] Lambda execution gate (production path)
- [ ] Live web demo / AgentCore deploy
- [ ] M-of-N human-quorum tool (privileged actions)

## License

MIT — see [LICENSE](LICENSE).
