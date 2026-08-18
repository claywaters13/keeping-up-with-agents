---
title: "Building Closed-Loop Evals for a Multimodal Agent at Scale"
type: "talk"
slug: "building-closed-loop-evals-for-a-multimodal-agent-at-scale"
track: "Evals"
org: "Uber"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "31GUkCBD-Uc"
duration_sec: 1298
word_count: 3775
speakers: ["Jai Chopra", "Soumya Gupta"]
---

# Building Closed-Loop Evals for a Multimodal Agent at Scale

*Program title: Building Closed-Loop Evals for a Multimodal Agent at Uber Scale*

**Speakers:** [Jai Chopra](../speakers/jai-chopra.md), [Soumya Gupta](../speakers/soumya-gupta.md)

**Org:** Uber

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=31GUkCBD-Uc)

## Summary

Jai Chopra and Soumya Gupta of Uber's computer vision team walk through the production agent system that automatically enhances food photography on Uber Eats, and the closed-loop eval machinery that keeps it safe. The core tension: independent merchants lack good photos, but a meaningful fraction of consumers distrust anything AI-generated, so every edit must stay faithful to the original dish, preserve merchant brand identity, and avoid collapsing marketplace diversity into one generic look. They break the pipeline into an image-understanding/routing agent (evaluated as a classifier with a confusion matrix, guardrailed on recall), an enhance-QA loop measured by pass@K with pairwise before/after comparison, and a final publish-ready QA gate justified by a Swiss cheese redundancy model. The most transferable part is the auto-tuning loop: production samples go to human labelers on objective guidelines, mismatches feed a 'diagnoser' agent that localizes the failing component, and reflect/synthesize sub-agents rewrite that agent's config, benchmark it against a golden dataset, and register a new version — config-driven, with no human in the loop. Worth watching if you run multimodal agents in production and need a concrete template for drift correction, human-label alignment, and layered safety gates.

## Key Points

- Uber Eats runs roughly a $90B annual run rate across 10,000 cities and adds millions of items monthly, so photo quality improvement has to work at a scale where manual photo shoots are impossible.
- The design constraint is not just quality but trust: edits must preserve faithfulness to the actual dish and merchant brand, and using one shared prompt for every photo would collapse the visual diversity of the marketplace.
- The pipeline is an image-understanding and routing agent, an image editing agent in a self-correcting loop with a QA agent, and a final post-processing publish-ready QA gate, with everything logged in one flat JSON structure so non-technical staff can diagnose individual cases and roll up aggregates.
- Routing is evaluated like a traditional classifier via a confusion matrix on precision and recall, and recall is the chosen guardrail because letting a bad image through is worse than a false enhancement; more sophisticated routers (e.g. to cheaper, lower-latency models) need an n-by-n matrix rather than 2x2.
- Both routing error directions have concrete costs: false positives burn compute for zero quality lift and risk degrading an already-good image, while recall misses can push a six-wing photo into an enhancer that hallucinates two extra wings to match an 'eight pieces' dish name.
- Human labels are treated as ground truth, collected on a representative dataset stratified by geography, dish type, and image quality, with deliberately objective labeling guidelines to suppress subjective bias and labeler noise.
- Drift is handled by a closed loop: sample production data on a cadence, re-label it, feed mismatches to a diagnoser agent that localizes the failing component, then run a prompt optimizer built from a reflect agent and a synthesize agent that rewrites the config, re-benchmarks against the golden dataset, and registers a new agent version.
- The enhancement loop is scored with pass@K using pairwise input-versus-output comparison against criteria (faithful, complete, natural, realistic) negotiated with product, design, policy, and legal, and it fails in interesting ways — including reward hacking where a rejected creative edit oversteers into a generic ceramic bowl.
- Multiple redundant QA gates are intentional (a Swiss cheese model), and observed failures sometimes trace back to frontier image-editing model weaknesses in object coherence and physics plausibility, which the team reports back to the frontier labs.
- Beyond the model loop, internal dogfooding thumbs-up/down plus free-form merchant and internal feedback feed the same diagnoser, and production impact is tracked on marketplace metrics like add-to-cart conversion, sliceable by geo, device, and dish type for segment-level tuning.

## Notable Quotes

> "our delivery marketplace Uber Eats, we do about 90 billion run rate per year at the moment"
>
> — [0:01](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1s) &middot; *sizes the business the system operates on*

> "We're growing at 20% year-on-year and and we operate in 10,000 cities globally."
>
> — [1:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=66s) &middot; *concrete scale numbers that justify the automation*

> "So a photo is quite often the first signal that a customer gets that gives them that initial impression about a merchant."
>
> — [1:50](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=110s) &middot; *states why image quality is the lever they chose*

> "If we have the same prompt for every photo that we're editing, the diversity of the marketplace is going to collapse."
>
> — [2:37](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=157s) &middot; *names a failure mode of naive prompt standardization at scale*

> "you might notice that all of the agents in this end-to-end orchestration is within one It's It's basically a flat structure in this JSON."
>
> — [6:02](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=362s) &middot; *specific, opinionated logging design choice*

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s) &middot; *the talk's ordering claim about what to build first*

