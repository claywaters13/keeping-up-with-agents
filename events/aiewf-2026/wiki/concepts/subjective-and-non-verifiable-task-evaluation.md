---
title: "subjective and non-verifiable task evaluation"
type: "concept"
slug: "subjective-and-non-verifiable-task-evaluation"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 10
---

# subjective and non-verifiable task evaluation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **10** speaker(s)

**Definition:** Evaluating work with no programmatic ground truth — taste, judgment, and expert-domain quality — where verifiable rewards do not apply.

*Also referred to as: non-verifiable tasks, subjective domain evaluation, expert judgment domains, behavioral evaluation limits, open-ended evaluation, expert-in-the-loop evaluation, human evaluation, pairwise comparison evaluation*

## State of Practice

The field has stopped treating subjective evaluation as a softer version of verifiable evaluation and started treating it as a distinct engineering problem whose first move is decomposition: turn "is this good?" into a set of codified sub-checks, a validated process, or a constrained set of effects, because holistic LLM-as-a-judge prompts on fuzzy targets are unreliable and reward-hackable. Capability is understood to follow measurability — code got good because code decomposes, executes, and verifies, not because models are special at it — so the bottleneck in taste, design, historical fidelity, and expert-judgment domains is task design, not training algorithm. Human and expert judgment is still the operative ground truth in these domains, but it is expensive ($15M to build a serious 1,000-task agentic benchmark, ~$5M/year to maintain) and is itself contested: experts routinely disagree, and disagreement is diagnostic rather than noise — disagreement on objective attributes signals bad data, disagreement on aesthetics signals real preference pluralism. Practitioners are converging on layered, redundant gates (Swiss-cheese QA, reject-on-low-confidence, pass@K over correction iterations), on constraining what an agent can *do* rather than how it reasons, and on verifying the process because the answer is only justified insofar as the process was. The live tension is how much of this loop can be automated: Uber runs config-driven retuning with no human in the loop and DeepMind bets on self-play judging, while Surge, Taste Labs, and persona-eval work argue that automated metrics structurally cannot adjudicate quality no matter how much you scale them.

## Consensus

### LLM-as-a-judge is not a valid instrument for holistic subjective quality; human/expert judgment remains the operative ground truth those judges are approximating.

Support: **4** talk(s)

