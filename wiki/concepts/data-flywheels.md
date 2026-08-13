---
title: "data flywheels"
type: "concept"
slug: "data-flywheels"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 12
---

# data flywheels

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **12** speaker(s)

**Definition:** Product usage generating proprietary data that improves the product, compounding into a durable advantage.

*Also referred to as: data flywheel, production data flywheels, product feedback loops, training data feedback loops, user feedback signals, customer engagement as evaluation set, eval data collection, proprietary data moats*

## State of Practice

The flywheel argument has moved from "we'll accumulate proprietary data" to a concrete claim about mechanism: the model is the commodity, and the durable asset is the instrumented loop that converts production usage into outcome-labeled data and routes it back into retrieval, skills, prompts, or post-training weights. Intuit's version is the sharpest — a mid-size, cheaper model grounded in ~100,000 observed business outcomes beat frontier models whose advice collapsed into "acquire new customers" 40% of the time — and the same shape recurs as post-training an open model on your own harness, per-conversation scoring by an analyzer agent, and treating customer field engagements as the highest-fidelity eval set. The agreed failure mode is that the loop does not close by itself: traces land in a dashboard, evals land in CI, thumbs land in a table, and nothing routes back into the agent's context or retrieval. Duolingo pushes this further into interaction design: reviewers scoring above 90% on calibration still upheld 50% of fabricated AI flags, and a pure guideline-copy change moved rejection rates 21% — meaning rubber-stamped approvals get logged as ground truth and make the next model spuriously more confident. What remains argued is how much of the write-back can run autonomously at runtime, whether coarse binary feedback is usable fuel or active contamination, and whether raw usage volume compounds at all absent verified outcomes.

## Consensus

### Production usage — not pre-launch tests, scripted simulations, or synthetic evals — is the only source of the data that actually improves an agent, so the eval set is discovered in the field rather than authored up front.

Support: **5** talk(s)

