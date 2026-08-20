---
title: "rubric design"
type: "concept"
slug: "rubric-design"
tier: "supporting"
maturity: "contested"
talk_count: 18
speaker_count: 23
---

# rubric design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **18** talk(s) by **23** speaker(s)

**Definition:** Writing the scoring criteria that graders — human or model — apply, including criterion drift and inter-grader consistency.

*Also referred to as: rubric-based evaluation, evaluation rubric design, rubric-based grading, qualitative grading rubrics, rubrics and graders, llm-as-judge rubrics, criteria drift*

## State of Practice

Rubrics moved from a testing detail to the primary control surface of agent development this year: several speakers described the rubric, not the model or the harness, as the thing that determines whether a system improves. The dominant pattern is expert-authored, multi-criterion rubrics validated against human labels — Abridge has two physicians independently write rubrics for the same open-ended clinical question, a third adjudicate them into one, and a fourth QA the result; Lyft validates judges as binary classifiers on ~100 hand-labeled examples split train/dev/test and scores them on precision and recall. Everyone agrees the criteria cannot be written before looking at data, and that single golden-response comparison is dead for open-ended work because the space of correct answers is unenumerable. The unresolved fights are about granularity (binary task success vs. Theta's ~20 criteria × 10 subcriteria), about whether the judge should grade the trajectory or only the end state, and about whether rubric-scored LLM judges are trustworthy at all in domains without answer keys — LatchBio found rubric scores only loosely correlated with verifiable outcomes and will not use them for RL, and Allos argues rubrics-as-rewards in finance and pharma just build an echo chamber. Second-order rubric failure modes are now being named explicitly: rubric density that degrades judge consistency on frontier problems, criteria undefined at the boundaries that RL will exploit, and rubrics that are themselves too strict or too loose and need a standing human review group to audit.

## Consensus

### Rubric criteria for expert domains must be authored and adjudicated by domain experts, not by the engineers building the system and not by the model being graded.

Support: **5** talk(s)

> "And then we had a separate physician that actually adjudicated it, brought these two independent rubrics together, created a final rubric, and we actually had a fourth clinician do QA on these rubrics."
>
> — [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [17:05](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1025s)

Supporting talks: [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

### Evaluation criteria cannot be fully specified up front; they must be discovered by grading real production data and refined continuously.

Support: **4** talk(s)

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)

### A model grader applying a rubric is untrustworthy until its agreement with expert human raters is measured and monitored on an ongoing sampling pipeline.

Support: **5** talk(s)

> "if you can have a sample pipeline of sorts that is monitoring how a human raider or some expert would rate an eval versus how an LLM would rate it. You can get a sense of like how it's trending"
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [9:46](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=586s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### Scoring open-ended work against a single golden reference answer or reference trajectory fails; rubrics must specify required elements in a way that is invariant to which valid path the agent took.

Support: **3** talk(s)

> "that really does not work for these more ambiguous or open-ended tasks because there's so many possible correct solutions. It's basically impossible to account for every single one."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s)

Supporting talks: [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### Rubric quality is the binding constraint on the whole system: criteria that are loose or undefined at the boundaries get reward-hacked, and that is a rubric failure rather than a model failure.

Support: **5** talk(s)

> "of course the evaluation is the most important piece and LLMs aren't malicious, but they can make, you know, very silly mistakes and if you're optimizing against a bad a bad eval, the whole thing kind of falls apart."
>
> — [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [9:18](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=558s)

Supporting talks: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [State of Data](../talks/state-of-data.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)

### The expensive, bottlenecking part of rubric design is getting humans to agree with each other on the criteria — human-human agreement has to be established before human-model agreement is meaningful.

Support: **4** talk(s)

> "there's a funny visual here about writing the evals can be a very small point and humans arguing over what the rubric should be is, uh, is kind of like a very large task here"
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [6:11](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=371s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

## Disagreements

### Should a rubric collapse to a single binary pass/fail judgment, or decompose into many weighted criteria?

| Position A | Position B |
|---|---|
| Frame every eval as binary task success or failure tied to a business outcome; binary is easy to calibrate, easy to train a judge on, and directly actionable. Continuous quality scores like 'helpfulness 0.5' are unactionable.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Binary is too coarse a signal. Raters must supply explanations for their verdicts, end-to-end outcome grading is too sparse to learn from and must be decomposed into intermediate nodes, and useful training rubrics need roughly 20 criteria with about 10 subcriteria each.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* |

*Why it matters: Binary rubrics give you a calibratable ship gate but no credit assignment; dense rubrics give you a training signal but degrade judge consistency exactly on the frontier problems you care most about. The choice determines whether your eval can gate a release, drive RL, or both.*

### Can a rubric-driven LLM judge be trusted as the primary quality signal in domains with no answer key?

| Position A | Position B |
|---|---|
| Yes, if the rubric encodes embedded domain experts' judgment and the judge is calibrated against their labels. Expert-calibrated judges are what let non-expert engineers move fast, and qualitative process rubrics can grade research rollouts and score production conversations automatically.<br>*[From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* | No. A verifier good enough to grade would already be your best generator; rubric scores correlate only loosely with verifiable outcomes and are not trustworthy for RL or benchmarking; and in finance and pharma the judge produces plausible jargon without understanding the concepts, so rubrics-as-rewards become an echo chamber where the AI grades itself into agreement.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [State of Data](../talks/state-of-data.md)* |

*Why it matters: If rubric-scored judges are trustworthy, evaluation scales with compute and the expert is only needed for calibration; if they are not, every quality signal stays gated on scarce expert hours and RL against rubrics is actively dangerous.*

### Should the rubric grade the agent's trajectory and process, or only its final outcome?

| Position A | Position B |
|---|---|
| Grade the trajectory. Judges must inspect the path — that is how sandbox escape, hidden-test-reading, and other reward hacks are caught — and process rubrics for 'what makes a good researcher' or 'is this query a natural sentence' are themselves a legitimate reward. Aggregate pass rates hid a legally-required disclaimer being deleted; only trace inspection found it.<br>*[Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* | Grade the outcome. Criteria should be desired behaviors, objectives, and hard constraints rather than implementation details; the honest signal is whether the PR opened, the report saved, or the money was made — not thumbs up/down or path conformance.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* |

*Why it matters: Process criteria catch reward hacking that outcome criteria miss, but enforcing the path too tightly collapses the state space of solutions the agent explores and, per the benchmark critique, leaks the answer into the task.*

### Should a rubric be fixed and applied identically to every run, or adapt per-trajectory at evaluation time?

| Position A | Position B |
|---|---|
| Fixed. Pre-commit the criteria and the launch gatekeeping rule before you run the regression analysis, validate the judge against a held-out labeled set, and keep the rubric stable so scores are comparable across runs.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* | Adaptive. Fixed rubrics with fixed scores structurally cannot catch modern multi-step agent failures; the grader should be an agent with read-only environment access that segments and queries the trajectory, and dynamic evaluation-time rubrics can grant partial credit by conditionally assuming an agent's earlier wrong assumption.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: Adaptive graders find subtle failures a fixed rubric never encodes, but a rubric that changes per run destroys the run-to-run comparability that ship decisions and regression suites depend on.*

## Practical Guidance

**Do:**

- Have two independent domain experts write rubrics for the same open-ended task, a third adjudicate them into a single final rubric, and a fourth do QA on the result.
- Validate the judge like a binary classifier: hand-label ~100 examples pass/fail, split into train/dev/test, and report precision and recall — the labels inform the judge prompt, not model weights.
- Attach a confidence interval to every reported rubric score; 84% vs 88% alignment on 50 traces is not a demonstrated gain.
- Give the judge read-only access to the environment so it can verify claimed work against actual state (GitHub, AWS logs) instead of trusting the agent's reported tool calls, with permissions that prevent it from mutating state after the run.
- Require raters — human or model — to write the reasoning behind a verdict, not just the verdict, so the score tells you where to fix the agent.
- Run a standing human review group over auto-scored production conversations specifically to check whether the rubrics themselves are too strict or too loose.
- QA rubric density rather than maximizing it: on problems models can't yet do, dense rubrics measurably degrade judge consistency.
- Score humans on the same rubric you score the system on, to know what the bar actually is (Hippocratic: 99.89% no-harm for Polaris vs ~81% for human clinicians).
- Judge in hindsight — after the full chain of events, or by polling several models — rather than trying to enumerate prohibited behaviors in the instructions up front.
- Fix the launch gatekeeping criteria before you run the regression analysis, not after seeing the results.
- Check that the rubric penalizes bad actions, not just missing good ones — verifying the model didn't do something harmful is as critical as verifying it did the task.

**Avoid:**

- Weak verifier criteria: asserting variable names the instruction never specified, or testing unexported functions. In SWE-Bench Pro this accepts wrong implementations 8.5% of the time and rejects correct ones over 24% of the time.
- Using pre-built generic metrics (helpfulness, toxicity, conciseness) as core criteria — a 0.5 helpfulness score is not an action.
- Shipping a judge whose score gates no decision.
- Buying your evals and your definition of task realism from the same vendor — that is letting the test writer grade the test.
- Rewriting the rubric or prompt in response to one failing run; measure the failure pattern across many examples first.
- Trusting a suspiciously high pass rate: Lyft's first offline eval scored 90%+ purely because the simulated user was unrealistically polite.
- Scaling to a large rater pool before the rubric is calibrated — it produces big swings while both the eval and the model are still moving.
- Treating rubric scores that only loosely correlate with verifiable outcomes as a reward signal for RL or as a benchmark.
- Letting the rubric embed implementation details or point at the test file — that leaks the answer and invalidates the task.

## Notable Outliers

- Fine-tune the user simulator until the evaluation score goes down — a falling score is evidence the eval got more realistic, not that quality dropped. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- You need about 450 tests to be 99% sure of catching a 1% error rate, and about 1,900 to see it caught ten times. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:13](https://www.youtube.com/watch?v=AN65uc645mE&t=1033s))
- Public benchmark rubrics are too coarse to train on; useful reward signal needs roughly 20 criteria with about 10 subcriteria each. ([Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [19:57](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1197s))
- Writing the eval forces more rigorous reasoning than doing the analysis yourself — building rubrics exposed that many canonical bioinformatics QC thresholds are arbitrary. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- The human-chosen structure of the grading harness is itself arbitrary and should be meta-optimized by an LLM rather than hand-designed. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [15:00](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=900s))
- Telling a judge model not to allow a behavior does not prevent it in the rollout; simple hindsight review catches most reward hacks in practice. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [15:15](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=915s))
- Cherry-picking tasks where models diverge, packaging them as a hard benchmark, and then selling the data to climb that same benchmark is Goodhart's law with a profit motive. ([State of Data](../talks/state-of-data.md), [8:11](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=491s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)
- [State of Data](../talks/state-of-data.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Ali Khial](../speakers/ali-khial.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [George Cameron](../speakers/george-cameron.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Rayan Garg](../speakers/rayan-garg.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Vivek Muppalla](../speakers/vivek-muppalla.md)
- [Will Brown](../speakers/will-brown.md)

