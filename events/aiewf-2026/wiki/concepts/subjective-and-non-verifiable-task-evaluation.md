---
title: "subjective and non-verifiable task evaluation"
type: "concept"
slug: "subjective-and-non-verifiable-task-evaluation"
tier: "supporting"
maturity: "contested"
talk_count: 11
speaker_count: 13
---

# subjective and non-verifiable task evaluation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **11** talk(s) by **13** speaker(s)

**Definition:** Evaluating work with no programmatic ground truth — taste, judgment, and expert-domain quality — where verifiable rewards do not apply.

*Also referred to as: non-verifiable tasks, subjective domain evaluation, expert judgment domains, behavioral evaluation limits, open-ended evaluation, expert-in-the-loop evaluation, human evaluation, pairwise comparison evaluation*

## State of Practice

The field now treats measurability, not model capability, as the binding constraint on subjective domains: code got good because code decomposes, executes, and verifies, and everything without that property lags. The dominant working method is decomposition — break "on brand," "empathetic," "in character," or "clinically safe" into named, individually checkable elements, then grade against that decomposition rather than against a reference artifact, so novel-but-valid answers aren't penalized. Human expert labels are treated as the golden source of truth that models and judges are aligned to, and LLM-as-a-judge is widely described as inadequate on its own for taste-bearing axes; several speakers report it being actively reward-hacked. There is broad distrust of public benchmarks here — IFEval verifiers that don't check what the prompt asks, audio benchmarks recorded in quiet rooms, persona benchmarks that score personality consistency while missing anachronistic compositing, and SWE-bench-style pass/fail that captures a sliver of the actual job. The frontier practice is instrumenting the process rather than only the output: verify how the answer was produced, layer redundant gates, reject on judge low-confidence, and use expert-authored pre-ship gates re-run when the base model changes. What remains genuinely open is whether this is a temporary scaffold on the way to automated verification of taste, or a permanent structural requirement for humans in the loop.

## Consensus

### Human expert judgment, not an automated metric or an LLM judge, is the ground truth that subjective evaluation must be aligned to.

Support: **6** talk(s)

> "we believe human judgment is still at a much higher level than any LLM as a judge"
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [9:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=584s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)

### Holistic judging of a fuzzy quality ('is this on brand', 'is this good writing') fails; the working method is to decompose the quality into named elements that are individually codifiable and checkable.

Support: **5** talk(s)

