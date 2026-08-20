---
title: "Shipping AI to a Million Patients Without an A/B Test"
type: "talk"
slug: "shipping-ai-to-a-million-patients-without-an-ab-test"
track: "AI in Healthcare"
org: "Ufonia"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "McknwOzbmyg"
duration_sec: 1154
word_count: 3617
speakers: ["Jared Joselowitz"]
---

# Shipping AI to a Million Patients Without an A/B Test

**Speakers:** [Jared Joselowitz](../speakers/jared-joselowitz.md)

**Org:** Ufonia

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 19m 14s

[Watch on YouTube](https://www.youtube.com/watch?v=McknwOzbmyg)

## Summary

Jared Joselowitz, a research engineer at Ufonia, explains how his team proves the safety of Dora — a voice AI agent that phones patients for post-op follow-ups and pre-op checks — when the usual ship-small/watch-dashboard/roll-back playbook is unavailable. Because Dora asks about symptoms and gives advice, it is a regulated medical device, and A/B testing patients into a worse variant would be unethical and illegal; a call that has happened cannot be rolled back. Ufonia's answer, borrowed from self-driving cars, is simulation-first: a framework called Matrix pairs an LLM 'PatBot' playing conditioned patient scenarios against Dora, and a validated LLM judge ('BehJudge') grades transcripts against a documented hazard list, scoring an F1 of 0.96 against ten clinicians. Grading alone doesn't improve the product, so failures feed a GEPA-style prompt optimizer with a clinician-defined cost matrix that deliberately over-weights sensitivity to red flags. Worth watching if you ship AI where being wrong for a few users is not an acceptable cost, or if you want a concrete pattern for replacing canary deploys with simulation gates plus staged, evidence-earned autonomy.

## Key Points

- The standard de-risking playbook — ship to 5%, watch dashboards, roll back — silently assumes you can afford to be wrong for a while, an assumption that collapses when the user is a patient and a red dashboard means someone was already harmed.
- Because Dora asks about symptoms and gives medical advice, it legally counts as a medical device, so regulation reduces to three questions: what does the software do, what could go wrong, and how do you ensure it doesn't.
- Ufonia starts safety work from an enumerated hazard list (missed red flags like sudden vision loss, hallucinated answers, ignored patient distress — 20 to 40 documented hazards) rather than from model benchmarks.
- The Matrix framework simulates clinical conversations with an LLM-played 'PatBot' conditioned on scenarios grounded in real clinical workflows; simulated patients are used instead of hired actors purely because actors don't scale to fast iteration.
- PatBot realism was validated with a patient and public involvement study: in three of four side-by-side comparisons, most real patients judged the simulated patient more realistic than the real one — while confirming there is no single 'realistic patient' persona to target.
- The LLM judge was validated against 240 labelled examples reviewed by ten clinicians across ten specialties, reaching F1 0.96 (Gemini 2.5 Pro at the time of the paper) with near-perfect sensitivity — the metric clinicians care about, since over-calling hazards is cheap and missing them is catastrophic.
- Manual prompt engineering is rejected as non-reproducible and brittle — formatting changes alone have swung benchmarks by 76 percentage points — and replaced with automated prompt optimization (GEPA, from the DSPy authors), which turns hours-to-days of tuning into 30–60 minutes with an audit trail.
- The reactive ship/watch/rollback loop is replaced by a flywheel: real call data plus synthetic edge cases → prompt optimization → Matrix as a simulation safety gate → gated deploy, with every new call feeding back into the dataset.
- Simulation is necessary but not sufficient — it is the inner loop that earns the right to a staged outer loop of user testing, supervised clinical evaluation with clinicians in the loop, and monitored deployment, where autonomy is granted in proportion to accumulated evidence.
- The same black-box method transfers to new modalities: voice introduces failure modes like back-channeling and interruptions that make weak models abandon safety advice mid-sentence, but the hazard-enumerate-simulate-judge framework itself doesn't change.

## Notable Quotes

> "you can't actually AB test on patients of course. Randomizing patients into a worse variant is unethical and often illegal."
>
> — [0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s) &middot; *States the core constraint the entire talk is built around.*

> "you can't undo a call. Once Dora says it, it's been said and there is no rollback."
>
> — [0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s) &middot; *Names the second missing safety net — irreversibility — in one line.*

> "And very importantly the model card won't save you. Um you can't claim like some model vendors said that they have 92% on some benchmark."
>
> — [0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s) &middot; *A direct swipe at vendor benchmarks as a regulatory defense.*

> "so far we've done around 200,000 real clinical calls within the UK across 20 hospitals. And we are contracted to scale to a million patients in the next 2 years."
>
> — [1:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=85s) &middot; *Establishes the deployment scale that makes the safety argument concrete.*

> "Roll back. You can't really roll back. The call has already happened. The person has already been harmed."
>
> — [4:46](https://www.youtube.com/watch?v=McknwOzbmyg&t=286s) &middot; *The sharpest statement of why canary deploys break in healthcare.*

> "Well, they didn't just drive around crashing into walls and say, "We won't do that again." and then doing another RL loop."
>
> — [5:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=318s) &middot; *The self-driving analogy that motivates simulation-first development.*

> "Simulation is only the real ethical option we can go with. You can't run all the hazard the hazards I just mentioned on real people as a first grasp."
>
> — [5:56](https://www.youtube.com/watch?v=McknwOzbmyg&t=356s) &middot; *Frames simulation as an ethical requirement rather than a convenience.*

> "We use a simulated patient and not a hired actor because hired actors don't scale."
>
> — [6:29](https://www.youtube.com/watch?v=McknwOzbmyg&t=389s) &middot; *Names the explicit tradeoff behind synthetic user simulation.*

> "In three out of the four, the majority of people actually thought that the simulated patient was more realistic."
>
> — [8:27](https://www.youtube.com/watch?v=McknwOzbmyg&t=507s) &middot; *Reports the counterintuitive validation result for the patient simulator.*

> "The top model, which as of a year ago when we wrote the paper, was Gemini 2.5 Pro. Now we've maybe updated the models. Um it achieved an F1 score of of 0.96."
>
> — [10:13](https://www.youtube.com/watch?v=McknwOzbmyg&t=613s) &middot; *The headline number for LLM-judge-versus-clinician agreement.*

> "You would rather overcall hazards that aren't there than undercall hazards that are there."
>
> — [10:51](https://www.youtube.com/watch?v=McknwOzbmyg&t=651s) &middot; *The asymmetric-cost principle that drives their whole metric design.*

> "grading isn't technically improving the product. A pile of pass/fails tells you where Dora breaks and where it's not safe, but doesn't actually make the product better."
>
> — [10:51](https://www.youtube.com/watch?v=McknwOzbmyg&t=651s) &middot; *The pivot from evaluation to optimization, and a critique of eval-only stacks.*

> "Formatting changes alone have been seen to swing benchmark by 76 percentage points. And reordering few-shot examples flips a model from near random, so near 50%, to near state-of-the-art on some benchmarks."
>
> — [11:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=685s) &middot; *Quantified case against hand-tuned prompts in a regulated setting.*

> "Simulation is the inner loop. It's fast, it's free, you can do thousands of runs before anyone actually real is is exposed."
>
> — [15:07](https://www.youtube.com/watch?v=McknwOzbmyg&t=907s) &middot; *Crisp framing of simulation's role in the development cycle.*

> "But, real patients are the outer loop, and that's where the only real proof is. So, simulation is necessary, but it's not sufficient."
>
> — [15:44](https://www.youtube.com/watch?v=McknwOzbmyg&t=944s) &middot; *Guards against over-trusting simulation, balancing the talk's main thesis.*

> "And how much autonomy you allow the system to do depends on your evidence. As the system gets more evidence, you can give it more independence."
>
> — [16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s) &middot; *States the evidence-gated autonomy principle other teams could adopt directly.*

> "The important thing is that you don't ship the model, you ship the evidence when trying to regulate."
>
> — [16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s) &middot; *The talk's thesis compressed into a single line.*

> "You first have to define exactly what harm is for your product. You have to manufacture your rare but then but dangerous cases. Don't wait for them just to happen naturally."
>
> — [16:55](https://www.youtube.com/watch?v=McknwOzbmyg&t=1015s) &middot; *The most portable takeaway for non-healthcare teams.*

> "Voice is just a new module in the same safety case"
>
> — [18:14](https://www.youtube.com/watch?v=McknwOzbmyg&t=1094s) &middot; *Argues the hazard framework generalizes across modalities without a rebuild.*

## Positions

- A/B testing and canary rollouts are unusable for patient-facing AI because randomizing patients into a worse variant is unethical and often illegal. ([0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s), confidence: stated)
- Vendor benchmark scores on a model card are not a valid defense in a post-incident review. ([0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s), confidence: stated)
- The ship-to-5%-and-watch-dashboards playbook depends on a hidden assumption that being wrong for a short time is affordable, which does not hold for patients. ([4:46](https://www.youtube.com/watch?v=McknwOzbmyg&t=286s), confidence: stated)
- Large-scale simulation, as used by self-driving car companies, is the only ethical way to iterate on patient-facing AI before exposure. ([5:56](https://www.youtube.com/watch?v=McknwOzbmyg&t=356s), confidence: stated)
- Simulated LLM patients are preferable to hired standardized-patient actors because actors cannot scale to fast iteration across many scenarios. ([6:29](https://www.youtube.com/watch?v=McknwOzbmyg&t=389s), confidence: stated)
- There is no single realistic patient to simulate; diverse personas (verbose vs. terse) must be simulated instead. ([9:03](https://www.youtube.com/watch?v=McknwOzbmyg&t=543s), confidence: stated)
- An LLM judge validated on 240 examples performs at least on par with, if not slightly better than, expert clinicians at detecting clinical hazards, reaching F1 0.96 with near-perfect sensitivity. ([10:13](https://www.youtube.com/watch?v=McknwOzbmyg&t=613s), confidence: stated)
- In healthcare evaluation you should deliberately over-call hazards rather than risk under-calling them, because false positives are mildly annoying while false negatives can be catastrophic. ([10:51](https://www.youtube.com/watch?v=McknwOzbmyg&t=651s), confidence: stated)
- Evaluation alone does not improve a product; pass/fail grading must be wired into an optimization loop. ([10:51](https://www.youtube.com/watch?v=McknwOzbmyg&t=651s), confidence: stated)
- Manual prompt engineering cannot survive prompt brittleness — formatting changes alone have swung benchmarks by 76 percentage points — so it should be replaced by automated prompt optimizers like GEPA. ([11:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=685s), confidence: stated)
- Automated prompt optimization reduces tuning time from hours or days to roughly 30 to 60 minutes while producing a reproducible audit trail. ([12:41](https://www.youtube.com/watch?v=McknwOzbmyg&t=761s), confidence: stated)
- Evaluation metrics should be defined jointly with clinicians as an explicit cost matrix rather than a flat accuracy score. ([13:14](https://www.youtube.com/watch?v=McknwOzbmyg&t=794s), confidence: stated)
- Passing every simulated test does not prove the product helps real patients; simulation is necessary but not sufficient and only earns the right to test carefully. ([15:44](https://www.youtube.com/watch?v=McknwOzbmyg&t=944s), confidence: stated)
- System autonomy should be granted in proportion to accumulated evidence, expanded stage by stage with clinicians in the loop. ([16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s), confidence: stated)
- The regulatory deliverable is the traceable evidence — calls, datasets, pinned prompts, judge verdicts mapped to specific hazards — not the model itself. ([16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s), confidence: stated)
- Voice introduces new failure modes such as back-channeling and interruptions that cause weak models to abandon in-progress safety advice, but the hazard-simulation framework transfers unchanged to new modalities. ([17:35](https://www.youtube.com/watch?v=McknwOzbmyg&t=1055s), confidence: stated)
- Dora augments rather than replaces clinicians by removing time-consuming follow-up calls from their workload. ([1:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=85s), confidence: stated)

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [simulation environments](../concepts/simulation-environments.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)
- [voice agents](../concepts/voice-agents.md)

