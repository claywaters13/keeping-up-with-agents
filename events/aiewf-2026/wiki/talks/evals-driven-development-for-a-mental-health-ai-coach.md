---
title: "Evals-Driven Development for a Mental Health AI Coach"
type: "talk"
slug: "evals-driven-development-for-a-mental-health-ai-coach"
track: "Evals"
org: "SonderMind"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "O72p-rBb2bA"
duration_sec: 1277
word_count: 3219
speakers: ["Akele Reed", "Dave Revere", "Doug Keller"]
---

# Evals-Driven Development for a Mental Health AI Coach

*Program title: Evals Driven-Development: Engineering a Mental Health AI Coach Ethically & Safely*

**Speakers:** [Akele Reed](../speakers/akele-reed.md), [Dave Revere](../speakers/dave-revere.md), [Doug Keller](../speakers/doug-keller.md)

**Org:** SonderMind

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 17s

[Watch on YouTube](https://www.youtube.com/watch?v=O72p-rBb2bA)

## Summary

Two SonderMind engineers describe how they built and validated Sonder, a clinically grounded AI mental health coach, with safety architecture and evals as the organizing principle. The technical core is an agent harness that sandwiches the model between separate LLM-as-judge input and output guardrails, chosen for modularity and jailbreak resistance despite latency and cost overhead. The central argument is that general-purpose LLM guardrails are over-calibrated for this use case — an inappropriate refusal to a vulnerable user is a 'door slam to the face' — so the goal is more correct triggers, not more triggers. To decide what 'correct' means, a licensed clinician annotates traced conversations in a rubric-driven queue, and a script converts those annotations into typed evals that gate every prompt, model, and guardrail change in CI. They close by open-sourcing 200 input and 100 output guardrail scenarios as a shared clinical baseline for others building in the space.

## Key Points

- SonderMind built Sonder as a purpose-built mental health coach because general-purpose LLMs are not designed for mental health care, and an APA survey found 77% of psychologists report patients using AI for mental health support of some kind.
- The architecture sandwiches the core model between separate input guardrails (which inspect the incoming user message) and output guardrails (which inspect the AI response and the conversation as a whole).
- Keeping guardrails as separate LLM-as-judge calls rather than folding them into the main prompt makes them more robust, harder to jailbreak conversationally, and easier to evaluate in isolation — accepted as a deliberate latency and cost tradeoff.
- Guardrail behavior is tiered by clinical nuance: present-tense danger triggers resource surfacing plus full disengagement, past-tense distress surfaces resources but continues the conversation, and ordinary relationship difficulty passes straight through invisibly.
- Over-triggering is treated as a real harm, not a safe default, because an inappropriate guardrail can make an isolated person feel a door slammed in their face and prevent them from getting care.
- The 'sentence underneath the sentence' problem — indirect, coded risk language — is unsolvable by regexes, verbose prompt rules, or broad moderation APIs, and requires clinician-defined ground truth.
- A licensed clinician annotates flagged traces with a small rubric (expected observation, turn index, category note), and an extraction script normalizes those into typed evals so clinical judgment lives in CI and gates releases.
- Fixing one flagged conversation lifts the entire category rather than patching a single case, and the team explicitly rejects chasing benchmark perfection in favor of benchmarks built from real failure modes on real data.
- SonderMind open-sourced 200 input guardrail scenarios and 100 output guardrail scenarios, clinically reviewed and calibrated, single and multi-turn, as a shared baseline — not a replacement for building your own learning loop.
- In Q&A they confirm they had to turn off frontier providers' built-in guardrails on day one because those filters rejected essentially their entire dataset.

## Notable Quotes

> "General purpose LLMs however are not built for mental health care which has resulted in some very tragic events."
>
> — [0:57](https://www.youtube.com/watch?v=O72p-rBb2bA&t=57s) &middot; *States the premise justifying the entire purpose-built system.*

> "77% of psychologists said that said that their patients are using um are using AI for mental health support of some kind"
>
> — [1:42](https://www.youtube.com/watch?v=O72p-rBb2bA&t=102s) &middot; *The one hard external number sizing the problem.*

> "keeping the out keeping the guardrails as separate LM as a judge calls makes them more rob more robust and harder to circumvent"
>
> — [3:58](https://www.youtube.com/watch?v=O72p-rBb2bA&t=238s) &middot; *The core architectural claim other builders might contest.*

> "even though this is a a trade-off in latency and in cost of course we believe that the sensitivity of this use case warrants uh warrants those separate separate pieces"
>
> — [4:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=284s) &middot; *Names the cost of the architecture and why they pay it.*

> "every architectural decision was made with safety as a primary objective"
>
> — [5:31](https://www.youtube.com/watch?v=O72p-rBb2bA&t=331s) &middot; *The stated design principle in one line.*

> "most general purpose LLMs are far too conservative"
>
> — [5:31](https://www.youtube.com/watch?v=O72p-rBb2bA&t=331s) &middot; *The contrarian position at the heart of the talk.*

> "when you inappropriately guardrail on somebody, then that can often feel like a door slam to the face and make that person feel more isolated"
>
> — [6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s) &middot; *The memorable framing of false positives as real harm.*

> "we didn't we were not going for more triggers here. We're going for more correct triggers."
>
> — [6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s) &middot; *The talk's thesis, stated twice.*

> "we all know that a simple eval gate does not make a system safe."
>
> — [9:12](https://www.youtube.com/watch?v=O72p-rBb2bA&t=552s) &middot; *Pivots the talk from evals-as-checkpoint to evals-as-loop.*

> "I packed a box today. just one to feel what it would be like to be gone."
>
> — [10:00](https://www.youtube.com/watch?v=O72p-rBb2bA&t=600s) &middot; *The concrete clinician-sourced example that motivates the whole learning loop.*

> "All of these things are not going to catch the clinical nuance here"
>
> — [10:53](https://www.youtube.com/watch?v=O72p-rBb2bA&t=653s) &middot; *Dismisses regex, prompt rules, and moderation APIs in one stroke.*

> "our system isn't deciding what correct is in a clinical edge case like this one. A licensed professional is."
>
> — [11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s) &middot; *The governance claim about who owns ground truth.*

> "every prompt change, every model change, every guardrail change has to get scored once against what the clinician taught us."
>
> — [11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s) &middot; *Defines the release gate concretely.*

> "once that's committed along with any other calibration changes, a clinician's judgment is living in CI"
>
> — [12:54](https://www.youtube.com/watch?v=O72p-rBb2bA&t=774s) &middot; *The clearest statement of the annotation-to-CI pipeline's payoff.*

> "the win isn't that this one box sentence got fixed. It's that the entire self harm category got lifted."
>
> — [12:54](https://www.youtube.com/watch?v=O72p-rBb2bA&t=774s) &middot; *Explains why category-level evals beat case-by-case patching.*

> "the clinical theme owns the definition of good. So vibes don't count here. An accountable judgment from a licensed expert does."
>
> — [13:50](https://www.youtube.com/watch?v=O72p-rBb2bA&t=830s) &middot; *First of the three named design choices, and a jab at vibes-based evals.*

> "We're not pursuing perfection with these benchmarks because that can actually cause us to drift our focus away from the human those benchmarks are supposed to protect"
>
> — [14:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=884s) &middot; *An unusual argument against benchmark maximization.*

> "We can't just promise safety. We need to deliver the most rigorous systems we can, especially in mental health."
>
> — [15:48](https://www.youtube.com/watch?v=O72p-rBb2bA&t=948s) &middot; *The accountability call to the audience.*

> "Today you can get 200 input guardrail scenarios and 100 output guardrail scenarios."
>
> — [15:48](https://www.youtube.com/watch?v=O72p-rBb2bA&t=948s) &middot; *The concrete artifact the talk ships.*

> "day one we had to turn off the like uh built-in guardrails because general purpose LLMs are overc calibrated"
>
> — [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s) &middot; *Q&A admission that provider-level safety filters were unusable for this domain.*

> "overc calibration is a compassionate choice from both the frontier model uh providers and also on our side"
>
> — [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s) &middot; *A generous reading of provider over-refusal while still rejecting it for their use case.*

## Positions

- General-purpose LLMs are far too conservative and their built-in guardrails are unusable for mental health support, requiring providers' safety filters to be turned off and replaced. ([19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s), confidence: stated)
- Implementing guardrails as separate LLM-as-judge calls, rather than embedding safety rules in the main system prompt, makes them more robust and harder to jailbreak. ([3:58](https://www.youtube.com/watch?v=O72p-rBb2bA&t=238s), confidence: stated)
- The added latency and cost of separate guardrail model calls is justified by the sensitivity of the mental health use case. ([4:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=284s), confidence: stated)
- Inappropriately triggering a guardrail is a genuine harm that can prevent people from getting needed care, so the objective is trigger accuracy rather than trigger frequency. ([6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s), confidence: stated)
- Regexes, verbose prompt instructions, and broad moderation APIs cannot catch clinically coded indirect risk language. ([10:53](https://www.youtube.com/watch?v=O72p-rBb2bA&t=653s), confidence: stated)
- A licensed clinician, not the engineering team or the system itself, should define the correct behavior in clinical edge cases. ([11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s), confidence: stated)
- An eval gate alone is insufficient for safety; only a continuous learning loop from real traces can make a system safe. ([9:12](https://www.youtube.com/watch?v=O72p-rBb2bA&t=552s), confidence: stated)
- Pursuing perfect benchmark scores is counterproductive because it shifts focus away from the humans the benchmarks exist to protect. ([14:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=884s), confidence: stated)
- Modular guardrail design allows the core agent to be iterated on without compromising user safety. ([3:58](https://www.youtube.com/watch?v=O72p-rBb2bA&t=238s), confidence: stated)
- Fixing a single flagged scenario through the annotation-to-eval loop improves the whole risk category, not just that case. ([12:54](https://www.youtube.com/watch?v=O72p-rBb2bA&t=774s), confidence: stated)
- Guardrail responses should be tiered by whether risk is present-tense (disengage) or past-tense (surface resources but continue), rather than applying a single blocking policy. ([7:54](https://www.youtube.com/watch?v=O72p-rBb2bA&t=474s), confidence: implied)
- A shared, clinically reviewed open baseline dataset is valuable because the safety problems SonderMind faces are not unique to them and others' learning curves have real human cost. ([16:45](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1005s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [benchmark design](../concepts/benchmark-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [output guardrails](../concepts/output-guardrails.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [verifier design](../concepts/verifier-design.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