> "We have the highest fidelity evaluation set that comes back from our customers, right? We are in the field every single day."
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [7:08](https://www.youtube.com/watch?v=RVxym6mmIns&t=428s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

### The return path is the missing piece: teams capture traces, evals, and feedback but build no mechanism that feeds them back into context, retrieval, or skills, so the signal terminates in a dashboard and the system never compounds.

Support: **4** talk(s)

> "The eval signal dies in the dashboard. This is a missing layer, a system that consume traces, absorb eval, and convert both into retrieval guidance for future runs."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [2:35](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=155s)

Supporting talks: [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

### Model access is not a moat because everyone has the same models; the defensible asset is the proprietary data and the harness built around it.

Support: **3** talk(s)

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Every logged human decision is reused as a training or eval label, so the quality of the flywheel's fuel is set by how the interaction captures that decision — not by reviewer skill or model quality.

Support: **3** talk(s)

> "Next principle is every interaction is already a label."
>
> — [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [21:10](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1270s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

### Shipping is the start of the work, not the end — the post-launch operating loop deserves at least as much engineering investment as the agent itself.

Support: **3** talk(s)

> "Shipping is the start, not the finish."
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [8:56](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=536s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)

## Disagreements

### Should the learning loop write back into the system autonomously at runtime, or must every improvement pass through a human or review gate?

| Position A | Position B |
|---|---|
| The agent should learn during execution — memories are re-ranked by a utility score reflecting whether they historically helped or hurt the outcome, and after ~10 accumulated memories the reasoning is automatically baked into skills so operating instructions stay current without manual prompt engineering or retraining.<br>*[User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* | Write-back must be gated: deterministically interrupt the agent loop for tool-call approval rather than trusting model judgment, separate the fix-generating agent from the review agent because the fixer is biased toward its own diagnosis, and deliberately add friction where stakes are high. Close the loop until you personally are the bottleneck, and only then remove yourself.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: If the loop is gated, flywheel velocity is capped by human review throughput and you need to staff for it; if it is autonomous, the system improves between deploys but a bad outcome label can silently compound into retrieval and skills with no one in the path to catch it.*

### Is coarse binary feedback (thumbs up/down, accept/reject, approve) usable flywheel fuel?

| Position A | Position B |
|---|---|
| Yes — automated evals asserting tool-call behavior against real completions, combined with thumbs up/down feedback, are what enable fast iteration on agent quality in production.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* | No — thumbs up/down is insufficient, and a single yes/no CTA that conflates "was the model's perception correct" with "what action should follow" manufactures false labels. Rubber-stamped approvals get logged as truth and make the model spuriously more confident over time; noisy human review labels propagate directly into noisy utility scores.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* |

*Why it matters: This is the difference between shipping a cheap feedback widget and funding interaction design as a data-engineering discipline — and if the pessimists are right, the cheap version does not merely underperform, it actively poisons the dataset the flywheel runs on.*

### Does the volume of usage data compound on its own, or does only outcome-verified data compound?

| Position A | Position B |
|---|---|
| Volume compounds directly: because coding agents default to TypeScript, more TypeScript applications get written, which feeds the next generation of training, which makes agents better at TypeScript — a self-reinforcing loop driven by sheer corpus share.<br>*[A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)* | Volume without verified outcomes is inert. A frontier model has read about a domain but never watched what happens; more context is not a substitute for grounding, and you must adjust for selection bias to know whether an action caused the result. The concrete path is building an RL environment for your use case and learning from real production traces.<br>*[Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* |

*Why it matters: It decides whether you instrument for outcome capture and causal adjustment — expensive, and the reason a mid-size grounded model beat frontier models on business advice — or simply accumulate logs and assume scale does the work.*

## Practical Guidance

**Do:**

- Run evals in CI against real completions that assert tool-call behavior — did it hit the right tools, did it do what it was supposed to do — not just output text quality.
- Rank retrieved memories by semantic similarity weighted by whether that memory historically helped or hurt the outcome, and consolidate roughly every 10 accumulated memories into a skill so the operating instructions stay current.
- Frame the AI signal in reviewer-facing copy as a preliminary alert requiring independent evidence and name the human as final decision-maker — at Duolingo this alone moved rejection rates 21% with no model or UI change.
- Split a review decision into separate questions ('was the model's perception correct' vs. 'what action should follow') so each produces an honest label instead of one conflated one.
- Log the human's subsequent manual edit, not just their yes/no — a system that records the decision but not the correction captures a false signal.
- Adjust for selection bias before attributing outcomes to actions: the raw gap of $4,200/day vs $2,800/day for price-raisers collapses to ~$1,150 once you account for those firms already being stronger.
- Give any monitoring or analyzer agent access to trajectories, metrics, the database, and the UI — without all four its diagnosis is guesswork.
- Use a separate agent with fresh context to review fixes, since the fix-generating agent is biased toward its own diagnosis and eager to ship PRs.
- Define success metrics and the data you need to compute them before building the system, rather than asking afterward how to evaluate the model.
- Post-train an open model on the specific harness and traces you care about — a specialized finance model beat Opus at a fraction of Haiku's cost in one to two weeks.
- Route field-engagement learnings back into the roadmap as an explicit deliverable — solving the customer's problem is only half the job.

**Avoid:**

- Treating 'task completed' as a quality signal — an agent can technically succeed and still fail the user, and one that recovers by luck with no alert raised is a hidden defect.
- Assuming skilled reviewers are immune to automation bias — reviewers scoring above 90% on calibration still upheld 50% of fabricated flags.
- Relying on more human oversight as the fix; when the interaction design is wrong, added reviewers become additional rubber stamps.
- Using chat-style memory — user preferences, profiles, conversation history — as the substrate for a self-improving production agent; it retrieves by embedding similarity and never learns from outcomes.
- Deploying agents with no specific direction: with no defined problem you are token-maxing, and ROI measurement remains genuinely unsolved.
- Assuming more context substitutes for outcome grounding — a company's complete financial data is still just one group of data points.
- Shipping the two dominant coding-agent review patterns (one giant diff, or per-file approve prompts) as-is; both reduce the developer to a rubber stamp and yield low-information accept/reject data.
- Leaving stale instructions in the system prompt — a column that no longer exists still shapes agent behavior, and no current system updates it.
- Believing scripted customer simulations, regex, and rule-based checks cover agent failure; trajectories are non-deterministic and the coverage space is unbounded.

## Notable Outliers

- In the Princeton 500-day business simulation, most frontier models drove the company bankrupt in under 500 days — and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Measuring ROI on agent deployments is an unsolved problem, and whoever solves it becomes a $5 trillion market cap company; the deployed-engineering KPI has already shifted from maximizing token usage to measurable delivery outcomes. ([How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s))
- Outcome-weighted memory raises tau-bench policy-following from 66% to 76%, and to 80% once memories are consolidated into skills — with cold start explicitly conceded as unfixable. ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s))
- 73% of agent pipeline failures come from retrieval and context stuffing, not generation — 'We made wrong answers appear faster and cheaper, but we forgot to make retrieval learn.' ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [1:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=99s))
- Build the monitoring and feedback system yourself rather than buying a vendor tool, because you are the only one who knows what you are looking for — and the resulting PR/review agent pair ships 10x more PRs per day than the three-person team. ([The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [13:59](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=839s))
- Because coding agents default to TypeScript output and every new app now embeds agentic capability, TypeScript code volume feeds the next training generation and coding-agent quality in TypeScript will improve faster than in other languages. ([A Song of Types and Agents](../talks/a-song-of-types-and-agents.md), [7:21](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=441s))
- That frontier labs ship custom model variants for their own products is proof that off-the-shelf general models are insufficient for serious applications — if GPT-5 isn't good enough for their own browser, why is it good enough for yours? ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [16:55](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1015s))
- Coding is the only domain where outcome-verified model training is well developed; finance and most other domains remain largely unexplored, and you close the gap with embedded experience rather than bigger models. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [17:51](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1071s))

## All Talks

- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
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

