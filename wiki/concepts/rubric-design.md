---
title: "rubric design"
type: "concept"
slug: "rubric-design"
tier: "supporting"
maturity: "contested"
talk_count: 14
speaker_count: 19
---

# rubric design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **14** talk(s) by **19** speaker(s)

**Definition:** Writing the scoring criteria that graders — human or model — apply, including criterion drift and inter-grader consistency.

*Also referred to as: rubric-based evaluation, evaluation rubric design, rubric-based grading, qualitative grading rubrics, rubrics and graders, llm-as-judge rubrics, criteria drift*

## State of Practice

The field has stopped treating the rubric as a static artifact written before evaluation and started treating it as an error-prone system with its own measurable accuracy. Lyft validates judges like binary classifiers on ~100 hand-labeled traces split train/dev/test and reports precision and recall; G2i measured a public benchmark's graders accepting wrong implementations on 8.5% of tasks and rejecting correct ones on 24%. Everyone converged on the point that final-state or aggregate pass-rate scoring is insufficient for agents — criteria must be applied to the trajectory, with judges built as agents that hold read-only access to the environment and independently verify state rather than trusting the agent's reported tool calls. Reward hacking is now attributed to the rubric rather than the model: a proxy left undefined at its boundaries is what gets exploited, and the standard defense is hindsight review of the full chain plus explicit criteria for prohibited actions, not instructions telling the judge to disallow a behavior. The live arguments are about granularity (binary business-outcome pass/fail versus ~20 criteria × 10 subcriteria), about whether a fixed rubric or an adaptive agent-judge is the right instrument, and about whether rubric scores are yet trustworthy enough to serve as an RL reward — LatchBio found their path-invariant rubric scores only loosely correlated with verifiable outcomes, and Theta found judges apply dense rubrics inconsistently on frontier problems.

## Consensus

### Rubrics must be applied to the agent's trajectory, not just its final output or an aggregate pass rate — critical failures are invisible in categorical scores.

Support: **6** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

### Grading criteria cannot be fully specified in advance; they are discovered by grading real outputs and refined in hindsight.

Support: **4** talk(s)

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

### The grader is itself an error-prone system whose accuracy must be measured against human labels — inter-grader agreement and judge precision/recall are first-class metrics, not assumptions.

Support: **4** talk(s)

> "In Sweet Bench Pro, 8.5 of 8.5% of all the tasks uh accepted wrong implementation in one hand and more than 20 24% of the tasks uh rejected um correct implementations."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### Reward hacking is a defect in the rubric, not the model: criteria that are loose proxies undefined at their edges get exploited, so rubrics must explicitly score what the agent must not do.

Support: **4** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

### Generic off-the-shelf quality criteria (helpfulness, toxicity, conciseness, thumbs up/down) are not usable core criteria; rubric items must be tied to a concrete task or business outcome to be actionable.

Support: **3** talk(s)

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)

## Disagreements

### Should a rubric collapse to a binary pass/fail outcome, or decompose into many graded criteria?

| Position A | Position B |
|---|---|
| Frame every criterion as binary task success/failure tied to a business outcome — binary is easy to calibrate and produces consistent judge scoring across trajectories.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Binary is too coarse to act on: raters must supply explanations, end-outcome grading is too sparse a signal and must be decomposed into intermediate analysis-DAG nodes, and training-grade rubrics need roughly 20 criteria with ~10 subcriteria each.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)* |

*Why it matters: Binary rubrics give a calibratable ship/no-ship gate but no credit assignment; dense rubrics localize the failure but degrade judge consistency exactly on the frontier problems you care most about. The choice determines whether your score can be used to debug the agent or only to gate it.*

### Is a fixed rubric applied by a judge still the right instrument for multi-step agents, or must the judge itself be an agent that decides what to examine?

| Position A | Position B |
|---|---|
| Keep the rubric fixed and the grader cheap and deterministic where possible: a hand-tuned judge prompt validated on labeled examples, or a deterministic Python grader per task alongside human verification.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)* | Fixed rubrics structurally cannot catch modern agent failures because trajectories differ every run; the grader must be an agent that reuses the task harness, queries the enriched trajectory, and inspects environment state adaptively.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: Agent-judges cost far more per grade and are themselves unvalidated, but fixed rubrics silently miss loops, sandbox escapes, and hidden-test-suite reads. This decides whether evaluation cost scales with trace length or with test-case count.*

### Are rubric scores reliable enough to use as a training/RL reward, or only as diagnostics?

| Position A | Position B |
|---|---|
| Yes — qualitative process rubrics grading how well a rollout followed the research process, and trajectory rubrics judging query quality and exploration volume, work today as RL reward alongside outcome metrics, and hindsight review catches most hacks.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | Not yet — rubric scores built from path-invariant choke points correlate only loosely with verifiable outcomes, and judges apply dense rubrics inconsistently on problems models cannot yet solve, so they are not trustworthy for RL or benchmarking.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)* |

