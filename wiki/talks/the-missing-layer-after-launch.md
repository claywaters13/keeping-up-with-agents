---
title: "The Missing Layer After Launch"
type: "talk"
slug: "the-missing-layer-after-launch"
org: "Wandero AI"
day: "Day 4 — Session Day 3"
room: "Expo Stage 1 NE"
video_id: "kZsf_Sfm7RU"
duration_sec: 1173
word_count: 3369
speakers: ["Giedrius Steimantas"]
---

# The Missing Layer After Launch

*Program title: The Missing Layer in Agentic AI*

**Speakers:** [Giedrius Steimantas](../speakers/giedrius-steimantas.md)

**Org:** Wandero AI

**Day/Room:** Day 4 — Session Day 3 &middot; Expo Stage 1 NE &nbsp;|&nbsp; **Duration:** 19m 33s

[Watch on YouTube](https://www.youtube.com/watch?v=kZsf_Sfm7RU)

## Summary

Raphael Kalandadze argues that most agent talks stop at the moment of shipping, but shipping is where the real work starts — the 'missing layer' is the post-launch feedback loop that tells you whether your agent is actually working across thousands of live conversations. He explains why agents break classical safety nets: LLMs are non-deterministic, the coverage of possible conversations is endless, and the scariest failures are silent ones where the agent recovers by luck or marks a task complete without verifying it worked. His answer is a 'meta harness': a log-monitoring agent that runs hourly and opens PRs, a separate fresh-context review agent that criticizes and sometimes closes those PRs, a weekly session analyzer that scores every conversation for system health, and a computer-use agent that logs into the product as a customer. He reports his three-person team receives 10x more PRs from the agent pair than the humans open themselves, and treats the human as a bottleneck to be removed only after the loop is closed. Watch this if you have an agent in production and lack visibility into what it's doing — it's a concrete, opinionated architecture rather than a tooling survey.

## Key Points

- Agents cannot be pre-tested the way classical software can, because the same input can produce different trajectories and the space of possible user conversations is effectively unbounded.
- The most dangerous production failures are invisible: the agent struggles mid-task, finds a workaround by luck, and finishes with no red alerts on any dashboard, leaving a latent problem in the codebase.
- Technical success is not task success — an agent can complete a flow (e.g. building a travel itinerary) while using the wrong service and miscalculating prices, so the trace looks clean but the user is unhappy.
- Operating an agent is itself an agent problem: reading logs requires enough reasoning to separate real bugs from noise and symptoms from root causes, so it needs an agent rather than regex and scripts.
- The fast loop is a log-monitoring agent with codebase access that runs every 15-60 minutes, diagnoses issues, and opens a PR — with a separate review agent holding fresh context to criticize, score, request changes, or close the PR, since fixer agents are eager to ship fixes and are biased toward their own diagnosis.
- The slow loop is a session analyzer that scores every conversation and surfaces high-level health metrics, trends, cost, sentiment, tool-call success rates, and AI-generated insights about recurring patterns and their root causes.
- Log- and code-based views miss UI-level breakage, so a computer-use agent opens the browser, logs in, and simulates a customer — with a custom skill that knows the site's DOM being much faster than generic browser driving.
- Every agent in the harness needs access to the same surfaces a human would use — trajectories, metrics, database, UI — otherwise its conclusions are guesses rather than grounded in the real problem.
- The speaker built the monitoring stack in-house despite available vendor tools, because he wanted the system to reflect exactly what he cared about looking for.

## Notable Quotes

> "most of the talks about the agents end up the moment when you ship. So, apparently it did work, the end."
>
> — [0:00](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=0s) &middot; *States the gap the entire talk is built around.*

> "But I think the shipping is the moment when the real work begins. And somehow only a few people are talking about that. And I'm calling it the missing layer."
>
> — [0:30](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=30s) &middot; *The thesis and the source of the title.*

> "the loop is uh at least as important as the product itself, sometimes even more."
>
> — [1:00](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=60s) &middot; *A ranking claim others might contest.*

> "You don't have a predefined flow that you can test before you go to the to the live. Uh and the coverage is endless."
>
> — [1:38](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=98s) &middot; *Names the structural reason classical testing fails for agents.*

> "The part that keeps me up all night. Which is you lose the feel for your own system."
>
> — [2:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=136s) &middot; *Frames the core problem as loss of intuition rather than lack of metrics.*

> "We we we build the unit test. We had some regex, some rule-based checks. We even created some scripts to simulate the customer conversation."
>
> — [2:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=136s) &middot; *Reports what they tried before concluding it was insufficient.*

> "you don't know what your agent will do until it is in the production."
>
> — [2:56](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=176s) &middot; *Compact statement of the non-testability position.*

> "LLMs are not deterministic. The same input can have a different path. Even slight modification of the input can cause a different trajectory and the coverage is endless."
>
> — [2:56](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=176s) &middot; *The technical premise underlying the whole argument.*

> "if you're talking about uh reliable agents, uh it shouldn't be depend on the luck"
>
> — [4:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=256s) &middot; *Defines reliability against lucky recovery, the talk's sharpest failure-mode claim.*

> "sometimes the agent love to make marketing features as complete uh without checking they actually worked."
>
> — [4:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=256s) &middot; *Cites an external report of agents self-declaring success.*

> "sometimes finish doesn't mean it is helpful for the user."
>
> — [4:54](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=294s) &middot; *Separates completion from usefulness in one line.*

> "So, technically it's successful but still failing the task."
>
> — [4:54](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=294s) &middot; *Names the silent-failure category his session analyzer exists to catch.*

> "production is the place when you learn what you need to uh what you need to test on the first place."
>
> — [5:36](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=336s) &middot; *Inverts the usual test-then-ship ordering.*

> "you'll find out that the operate operating agent itself is an agent problem."
>
> — [6:12](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=372s) &middot; *The pivot from dashboards to agentic observability.*

> "most of the agents are pretty eager to send the PR. They love to fix the problems. We prefer to have a separate agent which has a like fresh context."
>
> — [6:50](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=410s) &middot; *Justifies the reviewer-agent split with a concrete behavioral failure mode.*

> "a lot of teams use the same practice, but I think people don't appreciate how important it is, and you you need to spend some time on that. You need to calibrate. You need to make it reliable to trust the loop."
>
> — [7:31](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=451s) &middot; *Argues the differentiator is calibration effort, not the idea itself.*

> "the the the the PR agent and the review agent send 10 times more PR than the three of us every day."
>
> — [10:19](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=619s) &middot; *The one hard number in the talk, sizing the throughput shift.*

> "let's make the problem when you are the bottleneck and then you can remove yourself pretty easily, I think."
>
> — [11:38](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=698s) &middot; *A staged position on human-in-the-loop removal.*

> "visibility is the easiest piece. Before the agent, it was impossible, so you cannot deep dive or summarize some of the top conversations."
>
> — [13:10](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=790s) &middot; *Claims agents made per-conversation review newly tractable.*

> "we built it ourselves, so there are a lot of other companies and tools that provide the same kind of system, but I prefer to build it myself because I know what I'm interested in for, what I'm looking for."
>
> — [13:59](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=839s) &middot; *A build-vs-buy stance many observability vendors would dispute.*

> "the most is not the model alone, and you need to build the agent, or a system, or a harness around it, which which watches itself"
>
> — [18:30](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1110s) &middot; *The closing framing of the meta harness.*

> "shipping is the easiest part today. If you want to if you want to build a production agent, you need to close the loop first"
>
> — [18:30](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1110s) &middot; *The talk's takeaway imperative.*

## Positions

- The post-launch feedback loop is at least as important as the agent product itself, sometimes more important. ([1:00](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=60s), confidence: stated)
- Unit tests, regex, rule-based checks, and scripted customer simulations cover only one slice of agent failure and cannot substitute for production monitoring. ([2:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=136s), confidence: stated)
- You cannot know what your agent will do until it is running in production, because trajectories are non-deterministic and coverage is unbounded. ([2:56](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=176s), confidence: stated)
- An agent that recovers from a mid-task problem by luck, with no alert raised, is a hidden defect that should be fixed — reliability must not depend on luck. ([4:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=256s), confidence: stated)
- A technically successful agent run can still fail the user's task, so completion signals are inadequate as a quality metric. ([4:54](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=294s), confidence: stated)
- Log analysis for agents requires enough reasoning that it must itself be done by an agent rather than by scripts and filters. ([6:12](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=372s), confidence: stated)
- The fix-generating agent should be separated from the review agent, because the fixer is biased toward its own diagnosis and eager to ship PRs. ([6:50](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=410s), confidence: stated)
- This pattern is already widely used, but most teams under-invest in calibrating it enough to trust the loop. ([7:31](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=451s), confidence: stated)
- The fast loop can take a production issue from detection to a review-ready PR in about half an hour. ([8:10](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=490s), confidence: stated)
- The correct sequencing is to close the loop first and become the bottleneck yourself, then remove the human — not to remove the human up front. ([11:38](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=698s), confidence: stated)
- Per-conversation scoring across hundreds or thousands of sessions was impossible before agents and is now routine. ([13:10](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=790s), confidence: stated)
- Building your own monitoring system is preferable to using available vendor tools because you know what you are looking for. ([13:59](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=839s), confidence: stated)
- A purpose-built skill that encodes knowledge of your own site's DOM drives the browser much faster than a generic computer-use agent. ([16:47](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1007s), confidence: stated)
- Every monitoring agent must be given access to trajectories, metrics, database, and UI, or its output will be guesswork rather than grounded diagnosis. ([17:35](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1055s), confidence: stated)
- Competitive advantage now comes from the internal harness around the model, not the model or agent itself, since everyone has access to the same models. ([18:30](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1110s), confidence: stated)
- The session analyzer is expensive to run — it spends a lot of tokens — so it is run weekly rather than continuously. ([13:10](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=790s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [data flywheels](../concepts/data-flywheels.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [online evaluation](../concepts/online-evaluation.md)

