---
title: "llm-as-a-judge"
type: "concept"
slug: "llm-as-a-judge"
tier: "core"
maturity: "consolidating"
talk_count: 33
speaker_count: 43
---

# llm-as-a-judge

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **33** talk(s) by **43** speaker(s)

**Definition:** Using a language model to grade or compare outputs, including its calibration against human labels and its known failure modes as an evaluator.

*Also referred to as: llm-as-judge, llm as a judge, llm-as-judge evaluation, llm-as-a-judge limitations, llm-as-judge limitations, agent as a judge, judge validation with precision and recall*

## State of Practice

The conference treated LLM-as-a-judge as infrastructure that itself needs engineering, not as a metric you drop in. The converged protocol is: hand-label ~100 examples, split train/dev/test, prompt (not train) the judge against them, and score it as a binary classifier on precision and recall — then re-verify the judge before believing any drop in its score, because in a non-deterministic system the scorer is non-deterministic too. Judges are increasingly agents rather than single calls: they read the full trajectory, get read-only access to the environment to check state (GitHub, AWS logs, DB) instead of trusting the agent's self-reported tool calls, and segment long traces into queryable phases rather than stuffing them into one context window. The hard limit everyone runs into is the generator-verifier gap — in cybersecurity, finance, pharma, and writing, speakers reported the judge is no better than the thing it grades (models reliably claim their own exploits succeeded), which pushes those teams to deterministic verifiers, expert-authored rubrics, or human labels as ground truth. Reward hacking against the judge is assumed, not hypothesized: teams reported agents oversteering into generic outputs to pass QA gates, judges scoring 9.2 on camera work for a static camera, and evaluator models that learned 'the vibe' instead of the axes they were trained to score. Judge criteria are discovered from production data rather than specified up front — a new production failure simply means you now have a new judge.

## Consensus

### A judge must be calibrated against human labels and treated as software to be verified, not as a trusted oracle; when its score moves, check the judge before changing the agent.

Support: **8** talk(s)

> "In a non-deterministic system, the judge is also non-deterministic. Before you trust the score, verify the scorer."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [17:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1052s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)

### No single LLM judge can serve as ground truth in domains where the judge is no better than the generator; those domains need deterministic verifiers, expert-authored rubrics, or human labels.

Support: **6** talk(s)

