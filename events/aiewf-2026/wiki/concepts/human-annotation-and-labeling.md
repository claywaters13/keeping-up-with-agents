---
title: "human annotation and labeling"
type: "concept"
slug: "human-annotation-and-labeling"
tier: "supporting"
maturity: "consolidating"
talk_count: 16
speaker_count: 23
---

# human annotation and labeling

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **16** talk(s) by **23** speaker(s)

**Definition:** Sourcing and calibrating human judgments used as ground truth — annotator agreement, expert labeling, and alignment of judges to human labels.

*Also referred to as: human data annotation, expert-annotated evals, human annotation calibration, inter-rater agreement, expert annotation quality, human-in-the-loop labeling, eval rubrics and human feedback, human label alignment*

## State of Practice

The conference treated human labels as the top of the ground-truth chain: LLM judges are downstream artifacts that must be validated against a hand-labeled set, and the recurring failure mode is teams shipping a judge nobody ever checked against a human. The dominant recipe is small and statistical rather than large-scale: hand-label on the order of 100 examples drawn from stratified production traffic, split them train/dev/test, and score the judge as a binary classifier on precision and recall, then keep a sampling pipeline running to track human-vs-LLM agreement drift. In vertical domains the labeler must be a licensed or credentialed expert — clinician, trader, designer, bench scientist — because AI engineers demonstrably cannot tell whether a clinical note, a trade thesis, or a slide is good, and several teams built explicit interfaces (skills, YAML eval configs, rubric adjudication chains) to get expert judgment into CI without engineering in the middle. The field also stopped treating annotator disagreement as noise: disagreement clusters in a gray zone near the decision boundary where no correct label exists, and multiple teams now use cross-run or cross-model disagreement — not model-reported confidence — as the trigger for routing a case to human review. What is unresolved is the label format (binary pass/fail vs. explained vs. pairwise vs. per-rater preference vectors), whether disagreement should be adjudicated into one truth or preserved, and how much of the loop can run without a human once the golden set exists.

## Consensus

### The domain expert, not the AI engineer, must own the definition of 'good' — engineers cannot judge output quality in a vertical domain.

Support: **6** talk(s)

> "the clinical theme owns the definition of good. So vibes don't count here. An accountable judgment from a licensed expert does."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [13:50](https://www.youtube.com/watch?v=O72p-rBb2bA&t=830s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Don’t be data poor](../talks/dont-be-data-poor.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### An LLM judge must be validated against human labels like a classifier — roughly 100 hand-labeled examples, split train/dev/test, scored on agreement — and the agreement rate monitored continuously afterward.

Support: **5** talk(s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)

### Human judgment is still the ground truth that automated evaluation approximates; LLM-as-judge cannot sit at the top of the chain in subjective or high-stakes domains.

Support: **5** talk(s)

> "we believe human judgment is still at a much higher level than any LLM as a judge"
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [9:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=584s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)

### Labeling criteria cannot be fully specified before annotation begins; they are discovered by grading real outputs, and negotiating the rubric is a larger task than writing the eval.

Support: **4** talk(s)

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)

### Annotation is a standing loop, not a one-off pass: production failures are triaged by humans and committed back into the golden dataset so every subsequent change is rescored against them.

Support: **5** talk(s)

> "all the failure modes that we are founding during this investigation step, they will become part of the golden dataset that we mentioned earlier and the eval suite is updated to spot those regressions."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

### Expert annotators disagree in a predictable gray zone near the decision boundary, and that disagreement is information about the label space rather than annotator error.

Support: **3** talk(s)