> "Verifying in general if something's on brand and you can try this uh by prompting an LLM as a judge to do it is quite hard. But once you start picking apart the exact elements that represent what great is, then it suddenly becomes the shape of something that is codifiable and verifiable."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:07](https://www.youtube.com/watch?v=lCBf9slCanI&t=307s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Respect The Process](../talks/respect-the-process.md)

### Existing public benchmarks in these domains measure a proxy that diverges from what practitioners care about, so they cannot be used as evidence of subjective quality.

Support: **5** talk(s)

> "There's nothing in the verifier that checks that a story was written. It just checks that the asky character I is not used more than once, which means that all of these responses get a full score, including response D."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [9:03](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=543s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [Ending AI Slop](../talks/ending-ai-slop.md)

### Building a credible subjective eval requires injecting external domain expertise that cannot be substituted with AI assistance, generic annotators, or cheap labor.

Support: **5** talk(s)

> "Like you can't push the frontier forward from within the frontier. You need to inject that external human expertise and it needs to be good expertise."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [Ending AI Slop](../talks/ending-ai-slop.md)

### Optimizing against a subjective proxy reliably produces reward hacking — the score rises while the underlying quality flattens or degrades — so the gate itself must be treated as an adversarial target.

Support: **4** talk(s)

> "there is a point where you can keep hill climbing on a benchmark and the human eval stays flat. And you can actually take it even further if you want where you keep hill climbing on a benchmark even as the human eval goes down."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [11:17](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=677s)

Supporting talks: [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Respect The Process](../talks/respect-the-process.md)

### Fluency, plausibility, and convincingness are independent of correctness, so surface-level scoring systematically misses the dominant failure mode.

Support: **4** talk(s)

> "Convincingness and fidelity are independent properties. A system can score perfectly on personality consistency and still produce a figure reasoning from knowledge his historical counterpart never possessed."
>
> — [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [9:50](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=590s)

Supporting talks: [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Respect The Process](../talks/respect-the-process.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)

## Disagreements

### Can subjective quality be converted into an automated verifier, or does it structurally require a human expert in the loop indefinitely?

| Position A | Position B |
|---|---|
| Yes — decompose the domain, build RL environments and continuous loss functions around it, and let the system judge and retune itself; Uber runs fully config-driven agent retuning with no human in the loop, DeepMind argues self-play where models generate and judge their own challenges is what produces superhuman coding, and Adaption reports an automated research agent beating its own staff.<br>*["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)* | No — automated metrics structurally cannot adjudicate a relation between output and an external standard (archive, clinical practice, taste), LLMs lack the taste required to judge writing, and contextual/time-dependent/preference-dependent problems should be routed to human judgment rather than into a programmatic RL environment.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Ending AI Slop](../talks/ending-ai-slop.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)* |

*Why it matters: It determines whether your evaluation cost curve bends down over time or stays a permanent per-release expense in expert hours — Surge prices a serious agentic benchmark at $15M plus $5M/year, while Uber's closed loop is designed to need nobody. It also decides whether a subjective capability can be trained via RL at all, or only gated at ship time.*

### For high-stakes subjective domains, do you need a vertically specialized system, or a general-purpose frontier model with the right context and constraints?

| Position A | Position B |
|---|---|
| Specialize: off-the-shelf stacks cannot hit clinical accuracy bars, standard audio encoders trained on monotone audiobooks cannot drive expressive output, and general-purpose AI cannot catch what a domestic violence specialist hears in the first 90 seconds — so build the stack, the embeddings, and the clinical protocols yourself.<br>*[200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)* | Generalize and constrain: general-purpose frontier models outperformed dedicated specialized clinical tools in physician-reviewed evaluation and biomedically fine-tuned models underperformed their own base models; don't constrain how the agent reasons, constrain its effects and anchor it in context rather than in weights.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Respect The Process](../talks/respect-the-process.md)* |

*Why it matters: This is the build-vs-buy decision for every regulated or taste-heavy vertical, and it changes where the audit surface lives: a fine-tuned specialist hides its behavior in weights you cannot version or inspect, while a context-anchored generalist keeps provenance reviewable but inherits the base model's cultural priors.*

### When expert annotators disagree, is that noise to be engineered out or signal to be preserved?

| Position A | Position B |
|---|---|
| Noise — write deliberately objective labeling guidelines to drive raters toward one answer, and where possible pick task formulations whose payload can be measured mechanically (e.g. SQL injection scored by static analysis) precisely so no judgment is involved.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)* | Signal — disagreement on style or aesthetics is good data indicating genuine multi-preference structure, so attach preferences to per-rater vectors instead of averaging; where six experts given identical data diverge by up to 50%, the answer cannot be the target and you must validate the process instead.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Respect The Process](../talks/respect-the-process.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)* |

*Why it matters: Averaging across unmodeled raters is exactly the mechanism that produces collapse-to-the-mean slop, but preserving pluralism means you no longer have a single scalar to hill-climb — you need per-user matching or process validation instead of a leaderboard.*

## Practical Guidance

**Do:**

- Decompose the subjective target into codified elements, then grade the output against that decomposition rather than against the original reference artifact, so novel-but-valid solutions are not penalized
- Sit with the domain expert before writing any prompt and encode what good looks like as hundreds of TDD-style evals; treat one failing safety eval out of tens of thousands of runs as a ship blocker
- Size your eval set to the error rate you care about — roughly 450 tests to be 99% confident of catching a 1% error rate, and ~1,900 to observe it ten times
- Log every stage of the orchestration in a flat, human-readable structure before attempting any optimization or self-learning loop
- Pick recall as the guardrail metric wherever letting a bad artifact through is worse than an unnecessary intervention, and reject rather than publish when the judge is low-confidence
- Verify the process that produced the answer, not just the answer, and have the harness independently confirm that claimed edits actually landed
- Emit deterministic structured review artifacts that non-engineers can validate, instead of expecting domain reviewers to read agent-written code
- Explicitly exclude voice/style authenticity as a scoring axis when the property you actually care about is substantive fidelity
- Attach preferences to per-rater preference vectors and force distribution across expert styles, rather than averaging labels into a single consensus
- Tie expert commentary to the specific artifact component it refers to (e.g. the code that renders the visual element) to cut label noise
- Slice production eval results by segment — geography, device type, item type — so tuning targets the specific underperforming population
- Layer redundant, overlapping QA gates on the Swiss cheese model and accept the cost as the price of lower escape probability
- Buy a small volume of expensive high-taste expert data over a large volume of cheap noisy data
- Use the product yourself in emotionally loaded conditions — evals do not substitute for a human read on tone

**Avoid:**

- Prompting an LLM judge for a holistic verdict on brand adherence, writing quality, or taste — models do not have the taste to score these and the judge gets hacked
- Citing public leaderboards or popular benchmarks as evidence of subjective quality; contamination is the default outcome and crowdsourced arenas can be gamed by hiring voters against watermarked outputs
- Building eval sets from obviously synthetic data, which raises eval awareness and pushes the model out of distribution, invalidating the measurement
- Optimizing session count, session length, or emotional reliance as a quality proxy in therapeutic or relationship products — the clinically correct direction is the user needing the product less
- Reading ~80% benchmark saturation as exhausted headroom; the unsolved remainder is often broken tasks that also bias model rankings
- Relying on synthetic data alone to reach high accuracy bars in expert domains
- Fine-tuning a persona or specialist into the weights when context-window anchoring would preserve provenance, versioning, and auditability
- Handing an agent a general-purpose VM, which invites it to route around your instructions using whatever tools it finds there
- Spending compute enhancing an artifact that is already good — you pay for zero quality lift and risk degrading it
- Treating sycophantic agreement as a polish issue rather than a domain failure mode with downstream consequences
- Assuming a statically tuned offline judge or router will hold up in production without a retuning mechanism for online drift

## Notable Outliers

- On the identical harm rubric used to score humans, the Polaris system reaches 99.89% no-harm accuracy against roughly 81% for human clinicians — because AI systems do not get tired and are backed by 30+ supervisor models. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:50](https://www.youtube.com/watch?v=AN65uc645mE&t=1070s))
- Six experts given the exact same data on the exact same bottle of wine produced answers varying by up to 50%, which is why the answer cannot be the validation target. ([Respect The Process](../talks/respect-the-process.md), [1:05](https://www.youtube.com/watch?v=CLttOU7n6sI&t=65s))
- A serious 1,000-task agentic coding benchmark costs about $15M to build and ~$5M/year to maintain as a third of tasks wash out annually. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s))
- Expert disagreement is diagnostic: disagreement on objective attributes like alignment means bad data, while disagreement on style or aesthetics is valuable signal about genuine preference structure. ([Ending AI Slop](../talks/ending-ai-slop.md), [14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s))
- For role-playing systems the word 'agent' is itself an error, because it locates the persona in the weights where it cannot be inspected, versioned, or handed to a qualified reviewer — the persona is the configuration, not the checkpoint. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [24:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1459s))
- Self-play — models generating their own coding challenges and judging the answers — is what will produce superhuman coding, with compute and self-play time as the only limiting factors. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [10:18](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=618s))
- SQL injection was deliberately chosen as the research payload over subjective harms precisely because static analysis measures it objectively with no LLM judge in the loop. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [5:04](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=304s))
- Non-verifiable tasks, not verifiable ones, are where the bulk of everyday value and the next year of progress lie. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [8:55](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=535s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
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
- [Clay Cockrell](../speakers/clay-cockrell.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Nick Heiner](../speakers/nick-heiner.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Tony Fabrikant](../speakers/tony-fabrikant.md)
- [Vivek Muppalla](../speakers/vivek-muppalla.md)

