# THE MAST — builder.aws Blog Post (bonus +0.6, up to 3 posts × 0.2)

> **Rule requirement**: published publicly on builder.aws.com, and the TITLE must
> include "Agents for Humans".
> Bonus: up to 3 posts, 0.2 each, max +0.6 on Stage-2 score.

## Post 1 (primary) — title must contain "Agents for Humans"

**Title:** *THE MAST: Building "Agents for Humans" safety in — where the agent refuses, even you*

**Hook (first 2 lines):**
> Every hackathon entry asks "what more can the agent do?" We asked the opposite:
> "once the agent is powerful, how does the human who made it keep control — even
> from the human they may become?"

**Body outline (journey + build):**
1. **The problem**: agents getting powerful → hijacked/coerced/compromised future self
2. **Why blockchain**: a normal DB lets an admin quietly rewrite; only an immutable
   ledger (SHA-256 hash chain + ECDSA) makes "refuse forever" real.
3. **Why Strands**: InterventionHandler.before_tool_call IS the intended safety hook
   — not a hack. Return Deny before a tool runs.
4. **Build truth**: as a non-technical builder, shipping on AWS in a week was only
   possible side-by-side with an AI coding assistant — the literal "Agents for Humans".
5. **The demo**: "sell everything" → refused, by the constitution your past self sealed.
6. **Takeaway**: AWS's "human stays in control" stops being a slogan when it's
   cryptographically impossible to violate.

## Post 2 (optional, +0.2) — the Odyssey angle

**Title:** *Ulysses Was the First Agent-Safety Engineer: Agents for Humans and the Mast*

- The Odyssey → Odysean/Ulysses contract → precommitment devices → why designing
  the structure matters more than holding today's biggest key.

## Post 3 (optional, +0.2) — the Good Neighbor angle

**Title:** *Protecting Cognitive Decline & Coercion with Strands: an Agents for Humans story*

- Who it's for (dementia, coercion, compromised accounts), why a structural
  (not policy) guardrail matters, and the roadmap to care robots.

---

## Publishing notes
- Sign in at builder.aws.com (already created — handle `agenticguides`).
- Title MUST literally contain "Agents for Humans".
- Post publicly; Devpost bonus URLs go in the "optional bonus blog post" field.
- Keep each post ~600–900 words; be honest that this is a working local gate
  (design + code) with a production roadmap — do not overclaim full AWS deployment.
