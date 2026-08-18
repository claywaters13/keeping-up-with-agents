---
title: "Build Evals That Actually Matter"
type: "talk"
slug: "build-evals-that-actually-matter"
org: "Lyft"
video_id: "3z2uT5aDx_Y"
duration_sec: 2264
word_count: 5291
speakers: ["Akshay Sharma", "Nick Ung"]
---

# Build Evals That Actually Matter

**Speakers:** [Akshay Sharma](../speakers/akshay-sharma.md), [Nick Ung](../speakers/nick-ung.md)

**Org:** Lyft

**Duration:** 37m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=3z2uT5aDx_Y)

## Summary

Two Lyft data scientists describe the end-to-end evaluation system they built over roughly two years for Lyft's multi-agent customer support AI. They argue that offline evaluation must gate production launches the way traditional ML model validation does, and that the hard parts are making the simulated user realistic and making the LLM judge actionable. Their most concrete lesson: using a frontier model to role-play users produced unrealistically polite, verbose transcripts and a 90%+ pass rate, so they fine-tuned a user LLM on real Lyft user verbatims plus defined personas — scores dropped, which they treat as the correct outcome. On the judge side, they advocate binary pass/fail metrics tied to business outcomes, hand-labeling ~100 examples, and scoring judge precision/recall against human ground truth with train/dev/test splits. Worth watching if you're building user-facing agents and need a practical template for user simulation, judge validation, error-analysis loops, and a config-driven eval harness.

## Key Points

- Offline evaluation should be a hard launch gate before an agent reaches production, on the principle that live users should not serve as test data for your AI agent.
- For multi-turn agents, offline eval requires a simulated conversation loop — an agent LLM talking to a user LLM — rather than static input/output pairs, an approach they adapted from Sierra AI's TauBench paper.
- Frontier models role-playing users are trained to be helpful assistants and produce unrealistically patient, verbose complaints, which inflated Lyft's first-pass eval results to a 90%+ pass rate.
- Lyft fine-tuned a user-simulator LLM on real Lyft user verbatims and grounded it in personas (escalation-seeking bypasser, refund seeker, AI skeptic), which lowered eval scores — the intended and correct signal that the eval got harder and more realistic.
- Off-the-shelf metrics like response helpfulness, toxicity, and conversation naturalness are usable as a baseline but too generic to act on: a helpfulness score of 0.5 tells you nothing about what to fix.
- Judges should emit binary pass/fail on task-specific rubrics co-designed with domain experts, because binary outcomes are easier to calibrate and let you systematically analyze error patterns.
- Validate the judge like a classifier: hand-label ~100 examples, split into train/dev/test (train supplies few-shot examples, dev tunes the prompt, test checks for overfitting), and report precision and recall against human ground truth.
- Evaluation criteria drift — you discover the real criteria by looking at data, so evals must be co-developed with the model rather than fixed up front — and reported alignment rates need confidence intervals, since an 84% vs 88% difference on 50 traces proves nothing.
- Lyft's next steps are a config-driven (YAML) eval harness runnable locally, at pre-commit, and in CI/CD, plus post-training and reward modeling using accumulated real user signals.

## Notable Quotes

> "the real imperative here really is that it we don't want to use our live user as, you know, test data for our AI agents"
>
> — [4:23](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=263s) &middot; *States the core justification for gating launches on offline eval.*

> "If your LM as a judge is just floating out there, that there's a score, but no one is really using that score as a meaningful gate uh for your development and production environment, then that LM as a judge is not not available."
>
> — [6:04](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=364s) &middot; *Names the first and most common failure mode: ungated scores.*

> "in our first pass at running our offline evaluation, what we noticed is that our LM user sounds almost too nice"
>
> — [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s) &middot; *The talk's central empirical finding about simulated users.*

> "our first attempt at our offline evaluation gave us 90 plus pass rate or accuracy rate, right? Uh this almost sounds too good to be true, and I think it indeed is the too good to be true."
>
> — [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s) &middot; *Reports the specific number that exposed the broken simulator.*

> "most user, they are they're impatient, they're already frustrated. So, the verbatim they they they they don't want to explain their issues like a l- LM user well."
>
> — [14:27](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=867s) &middot; *Contrasts production reality against synthetic user behavior.*

> "we fine-tune a LLM model with Lyft user verbatim"
>
> — [14:27](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=867s) &middot; *The concrete intervention that fixed the simulator.*

> "If you have an eval that's too easy, that doesn't give you any real uh, production insights into how your AI agent is actually going to perform."
>
> — [15:30](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=930s) &middot; *Frames falling scores as a feature, not a regression.*

> "They fine-tune a uh, user LLM model until evaluation score goes down."
>
> — [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s) &middot; *Cites external corroboration for the counterintuitive tuning target.*

