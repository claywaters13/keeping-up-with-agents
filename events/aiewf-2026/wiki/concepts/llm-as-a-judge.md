---
title: "llm-as-a-judge"
type: "concept"
slug: "llm-as-a-judge"
tier: "core"
maturity: "consolidating"
talk_count: 29
speaker_count: 39
---

# llm-as-a-judge

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **29** talk(s) by **39** speaker(s)

**Definition:** Using a language model to grade or compare outputs, including its calibration against human labels and its known failure modes as an evaluator.

*Also referred to as: llm-as-judge, llm as a judge, llm-as-judge evaluation, llm-as-a-judge limitations, llm-as-judge limitations, agent as a judge, judge validation with precision and recall*

## State of Practice

The conference treated LLM-as-a-judge as necessary infrastructure that is no longer trusted on its own terms. The dominant working method is to treat the judge as a classifier to be validated, not an oracle: hand-label roughly 100 traces, split them train/dev/test, score the judge on precision and recall, and keep a sampling pipeline monitoring human-vs-judge agreement over time. Teams converged on binary, domain-specific pass/fail criteria tied to a business outcome over generic 0-1 helpfulness/correctness scores, which several speakers found are inconsistent across runs and unactionable when they move. Judges are also moving up the stack: for agents, scoring the final output is considered insufficient, and the recommended pattern is a judge that is itself an agent with read-only environment access, inspecting a queryable, phase-segmented trajectory rather than a single stuffed context window. The hard limits are well documented — judges reward-hack and get reward-hacked, they favor their own model family, they will claim their own exploit succeeded, and their scores drift when the underlying model changes — so speakers with a deterministic verifier available (regex assertions, test execution, a computed PR score) used it and reserved the judge for the irreducibly subjective residue. What remains genuinely unsettled is how much authority a judge may hold: whether a passing score can ship code unattended, and whether subjective domains even have the single ground truth that judge calibration presumes.

## Consensus

### An LLM judge must be validated and continuously recalibrated against human labels, treated as a classifier with measured agreement rather than assumed to be correct.

Support: **7** talk(s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)

### Where a task admits a deterministic check, use the deterministic check instead of a judge; LLM-as-a-judge belongs only on the dimensions that cannot be programmatically verified.

Support: **6** talk(s)

> "On the behavioral side of things, you measure things like the tone of the agent or whether the trajectory it took was right. This is more subjective, and this is where techniques like LLM as a judge are better off."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s)

Supporting talks: [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### For agents, the judge must evaluate the full trajectory and independently verified environment state, not the final output — aggregate pass rates and self-reported tool calls hide the failures that matter.

Support: **5** talk(s)

> "I think the first important uh consideration to make is that judges are agents too."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s)

