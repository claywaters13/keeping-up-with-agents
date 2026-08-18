---
title: "Why Your Agent Disagrees With Itself (And What To Do About It)"
type: "talk"
slug: "why-your-agent-disagrees-with-itself-and-what-to-do-about-it"
org: "Datadog"
video_id: "wEc9aG7cRQc"
duration_sec: 1538
word_count: 2872
speakers: ["Diane Lin"]
---

# Why Your Agent Disagrees With Itself (And What To Do About It)

**Speakers:** [Diane Lin](../speakers/diane-lin.md)

**Org:** Datadog

**Duration:** 25m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=wEc9aG7cRQc)

## Summary

Diane Lin (Datadog, formerly co-founder of an acquired security-triage startup) tackles the problem of AI agents producing semantically different verdicts on the same input across runs. Her core argument is that this inconsistency is not primarily model stochasticity or a model defect — it concentrates on data points near the decision boundary, the 'gray zone', where human experts also disagree and where the right answer depends on customer policy or preference. She proposes borrowing active learning from classical ML, but with two LLM-specific refinements: use inter-run/inter-model disagreement rather than LLM-reported uncertainty as the selection signal, and replace expensive fine-tuning with semantic memory (distilled domain rules) plus episodic memory (references to past similar cases). She reports a concrete experiment on 93 security alerts run three times: ~25% flip-flopped, episodic memory fixed about 15 percentage points, leaving ~10% for human review. The talk is worth watching for anyone building classification-style agents who needs a cheap, feedback-driven consistency loop rather than a retraining pipeline.

## Key Points

- Agent inconsistency on identical inputs is not merely wording variation but semantically different verdicts, which creates a trust problem that can lose deals in a POC bake-off.
- The data points that flip-flop cluster around the decision boundary — the gray zone — where human experts disagree and traditional ML classifiers also struggle, so the agent is surfacing pre-existing ambiguity rather than failing.
- Many gray-zone cases have no objectively right answer; the correct label depends on the particular customer's policy or preference, such as whether a hotel wants to hear complaints outside its control or whether an enterprise wants alerts about attackers who never got in.
- Because a single evaluation run does not tell the whole story, evaluations must be repeated multiple times and averaged to get a holistic picture.
- Active learning, an existing ML technique, transfers to LLM agents for finding which outputs deserve scarce human attention without reviewing every output.
- LLM self-reported uncertainty is an unreliable selection signal — the model doesn't know what it doesn't know — so query-by-committee style disagreement across runs or models is the better trigger for human review.
- Fine-tuning is not the only remediation: augmenting the agent with semantic memory (distilled factual rules that sharpen the decision boundary) and episodic memory (retrieved past similar cases and their decisions) is lighter weight and easier to iterate.
- Semantic and episodic memory are complementary in a pipeline: episodic memory auto-resolves recurring cases, the residue goes to human review, and human review distills domain knowledge into semantic memory for next time.
- In an experiment on 93 real security alerts run three times, roughly a quarter flip-flopped; episodic memory made about 15% consistent, leaving 10% still inconsistent for human handling.
- The approach yields three benefits beyond consistency: efficient quality control on a small high-return labeling subset, and an agent that adapts to each customer's environment via gathered feedback.

## Notable Quotes

> "Same model, same input. But different output. Here I don't mean the wording different. I mean semantically different output. You might be thinking that's the stochastic nature of LM."
>
> — [2:01](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=121s) &middot; *States the problem precisely and preempts the easy dismissal the rest of the talk argues against.*

> "That means a single evaluation run didn't tell you the whole story. You need to repeat your evaluation multiple times in order to get a holistic picture by the average over the different runs results."
>
> — [3:03](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=183s) &middot; *Concrete methodological prescription for eval design.*

> "So, the inconsistency is causing a trust issue in your product. Imagine if you were in a POC bake-off, one vendor give the consistent wording all the time while the other vendor have this flip-flop wording. You can imagine which one would win the deal."
>
> — [5:13](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=313s) &middot; *Frames consistency as a commercial stake, not a technical nicety.*

> "The good news is the data points tend to flip-flop actually concentrate around the decision boundary, the so-called gray zone."
>
> — [5:13](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=313s) &middot; *The central empirical claim the whole solution rests on.*

> "In this case, you'll find that even human experts will have a disagreement on these cases. In fact, there's no right or wrong answer."
>
> — [6:31](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=391s) &middot; *Reframes inconsistency as label ambiguity rather than model error.*

> "So, here whether we label them malicious or benign depends on company preference whether they wanted to be notified about such situation."
>
> — [8:41](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=521s) &middot; *Grounds the 'no right answer' claim in a specific security-triage decision.*

