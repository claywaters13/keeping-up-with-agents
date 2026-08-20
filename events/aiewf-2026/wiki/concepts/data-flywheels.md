---
title: "data flywheels"
type: "concept"
slug: "data-flywheels"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 14
---

# data flywheels

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **14** speaker(s)

**Definition:** Product usage generating proprietary data that improves the product, compounding into a durable advantage.

*Also referred to as: data flywheel, production data flywheels, product feedback loops, training data feedback loops, user feedback signals, customer engagement as evaluation set, eval data collection, proprietary data moats*

## State of Practice

The conference converged hard on one claim: model access is a commodity, and the only durable advantage is a proprietary corpus of situations-plus-verified-outcomes that the labs cannot buy or scrape — Intuit's ~100,000 business situations with observed results, Abridge's ~100 million medical conversations a year, the hedge fund's trade theses, pharma's failed-experiment data. The sharpest version of the argument is that more context is not a substitute for grounding: giving a frontier model all of a company's financials still yields one group of data points, and in Intuit's study 54% of frontier advice collapsed to 'acquire new customers' or 'raise revenue.' A mid-size grounded model beat frontier head-to-head; a post-trained open model beat Opus on finance at a fraction of Haiku's cost in one to two weeks. But the field is much less settled on the wheel's second half — how the exhaust actually gets back in. Speakers split on whether the loop terminates in weight updates (RL selectors, per-section post-trained models) or in runtime artifacts (outcome-weighted memory, agent-authored PRs, updated skills), and on whether AI graders can generate the label or whether a paid domain expert must be the ground truth. The most under-appreciated finding is upstream of all of this: Duolingo showed that interaction design, not model quality, determines label quality — reviewers scoring >90% on calibration still rubber-stamped 50% of fabricated flags, and a copy-only change moved rejection rates 21%. A flywheel built on rubber-stamped approvals spins itself into spurious confidence.

## Consensus

### Proprietary data — specifically data the frontier labs cannot access — is the moat; the model, infrastructure, and tooling layer is a commodity.

Support: **4** talk(s)

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### The training and eval signal comes from production, not from pre-launch testing; shipping starts the loop rather than ending it, and teams that stop at launch never accumulate the data.

Support: **5** talk(s)

> "shipping is the easiest part today. If you want to if you want to build a production agent, you need to close the loop first"
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [18:30](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1110s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)

### A smaller, cheaper model specialized on proprietary data beats a frontier general model on a narrow task, and the payoff is primarily cost and latency once quality is already at the bar.