> "In this case, you'll find that even human experts will have a disagreement on these cases. In fact, there's no right or wrong answer."
>
> — [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [6:31](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=391s)

Supporting talks: [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

## Disagreements

### What label format should human annotators produce — a binary pass/fail verdict, or something richer?

| Position A | Position B |
|---|---|
| Collect binary pass/fail labels tied to a business outcome; binary is what makes a judge calibratable and consistently trainable, and continuous quality scores like 'helpfulness 0.5' are unactionable.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Binary is not enough. Raters must supply explanations of their reasoning (otherwise you learn nothing about where the agent should improve); judges align better when trained on A-vs-B pairwise comparisons than on absolute scores, because humans agree on comparisons but not on scales; and in subjective domains labels should be per-rater preference vectors rather than a single collapsed verdict.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Ending AI Slop](../talks/ending-ai-slop.md)* |

*Why it matters: Label format determines annotation cost per example, how many examples you need for a stable judge, and whether the resulting dataset can be reused for RL or preference training rather than only for pass-rate gating.*

### Should annotator disagreement be adjudicated into a single ground truth, or preserved as legitimate plurality?

| Position A | Position B |
|---|---|
| Drive toward one golden label: write deliberately objective annotation guidelines, and where experts differ, have an independent senior expert adjudicate the competing rubrics into a final one with a further reviewer doing QA. In a clinical edge case one licensed professional defines what correct is.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | For gray-zone and taste-driven cases there is no correct label — the answer depends on the customer's policy or the rater's taste. Averaging preferences across unmodeled raters manufactures noise; the disagreement itself should be retained and attached to rater identity or to an explicit per-customer rule.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)* |

*Why it matters: Adjudicating to one label makes evals cheap and CI-gateable but bakes one reviewer's taste into the product; preserving plurality means your eval score is a distribution, not a number, and shipping decisions need a different gate.*

### Can synthetic data substitute for expensive human-labeled ground truth?

| Position A | Position B |
|---|---|
| Largely yes, if you invert the generation process: sample a label from an explicit symbolic policy and generate the record backwards, so labels are correct by construction and no ground-truth labeling pass is needed. About 90% of datasets can be synthetic, and clinicians in blind review distinguished synthetic from real only ~60% of the time.<br>*[Don’t be data poor](../talks/dont-be-data-poor.md), [Evaling Video Slop](../talks/evaling-video-slop.md)* | No — synthetic data cannot reach the accuracy scale required, and frontier-quality evaluation requires injecting external human expertise that cannot be bought cheaply or generated by models. Obviously synthetic material also raises eval awareness and pushes the model out of distribution, invalidating the measurement.<br>*[200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md)* |

*Why it matters: This is the difference between a five- or six-figure annotation budget and a seven- or eight-figure one, and it decides whether a team can go live before it has customer data or must wait for real labeled traffic.*

### Once human ground truth exists, can the calibration loop run without a human in it?

| Position A | Position B |
|---|---|
| Yes. With human labels frozen as the golden source, retuning can be fully config-driven with no human in the loop, protected by guardrail observability and fast rollback; an agent can likewise optimize against the eval suite autonomously provided it is forbidden from editing the golden datasets or scorers.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents Building Agents](../talks/agents-building-agents.md)* | No. The expert has to adjudicate on every iteration — clustered failures are triaged by human SMEs before fixes, each clinical edge case is scored by a licensed professional and committed into CI, and in finance and pharma the right model is AI-in-the-loop where the expert makes the call and AI only compresses their time.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Don’t be data poor](../talks/dont-be-data-poor.md)* |

*Why it matters: It sets the marginal cost of every improvement cycle, and determines whether a frozen golden set can be trusted to catch drift the original annotators never anticipated.*

## Practical Guidance

**Do:**