> "If I had a really really good generator verifier, then that would just be my generator itself."
>
> — [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [15:58](https://www.youtube.com/watch?v=u6q-byPWUuo&t=958s)

Supporting talks: [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Ending AI Slop](../talks/ending-ai-slop.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Judges must grade the trajectory and resulting environment state, not the final output alone, because whole classes of failure are invisible in aggregate pass rates.

Support: **5** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Agents reward-hack judges and proxy rubrics as a matter of course, so judge design must anticipate gaming rather than assume good-faith outputs.

Support: **6** talk(s)

> "LLM LLM as a judge might not necessarily always be the best method. We know that there's a lot of reward hacking."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)

### Judge criteria cannot be fully specified before looking at data; the eval suite is discovered incrementally from graded production examples and new production failures.

Support: **5** talk(s)

> "A new failure that you see in production simply means you now have a new judge."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [12:14](https://www.youtube.com/watch?v=YXEqC05WEI0&t=734s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### Generic prebuilt scalar metrics (helpfulness, correctness, toxicity on a 0-1 or 1-5 scale) are low-signal because the levels are never defined; judge criteria should be binary and domain-specific.

Support: **4** talk(s)

> "eval should be framed around a task success or failure. And a binary outcome is very easy to calibrate and train um LLM judge that can consistently score your agent trajectory."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

## Disagreements

### Can an LLM judge be the primary grader for a domain, or must the authoritative signal be deterministic or human?

| Position A | Position B |
|---|---|
| In high-stakes, adversarial, or taste-driven domains the judge is structurally unable to grade: models claim their own exploits succeeded, produce plausible finance/pharma jargon without understanding it, lack taste in writing, and give scores that shift when the base model changes. Use deterministic oracles, deterministic PR scoring, or expert human judgment as the authoritative signal.<br>*[Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)* | For the economically valuable soft-verifiable domains now being targeted, deterministic verifiers are brittle, impractical, or impossible, and a validated judge measurably matches expert humans (F1 0.96 against clinicians on hazard detection). Judges are required, and the right move is to make prompts more open-ended by adding hybrid LLM-as-judge verification.<br>*[Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* |

*Why it matters: It determines whether your eval budget goes into building deterministic oracles and expert labeling capacity, or into judge calibration and rubric engineering — and whether judge output can gate a release at all.*

### Should a judge emit a binary pass/fail, or a decomposed multi-criterion score with reasoning?

| Position A | Position B |
|---|---|
| Binary pass/fail tied to a business outcome. It is easy to calibrate, consistent across runs, and produces an actionable call to action; scalar rubrics whose levels are undefined are low-signal and inconsistent.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* | Pass/fail alone tells you nothing about where the agent should improve, so raters and judges must supply explanations; training-grade reward signal needs roughly 20 criteria with about 10 subcriteria each, plus dynamic partial credit for agents that reasoned correctly from an earlier wrong assumption.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: Binary judges are cheap to validate as classifiers but give no credit assignment; dense rubrics give a trainable gradient but degrade judge consistency on exactly the frontier problems you most want to measure.*

### Can the judge-to-fix loop run without a human, or does an expert have to own the definition of 'good'?

| Position A | Position B |
|---|---|
| Fully automated: retuning is config-driven with no human in the loop given guardrail observability and fast rollback; an optimized variant that meets target eval scores ships automatically; an evaluation agent can open the PR with the fix itself.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* | A qualified human owns the definition of correct and the loop is capacity-bound by human attention: a licensed clinician defines correct behavior in edge cases, domain experts must be hired before iteration starts, production data must be reviewed by humans and not only by coding agents, and automated metrics structurally cannot adjudicate fidelity.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Ending AI Slop](../talks/ending-ai-slop.md)* |

*Why it matters: It sets whether your throughput ceiling is compute or headcount, and whether 'the judge approved it' is an acceptable answer in a post-incident review.*

## Practical Guidance

**Do:**

- Hand-label ~100 examples with pass/fail, split into train/dev/test, and score the judge on precision and recall like any binary classifier — the labels inform the judge prompt, not a training run.
- Attach a confidence interval to every reported alignment number; 84% vs 88% on 50 traces is not a demonstrated gain.
- When a judge score drops, verify the judge first and edit the judge prompt if it is wrong — judges are software, and fixing a judge prompt is not cheating.
- Give the judge read-only access to the same environment through the same harness and independently check state (GitHub, AWS logs, DB) rather than believing the agent's reported tool calls; prevent the judge from mutating state after the agent finishes.
- Judge in hindsight — after the full chain of events is visible, or by polling several models — rather than instructing a judge in advance not to allow a behavior.
- Use pairwise A-vs-B comparison instead of absolute 1-10 scoring when humans do not agree on an absolute scale but do agree on comparisons.
- Run judges continuously against live production traffic, not only against a saved golden dataset, and route sampled disagreements between agent and verifiers to subject-matter experts.
- Replace a single golden response with an expert-authored rubric of required elements for open-ended outputs, adjudicated by an independent second expert and QA'd by a third.
- Store, enrich, and phase-segment long trajectories so the judge can query them, instead of stuffing the whole trace into one LLM call.
- Use cheap regex assertions wherever they suffice — most skill evals do not need an LLM judge at all.
- Implement safety guardrails as separate judge calls outside the main system prompt, and put deterministic code above the model for anything that can never be wrong.
- Make the judge score gate something concrete: a merge, a release, or a prompt-optimizer loop.

**Avoid:**

- Letting a judge score float with nothing gated on it — an ungated judge score is worthless.
- Using prebuilt generic metrics (helpfulness, conciseness, toxicity, correctness on 0-1) as core metrics; a 0.5 helpfulness score is not actionable.
- Trusting a model's self-report of success — in cybersecurity, models consistently claim their hacks worked.
- Judging with a model from the same family as the generator; Claude Opus favored Claude Sonnet's output over Llama's.
- Maximizing rubric density — overly dense rubrics degrade judge consistency exactly on frontier problems.
- Prompting a judge for holistic subjective verdicts ('is this on brand?', 'is this good writing?'); decompose into codified elements or route to humans.
- Training an evaluation model on naively generated pairs — it will learn surface gloss and score 9.2 on camera work for a static camera.
- Building good-vs-bad pairs as human-footage vs AI-footage; you get an AI detector, not a quality detector.
- Publishing an LLM-judged score that must stay stable and defensible to leadership — the same artifact scores differently when the model changes.
- Rewriting the prompt off a single failing judged run; drive fixes from failure patterns measured across multiple examples.
- Reading all traces with an LLM at scale — at millions of traces that costs more than the original agent executions.

## Notable Outliers

- The existence of roughly a hundred LLM-as-a-judge startups in the expo hall is a direct consequence of 'safe' being formally unspecifiable — you cannot write a proof that an answer is safe, so the industry outsourced it to another model. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [8:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=522s))
- Claude Opus systematically favored Claude Sonnet's response over Llama 3.2's when judging, so eval scores must be manually inspected rather than trusted numerically. ([Frontier results, on device](../talks/frontier-results-on-device.md), [25:57](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1557s))
- A judge can be used inside training, not just evaluation: to choose where in a rollout to inject a hint, and to mask which teacher tokens the student learns from — improving out-of-distribution behavior acquisition while reducing catastrophic degradation. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [17:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1025s))
- Expert disagreement is diagnostic, not noise: disagreement on objective attributes like alignment means bad data, while disagreement on style or aesthetics is valuable signal that should be preserved as per-rater preference vectors rather than averaged. ([Ending AI Slop](../talks/ending-ai-slop.md), [14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s))
- Running LLM-as-judge grading through a coding-agent subscription is cheaper than paying per-token API prices. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [39:09](https://www.youtube.com/watch?v=WP3hjUXd918&t=2349s))
- Claimed benchmark saturation around 80% often reflects broken tasks rather than exhausted headroom, and you cannot tell which 20% are broken until you have solved all the others. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [14:44](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=884s))

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
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
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
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
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
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
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
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
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