Support: **3** talk(s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### The mechanism that captures human judgment determines whether the flywheel compounds or poisons itself; low-information capture (single yes/no, thumbs up/down, unlogged manual edits) produces false labels that make the model spuriously confident.

Support: **4** talk(s)

> "Next principle is every interaction is already a label."
>
> — [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [21:10](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1270s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

## Disagreements

### Is the moat the proprietary data, or the internal harness built around commodity models?

| Position A | Position B |
|---|---|
| Only data and domain expertise are defensible. The scaffolding — prompts, data plumbing, observability — fits on one screen and any strong engineer reproduces it in minutes, so it is explicitly not a moat.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)* | Since everyone has the same models, competitive advantage now comes precisely from the harness — the self-watching agent loop, the deterministic interrupt and sandbox layer, the org-wide agent deployment — with an agent harness roughly doubling PR output over single-point tools.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* |

*Why it matters: It determines whether early engineering effort goes into acquiring gatekept data and hiring domain experts, or into building custom agent loops and monitoring infrastructure. Getting it wrong means building a replicable product on top of replicable data, or hoarding data you have no loop to exploit.*

### Can AI graders generate the flywheel's label, or must a human domain expert be the ground truth?

| Position A | Position B |
|---|---|
| Automated graders can carry the loop: evals in CI asserting tool-call behavior against real completions, an agent that reads its own production traces and opens PRs, and retrieval that re-ranks memories by whether they historically helped or hurt the outcome — all without a human in the grading path.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* | In domains with no answer key, models cannot verify themselves — a verifier good enough to grade would already be the best generator, LLM-as-judge produces plausible jargon without understanding, and rubrics-as-rewards creates an echo chamber where the AI grades itself into agreement. The signal has to originate from paid experts, encoded as multi-clinician-adjudicated rubrics or expert-calibrated judges.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: Expert-sourced labels cost orders of magnitude more and cap flywheel throughput at human review bandwidth; AI-sourced labels scale to every session but risk compounding the model's own errors into the training set. The right answer likely depends on whether your domain has verifiable outcomes, which is exactly what nobody agreed on.*

### Does the flywheel have to close in the weights, or can it close entirely at runtime?

| Position A | Position B |
|---|---|
| The loop terminates in training. Ground a model in observed outcomes and train an RL selector over frontier-generated hypotheses; post-train smaller models down to the granularity of individual note sections; build an RL environment for your use case and learn from production traces. You don't close the gap with bigger models, you close it by embedding verified outcomes into the weights.<br>*[Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* | The loop should close at runtime without touching weights: outcome-weighted memory that improves during execution and consolidates into skills after ~10 entries, agent-generated PRs that fix the harness within half an hour of detection, and error analysis over logs as the cheapest and highest-ROI method — explicitly before any weight-touching technique, since each new base model release forces you to redo fine-tuning.<br>*[User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* |

*Why it matters: Training-based flywheels build an asset that depreciates on every base-model release; runtime flywheels stay portable but never compress the learning into cheaper inference. This decides whether you staff an ML training team or an agent-ops team.*

### Is human review a permanent fixture of the loop or transitional scaffolding to be removed?

| Position A | Position B |
|---|---|
| Close the loop with yourself as the deliberate bottleneck first, then remove the human — the sequencing is loop-first, human-removal-second, and calibration is what earns the removal.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* | The expert stays in the decision seat indefinitely. In finance and pharma the correct model is AI-in-the-loop, where the expert decides and AI only compresses their time; mutating tool calls get deterministic interrupts with humans in the driver's seat; and friction should be deliberately added where stakes are high rather than engineered away.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: If human review is transitional, review UX is a temporary cost and label volume is capped only until autonomy arrives. If it's permanent, the review interface is the flywheel's primary data-generation surface and deserves the same investment as the model.*

## Practical Guidance

**Do:**

- Find a dataset where you observe many entities taking an action and can verify how it turned out — that observed-outcome pairing, not volume of context, is the thing frontier models do not have.
- Adjust for selection bias before believing an outcome delta: Intuit's raw $4,200/day vs $2,800/day gap for price-raising firms shrank to roughly $1,150 once you account for the fact that firms able to raise prices were already more successful.
- Run error analysis over your observability logs before any technique that touches weights — it is the cheapest and highest-ROI improvement path.
- Hire the domain expert before you start iterating; engineers building vertical AI literally cannot tell whether the output is good, and this is where vertical projects quietly die.
- For open-ended outputs, replace the single golden response with expert-authored rubrics of required elements — Abridge used two independent physician rubrics, a third physician to adjudicate them into a final rubric, and a fourth clinician for QA.
- Log the human's subsequent manual edit, not just their yes/no decision — recording only the accept/reject captures a false signal that pollutes the dataset.
- Split any CTA that conflates 'was the model's perception correct' with 'should we take the action' into separate signals, so a hearing aid correctly detected as an earbud is logged as a true positive with a benign outcome.
- Define success metrics and the data you need to compute them before building the system, instead of asking afterward how to evaluate the model.
- Use cheap event gates to decide when to escalate to heavy models, rather than running the expensive model continuously over the stream.
- Separate the fix-generating agent from the review agent and give the reviewer fresh context, because the fixer is biased toward its own diagnosis and eager to ship PRs.
- Consolidate accumulated runtime memories into skills once you hit roughly ten, so operating instructions stay current without manual prompt rewrites.
- Treat field/FDE engagements as your highest-fidelity eval set and route the findings back into the roadmap — the embedded team has the earliest signal on what to build next.

**Avoid:**

- Assuming more context substitutes for outcome grounding — a company's complete financial data is still just one group of data points, which is the difference between sounding right and being right.
- Letting eval results and observability traces terminate in a dashboard with no path back into context, skills, or retrieval.
- Treating LLM-as-judge as ground truth in domains without answer keys; a verifier good enough to grade would already be your best generator, and rubrics-as-rewards can become an echo chamber.
- Rubber-stamp interfaces — one giant diff, or per-file approve prompts — which reduce the reviewer to a validator and yield low-information accept/reject labels.
- Relying on thumbs up/down as your explicit feedback channel; it lacks the nuance to drive targeted improvements.
- Adding more human oversight as a fix: reviewers scoring above 90% on calibration still accepted 50% of fabricated flags, a coin-flip rate indicating automation bias.
- Planning to buy your way to gatekept expert data through annotation labor — NDAs block it and the experts earn far more than annotation rates.
- Treating fine-tuning as a one-time investment; every new base model release forces you to redo it.
- Expecting outcome-weighted retrieval to help early — cold start is an inherent limitation, and noisy human review labels propagate directly into noisy utility scores.
- Deploying agents with no specific direction and calling token consumption progress; that is token maxing with no tangible outcome and no measurable ROI.

## Notable Outliers

- A specialized team with unique data can beat the rate of improvement of the frontier models themselves — on a narrow problem the labs are not focused on, your flywheel outruns their scaling curve. ([From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [19:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1163s))
- Coding agents created a language-level data flywheel: they default to emitting TypeScript, that output feeds the next training generation, and TypeScript passed Python as the most-used language on GitHub in August 2025 as a result. ([A Song of Types and Agents](../talks/a-song-of-types-and-agents.md), [7:21](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=441s))
- In a 500-day Princeton business simulation, most frontier models drove the company bankrupt, and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Roughly 30% of pharma sponsors never disclose clinical trial results despite a legal requirement — the non-disclosure itself is what makes failed-experiment data a defensible corpus. ([Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [10:47](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=647s))
- The widely cited '89% of enterprise AI agents never reach production' framing is wrong: every AI reaches production, it just fails to justify its own cost. ([Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [16:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=980s))
- Changing only the guideline copy — framing the AI signal as a preliminary alert and naming the human as final decision-maker — shifted rejection rates 21% with no model or UI change. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- Maximally efficient inference cannot be achieved behind closed doors, because it depends on many small contributions from resource-constrained practitioners — the Linux argument applied to model optimization. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [29:21](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1761s))

## All Talks

- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)