- Hand-label ~100 examples with pass/fail, split into train/dev/test, and score the judge on precision and recall against them — you are not training a model, you are using the labels to inform the judge's prompt.
- Sample the labeling set from real production traffic, stratified to be representative, then mutate it to cover golden paths and edge cases.
- Have two experts author rubrics independently, a third adjudicate them into a final rubric, and a fourth do QA on the result — for open-ended clinical answers use required-element rubrics instead of a single golden response.
- Use disagreement across repeated runs or across different models to select cases for human review; treat each disagreement as a labeling opportunity.
- Ask raters for an explanation alongside the verdict, so failures point at what to fix rather than just registering as a failed row.
- Collect pairwise A-vs-B judgments instead of 1-10 absolute scores when the axis is taste-driven, and manufacture the negative side deliberately rather than sampling it.
- Commit each expert-adjudicated edge case into CI so every prompt, model, and guardrail change is rescored against what the expert taught you — fixing one flagged scenario lifts the whole risk category.
- Run short recurring team annotation sessions (10-15 minutes) so judge recalibration data keeps arriving instead of arriving once.
- Report confidence intervals on alignment numbers — 84% vs 88% on 50 traces is not a demonstrated gain — and reserve the expensive statistical rigor for shipping decisions and leadership reporting.
- Tie an expert's commentary to the specific artifact component it refers to (e.g. the code that renders the visual element) — unanchored commentary is noisy data.
- Have domain experts blind-review synthetic data against real data before you trust it as an eval substrate.
- Explicitly forbid any automated optimizer from editing golden datasets or scorers, and train cross-functional raters on how to rate before scaling them up.

**Avoid:**

- Prompting an LLM for ~50 test queries and calling that your eval dataset.
- Shipping an LLM judge whose score does not gate any decision, or that was never compared against a human label at all.
- Using an off-the-shelf frontier model as a user simulator — it is trained to be helpful and produces unrealistically polite, articulate complaints, which is how a 90%+ pass rate turns out to be an artifact.
- Moving to scaled raters before the rubric and the model have stabilized — you get large swings that reflect calibration churn, not quality.
- Averaging preference labels across raters you have not modeled, or treating stylistic disagreement as data to be cleaned up (disagreement on objective attributes like alignment is what signals bad data).
- Trusting the model's self-reported uncertainty to decide which cases go to human review — the model does not know what it does not know.
- Letting AI engineers, rather than domain experts, decide whether vertical output is good; this is where vertical AI projects quietly die.
- Using cheap or unfiltered labor for frontier-quality evaluation — an unfiltered crowd workforce can be hired to vote a leaderboard, and you cannot push the frontier from within the frontier.
- Building rubrics-as-rewards without external expert grounding, which creates an echo chamber where the AI grades itself into agreement.
- Judging quality only from aggregate pass rates — some failures (an agent finding and deleting a legally required disclaimer) are invisible unless a human reads the trace.
- Pairing human-made artifacts as 'good' against AI-made ones as 'bad' when building annotation pairs — you will train an AI detector instead of a quality detector.
- Skipping the raw data. Without looking at it you cannot write criteria, without criteria you cannot label, without labels you cannot evaluate your judges, and then you do not know if the pipeline works.

## Notable Outliers

- Human clinicians score about 81% on the same no-harm rubric where the system scores 99.89% — the human labelers being calibrated against are themselves the weaker grader, because they get tired. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:50](https://www.youtube.com/watch?v=AN65uc645mE&t=1070s))
- Fine-tune your user simulator on real user language until the evaluation score goes down; a falling score is evidence the eval got more realistic, not that quality dropped. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- Writing domain rules into semantic memory improves the consistency of human labelers, not just of the agent. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [17:14](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1034s))
- A serious 1,000-task agentic coding benchmark costs roughly $15M in human expertise to build and ~$5M/year to replace the third of tasks that models wash away annually. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s))
- Each verifiable biology eval task took a group of three scientists about a week to construct, and building the eval forced more rigorous reasoning than doing the analysis itself would have. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [12:39](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=759s))
- In blind review clinicians distinguished synthetic medical records from real ones only about 60% of the time, and generating records backwards from a sampled label removed the ground-truth labeling step entirely. ([Don’t be data poor](../talks/dont-be-data-poor.md), [14:26](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=866s))
- About 450 human-graded tests are needed to be 99% sure of catching a 1% error rate, and ~1,900 to see it caught ten times. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:13](https://www.youtube.com/watch?v=AN65uc645mE&t=1033s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
- [Agents Building Agents](../talks/agents-building-agents.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Don’t be data poor](../talks/dont-be-data-poor.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Anuj Iravane](../speakers/anuj-iravane.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
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
- [Vivek Muppalla](../speakers/vivek-muppalla.md)