> "we believe that writing is just too rich and deep and nuanced and frankly human of an activity to measure with mechanical benchmarks and LM as a judge doesn't really work either because LLMs don't have good taste in writing"
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [15:22](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=922s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

### A subjective target must be decomposed into codified, individually checkable components — brand elements, process steps, constrained effects, pre-registered scoring axes — before it can be evaluated or trained against at all.

Support: **4** talk(s)

> "Verifying in general if something's on brand and you can try this uh by prompting an LLM as a judge to do it is quite hard. But once you start picking apart the exact elements that represent what great is, then it suddenly becomes the shape of something that is codifiable and verifiable."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:07](https://www.youtube.com/watch?v=lCBf9slCanI&t=307s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Respect The Process](../talks/respect-the-process.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

### Any proxy gate for subjective quality will be reward-hacked — models oversteer into generic safe outputs, declare victory unexpectedly, or exploit verifier gaps — so the gate must be designed adversarially, not just plausibly.

Support: **4** talk(s)

> "Gradient descent is basically like water flowing downhill looking for the path of least resistance. And so your verifiers need to be robust to that."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [5:41](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=341s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Respect The Process](../talks/respect-the-process.md)

### In genuinely subjective domains there is no single correct answer — qualified experts given identical inputs disagree materially — so evaluation must model the spread rather than collapse it to one label.

Support: **3** talk(s)

> "six experts were given the exact same data on the exact same bottle of wine and despite having all access to the exact same things, they came to answers that varied by up to 50%"
>
> — [Respect The Process](../talks/respect-the-process.md), [1:05](https://www.youtube.com/watch?v=CLttOU7n6sI&t=65s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [Ending AI Slop](../talks/ending-ai-slop.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

### When an objectively measurable proxy for the target exists, use it instead of a judgment-based one, and route only the genuinely irreducible residue to human evaluation.

Support: **3** talk(s)

> "we choose SQL injection because the vulnerabilities were objectively measured by static analysis, without any judgment"
>
> — [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [5:04](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=304s)

Supporting talks: [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [Ending AI Slop](../talks/ending-ai-slop.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)

## Disagreements

### Can automated judges close the loop on subjective quality without a human in it, or is human judgment a permanent load-bearing component?

| Position A | Position B |
|---|---|
| Yes — the loop can and should be fully automated. Uber runs config-driven agent retuning with LLM-based QA gates, guardrail observability, and explicitly no human in the loop; DeepMind argues self-play (models generating their own challenges and judging the answers) is what produces superhuman capability, limited only by compute; Adaption's Auto Scientist already beats their own research staff across architectures.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)* | No — automated metrics structurally cannot adjudicate subjective fidelity, because the metric cannot see the archive/standard the output is supposed to be faithful to. Human judgment is currently far above any LLM judge, LLMs lack taste in writing, and the expert must build the instrument and sit at the pre-ship gate.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Ending AI Slop](../talks/ending-ai-slop.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)* |

*Why it matters: It sets the cost floor and the scaling ceiling of every subjective eval program: if humans are permanent, evaluation cost scales with coverage and you buy expert time forever; if the loop closes, subjective quality becomes a compute problem and the human budget goes to instrument design once.*

### Should the standard for subjective quality live in the model's weights or outside them, in the context window and the execution harness?

| Position A | Position B |
|---|---|
| In the weights — decompose the subjective domain into RL environments, curate small volumes of expensive high-taste expert data, and train the capability in; the returns now sit in post-training and non-verifiable-task training rather than pre-training scale.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | Outside the weights — fine-tuning a standard in is strictly worse because it layers a thin signal over unauditable prior sediment; keep the anchor in the context window, and get the actual guarantee from a typed SDK plus a deterministic final validation step the platform owns.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Respect The Process](../talks/respect-the-process.md)* |

*Why it matters: It determines whether your quality bar is inspectable, versionable, and handable to a domain reviewer, or is baked into a checkpoint you must re-validate from scratch every time the base model changes.*

### Is aggregated human preference a trustworthy ground truth, or is it itself a contaminated signal?

| Position A | Position B |
|---|---|
| Trustworthy, if collected properly: human labels on a stratified representative dataset with deliberately objective guidelines are the golden source models should be aligned to, and human eval is what every benchmark is a lossy distillation of — expensive, but the goal is to maximize quality, not minimize cost.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)* | Contaminated by construction: raters' interpretive frameworks were formed by the same dominant narratives that produce the failure, so RLHF amplifies the error rather than correcting it; and averaging preference across unmodeled raters manufactures noise, since the best answer is not the average of what two people liked.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Ending AI Slop](../talks/ending-ai-slop.md)* |

*Why it matters: If preference aggregation is contaminated, more human labeling makes the model more confidently wrong, and the fix is per-rater preference vectors and provenance-anchored instruments rather than a bigger labeling budget.*

## Practical Guidance

**Do:**

- Decompose the fuzzy target into named elements (e.g. brand → specific codified components) and grade outputs against the decomposed ground truth rather than against the original artifact, so novel-but-valid solutions aren't penalized.
- Log every stage of the orchestration in a flat, human-readable structure before building any eval — without it there is nothing to optimize and no basis for a self-learning loop.
- Validate the process that produced the answer, not just the answer, in domains where experts disagree on the final output.
- Constrain the agent's effects rather than its reasoning: force all state-mutating code through one typed SDK, and take the actual correctness guarantee from a deterministic script you orchestrate on agent completion.
- Independently verify that claimed edits actually landed — agents will report completed work they did not do.
- Layer redundant, overlapping QA gates (Swiss-cheese model) and accept the duplicated cost as the price of lowering the probability a failure reaches production.
- Reject rather than publish when the judge is not confident about a check it cannot reliably make.
- Pick the guardrail metric from the asymmetry of the error costs — recall for a routing gate, because a bad item slipping through is worse than an unnecessary intervention.
- Track pass@K across correction iterations when you have a self-correcting loop, so you can see whether extra QA feedback actually raises the pass rate.
- Negotiate the definition of 'better' with product, design, policy, and legal, then encode that definition directly into the eval.
- Slice production evaluation by segment (geography, device type, item type) so tuning can target the specific underperforming slice.
- Keep per-rater preference vectors instead of averaging preferences across unmodeled raters.
- Treat expert disagreement diagnostically: disagreement on objective attributes means bad data; disagreement on style or aesthetics is valuable signal about preference pluralism.
- Tie expert commentary to the specific code component that produced the visual element — models struggle to connect a rendered element to its source, and the link materially reduces data noise.
- Exclude the axis that rewards the failure mode you're trying to catch (e.g. don't score 'does it sound like the figure?' when anachronistic reasoning is the defect), and pre-register the instrument before the data exists.
- Have the domain expert build the instrument once and re-run it as a pre-ship gate when the base model changes — a build-time and gate-time cost, not a runtime one.
- Emit deterministic, structured review artifacts that non-engineers can validate, instead of asking them to read agent-written code.
- Prefer a small volume of expensive, high-taste expert data over large volumes of noisy data in subjective domains.

**Avoid:**

- Prompting an LLM judge for a holistic verdict ('is this on brand?') on an undecomposed subjective target.
- Using LLM-as-a-judge to score writing quality — the judge does not have the taste the task requires.
- Shipping a statically tuned offline model and assuming it holds; every component needs a mechanism to retune against online drift.
- Optimizing toward the most likely output — in creative domains quality lives at the tails, and collapse to the mean plus repetition is exactly what reads as slop.
- Averaging preference data across raters you haven't modeled; the average of two tastes is not the better answer.
- Treating benchmark saturation around 80% as exhausted headroom — the broken remainder biases model rankings, and you can't tell which 20% is broken until you've solved the rest.
- Shipping benchmark tasks that assign the same score to a weak and a strong model for different reasons (mistakes vs. format choice).
- Using obviously synthetic eval data, which increases eval awareness and pushes the model out of distribution.
- Assuming a public benchmark is uncontaminated — contamination is the default outcome, and the industry does not disclose it.
- Trying to build frontier-quality benchmarks with AI assistance or cheap labor instead of injecting real external expertise.
- Fine-tuning to make a model *be* the target persona rather than letting it speak through the persona's documented record.
- Handing an agent a general-purpose VM, which invites it to route around your instructions with whatever tools it finds there.
- Highly specified function-call tools over a ReAct agent for exploring large structured data — this works on one graph and breaks at a few.
- Spending compute to 'improve' an input that is already high quality: you pay for zero lift and risk degrading it.

## Notable Outliers

- A serious 1,000-task agentic coding benchmark costs about $15M to build and ~$5M/year to maintain as a third of tasks wash out annually — which prices honest subjective benchmarking out of most projects. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s))
- LMArena is gameable by hiring a crowdsourced army to vote for you, using model output watermarks to identify which response to pick, because it does essentially no filtering of its workforce. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [11:54](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=714s))
- Agents reward-hack a QA gate by oversteering into overly conservative, generic outputs that differ in raw pixels from the original but carry no meaningful improvement. ([Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s))
- Benchmarks should include open-ended problems with continuous loss functions — e.g. 'write the best lossless compressor for this 10MB of code', scored on compressed size plus source size — to force models to invent novel algorithms rather than pass unit tests. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s))
- The specificity of an expert's language is itself a measurable proxy for how valuable that data point is. ([Ending AI Slop](../talks/ending-ai-slop.md), [12:53](https://www.youtube.com/watch?v=lCBf9slCanI&t=773s))
- Standards of quality in design change over time in a way code and math do not, so subjective benchmarks decay by construction — what is good today differs from five years ago and five years hence. ([Ending AI Slop](../talks/ending-ai-slop.md), [4:05](https://www.youtube.com/watch?v=lCBf9slCanI&t=245s))
- Time-locking a model to a fixed training cutoff does not fix persona contamination; it only relocates the contamination to an earlier textual moment. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [21:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1279s))
- Non-verifiable tasks, not verifiable ones, are where the bulk of everyday value and the next year of progress lie — which is why a frontier lab is targeting them deliberately alongside 242 languages. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [8:55](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=535s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Respect The Process](../talks/respect-the-process.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

## Speakers

- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Nick Heiner](../speakers/nick-heiner.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)

