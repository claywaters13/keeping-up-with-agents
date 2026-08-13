---
title: "How Evals and Prompts Shape Agent Behavior"
type: "talk"
slug: "how-evals-and-prompts-shape-agent-behavior"
track: "Evals"
org: "YouTube Ads"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "xyL2Ltkh-SA"
duration_sec: 1169
word_count: 3548
speakers: ["Chris Souza", "Daniel Bump", "Preetika Bhateja"]
---

# How Evals and Prompts Shape Agent Behavior

*Program title: Model Whisperers: How Evals and Prompts Shape Agent Behavior*

**Speakers:** [Chris Souza](../speakers/chris-souza.md), [Daniel Bump](../speakers/daniel-bump.md), [Preetika Bhateja](../speakers/preetika-bhateja.md)

**Org:** YouTube Ads

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 19m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=xyL2Ltkh-SA)

## Summary

Two engineers from the YouTube Ads team (working on image and video models for ads) walk through the practical lifecycle of building evals for a production agent. Their core argument is that eval maturity should track agent maturity: start with unscalable, intuition-driven 'vibe' evaluation to learn failure patterns fast, then graduate to golden sets, human scale raters, and LLM judges once the architecture stabilizes. They give concrete operational advice — rubrics with clear examples, requiring rater explanations rather than bare pass/fail, monitoring human-vs-LLM agreement rates, and inspecting agent traces rather than only aggregate pass rates. A worked example shows an agent that repeatedly removed a legally-required ad disclaimer despite explicit prompt instructions, a failure invisible in categorical pass-rate metrics but obvious in the trace. Useful for anyone standing up an eval practice on a nondeterministic agent system, especially teams deciding when to invest in scaled raters and how to set launch criteria.

## Key Points

- Agent reliability is framed as a function of three things — the agent's capabilities, its guardrails, and its evals — so eval investment should not be separated from tooling investment.
- Before building large agent-level evals, optimize the underlying LLM-friendly tool set, and consider an independent critique agent with a remediation loop to cover gaps the base tools cannot close.
- Early on, non-scalable 'vibing' — eyeballing outputs and iterating on intuition — beats building a comprehensive eval, because a rigid eval hinders radical architecture changes and causes noisy ups and downs during calibration.
- Golden sets should start small around a few core tasks and expand; they must also test negatives, since verifying the model didn't do something bad is as critical as verifying it did the task.
- Scale raters need clear rubrics with concrete examples, and the team itself must reach strong human-human agreement on what counts as a pass before handing rating out.
- Rater explanations (for both single-side and side-by-side evals) are what tell you where the agent is failing; a bare pass/fail gives no signal for improvement, especially in multi-output settings like accuracy vs. brand safety.
- For LLM judges, monitor human-vs-LLM disagreement rates via a sampling pipeline and spot-check the judge's reasoning rather than trusting aggregate pass rates.
- Agent traces surface failures that categorical pass rates hide — the team caught the agent explicitly detecting a disclaimer and deciding to remove it despite repeated prompt instructions never to.
- Fix patterns, not individual runs: because the systems are nondeterministic, tuning a prompt off one failing trace is a trap; use multiple golden-set examples per pattern and measure failure frequency.
- Traditional ML discipline still applies — hold out a test set, use it sparingly, and refresh it with production data alongside online evals.

## Notable Quotes

> "the reliability of your agent is basically a function of the capabilities of the agent uh the guard rails and the evals"
>
> — [2:04](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=124s) &middot; *The talk's compressed thesis on where reliability actually comes from.*

> "it's important to first optimize these tools and make sure they're the best they can be before just jumping onto um larger agent evals"
>
> — [1:22](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=82s) &middot; *States an ordering position — tools before evals — that other eval-first talks would contest.*

> "having a strong eval is very important as this gives you um like a way of proving the value of changes you make as well as running ablation experiments on any changes you make"
>
> — [2:04](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=124s) &middot; *Frames evals as an experimentation instrument rather than a quality gate.*

> "an interesting uh thing here that I think might be somewhat counterintuitive is that early on vibing can actually be kind of good for you"
>
> — [3:41](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=221s) &middot; *The talk's most contrarian claim, explicitly flagged as counterintuitive by the speaker.*

> "even though this is non-scalable it will still give you like a very good idea of when you change this what happens"
>
> — [3:41](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=221s) &middot; *Defends deliberately unscalable evaluation on iteration-speed grounds.*

> "at this stage prompt tweaks can also have like large performance gains you can make a radical change to the architecture um and your eval is not kind of like hindering you in this way"
>
> — [4:52](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=292s) &middot; *Names the tradeoff: a mature eval is a constraint on architectural churn.*

> "if if you uh jump to scale to um these scaled raiders like too early uh it can cause you to kind of have like very big ups and downs as you might be iterating and calibrating the eval"
>
> — [5:32](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=332s) &middot; *Gives the concrete failure mode of premature scaled rating.*

