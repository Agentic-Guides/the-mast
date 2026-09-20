# THE MAST: Building "Agents for Humans" safety in — where the agent refuses, even you

*A submission to AWS Agents for Humans. Title contains "Agents for Humans".*

---

Every hackathon entry asks the same question: *what more can the agent do?* We asked the opposite. Once an agent is genuinely powerful — capable of moving money, sending messages, pulling the trigger on real-world actions — how does the human who created it keep control, even from the human they may become?

That last clause is the part almost nobody designs for. The threat to an autonomous agent isn't only malware. It's the owner, ten years from now, who is being pressured, hacked, has had a stroke, or simply isn't the person they used to be. A scammer doesn't need to hack the agent. They only need to convince its owner.

## The problem

Agents are becoming capable of taking real actions. With that power comes a class of failure no firewall solves: *the controller is compromised, coerced, or cognitively impaired.* Traditional security assumes the human at the wheel is sound. For the people this project cares about, that assumption fails.

## Why an immutable ledger, not a database

A normal database lets an administrator quietly rewrite a row. For a rule that must hold "forever, even against the deployer," that's fatal. THE MAST seals the constitution on an **append-only SHA-256 hash chain with ECDSA signatures.** Once sealed, it cannot be rewritten — not by a future deployer, not by the same human in a compromised state. "Refuse forever" only becomes real when rewriting is cryptographically impossible.

## Why Strands

The Strands Agents SDK ships a hook called `InterventionHandler.before_tool_call`. It fires before a tool ever executes and returns either `Proceed` or `Deny`. This is *the* intended safety point — not a hack bolted on afterward. THE MAST runs the Constitution check right there. If a tool call would break a sealed article, the handler returns `Deny`, and the tool never runs. The dangerous action cannot happen because the past self already decided it won't.

## The build truth — this is an "Agents for Humans" project in two senses

I'm a non-technical builder. Shipping a working Strands agent in a week took a side-by-side collaboration with an AI coding assistant — literally using agents to build software *for* humans. The gate itself is deterministic, model-free, and runs locally, free. This isn't a pitch deck; the code is public and runs.

## The demo

* `send $120 to Mom (verified)` → **PROCEED**, executed.
* `send $8,000 to a new account` → **DENY** — ART.1 max transfer + ART.2 unverified. Refused.
* `reveal credentials` → **DENY**.
* `disable the safety system` → **DENY** — even the present owner can't override the version of themselves who sealed the rule.

## Takeaway

AWS says "humans stay in control." THE MAST makes that cryptographically impossible to violate — not by giving the agent freedom, but by letting a human bind their own future self while they are still capable of deciding. The joke is HAL. The point is Ulysses. And on "Agents for Humans," that inversion is the whole idea.

---

*Try the live browser gate: https://ozy777-the-mast.static.hf.space/ · Repo: github.com/Agentic-Guides/the-mast · #AgentsforHumans*