*Why it matters: If rubric scores are trainable signal, soft-verifiable domains (finance, biology, research) open to RL immediately; if not, those domains stay gated on deterministic verifiers and expensive human grading.*

### Who should author and maintain the rubric — trained humans, or an automated loop?

| Position A | Position B |
|---|---|
| Humans, deliberately and expensively: instructions and criteria authored and reviewed by humans, scientists grading each other's tasks to expose bad specifications, and cross-functional teams and scaled raters trained on how to rate.<br>*[Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* | Reward and rubric design will climb the abstraction ladder the way coding agents did — harness and criteria design is itself a verifiable loop an LLM should meta-optimize, with humans reserved for the highest-level judgments about goals and quality.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)* |

*Why it matters: LatchBio reports each task took three people about a week to build; if rubric authoring can be automated, eval coverage scales with compute instead of headcount, and the human role shifts from writing criteria to auditing them.*

## Practical Guidance

**Do:**

- Hand-label ~100 traces pass/fail, split into train/dev/test, and score the judge on precision and recall before letting its output gate anything
- Give the judge read-only access to the same environment the agent ran in and have it verify state directly (GitHub, AWS logs) rather than trusting the agent's reported tool calls
- Store, enrich, and phase-segment long trajectories so the judge can query them, instead of stuffing the whole trace into one LLM call
- Attach confidence intervals to every reported score — 84% vs 88% alignment on 50 traces is not a demonstrated gain
- Include criteria for what the agent must not do (e.g. removing a legally required disclaimer), not only whether the task succeeded
- Judge in hindsight, after the full chain of events, or by polling several models, rather than instructing a judge in advance not to allow a behavior
- Write task instructions as desired behaviors, objectives, and hard constraints — not implementation details, interfaces, or pointers to the test file
- Make the rubric path-invariant: check that several valid solution paths all pass before trusting a failure
- Decompose sparse end-outcome grading into intermediate nodes of the analysis DAG when models are too weak for the final outcome to carry signal
- QA rubric density explicitly rather than maximizing criterion count, and re-check judge consistency after each density increase
- Have domain experts grade each other's tasks — disagreement surfaces badly specified rubrics rather than bad work
- Fix criteria based on failure patterns across many examples, not on one failing run
- Decide launch gatekeeping thresholds before running the regression analysis, not after seeing results
- Keep the eval/rubric config in editable YAML so analysts and domain experts, not only engineers, can add cases

**Avoid:**

- Tests that assert unspecified variable names or exercise unexported functions — weak verifiers that would fail code review
- Instructions that name the test file or hand over the full implementation interface, which leaks the answer and removes the task
- Helpfulness/toxicity/conciseness-style prebuilt metrics as core criteria; a 0.5 helpfulness score implies no action
- Grading open-ended work by diffing against one reference answer or sample trajectory — there are too many correct solutions to enumerate
- Maximizing rubric density on frontier problems, where judges cannot apply dense criteria consistently
- Moving to scaled human raters before the rubric is calibrated, which produces large swings in measured quality
- Shipping an LLM judge whose score gates no decision
- Buying your eval, your tasks, and your definition of task realism from the same vendor
- Accepting a 90%+ pass rate without checking whether the simulated user or environment is unrealistically easy
- Generating ~50 test queries by prompting an LLM instead of sampling and mutating production traffic

## Notable Outliers

- Fine-tune the user simulator until the eval score goes down — a falling score is evidence the rubric got more realistic, not that quality dropped. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- Evaluation-time rubrics can be dynamic: grant partial credit by assuming an agent's earlier mistaken assumption was correct, then grade the rest of the trajectory conditionally. ([Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [17:13](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1033s))
- Vendors cherry-pick tasks where models diverge, package them as a hard North Star benchmark, then sell the data to hill-climb that same benchmark — Goodhart's law with a profit motive. ([State of Data](../talks/state-of-data.md), [8:11](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=491s))
- Writing the eval forces more rigorous reasoning than doing the analysis yourself, and doing so revealed that many canonical bioinformatics QC thresholds are arbitrary. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- Writing the evals is a small point on the diagram; humans arguing over what the rubric should be is the large task. ([How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [6:11](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=371s))
- A rubric-based grader agent running alongside the agent loop can keep the agent retrying until it meets the defined success criteria, turning the rubric into a control mechanism rather than a measurement. ([Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [28:58](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1738s))

## All Talks

- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)
- [State of Data](../talks/state-of-data.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Ali Khial](../speakers/ali-khial.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
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
- [Will Brown](../speakers/will-brown.md)

