---
title: "eval-driven development"
type: "concept"
slug: "eval-driven-development"
tier: "supporting"
maturity: "consolidating"
talk_count: 13
speaker_count: 18
---

# eval-driven development

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **13** talk(s) by **18** speaker(s)

**Definition:** Treating evals as the development loop — writing them first, hill-climbing against them, and gating releases on them.

*Also referred to as: eval-driven hill climbing, eval feedback loops, evals in ci as release gates, quality hill climbing, benchmark ci, eval-in-the-generation-loop, release gating*

## State of Practice

The field has moved past "do evals" to a fairly specific operating discipline: an eval is only real if some score blocks something, the dataset comes from your own production traces rather than public benchmarks or LLM-generated test queries, and the judge is itself a model that must be validated like a classifier against roughly a hundred hand-labeled examples. Practitioners now insist the criteria cannot be written before looking at data — rubrics are discovered by grading traces, and the eval suite is a product of discovery from production failures, not an upfront spec. Evaluation targets the whole trajectory (context completeness, every tool output, final environment state, the harness itself), because aggregate pass rate demonstrably hides failures like an agent removing a legally required disclaimer or claiming edits it never made. There is strong agreement that an eval too easy to fail is worse than none: unrealistically polite simulated users produced a 90%+ pass rate at Lyft, naively generated training pairs taught a video judge to score "the vibe" and rate a static shot 9.2 on camera work, and simulation environments distinguishable from production get reward-hacked. The live arguments are about where evaluation runs (pre-release gate versus inside the generation/inner agentic loop), what the judge should emit (binary pass/fail versus explanations or pairwise comparisons), and how much of the loop a human must still own.

## Consensus

### An eval only counts if its score gates a decision — a judge or check that merely reports, logs, or warns is worthless.

Support: **6** talk(s)

> "A gate which logs only warnings is not a gate. It's a suggestion. The gate needs to block the artifact from moving forward."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

### Evaluation criteria and the eval suite cannot be fully specified upfront; they are discovered by grading real traces and accumulating production failures.

Support: **5** talk(s)

> "But essentially, the real and the complete eval suite is a product of discovery."
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [12:40](https://www.youtube.com/watch?v=pSto5YaNGUo&t=760s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

### The LLM judge is itself an artifact that must be validated and continuously recalibrated against human or expert labels before its scores can be trusted.

Support: **5** talk(s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### Scoring the final output is insufficient for agents; the trajectory, tool outputs, environment state, and process must be verified, because aggregate pass rates conceal specific catastrophic failures.

Support: **5** talk(s)

> "you have to verify the process in addition to the answer because the answer is really only justified in so far as it the process that produced that answer is correct"
>
> — [Respect The Process](../talks/respect-the-process.md), [0:33](https://www.youtube.com/watch?v=CLttOU7n6sI&t=33s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)

### An eval that is too easy — unrealistically cooperative simulated users, naively generated judge-training data, happy-path-only cases, or a simulation the agent can tell is a simulation — is actively misleading, and a falling score after making it harder is progress, not regression.

Support: **4** talk(s)

> "If you have an eval that's too easy, that doesn't give you any real uh, production insights into how your AI agent is actually going to perform."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [15:30](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=930s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)

### When an eval fails, the fix belongs in the harness, skills, tooling, or a deterministic execution layer — patching the prompt with another prohibition is an anti-pattern.

Support: **4** talk(s)

> "There is a bit of an anti-pattern in the industry where like folks try to fix things in the prompt."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Respect The Process](../talks/respect-the-process.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

### Public benchmarks and off-the-shelf metrics are useful only as orientation or baseline; shipping requires a private benchmark whose metrics are tied to your own business outcomes.

Support: **3** talk(s)

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)

## Disagreements

### Should evaluation primarily run as an offline pre-release gate, or inline inside the generation / inner agentic loop?

| Position A | Position B |
|---|---|
| The core mechanism is an offline eval gate: build a private benchmark or simulator, run the agent against it before exposure to users, and use the result as a release gate in CI. Rigor lives outside the runtime path so it can be slow, statistical, and repeatable.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* | A pre-release gate is insufficient. Verification must run inside the inner loop — as guardrail judge calls at request time, as quality checks inside the generation loop, as verification in the agentic coding loop before defects propagate, or as eval outcomes fed back into retrieval at runtime.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* |

*Why it matters: It determines whether your evaluator can be a slow frontier model or must be a distilled 3-second scorer, and whether eval results terminate in a dashboard or become a live control signal. Character.ai distilled a small VLM specifically to move eval into the generation loop; SonderMind accepted per-request latency and cost for separate guardrail judge calls.*

### What should an LLM judge actually emit — a binary label, a rationale, or a pairwise preference?

| Position A | Position B |
|---|---|
| Binary pass/fail tied to task success is best: it is easy to calibrate, easy to train a consistent judge on, and produces an actionable call to action. Continuous 1-10 or 0-1 quality scores tell you nothing you can fix.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* | A bare pass/fail is not enough signal. Raters and judges should supply explanations of their reasoning, or judges should be trained on A-vs-B comparisons rather than any absolute scale, because humans do not agree on absolute scores but do agree on comparisons.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evaling Video Slop](../talks/evaling-video-slop.md)* |

*Why it matters: The output format determines your labeling protocol and judge-training data: binary labels support precision/recall validation on ~100 examples, while pairwise preference requires manufacturing matched good/bad pairs and carries its own overfitting risk (Character.ai's human-vs-AI pairing produced an AI detector rather than a quality detector).*

### How early in a project should rigorous eval infrastructure be built?

| Position A | Position B |
|---|---|
| The eval comes first and must be right before anything is optimized against it, because optimizing against a bad eval collapses the whole system; every company needs its own benchmark and it is an engineering discipline with its own CI pipeline.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)* | Early on, intuition-based non-scalable evaluation is genuinely better — a few core tasks, no massive golden set, no scaled raters — because the eval and the model are both still being calibrated and a heavy eval hinders radical architecture changes; expensive statistical rigor should be reserved for shipping decisions and leadership reporting.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* |

*Why it matters: This decides whether a team spends its first month building simulation infrastructure or shipping and grading by hand. Get it wrong toward rigor and the eval ossifies an architecture you should have thrown away; get it wrong toward vibes and you hill-climb on noise or ship an unsafe agent.*

### Can the eval-and-improve loop be closed automatically, or must a human own the definition of correct and approve each change?

| Position A | Position B |
|---|---|
| Automate it. Once an optimized variant hits target eval scores it can ship to production without human review, and even harness architecture decisions should be meta-optimized by an LLM rather than hand-designed, since manual human-in-the-loop iteration stops scaling past a certain number of agents.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)* | A human owns the definition of good and the admission gate. A licensed clinician — not the engineering team, not the system — decides correct behavior in edge cases; skill changes need PR-style admission gates with a human in the loop; and not looking at raw data yourself is the single most damaging eval anti-pattern.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* |