> "Checking if the model like didn't do something as bad, uh, something bad is just as critical as checking if it did the task."
>
> — [6:11](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=371s) &middot; *Negative testing stated as equal in priority to capability testing.*

> "there's a funny visual here about writing the evals can be a very small point and humans arguing over what the rubric should be is, uh, is kind of like a very large task here"
>
> — [6:11](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=371s) &middot; *Locates the real cost of evals in human rubric alignment, not engineering.*

> "human human agreement should be strong within your team of what you consider a good use case and a good past case for an eval"
>
> — [8:02](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=482s) &middot; *Sets internal agreement as a prerequisite before scaling out rating.*

> "if it's a pass or a fail, that doesn't really tell you much about where should the agent improve, what was the thinking that went behind coming to that conclusion"
>
> — [8:02](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=482s) &middot; *The argument for collecting rater explanations, stated as a limitation of binary labels.*

> "if you can have a sample pipeline of sorts that is monitoring how a human raider or some expert would rate an eval versus how an LLM would rate it. You can get a sense of like how it's trending"
>
> — [9:46](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=586s) &middot; *Concrete calibration mechanism for LLM-as-judge.*

> "if you if you want to know what it's doing look at it at its thinking"
>
> — [11:00](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=660s) &middot; *The one-line case for trace inspection.*

> "for legal reasons disclaimers can never be removed"
>
> — [11:00](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=660s) &middot; *The exact instruction the agent violated — sets up the talk's central failure example.*

> "it actually detects that there is a disclaimer in what it's searching for and it says, okay, I found a disclaimer and now I'm going to go ahead and remove it, which was not what we asked it to do"
>
> — [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s) &middot; *A specific, memorable instruction-following failure caught only in the trace.*

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s) &middot; *States the limit of aggregate metrics with a real case behind it.*

> "if you have a test set, use it sparingly and also refresh it with prod data"
>
> — [12:44](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=764s) &middot; *Carries classical ML hygiene directly into agent evaluation.*

> "identify where and why the model performance is uh degrading so that you can distinguish between acceptable trade-offs and critical failures"
>
> — [13:51](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=831s) &middot; *Defines what launch-readiness regression analysis is actually for.*

> "you should focus on patterns rather than isolated runs so a tempting thing is to hyperfixate on very small examples from the model"
>
> — [13:51](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=831s) &middot; *Names a specific anti-pattern most agent builders fall into.*

> "you basically want to look at the entire picture of how often is it failing on that pattern, not that specific individual example"
>
> — [15:10](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=910s) &middot; *Operationalizes the pattern-over-instance principle.*

> "it should be representative of what you want your product to be great at"
>
> — [15:51](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=951s) &middot; *The speakers' summary definition of a good eval system.*

> "it's important to like uh get some clarity early on on what is your gatekeeping rule like what's your launch criteria"
>
> — [17:13](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=1033s) &middot; *Pushes launch-threshold decisions upstream of the eval results.*

## Positions

- Tooling should be optimized before investing in larger agent-level evals. ([1:22](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=82s), confidence: stated)
- Agent reliability is a function of agent capabilities, guardrails, and evals together. ([2:04](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=124s), confidence: stated)
- Intuition-based, non-scalable evaluation early on works better than immediately building a comprehensive eval. ([3:41](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=221s), confidence: stated)
- Moving to scaled raters too early produces large swings in measured quality while the eval and the model are both still being calibrated. ([5:32](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=332s), confidence: stated)
- You do not need a massive golden set on day one; starting with a few core tasks is sufficient. ([5:32](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=332s), confidence: stated)
- Checking that the model did not do something bad is as critical as checking that it did the task. ([6:11](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=371s), confidence: stated)
- Binary pass/fail ratings are insufficient; raters should supply explanations for their judgments. ([8:02](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=482s), confidence: stated)
- LLM judges must be calibrated by monitoring human-vs-LLM agreement or disagreement rates through a sampling pipeline. ([9:46](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=586s), confidence: stated)
- Some agent failures — such as removing a legally required disclaimer despite explicit prompt instruction — are undetectable from aggregate pass-rate metrics and require trace inspection. ([11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s), confidence: stated)
- Repeating an instruction multiple times in the prompt does not guarantee the agent follows it in edge cases. ([11:00](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=660s), confidence: implied)
- Agents do not generalize well beyond the data sets they were developed against, so edge-case data sets and held-out test sets are needed. ([12:07](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=727s), confidence: stated)
- Updating the prompt in response to a single failing run is a trap because the systems are non-deterministic; fixes should be driven by failure patterns measured across multiple examples. ([15:10](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=910s), confidence: stated)
- Test sets should be used sparingly and refreshed with production data. ([12:44](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=764s), confidence: stated)
- Launch gatekeeping criteria should be decided early, before regression analysis, rather than after seeing results. ([17:13](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=1033s), confidence: stated)
- Training cross-functional teams and scale raters on how to rate is a necessary investment; six months prior it was not yet common practice. ([16:26](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=986s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [online evaluation](../concepts/online-evaluation.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [rubric design](../concepts/rubric-design.md)