> "we might want to route an image to a lower latency smaller model to be able to save on cost and improve the user experience at the trade-off of quality"
>
> — [8:05](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=485s) &middot; *names the cost/latency/quality tradeoff explicitly*

> "For our use case, we consider human labels as the golden source of truth. And this is what we want to align our models to."
>
> — [8:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=533s) &middot; *takes a side on what ground truth means for a subjective visual task*

> "For routing, our guardrail metric is recall. We don't want any bad image to slip through our system."
>
> — [9:29](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=569s) &middot; *picks one metric as the guardrail and says why*

> "Firstly, you pay the compute cost for a zero quality lift from this image."
>
> — [9:29](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=569s) &middot; *quantifies the cost of a routing false positive*

> "there's a chance your model's going to hallucinate these two extra wings to to match the description"
>
> — [10:03](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=603s) &middot; *vivid, concrete faithfulness failure in a multimodal setting*

> "You need a way such that your prompts, agents, system itself is evolving over time."
>
> — [10:41](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=641s) &middot; *the core argument against static offline-tuned agents*

> "the beauty of this is this is completely config driven and doesn't require human in the loop"
>
> — [11:46](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=706s) &middot; *the strongest and most contestable automation claim in the talk*

> "And this is a closed-loop system as I mentioned, no human in the loop. We definitely have observability on the guardrails, quick rollback built in in case of any issues with the system itself."
>
> — [13:01](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=781s) &middot; *pairs the autonomy claim with the safety mechanism that makes it defensible*

> "You either keep enhancing for K iterations and you pass your QA gate and you publish, or you take a coverage hit and you never enhance this image."
>
> — [13:36](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=816s) &middot; *states the quality-versus-coverage tradeoff of the retry loop*

> "Pass at K is essentially the pass rate at Kth iteration."
>
> — [14:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=846s) &middot; *defines the loop's headline metric*

> "So, this is an example of a reward hacking actually."
>
> — [16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s) &middot; *labels an observed production behavior as reward hacking, not a hypothetical*

> "some of their problems will actually sort of leak up into our applied use case"
>
> — [16:48](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1008s) &middot; *notes that frontier model limitations propagate into product evals*

> "The reason is because we think of this like a Swiss cheese model."
>
> — [17:26](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1046s) &middot; *the mental model justifying redundant QA gates*

> "we want to try and optimize for reducing the chance of a failure getting into production. And so, there is some redundancy here or there. And that's okay."
>
> — [18:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1086s) &middot; *explicitly accepts redundant checks as a design cost*

> "So, we're looking for improvements in people adding to cart, converting, completing their orders."
>
> — [20:07](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1207s) &middot; *ties the eval stack to a business outcome metric*

## Positions

- Logging every stage of an agent orchestration in a flat, human-readable structure must come first, because without it there is nothing to optimize and no basis for a self-learning loop. ([6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s), confidence: stated)
- Human labels, collected on a representative stratified dataset with deliberately objective guidelines, should be the golden source of truth that agents are aligned to. ([8:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=533s), confidence: stated)
- Recall is the correct guardrail metric for the routing agent, because allowing a bad image through is a worse error than an unnecessary enhancement. ([9:29](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=569s), confidence: stated)
- Enhancing an already-high-quality image is doubly bad: it costs compute for zero quality lift and risks degrading the image. ([9:29](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=569s), confidence: stated)
- A statically tuned offline model will not hold up in a real production system; every component needs a mechanism to retune itself against online drift. ([10:41](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=641s), confidence: stated)
- Agent retuning can be fully automated and config-driven with no human in the loop, provided you have guardrail observability and fast rollback. ([11:46](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=706s), confidence: stated)
- Pass rate should increase with more QA feedback iterations, which is why pass@K is the right metric for a self-correcting edit loop. ([14:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=846s), confidence: stated)
- Definitions of a 'better' output must be negotiated with product, design, policy, and legal, then encoded directly into the evals. ([14:42](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=882s), confidence: stated)
- Agents can reward hack a QA gate by oversteering into overly conservative, generic outputs that differ in raw pixels but carry no meaningful improvement. ([16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s), confidence: stated)
- When the judge is not confident about a multimodal check such as item count, the correct production behavior is to reject rather than publish. ([17:26](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1046s), confidence: stated)
- Redundant, overlapping QA gates are worth their cost because layered defenses reduce the probability that a failure reaches production. ([18:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1086s), confidence: stated)
- Agentic systems are better suited than deterministic rules-based pipelines for this problem, because rules are brittle and cannot scale across a globally diverse marketplace. ([4:02](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=242s), confidence: stated)
- Failures traceable to frontier image-editing models, such as object coherence and physics implausibility, should be reported back to the frontier model teams rather than only patched downstream. ([16:48](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1008s), confidence: stated)
- At production scale, evaluation should be sliced by geography, device type, and dish type so that tuning can target specific underperforming segments. ([20:59](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1259s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [model routing](../concepts/model-routing.md)
- [online evaluation](../concepts/online-evaluation.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [reward hacking](../concepts/reward-hacking.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)
- [vision-language models](../concepts/vision-language-models.md)

