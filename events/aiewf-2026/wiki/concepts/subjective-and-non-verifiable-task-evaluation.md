---
title: "subjective and non-verifiable task evaluation"
type: "concept"
slug: "subjective-and-non-verifiable-task-evaluation"
tier: "supporting"
maturity: "contested"
talk_count: 8
speaker_count: 9
---

# subjective and non-verifiable task evaluation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **8** talk(s) by **9** speaker(s)

**Definition:** Evaluating work with no programmatic ground truth — taste, judgment, and expert-domain quality — where verifiable rewards do not apply.

*Also referred to as: non-verifiable tasks, subjective domain evaluation, expert judgment domains, behavioral evaluation limits, open-ended evaluation, expert-in-the-loop evaluation, human evaluation, pairwise comparison evaluation*

## State of Practice

The field has converged on a diagnosis: the reason models excel at code and math is a property of those domains — decomposable, executable, checkable — not a property of the models, and the bottleneck in taste-, judgment-, and expert-domain work is measurement rather than capability. The dominant working technique is decomposition: refuse the holistic 'is this good?' judgment, break the target into codified sub-criteria (brand elements, documentary-record constraints, per-segment slices), and grade against that decomposed ground truth rather than against a reference artifact, so novel-but-valid outputs aren't penalized. Naive LLM-as-a-judge is broadly distrusted for quality verdicts — speakers report it lacks taste in writing, cannot adjudicate archival fidelity, and is reward-hackable — while human expert judgment is treated as the anchor, though speakers disagree sharply on whether that anchor should be aggregated into consensus labels or preserved as per-rater preference vectors. Everyone who deployed something reports the same failure signature: optimize against an imperfect subjective proxy and the system oversteers into safe, generic, mean-collapsed output that scores well and is worse — Uber's edit agent producing pixel-different but meaningless enhancements, benchmaxxed models winning LMArena with nested bullets and emojis, 'AI slop' as distribution collapse. Second-order consensus: the final answer is not enough evidence, so process, trajectory, and provenance must be verified independently — Watershed validates the graph-edit script rather than the agent's claim, LexisNexis shows behavioral output monitors are structurally blind to backdoors. What is unresolved is the big one: whether subjective evaluation is a hard problem that decomposition and RL environments will eventually automate, or a category that structurally requires a domain expert in the loop forever.

## Consensus

### Verifiability is a property of the domain, not of the model — code and math are tractable because they execute and decompose, and subjective domains are hard because they lack that structure, so measurement (not model capability) is the binding constraint.

Support: **4** talk(s)

