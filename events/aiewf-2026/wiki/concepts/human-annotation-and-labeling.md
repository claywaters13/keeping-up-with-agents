---
title: "human annotation and labeling"
type: "concept"
slug: "human-annotation-and-labeling"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 19
---

# human annotation and labeling

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **19** speaker(s)

**Definition:** Sourcing and calibrating human judgments used as ground truth — annotator agreement, expert labeling, and alignment of judges to human labels.

*Also referred to as: human data annotation, expert-annotated evals, human annotation calibration, inter-rater agreement, expert annotation quality, human-in-the-loop labeling, eval rubrics and human feedback, human label alignment*

## State of Practice

The field has settled on human labels as the ground truth that every automated judge is a lossy approximation of, and on judge-vs-human agreement as the number that decides whether an eval is trustworthy. The concrete recipe that recurred across talks: hand-label roughly 100 traces sampled from production traffic with binary task-success labels, split them train/dev/test, and score the LLM judge as a binary classifier on precision and recall — then keep the loop running, because criteria are discovered by grading real data, not written down in advance. Who does the labeling has hardened into a requirement rather than a detail: a licensed clinician at SonderMind, scientists grading each other's work at LatchBio, a thousand vetted designers at Taste Labs, and an explicit claim from Surge that cheap labor and AI assistance cannot produce frontier-quality labels at any volume. Annotator disagreement has been reframed from noise to instrumentation — disagreement across runs or raters is a better routing signal for human review than any model-reported confidence score, and it localizes the gray zone where the label itself, not the model, is the problem. The live arguments are about aggregation (collapse raters to one objective truth vs. preserve per-rater preference vectors), about how much of the loop can run without a human at all, and about whether absolute rubric labels or pairwise comparisons elicit judgments humans can actually reproduce.

## Consensus

### Human labels are the golden source of truth; automated judges and models are aligned to them, not the reverse.

Support: **6** talk(s)