> "So in other words it's not your AI agent's fault. Your AI agent simply point out the ambiguity that already exists."
>
> — [9:37](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=577s) &middot; *The talk's thesis in one line.*

> "But you don't have bandwidth to check all of them. Otherwise, it lose a point of having agent to do the work."
>
> — [10:51](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=651s) &middot; *Names the tradeoff that motivates active learning over full review.*

> "At least from what we have tried so far the uncertainty score from LM is not very reliable. It's kind of a LM model doesn't know what it doesn't know."
>
> — [14:45](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=885s) &middot; *A directly checkable, contestable position on LLM confidence signals.*

> "However, the the disagreement from different runs or from different models actually give you a more reliable signal where the model actually not sure about its verdict and it need human guidance."
>
> — [14:45](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=885s) &middot; *States the recommended replacement signal.*

> "Yes, one option is retrain the model, but fine-tuning model is expensive. Here, we are proposing a more lighter weight solution, easier to iterate. It's about augment your agent with semantic and episodic memory."
>
> — [15:42](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=942s) &middot; *The core architectural recommendation and its cost rationale.*

> "So, this type of domain knowledge sharpen your decision boundary. And also, help the human beings."
>
> — [17:14](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1034s) &middot; *Notes that written-down rules improve human labeler consistency too, not just the agent.*

> "And the advantage of the this episodic memory way is it's relatively automatically. It has less human intervention."
>
> — [18:17](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1097s) &middot; *The tradeoff distinguishing episodic from semantic memory.*

> "And this particular useful in the case of cyber security alerts because a lot of noise especially those false positive noise are the one keep recurring. And that's the one are the low hanging fruit you can automate away."
>
> — [19:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1150s) &middot; *Explains when episodic memory pays off most.*

> "The two are actually not contradicting. In fact, they are complementary."
>
> — [20:05](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1205s) &middot; *Resolves the semantic-vs-episodic choice into a pipeline.*

> "So, here we collect uh 93 alerts, cybersecurity alerts, and then we run them three times. If without the solution we are proposing here, a quarter of them will flip-flop the verdict."
>
> — [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s) &middot; *The talk's only hard baseline number.*

> "In contrast, after applying our solution or using episodic memory, about 15% of them become consistent. However, there's still 10% of them remaining inconsistent."
>
> — [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s) &middot; *The headline result, honestly reported with the residual failure rate.*

> "inconsistency isn't usually your model problem. Stop blaming your model, but instead focus your energy on label issue and potentially insufficient information"
>
> — [23:12](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1392s) &middot; *Takeaway one, stated as an imperative others might dispute.*

> "Second, the model disagreement isn't a bug, but feature. Treat each disagreement as an opportunity for your model to learn."
>
> — [23:12](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1392s) &middot; *Takeaway two — the reframe that turns a defect into a data-selection mechanism.*

> "Third, fine-tuning isn't your only option. Augment your agent with semantic and episodic memory."
>
> — [24:24](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1464s) &middot; *Takeaway three, the actionable alternative to retraining.*

## Positions

- Agent inconsistency is usually caused by label ambiguity and missing information, not by a defective model. ([23:12](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1392s), confidence: stated)
- The data points that produce inconsistent verdicts concentrate near the decision boundary, where human experts also disagree and traditional ML classifiers also struggle. ([9:37](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=577s), confidence: stated)
- For many gray-zone cases there is no objectively correct label; the answer depends on the customer's policy or preference. ([7:31](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=451s), confidence: stated)
- LLM-reported uncertainty scores are not a reliable signal for selecting cases that need human review. ([14:45](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=885s), confidence: stated)
- Disagreement across multiple runs or across different models is a more reliable selection signal than model confidence. ([14:45](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=885s), confidence: stated)
- Augmenting an agent with semantic and episodic memory is cheaper and easier to iterate on than fine-tuning, and achieves comparable improvement in consistency. ([15:42](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=942s), confidence: stated)
- In a test of 93 cybersecurity alerts run three times, about 25% flip-flopped without the proposed solution; episodic memory made about 15% consistent, leaving 10% inconsistent. ([22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s), confidence: stated)
- A single evaluation run is insufficient; evals must be run multiple times and averaged. ([3:03](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=183s), confidence: stated)
- Semantic and episodic memory should be used together in a pipeline rather than chosen between, with episodic handling recurring cases and human review feeding semantic memory. ([20:05](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1205s), confidence: stated)
- Inconsistent agent output is a commercial liability that can decide competitive vendor evaluations. ([5:13](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=313s), confidence: implied)
- Writing domain rules into semantic memory improves human labeler consistency, not just agent consistency. ([17:14](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1034s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [structured output contracts](../concepts/structured-output-contracts.md)

