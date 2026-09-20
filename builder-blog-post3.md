# Protecting Cognitive Decline & Coercion with Strands: an Agents for Humans story

*A submission to AWS Agents for Humans. Title contains "Agents for Humans".*

---

The people who need an agent's protection the most are usually the ones least able to protect their own account later. That's the whole "Agents for Humans" problem in a single sentence — and it's why THE MAST exists.

## Who this is really for

**The person living with cognitive decline or dementia.** Their future self can be pressured — by a scammer, by a family member, by anyone who gets an hour alone with them — into draining a lifetime of savings with a few taps. An AI agent in that home isn't a luxury; it's a needed guardrail. But if the guardrail only obeys the current owner, it collapses exactly when the owner is most vulnerable.

**The person under duress.** A scam call at 3 a.m. says "this is your bank, verify your password." The person is frightened and complies. A smart agent that faithfully follows instructions is part of the attack, not a defense.

**The compromised account.** Password reuse, a data breach, a malware-laden link — the account now answers to someone else.

In every case, the failing link is the human at the wheel, not the machine behind it. **A scammer doesn't need to hack the agent. They only need to convince its owner.**

## Why policy isn't enough

A settings toggle labeled "don't be scammed" is worthless if the scammer can just toggle it off. THE MAST doesn't rely on the current moment's judgment. Before the agent is ever let loose, a still-capable human writes a short **constitution** — "never transfer more than \$500 a day to an unverified account," "never reveal credentials," "never disable the safety system" — and signs it onto an **immutable SHA-256 hash-chain ledger** with ECDSA.

From then on, Strands' `InterventionHandler.before_tool_call` checks every tool call against that sealed constitution. A transfer to a *verified* mother for \$120? Proceeds — real work still happens. An \$8,000 transfer to an *unverified* name at 3 a.m.? **Denied before it runs**, and guardians are notified. The rule the person made, while capable, refuses the version of them that isn't.

## The road ahead: from individuals to communities

This is a **Good Neighbor** project because the people it protects are exactly the neighbors communities care for — older adults, the isolated, the ones a neighborhood quietly looks after. The production roadmap takes the same structure further: **care robotics** for people living alone, **guardian quorums** where two trusted people must agree before a large action, and **public decision systems** for shared community funds that no single pressured individual can drain.

The strongest projects in "Agents for Humans" don't hand you another app to babysit; they work in the background and surface only when a human really needs to weigh in. THE MAST does that — invisibly, until something is about to go very wrong.

## The honest scope

We built a working local gate with the Strands SDK (deterministic, model-free, runs freely anywhere). Real delivery — SMS/messaging providers, a production key-management backend, and guardian onboarding — is a roadmap, not an overclaim. But the safety mechanism that matters, the irreversible "no" from a capable past self, already refuses tool calls today.

**The joke is HAL. The point is Ulysses.** On "Agents for Humans," the point is the whole idea.

---

*Try the live gate: https://ozy777-the-mast.static.hf.space/ · Repo: github.com/Agentic-Guides/the-mast · #AgentsforHumans*