> "the problem with this approach is uh that these metrics are too generic and not actionable"
>
> — [17:54](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1074s) &middot; *The thesis of the LLM-judge half of the talk.*

> "If something if let's say a response helpfulness is 0.5, then what do we do with it?"
>
> — [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s) &middot; *Makes the actionability critique concrete in one line.*

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s) &middot; *A clear tradeoff position on off-the-shelf metric libraries.*

> "eval should be framed around a task success or failure. And a binary outcome is very easy to calibrate and train um LLM judge that can consistently score your agent trajectory."
>
> — [19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s) &middot; *The prescriptive alternative to continuous scores.*

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s) &middot; *Gives an actionable sample size and method for judge validation.*

> "we are not actually training models. So, we are just using the data to inform judges prompt."
>
> — [22:09](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1329s) &middot; *Clarifies how the ML-splitting analogy differs in practice.*

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s) &middot; *Core statement of the criteria-drift argument.*

> "We cannot define the criteria beforehand and then evaluate agents against them."
>
> — [24:05](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1445s) &middot; *A sharp, contestable position on eval design order.*

> "every score needs an interval"
>
> — [25:01](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1501s) &middot; *Compresses the statistical-rigor argument into a rule.*

> "If you don't look at the data, you won't be able to create meaningful criteria uh or labels. And if you don't have labels, you won't be able to evaluate your judges. And if you're not evaluating your judges, you don't know if your uh agentic pipeline is working as as expected."
>
> — [26:58](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1618s) &middot; *Chains the whole argument from raw data to pipeline confidence.*

> "it is important to know that this loop is something which runs continuously. It's not uh not a one-off audit."
>
> — [27:42](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1662s) &middot; *Positions error analysis as ongoing process, not a milestone.*

> "our eval harness is config driven and these are typically stored as YAML file that's easily editable by different contributor and not just by engineers"
>
> — [34:42](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=2082s) &middot; *Describes the design choice that opens eval authoring to non-engineers.*

## Positions

- Agents should pass a rigorous offline evaluation gate before being exposed to live users, just as ML models are validated before production. ([2:37](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=157s), confidence: stated)
- An LLM judge whose score does not gate any decision is worthless. ([6:04](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=364s), confidence: stated)
- Prompting an LLM to generate ~50 test queries is an inadequate way to build an offline eval dataset; datasets should be sampled from production traffic and mutated to cover golden paths and edge cases. ([11:49](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=709s), confidence: stated)
- Off-the-shelf frontier models make poor user simulators for customer support because they are trained to be helpful and produce unrealistically polite, articulate complaints. ([12:41](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=761s), confidence: stated)
- Lyft's initial offline eval reported a 90%+ pass rate, which was an artifact of an unrealistically nice simulated user. ([13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s), confidence: stated)
- A user simulator should be fine-tuned on real user language until evaluation scores go down; a falling score is evidence the eval got more realistic, not that quality dropped. ([15:30](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=930s), confidence: stated)
- Pre-built eval metrics (DeepEval-style helpfulness, toxicity, conciseness) are acceptable as a baseline but should not be core metrics. ([18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s), confidence: stated)
- Binary pass/fail rubrics tied to business outcomes are more calibratable and more actionable than continuous quality scores. ([19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s), confidence: stated)
- Judges should be validated like binary classifiers, using roughly 100 hand-labeled examples split into train/dev/test and scored on precision and recall. ([21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s), confidence: stated)
- Evaluation criteria cannot be fully specified before looking at data; they must be co-developed with the model as more examples are graded. ([24:05](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1445s), confidence: stated)
- A difference between 84% and 88% alignment on 50 traces is not a demonstrably real gain; reported scores need confidence intervals. ([26:04](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1564s), confidence: stated)
- Expensive statistical rigor should be reserved for high-stakes moments such as shipping decisions or reporting to leadership, not applied uniformly. ([25:01](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1501s), confidence: stated)
- Not looking at raw data is the single most damaging eval anti-pattern, because labels, criteria, and judge validation all depend on it. ([26:58](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1618s), confidence: stated)
- Eval harnesses should be config-driven (YAML) so analysts and data scientists, not only engineers, can contribute test cases. ([34:42](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=2082s), confidence: stated)
- Evals should run at multiple points in development — locally, at pre-commit hooks, and in CI/CD as a regression suite. ([35:33](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=2133s), confidence: stated)
- Lyft's current offline simulator is not yet repeatable, existing as scattered scripts across notebooks and analysis repos. ([31:58](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1918s), confidence: stated)

## Concepts

- [continual learning](../concepts/continual-learning.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [online evaluation](../concepts/online-evaluation.md)
- [rubric design](../concepts/rubric-design.md)
- [simulation environments](../concepts/simulation-environments.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