> "we treat for example the fact that code is verifiable and measurable as something that is a property about models and models are great at at coding um because we've made them great at coding but realistically it's actually a fact about code."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [1:57](https://www.youtube.com/watch?v=lCBf9slCanI&t=117s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Respect The Process](../talks/respect-the-process.md)

### Naive LLM-as-a-judge cannot validly score subjective quality; expert human judgment remains the reference standard that automated graders are approximating, not replacing.

Support: **4** talk(s)

> "we believe that writing is just too rich and deep and nuanced and frankly human of an activity to measure with mechanical benchmarks and LM as a judge doesn't really work either because LLMs don't have good taste in writing"
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [15:22](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=922s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Optimizing against a proxy for subjective quality reliably produces reward hacking — outputs that satisfy the grader while getting worse on the thing the grader stands in for — so the verifier must be designed to be robust to that pressure, not just accurate on average.

Support: **4** talk(s)

> "Gradient descent is basically like water flowing downhill looking for the path of least resistance. And so your verifiers need to be robust to that."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [5:41](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=341s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Respect The Process](../talks/respect-the-process.md)

### In genuinely subjective domains there is no single ground-truth answer — qualified experts disagree with each other on the same input, and that spread is a real feature of the domain rather than measurement error to be eliminated.

Support: **4** talk(s)

> "six experts were given the exact same data on the exact same bottle of wine and despite having all access to the exact same things, they came to answers that varied by up to 50%"
>
> — [Respect The Process](../talks/respect-the-process.md), [1:05](https://www.youtube.com/watch?v=CLttOU7n6sI&t=65s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [Ending AI Slop](../talks/ending-ai-slop.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

### When the final answer cannot be fully verified, you must verify the process that produced it — trajectory logs, provenance, and independent confirmation that claimed work actually landed — because output-level checks pass on systems that are wrong for reasons the output does not expose.

Support: **4** talk(s)

> "you have to verify the process in addition to the answer because the answer is really only justified in so far as it the process that produced that answer is correct"
>
> — [Respect The Process](../talks/respect-the-process.md), [0:33](https://www.youtube.com/watch?v=CLttOU7n6sI&t=33s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

### Decompose the fuzzy quality target into named, individually checkable elements instead of asking a judge for a holistic verdict; the decomposition is the hard part and doing it is most of the work.

Support: **3** talk(s)

> "Verifying in general if something's on brand and you can try this uh by prompting an LLM as a judge to do it is quite hard. But once you start picking apart the exact elements that represent what great is, then it suddenly becomes the shape of something that is codifiable and verifiable."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:07](https://www.youtube.com/watch?v=lCBf9slCanI&t=307s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

## Disagreements

### Can subjective quality evaluation be decomposed until it becomes programmatically verifiable, or does it structurally require a domain expert in the loop indefinitely?

| Position A | Position B |
|---|---|
| Subjective domains are not a different category, just an unsolved measurement problem: pick apart what 'great' means into codified elements, turn them into RL environments and closed-loop graders, and automate the tuning — Uber runs config-driven agent retuning with explicitly no human in the loop, and DeepMind expects self-play where models generate and judge their own challenges to produce superhuman results.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | Automated metrics structurally cannot adjudicate these judgments because the criterion lives outside anything the metric can see (the archive, the reader's taste, the expert's context); the expert is a build-time and gate-time requirement, and the correct response to unverifiable answers is to constrain the system's effects and produce artifacts a human can validate, not to build a better automatic scorer.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Respect The Process](../talks/respect-the-process.md)* |

*Why it matters: It determines whether you spend budget on eval infrastructure and RL environments or on recruiting and retaining scarce expert reviewers, and whether 'human in the loop' is a temporary scaffold you plan to remove or a permanent line item in the product's unit economics.*

### Are aggregated human labels the golden ground truth for subjective tasks, or does aggregating across raters destroy the signal?

| Position A | Position B |
|---|---|
| Collect human labels on a representative stratified sample under deliberately objective guidelines, treat the resulting consensus as the golden source of truth, and align models and judges to it; hire vetted professionals and pay for quality rather than minimizing cost.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)* | Averaging preference across unmodeled raters manufactures noise and a mean that nobody actually wants — preferences should be attached to per-rater preference vectors — and human preference data is itself contaminated, since raters' frameworks were formed by the same dominant narratives the model absorbed, so RLHF amplifies the error rather than correcting it.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)* |

*Why it matters: If aggregation is valid you can build one eval and one aligned model; if it isn't, the eval must be conditioned on who is judging and for whom, and a single leaderboard number for a subjective task is meaningless by construction.*

### Should subjective quality be pushed into the model's weights via training, or held outside the model in context and harness constraints?

| Position A | Position B |
|---|---|
| Invest in training: build the data and RL environments for non-verifiable tasks, co-optimize data quality with the model, and use self-play so the model internalizes the standard — post-training on non-verifiable tasks is where the next year of returns lives.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | Keep the standard outside the weights: fine-tuning buries a thin signal under vast pre-training sediment in a form no longer open to audit, and specialized fine-tunes have been measured underperforming their general-purpose bases — put the source material in the context window and enforce correctness at the harness boundary with typed interfaces and a deterministic final validation pass.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Respect The Process](../talks/respect-the-process.md)* |

*Why it matters: The two paths have opposite cost curves and opposite auditability properties: training buys quality you cannot inspect or version, while context-and-harness buys inspectable, reversible behavior at recurring inference and engineering cost.*

## Practical Guidance

**Do:**

- Decompose the subjective target into named elements (brand components, documentary constraints, per-attribute checks) and grade outputs against the decomposition, not against the original reference artifact, so a novel-but-valid solution is not scored as a miss.
- Log every stage of the agent orchestration in a flat, human-readable JSON structure before attempting any optimization — without it there is nothing to tune and no basis for a self-learning loop.
- Pick guardrail metrics from the asymmetry of the errors: Uber uses recall on the routing agent because letting a bad image through is worse than a wasted enhancement, and enhancing an already-good image costs compute for zero lift while risking degradation.
- Use pass@K as the metric for self-correcting QA-and-edit loops, and require pass rate to rise with iteration count.
- Reject and withhold rather than publish when the judge is not confident on a multimodal check such as item count.
- Slice production evaluation by geography, device type, and item type so tuning can target the specific underperforming segment.
- Constrain the agent's effects rather than its reasoning: route all state-changing code through a typed SDK that is the only door, then run a deterministic validation script at agent completion — Watershed reports internal evals moving from ~43% to 92%.
- Independently verify that claimed edits actually landed; agents will report completed work they did not do.
- Emit structured, deterministic review artifacts a non-engineer can check, instead of asking domain users to read agent-written code.
- Attach preference data to per-rater preference vectors instead of averaging, and treat expert disagreement on style or aesthetics as signal while treating disagreement on objective attributes as a data-quality defect.
- Tie expert commentary to the specific code component that produces the visual element being critiqued — models struggle to connect the two on their own, and the linkage materially reduces label noise.
- Score reasoning against the source record and explicitly exclude voice or rhetorical authenticity as a scoring axis, since rewarding 'it sounds right' validates the exact failure the instrument exists to catch.
- Pre-register the instrument and its predictions before the data exists, and re-run the expert-built gate whenever the base model changes.
- When designing a research or eval payload, prefer one measurable by static analysis (LexisNexis chose SQL injection precisely to avoid needing an LLM judge) over a subjectively-scored harm.
- In subjective domains prefer a smaller volume of expensive high-taste data over large volumes of cheap noisy data.
- Negotiate the definition of a 'better' output with product, design, policy, and legal, then encode that definition directly into the evals.

**Avoid:**

- Prompting an LLM as a judge for a holistic verdict ('is this on brand?', 'is this well written?') — it fails on exactly the judgments you most want automated.
- Assuming personality-consistency or fluency scores measure fidelity; a system can hit 80.7% persona alignment while reasoning from knowledge the figure never had.
- Shipping a statically tuned offline grader or model into production with no mechanism to retune against online drift.
- Treating public benchmark numbers as clean — contamination is the default outcome, not an occasional lapse, and model cards generally do not disclose it.
- Building eval data that is obviously synthetic; it raises eval awareness and pushes the model out of distribution, invalidating the measurement.
- Continuing to hill-climb a benchmark past the point where human eval flattens — it can keep rising while human quality actively declines.
- Reading a claimed ~80% benchmark saturation as exhausted headroom; a large share of the remaining tasks are typically broken, and that broken remainder biases model rankings.
- Trusting unfiltered crowdsourced preference arenas as a quality signal — with no workforce filtering they can be gamed by hiring voters who identify outputs via model watermarks.
- Handing an agent a general-purpose VM, which invites it to route around your instructions with whatever tools it finds there (writing Python when told to write TypeScript).
- Fine-tuning to instill a subjective standard when auditability matters — it layers a thin signal over the base weights' existing bias in a form that can no longer be inspected, versioned, or reviewed.
- Assuming a time-locked or period-restricted model solves contamination; it relocates the contamination to an earlier textual moment rather than removing it.
- Building highly specified function-call tools for structured-data exploration and expecting them to scale past a handful of objects — schema hallucination and context exhaustion set in.
- Letting the system collapse to the modal answer: in creative and design work the most likely output is not the optimal one, and the mean is what 'slop' actually is.

## Notable Outliers

- Within about a year, generated code will ship without any human reading it, the same way nobody inspects compiler assembly output — a direct rejection of human-review-as-the-quality-gate. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [11:42](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=702s))
- A serious 1,000-task agentic coding benchmark costs about $15M to build and ~$5M/year to maintain, because roughly a third of tasks wash out annually as models improve. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s))
- For role-playing systems the word 'agent' is itself an error, because it locates the persona in the weights where it cannot be inspected, versioned, or handed to a qualified reviewer — the persona is the configuration, not the checkpoint. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [24:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1459s))
- The specificity of an expert's language is a measurable proxy for how valuable that data point is. ([Ending AI Slop](../talks/ending-ai-slop.md), [12:53](https://www.youtube.com/watch?v=lCBf9slCanI&t=773s))
- Benchmarks should include open-ended problems with continuous loss functions — e.g. 'write the best lossless compressor for this 10MB of code', scored on compressed size plus source size — to force models to invent novel algorithms rather than pass unit tests. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s))
- The documented correct-answer/correct-reasoning gap in verifiable math domains is strictly worse in domains where the answer cannot be fully verified. ([Respect The Process](../talks/respect-the-process.md), [6:48](https://www.youtube.com/watch?v=CLttOU7n6sI&t=408s))
- Non-verifiable tasks, not verifiable ones, are where the bulk of everyday value and the next year of progress lie. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [8:55](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=535s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Respect The Process](../talks/respect-the-process.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

## Speakers

- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Nick Heiner](../speakers/nick-heiner.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)