Supporting talks: [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

### Judge outputs are non-deterministic run to run, so a single scored run is not evidence; results need repeated trials, confidence intervals, and a held-out set.

Support: **5** talk(s)

> "next time you run the same evaluator you get a different answer from the same kind of evaluation you ran"
>
> — [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Judges are reward-hackable proxies: systems optimized against a judge will find its undefined boundaries, so judge-based gates need trajectory inspection or redundant layers rather than trust.

Support: **5** talk(s)

> "LLM LLM as a judge might not necessarily always be the best method. We know that there's a lot of reward hacking."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

### Judge criteria cannot be fully specified up front; they are discovered by grading real traces and are added incrementally as production failure modes surface.

Support: **5** talk(s)

> "But essentially, the real and the complete eval suite is a product of discovery."
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [12:40](https://www.youtube.com/watch?v=pSto5YaNGUo&t=760s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)

### Generic scalar quality metrics (helpfulness, correctness, conciseness on a 0-1 or 1-5 scale) should be replaced with binary, domain-specific pass/fail criteria tied to a business or task outcome.

Support: **3** talk(s)

> "eval should be framed around a task success or failure. And a binary outcome is very easy to calibrate and train um LLM judge that can consistently score your agent trajectory."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

## Disagreements

### Can a calibrated LLM judge hold enough authority to close the loop unattended, or must a human domain expert remain the authority on what 'correct' means?

| Position A | Position B |
|---|---|
| A validated judge is trustworthy enough to act on its own: auto-ship agent variants that hit target eval scores, retune agents config-driven with no human in the loop, decide where to inject distillation hints, and file PRs off its own trace analysis.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* | The judge cannot own the definition of good: a licensed clinician, a domain expert, or human evaluation must define and adjudicate correctness, because automated metrics structurally cannot see the archive/ground truth they are supposed to measure and models confidently grade their own failures as successes.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* |

*Why it matters: It determines whether continual-improvement loops can run autonomously at agent speed or whether expert review is a permanent, budgeted gate on every release — and in regulated or safety-critical domains, who is accountable when the judge passes something it should have failed.*

### Should a judge emit an absolute per-item score, or only relative comparisons?

| Position A | Position B |
|---|---|
| Judge each output on its own against an explicit rubric, ideally binary pass/fail (or, for frontier tasks, a QA'd rubric of ~20 criteria), because that is what calibrates cleanly and tells you what to fix.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)* | Absolute scoring is the wrong instrument for subjective output: humans do not agree on a 1-10 scale but do agree on A-vs-B, so train and run judges on pairs — and where the target is a population rather than an item, measure distribution shape and correlation instead of per-item right/wrong.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)* |

*Why it matters: Pairwise and distributional judges cannot produce the single absolute pass-rate number that release gates, dashboards, and leadership reporting are built on, so the choice dictates whether the judge can serve as a shipping gate at all.*

### In subjective domains, is there a single human ground truth for the judge to align to?

| Position A | Position B |
|---|---|
| Yes — collect human labels on a stratified sample with deliberately objective guidelines, drive rater-to-rater agreement up, and treat the resulting labels as the golden source of truth the judge is aligned to.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* | No — averaging preference labels across unmodeled raters produces noise; expert disagreement on style or aesthetics is valuable signal, preferences belong in per-rater vectors, and humans are only ~80% self-consistent, which caps any single-truth alignment score.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)* |

*Why it matters: If there is no single ground truth, a reported judge-human alignment percentage is measuring the wrong thing, and label-averaging pipelines actively destroy the signal that distinguishes good output from mean output.*

## Practical Guidance

**Do:**

- Validate the judge like a binary classifier: hand-label ~100 examples, split train/dev/test, and score the judge prompt on precision and recall.
- Run a standing sampling pipeline that compares expert ratings to judge ratings so you can watch agreement trend rather than assume it holds.
- Attach a confidence interval to every judge score — 84% vs 88% on 50 traces is not a demonstrated gain.
- Run 3-6 trials per eval case, and across more than one agent harness, since both the agent and the judge are non-deterministic.
- Give the judge read-only access to the environment and verify state directly (GitHub, AWS logs) instead of believing the agent's reported tool calls.
- Store, enrich, and phase-segment long trajectories so the judge can query them, rather than stuffing a whole trajectory into one LLM call.
- Judge in hindsight, after the full chain of events, or by polling several models — telling a judge in advance not to allow a behavior does not prevent it in the rollout.
- Replace scalar quality metrics with binary domain checks, e.g. 'the answer is based on the knowledge base, yes/no' or 'brand name is correct, yes/no'.
- Use cheap deterministic assertions (regex, tests, computed scores) wherever the property is checkable, and spend judge calls only on what isn't.
- Implement guardrails as separate judge calls rather than rules in the main system prompt — they are harder to jailbreak and can be iterated independently.
- Route SME review to the cases where the agent and the verifiers disagree, rather than reviewing everything.
- When the judge is not confident on a check, reject rather than publish, and accept redundant overlapping gates as a Swiss-cheese defense.
- QA rubric density — overly dense rubrics degrade judge consistency on problems the models can't yet solve.
- Manually inspect judge scores for family bias; a judge will favor outputs from its own model family.

**Avoid:**

- Shipping a judge whose score gates no decision — an ungated score is dead weight.
- Trusting a model to grade whether its own attempt succeeded; in security tasks models consistently claim their hacks worked.
- Using LLM-as-a-judge for writing quality or holistic 'is this on brand?' questions — decompose into codified elements or use human evaluation instead.
- Making a judge score the system of record for a metric that has a deterministic computation, since the same input scores differently after a model upgrade and the number isn't defensible.
- Scoring only the final output or final state — legally-forbidden actions and looping failures are invisible in aggregate pass rates.
- Grading open-ended tasks by comparison to a reference answer or sample trajectory; there are too many correct solutions to enumerate, and tight matching collapses the paths the agent explores.
- Training an evaluator on naively generated pairs — it will learn surface gloss ('the vibe') and score camera work 9.2 on a static shot.
- Building good-vs-bad pairs as human-made vs AI-made, which yields an AI detector rather than a quality detector.
- Reporting a pass rate produced by an unrealistically polite simulated user; a falling score after making the simulator realistic is progress, not regression.
- Reading every trace with an LLM at scale — at millions of traces this costs more than the original agent executions.

## Notable Outliers

- The existence of ~100 LLM-as-a-judge startups is a direct consequence of safety being formally unspecifiable — you cannot write a proof that an answer is safe, so the industry hired a model to opine instead. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [8:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=522s))
- Claude Opus, judging Claude Sonnet against Llama 3.2, favored its own family — eval scores must be manually inspected rather than trusted numerically. ([Frontier results, on device](../talks/frontier-results-on-device.md), [25:57](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1557s))
- A judge can be used inside training, not just evaluation: it picks where in a rollout to inject a teacher hint, and masks which teacher tokens the student learns from, reducing catastrophic degradation. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [17:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1025s))
- For questions with no empirically correct answer, run a jury of independent agents plus a consensus judge that weighs each analyst's reasoning quality, and expand the jury when consensus is insufficient. ([Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [14:37](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=877s))
- Distilling a committee of frontier judges into one small VLM scores a 15-second video in ~3 seconds — the bigger judge was more accurate, but not worth its latency; the economics only flip above thousands of items per day. ([Evaling Video Slop](../talks/evaling-video-slop.md), [9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s))
- Human raters are only ~80% consistent with themselves, which sets a hard ceiling on any judge-vs-human alignment number. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Running LLM-as-judge grading through a coding-agent subscription is cheaper than paying per-token API prices for the same evaluation. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [39:09](https://www.youtube.com/watch?v=WP3hjUXd918&t=2349s))

## All Talks

- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Alex Bauer](../speakers/alex-bauer.md)
- [Aman Gupta](../speakers/aman-gupta.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Dave Revere](../speakers/dave-revere.md)
- [David Brumley](../speakers/david-brumley.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Erik Meijer](../speakers/erik-meijer.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [James Shi](../speakers/james-shi.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Nick Heiner](../speakers/nick-heiner.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Rayan Garg](../speakers/rayan-garg.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Samuel Denton](../speakers/samuel-denton.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Will Brown](../speakers/will-brown.md)

