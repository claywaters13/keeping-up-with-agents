---
title: "eval-driven development"
type: "concept"
slug: "eval-driven-development"
tier: "supporting"
maturity: "consolidating"
talk_count: 14
speaker_count: 19
---

# eval-driven development

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **14** talk(s) by **19** speaker(s)

**Definition:** Treating evals as the development loop — writing them first, hill-climbing against them, and gating releases on them.

*Also referred to as: eval-driven hill climbing, eval feedback loops, evals in ci as release gates, quality hill climbing, benchmark ci, eval-in-the-generation-loop, release gating*

## State of Practice

The conference treated evals as the development loop itself, not a QA afterthought: a judge or benchmark whose score gates nothing is considered worthless, and several teams now run the eval suite locally, at pre-commit, in CI, and inside the agent's inner generation loop. The dominant construction recipe is inverted from how teams first attempt it — you do not write criteria upfront and then measure against them; you grade real traces, discover the criteria from the data, hand-label ~100 examples, and validate the LLM judge like a binary classifier on precision/recall before trusting a single number it emits. Datasets are expected to be drawn from production traffic and continuously repopulated, with simulation used to make runs repeatable (Snorkel runs millions of agent simulations monthly; Ufonia replaced A/B tests entirely with simulated patients because randomizing patients into a worse variant is illegal). Two things are treated as settled failure modes: scoring only the final answer rather than the trajectory, tool outputs, and final environment state; and fixing eval failures by appending prohibitions to the prompt. What remains open is whether an offline gate is ever sufficient to ship, how much rigor to buy on day one versus vibing, and what a judge should actually emit — binary pass/fail, pairwise preference, or a verdict plus written rationale.

## Consensus

### A judge score that does not gate a decision is worthless; the gate must be able to block the artifact, not just log a warning.

Support: **5** talk(s)

> "A gate which logs only warnings is not a gate. It's a suggestion. The gate needs to block the artifact from moving forward."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)

### Evaluation criteria and the eval suite cannot be fully specified upfront; they are discovered by grading real outputs and are co-developed with the system.

Support: **4** talk(s)