> "For our use case, we consider human labels as the golden source of truth. And this is what we want to align our models to."
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [8:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=533s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

### An LLM judge must be validated against hand-labeled human examples and monitored for human-vs-judge agreement; an unvalidated judge score is not evidence.

Support: **5** talk(s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### Labeling criteria cannot be fully specified before annotation begins; the rubric is discovered by grading real outputs, and sloppy ground-truth construction fails correct work.

Support: **4** talk(s)

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### Labels must come from accountable domain experts rather than generic or cheap raters; the expert, not the engineering team or the system, owns the definition of correct.

Support: **5** talk(s)

> "Like you can't push the frontier forward from within the frontier. You need to inject that external human expertise and it needs to be good expertise."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Agents Building Agents](../talks/agents-building-agents.md)

### Annotator and model disagreement is diagnostic signal that localizes ambiguous cases and badly specified tasks, not noise to be averaged away.

Support: **3** talk(s)

> "if they're disagreeing on things like sty style or um aesthetics that is not necessarily bad data that's actually good data. It shows you that there is a distinction for what people like."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### Annotation is a continuously running loop fed by production traces, not a one-time labeling pass or pre-launch audit.

Support: **5** talk(s)

> "it is important to know that this loop is something which runs continuously. It's not uh not a one-off audit."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [27:42](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1662s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

## Disagreements

### When raters disagree, should the labeling process drive them toward a single objective label, or preserve the disagreement as per-rater preference?

| Position A | Position B |
|---|---|
| Write deliberately objective annotation guidelines and enforce strong human-human agreement within the team; a single accountable expert (a licensed clinician, a stratified human-label set) defines the one correct label, and disagreement means the guidelines need tightening.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | For subjective and gray-zone cases there is no single correct label; averaging preferences across unmodeled raters produces noise, so preferences should be attached to per-rater preference vectors, and the right label depends on the specific customer's policy.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)* |

*Why it matters: It determines whether your dataset schema carries one consensus label per example or a rater-conditioned distribution, and whether a model trained on it collapses to the mean or can be steered per user. Chasing consensus in a genuinely multi-preference domain is exactly the mechanism speakers blamed for AI slop.*

### Can the human be removed from the retuning loop once guardrails and golden datasets exist?

| Position A | Position B |
|---|---|
| Retuning can be fully automated and config-driven with no human in the loop, and a coding agent optimizing against a frozen golden dataset can find improvements human engineers missed — provided guardrail observability and fast rollback exist.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents Building Agents](../talks/agents-building-agents.md)* | Human expert judgment is irreducible: a licensed professional must define correct behavior in edge cases, scientists must grade each other's work in the absence of canonical answers, human evaluation is the ground truth benchmarks approximate, and humans retain taste and judgment over final output.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)* |

*Why it matters: It sets the marginal cost and cadence of every improvement cycle — seconds versus a week per task with three people. Both sides agree the automated loop reward-hacks (oversteering into generic outputs, editing scorers to pass), so the answer really turns on whether your guardrails can detect hacking without a human reading traces.*

### What format should human judgments be collected in — absolute labels against a rubric, or relative comparisons between two outputs?

| Position A | Position B |
|---|---|
| Collect binary pass/fail labels tied to task success and business outcomes; a binary outcome is easy to calibrate and to train a consistent judge against, and continuous scores like 'helpfulness 0.5' are unactionable.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Don't score, compare: humans do not agree on absolute 1–10 scales but do agree on which of two outputs is better, so train judges on A-vs-B pairs — and binary pass/fail without a written explanation tells you nothing about where to improve.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* |

*Why it matters: The format determines inter-annotator agreement and therefore how much labeling budget converts into usable signal; it also determines whether the resulting judge can rank two candidate systems or only gate one. Pairwise collection additionally requires manufacturing negatives carefully — pairing human footage against AI footage yields an AI detector, not a quality detector.*

## Practical Guidance

**Do:**

- Hand-label ~100 production traces with binary pass/fail, split train/dev/test, and score the LLM judge on precision and recall as a binary classifier before trusting it
- Attach a confidence interval to every alignment number — 84% vs 88% on 50 traces is not a demonstrated gain — and reserve that statistical rigor for ship decisions and leadership reporting
- Route cases to human review based on disagreement across repeated runs or across models, not on the model's self-reported uncertainty score
- Make an accountable licensed expert own the definition of correct in edge cases, and commit their scored scenarios into CI so every prompt, model, and guardrail change is re-scored against them
- Sample the labeling set stratified from real production traffic and slice results by segment (geography, device type, item type) so tuning can target underperforming slices
- Require raters to write an explanation alongside the pass/fail label, since the verdict alone does not say where the agent should improve
- Tie expert commentary to the specific component that produced the artifact (e.g. the code that renders a visual element) rather than to the artifact as a whole — it materially reduces label noise
- Run short recurring team annotation sessions (10–15 minutes) and feed the labels back to recalibrate the judges continuously
- Treat every human-validated failure as a permanent addition to the golden dataset so the eval suite catches that regression forever
- Have subject-matter experts triage and validate clustered failure reports before engineering fixes them — clusters can be false positives or intended behavior
- Write recurring domain rules into shared semantic memory: it sharpens the decision boundary for human labelers as well as for the agent

**Avoid:**

- Prompting an LLM to generate ~50 test queries and calling it an eval dataset instead of sampling and mutating real production traffic
- Moving to scaled/crowd raters before the eval criteria and the model have been calibrated — you get large swings in measured quality with no way to attribute them
- Using cheap labor or AI assistance to produce frontier-quality benchmark labels, or treating unfiltered crowdsourced preference voting as ground truth (it can be gamed by hiring voters who identify outputs by watermark)
- Averaging preference labels across raters you have not modeled — the average of two valid tastes is noise, not the right answer
- Shipping any judge score that does not gate a decision; an unused judge score is not a signal
- Manufacturing negative examples by pairing human-made artifacts as 'good' against AI-made as 'bad' — the judge learns to be an AI detector, not a quality detector
- Letting an automated optimizer edit the golden dataset or the scorers — it will make the evals pass by cheating
- Judging holistic subjective qualities (on-brand, writing quality) by prompting an LLM judge, instead of decomposing them into codified, checkable elements
- Not looking at raw data — without it you cannot write meaningful criteria, without criteria no labels, without labels no judge validation
- Reading a single failing run as a defect to fix; measure the failure pattern across many labeled examples first
- Treating expert disagreement on objective attributes as acceptable variance — there it means the data or the guidelines are broken, unlike disagreement on style

## Notable Outliers

- Fine-tune the simulated user on real customer verbatims until the evaluation score goes down — a falling score is evidence the eval got more realistic, not that quality dropped; a 90%+ pass rate was an artifact of an unrealistically polite LLM user. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [15:30](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=930s))
- The specificity of an expert annotator's language is a measurable proxy for how valuable that data point is. ([Ending AI Slop](../talks/ending-ai-slop.md), [12:53](https://www.youtube.com/watch?v=lCBf9slCanI&t=773s))
- A serious 1,000-task agentic coding benchmark costs about $15M to build and ~$5M/year to maintain, because roughly a third of tasks wash out annually as models improve. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s))
- Building the eval forces more rigorous reasoning than doing the analysis yourself — it exposed that many canonical numerical QC thresholds in bioinformatics are arbitrary; each task took three people about a week. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- Across 93 cybersecurity alerts run three times, 25% flip-flopped their verdict; episodic memory made 15% consistent and 10% remained inconsistent — the residue is label ambiguity, not model defect. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s))
- Rubric scores built from path-invariant choke points are associated with verifiable outcomes but only loosely correlated numerically, so they are not yet trustworthy for RL or benchmarking. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [13:46](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=826s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [George Cameron](../speakers/george-cameron.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Nick Heiner](../speakers/nick-heiner.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)