*Why it matters: It sets where the throughput ceiling and the accountability sit. Auto-shipping on eval scores makes the eval the entire safety argument, which only holds if the judge is calibrated and the criteria were derived from expert-labeled data — exactly the step the automated path is trying to remove.*

## Practical Guidance

**Do:**

- Sample eval datasets from production traffic and mutate them to cover golden paths and edge cases, rather than prompting an LLM to generate ~50 test queries
- Hand-label ~100 traces with binary pass/fail, split train/dev/test, and score the judge on precision and recall before trusting it
- Report confidence intervals on eval scores — 84% vs 88% alignment on 50 traces is not a demonstrable gain
- Fine-tune your user simulator on real user verbatims until the evaluation score goes down, and treat the drop as evidence the eval got realistic
- Construct an Oracle solution for every benchmark task to prove it is solvable, and run a separate CI pipeline over the benchmark itself (pinned dependencies, base images, missing fixtures, Oracle passes)
- Verify final environment state, trace, and artifacts — not just the agent's final message — and independently confirm that claimed edits actually landed
- Run evals locally, at pre-commit, and in CI as a regression suite, with a config-driven (YAML) harness so analysts and non-engineers can contribute cases
- Decide launch gatekeeping criteria before running the regression analysis, not after seeing the results
- Instrument the most expensive handoff first — the one where bad data costs the most — not the most technically complex one
- Re-run skill and prompt evals on every model upgrade; skills are contracts versioned against a specific model, and instruction placement inside the file can silently stop working
- Route only cases where the agent and the verifiers disagree to subject-matter experts, instead of having SMEs review everything
- Decompose long-horizon tasks into steps with a separate prompt and verifier per step so a run can terminate early at the first failure
- Keep a held-out test set the agent has never seen during experimentation, use it sparingly, and refresh it with production data

**Avoid:**

- Shipping a judge whose score gates nothing, or a check that only logs a warning
- Using pre-built helpfulness/toxicity/conciseness metrics as core metrics — a 0.5 helpfulness score is not actionable
- Fixing a failure by adding another prohibition to the prompt instead of the harness, skill, or structured output
- Hyperfixating on a single failing run; drive fixes from failure patterns measured across many examples, since the systems are non-deterministic
- Using off-the-shelf frontier models as user simulators for support — they are trained to be helpful and produce unrealistically polite, articulate complaints
- Training a quality judge on human-footage-good vs AI-footage-bad pairs, which yields an AI detector rather than a quality detector
- Reading only aggregate pass rate — failures like removing a legally required disclaimer are invisible there and only show up in traces
- Using the same AI that wrote the code to verify the code; verification needs a different methodology than generation
- Letting the agent detect that it is in a simulation — it will reward-hack the environment
- Skipping looking at raw data, which breaks the chain from labels to criteria to judge validation to knowing whether the pipeline works
- Chasing perfect benchmark scores, which drifts focus away from the humans the benchmarks exist to protect
- Jumping to scaled raters too early, which produces large swings in measured quality while eval and model are both still being calibrated

## Notable Outliers

- Fine-tune the user simulator until the evaluation score goes down — a falling number is the success criterion for eval realism, not a quality regression. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- Evals and environments are the same thing — you just train in environments — so an enterprise's durable value is in building 10-20 careful environments, not harnesses, which will commoditize. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [16:21](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=981s))
- A larger evaluator model was measurably more accurate and was still rejected: a distilled small VLM scoring a 15-second video in ~3 seconds won because the added accuracy did not justify the slowness, and the tradeoff only flips at thousands to tens of thousands of videos per day. ([Evaling Video Slop](../talks/evaling-video-slop.md), [9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s))
- If an optimized agent variant meets its target eval scores, it can be shipped to production automatically with no human review. ([The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [22:47](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1367s))
- Day one they had to turn off the frontier providers' built-in guardrails because general-purpose LLMs are over-calibrated for mental health, and an inappropriate guardrail trigger is itself a harm — the objective is more correct triggers, not more triggers. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- Constraining the agent's effects rather than its reasoning — forcing all graph-editing code through a typed SDK as the only door, with a deterministic validation script on completion — moved internal eval outcomes from about 43% to 92%. ([Respect The Process](../talks/respect-the-process.md), [13:20](https://www.youtube.com/watch?v=CLttOU7n6sI&t=800s))
- Human code review is not a viable backstop: participants followed AI advice nearly 80% of the time even when the AI was wrong. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s))

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
- [Manoj Nair](../speakers/manoj-nair.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