> "But essentially, the real and the complete eval suite is a product of discovery."
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [12:40](https://www.youtube.com/watch?v=pSto5YaNGUo&t=760s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### Eval datasets must be sampled from and continuously refreshed with production traffic; synthetic or hand-written sets produce inflated, uninformative pass rates.

Support: **4** talk(s)

> "It's not a static benchmark. It's a constantly populated data set from your production traces."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### The LLM judge is itself a model that must be validated against human labels with classifier metrics and continuously recalibrated, not trusted on first use.

Support: **5** talk(s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

### Scoring the final output is insufficient; the trajectory, tool outputs, reasoning process, and final environment state must be verified, because aggregate pass rates hide category-level failures.

Support: **5** talk(s)

> "you have to verify the process in addition to the answer because the answer is really only justified in so far as it the process that produced that answer is correct"
>
> — [Respect The Process](../talks/respect-the-process.md), [0:33](https://www.youtube.com/watch?v=CLttOU7n6sI&t=33s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

### When an eval fails, the fix does not belong in the prompt; it belongs in the harness, skills, structured output, or a boundary check — and should be driven by a measured failure pattern, not a single bad run.

Support: **5** talk(s)

> "There is a bit of an anti-pattern in the industry where like folks try to fix things in the prompt."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Respect The Process](../talks/respect-the-process.md)

### Evaluation must run inside the inner generation loop, not only as an outer CI/CD stage, because defects caught after assembly are far more expensive to correct.

Support: **4** talk(s)

> "The verification needs to run in both the inner agentic loop and also in the outer loop for CICD."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [18:11](https://www.youtube.com/watch?v=03l29gJXpCE&t=1091s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)

### Generic off-the-shelf continuous quality metrics (helpfulness, toxicity, conciseness, absolute 1–10 scores) are not actionable and should not be the core metric; metrics must be tied to task or business outcomes.

Support: **3** talk(s)

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

### Simulation with an LLM standing in for the human user is the practical substitute for production A/B testing, because production runs are never apples-to-apples and real users cannot be used as test data.

Support: **3** talk(s)

> "it's hard to make sure that everything is repeatable because you will get different database state, different tool versions, and so on. So, never fully compare apples to apples."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

## Disagreements

### Can passing an offline eval gate justify shipping, or is the gate only a precondition to controlled real-world exposure?

| Position A | Position B |
|---|---|
| An offline benchmark is the release gate: agents pass a rigorous offline evaluation before touching live users, the private benchmark verifies no regression on any stack change, and a variant that hits its target eval scores can be shipped to production automatically with no human review.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* | An eval gate does not make a system safe. Simulation is necessary but not sufficient — passing every simulated test only earns the right to test carefully on real people, with autonomy expanded stage by stage as evidence accumulates and a continuous learning loop from real traces running underneath.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)* |

*Why it matters: It decides whether eval infrastructure buys you full CI-style autoship or only a staged rollout plan with humans in the loop — and therefore whether your headcount goes into benchmark engineering or into clinical/expert review capacity that never goes away.*

### How much eval rigor should exist before you start iterating on the agent?

| Position A | Position B |
|---|---|
| Start with the eval: it is the most important component of the system, every company needs its own private benchmark before it can reliably release, and ad-hoc dataset construction (prompting an LLM for ~50 queries) is disqualifying.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Early on, non-scalable intuition-based evaluation is actively better — a few core tasks, no massive golden set — because a heavyweight eval hinders radical architecture changes and moving to scaled raters too early produces large swings while the eval and the model are both still being calibrated.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* |

*Why it matters: Front-loading benchmark construction is weeks of engineering that either de-risks every later change or freezes an architecture you should still be tearing up.*

### What should a judge emit — a bare verdict, or a verdict plus rationale?

| Position A | Position B |
|---|---|
| Binary pass/fail tied to task success is the right unit: it is easy to calibrate, gives a consistent trajectory score, and produces a clear call to action, whereas score-based rubrics do not tell you what to fix.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* | Binary ratings are insufficient — a pass or fail tells you nothing about where the agent should improve or what reasoning produced the verdict, so raters (human and model) must supply explanations, and preference between two candidates is a better signal than any absolute scale.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evaling Video Slop](../talks/evaling-video-slop.md)* |

*Why it matters: It determines whether your eval output is aggregatable into a shippable number or a corpus you have to read, and whether judge calibration is a precision/recall exercise or an inter-annotator-agreement one.*

### Should evals be used to select the model, or is the model choice largely irrelevant next to the surrounding system?

| Position A | Position B |
|---|---|
| In production you do not care about the model, you care about the full system; intelligence is better placed in the harness, context, tools, and guardrails, where a weaker model reaches comparable results with more tokens.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)* | Models differ measurably on the axes that matter and should be benchmarked and swapped accordingly — across ~4,000 coding tasks, one model scored well on correctness and task-solving while another was the better choice when maintainability, security, or low complexity were the priority.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: If the system dominates, eval budget goes into harness and environment construction and model choice becomes a cost decision; if the model dominates on specific quality axes, you need per-axis model benchmarks and routing.*

## Practical Guidance

**Do:**

- Sample eval datasets from production traffic and mutate them for golden paths and edge cases; keep a held-out test set the agent has not seen, use it sparingly, and refresh it with prod data.
- Hand-label ~100 traces pass/fail, split train/dev/test, and score the judge on precision and recall before letting it gate anything; keep a sampling pipeline monitoring human-vs-LLM agreement over time.
- Fine-tune or otherwise harden the simulated user on real user verbatims until the eval score goes down — a falling score means the eval got more realistic.
- Construct an Oracle solution for every benchmark task to prove it is solvable, and run the benchmark itself through its own CI pipeline checking pinned dependencies, base images, and missing fixtures.
- Verify final environment state, trace, and artifacts — not just the model's output — and independently confirm that claimed edits actually landed.
- Instrument the most expensive handoff first (the one where bad data costs the most), not the most technically complex one.
- Attach confidence intervals to reported scores; a 84% vs 88% difference on 50 traces is not a demonstrated gain. Reserve the expensive statistical rigor for shipping decisions and leadership reporting.
- Make the eval harness config-driven (YAML) so analysts, domain experts, and clinicians can contribute cases without an engineer.
- Decide the launch gatekeeping criteria before you run the regression analysis, not after seeing the results.
- Define the cost matrix with domain experts — in high-stakes settings deliberately bias the judge toward over-calling hazards, since a false positive is annoying and a false negative is catastrophic.
- Re-run the full eval suite on every model upgrade: prompts and skills are contracts versioned against a specific model, and instruction placement that worked on one model gets ignored on the next.

**Avoid:**

- Shipping an LLM judge whose score gates nothing, or a gate that only logs warnings.
- Not looking at the raw data — without it you cannot write meaningful criteria, without criteria you have no labels, and without labels you cannot validate the judge.
- Trusting aggregate pass rate alone; it hid an agent deliberately deleting a legally required disclaimer, and a video judge scoring 9.2 on camera work for a static camera.
- Using off-the-shelf frontier models as user simulators for support-style tasks — they are trained to be helpful and produce unrealistically polite, articulate complaints, which is how a 90%+ pass rate turns out to be an artifact.
- Patching failures by adding prohibitions to the prompt, or rewriting the prompt in reaction to a single non-deterministic bad run.
- Using the same AI that produced the artifact to verify it; verification must use a different methodology than generation.
- Letting the agent detect that it is in a simulation — it will reward-hack the environment, so the sandbox must be indistinguishable from production.
- Training an evaluator on naively generated pairs (human footage as 'good', AI footage as 'bad'), which yields an AI detector or a vibe scorer rather than a measure of the axes you named.
- Chasing perfect benchmark scores, which drifts focus away from the humans the benchmark exists to protect.
- Treating annotation as a one-time labeling pass rather than a continuous loop feeding judge recalibration.

## Notable Outliers

- Evals and environments are the same artifact — an eval becomes an environment the moment you train in it — so an enterprise's durable value is in building 10–20 carefully constructed environments, not in the harness, which will commoditize. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [16:21](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=981s))
- An LLM judge validated on 240 examples matched or slightly beat expert clinicians at detecting clinical hazards, reaching F1 0.96 with near-perfect sensitivity — and the regulatory deliverable is the traceable evidence (calls, datasets, pinned prompts, judge verdicts mapped to hazards), not the model. ([Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [10:13](https://www.youtube.com/watch?v=McknwOzbmyg&t=613s))
- Human review is an unreliable backstop for AI output: participants followed the AI nearly 80% of the time even when it was wrong, so automated verification must backstop the reviewer rather than the reverse. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s))
- Once an agent variant hits its target eval scores it can be shipped to production automatically, with no human review in the path at all. ([The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [22:47](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1367s))
- General-purpose model guardrails had to be turned off entirely for mental health support because they are over-calibrated, and inappropriately triggering a guardrail is itself a harm — the objective is correct triggers, not more triggers. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s))
- Eval and observability results currently have no path back into the running agent — the signal dies in the dashboard — so agents cannot learn from yesterday's failures; weighting retrieved memories by whether they historically helped moved tau-bench policy-following from 66% to 80%. ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [2:35](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=155s))
- Distilling a committee of expert judges into one small VLM scores a 15-second video in ~3 seconds; the bigger judge was more accurate but not worth its latency, and the distillation only pays for itself past thousands of videos per day. ([Evaling Video Slop](../talks/evaling-video-slop.md), [8:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=494s))

## All Talks

- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [Respect The Process](../talks/respect-the-process.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

