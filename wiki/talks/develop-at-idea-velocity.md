---
title: "Develop at Idea Velocity"
type: "talk"
slug: "develop-at-idea-velocity"
org: "Snapchat"
video_id: "9arM9b7JgOo"
duration_sec: 928
word_count: 2704
speakers: ["Jeffrey Lee-Chan"]
---

# Develop at Idea Velocity

**Speakers:** [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)

**Org:** Snapchat

**Duration:** 15m 28s

[Watch on YouTube](https://www.youtube.com/watch?v=9arM9b7JgOo)

## Summary

A hands-on workshop-style session in which Snapchat's Jeffrey Lee-Chan walks through his personal 'idea velocity' development stack: talking to Open Claw over Slack, which orchestrates worker agents in git worktrees that themselves run Claude Code and sub-agents. His central argument is architectural — the orchestrator layer should hold spec, goals, and conversational history, while the coding layer holds implementation context, because loading CLAUDE.md, skills, and MCPs immediately eats a large fraction of a coding agent's context on 'how to do the task' rather than what to do. He also claims a practical benefit of the manager/worker split: a manager with different context is less biased toward declaring its own PR a success, and will recommend closing work a self-reviewing agent would have merged. The session is loose and demo-heavy (an AI RPG with D&D dice rolls, a multi-model consensus site, tmux/Cmux terminals, notification-driven workflow) with substantial audience Q&A on sandboxing and model choice. Worth watching if you want a concrete picture of a multi-layer agent setup and its cost tradeoffs; skip it if you want polished, generalized guidance.

## Key Points

- The stack is layered: frictionless Slack-style chat into Open Claw, which uses agent orchestrator managers (or tmux terminals for more manual control) to run workers, each of which runs Claude Code that can spawn its own sub-agents.
- The reason to use an orchestrator rather than talking to Claude Code directly is context specialization — the orchestrator's context should be spec, goals, and task history rather than implementation detail.
- Opening Claude Code immediately loads CLAUDE.md files, skills, and MCPs, which the speaker estimates can consume roughly 25% of context on how-to-do-the-task material before work begins.
- Persistent memory across conversations means instructions can be extremely terse — 'fix the skeptic agent' works because the agent already knows what that is.
- A separate manager agent produces less biased assessments than a coding agent reviewing its own work; in one case the manager recommended closing a PR that a self-reviewing agent would have called ready to merge.
- The speaker believes his own role in the loop is largely automatable — his replies to the agent are generic enough that an agent could replace him, which is his current direction of work.
- Agent capability at browser testing has improved sharply over roughly the past 6-12 months; tasks like finding a pop-up and entering a password that used to fail now work, shrinking the set of problems that truly require a human.
- Running a separate staging/sandbox agent alongside the production one increases token usage (and doubles it if you send the same work to both), so the recommended pattern is local development, integration tests on staging, then merge and deploy to production.
- Model selection is driven by cost as much as quality: the speaker runs Codex 53 until budget runs low then falls back to MiniMax, and avoids GPT 54 because it burns more tokens.

## Notable Quotes

> "when everything works, you know, maybe like 70% of the time, you describe your task"
>
> — [0:37](https://www.youtube.com/watch?v=9arM9b7JgOo&t=37s) &middot; *Rare candid success-rate number for an autonomous agent workflow.*

> "I use multiple agents with work trees, that's very key for parallelization"
>
> — [1:39](https://www.youtube.com/watch?v=9arM9b7JgOo&t=99s) &middot; *Names the specific mechanism that makes parallel agent work possible.*

> "the types of responses I give, they're not that like, um, special. As in I I actually think an agent could replace me. So, that's kind of what I'm working on right now to like get things even more autonomous."
>
> — [2:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=139s) &middot; *The talk's most provocative claim — the human in the loop is the next thing to automate.*

> "what's cool about Open Claw is it's not just about a particular repo or the code, but more of the concept"
>
> — [3:06](https://www.youtube.com/watch?v=9arM9b7JgOo&t=186s) &middot; *Frames the tool as an architectural pattern rather than a product.*

> "can you like easily talk to your AI versus like you've got a, um, remote desktop into your computer or you have to go sit down"
>
> — [3:06](https://www.youtube.com/watch?v=9arM9b7JgOo&t=186s) &middot; *Defines 'frictionless communication' as the first pillar of idea velocity.*

> "The reason I use Open Claw as specialization. So when Open Claw makes a decision, I want that context to be more about like the spec or the goals or like the history of what I want in the task rather than the code."
>
> — [5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s) &middot; *The core architectural thesis, stated directly in answer to the audience's main objection.*

> "As soon as you open up Claude, it reads Claude MDs, it reads skills, it reads um MCPs. A lot of those things are sort of independent of like the actual task. It's more about how to do the task."
>
> — [5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s) &middot; *Diagnoses the specific context pollution the separation is meant to solve.*

> "so imagine like 25% of your context already taken up by implementation"
>
> — [5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s) &middot; *Puts a concrete number on the context overhead cost.*

> "I would recommend you like try um similar approaches to this and be like, okay, like which problems truly needed that human or not"
>
> — [6:36](https://www.youtube.com/watch?v=9arM9b7JgOo&t=396s) &middot; *Gives the audience an actionable heuristic for finding automation boundaries.*

> "these things didn't work that well with agents like last year but like a year ago even 6 months ago. But now like um agents are pretty good at like nailing down a lot of browser tests for me."
>
> — [6:36](https://www.youtube.com/watch?v=9arM9b7JgOo&t=396s) &middot; *Time-stamped capability claim about browser automation improving.*

> "my agent would have a lot of problems, you know, finding a pop-up and entering a password. Now no problem."
>
> — [6:36](https://www.youtube.com/watch?v=9arM9b7JgOo&t=396s) &middot; *Concrete before/after example of the capability jump.*

> "whenever I was doing research or or whatever, I would go to multiple models and I'd be like, what's the answer? Then I copy and paste them all. I put them into one model."
>
> — [8:43](https://www.youtube.com/watch?v=9arM9b7JgOo&t=523s) &middot; *Describes a manual multi-model consensus workflow he then productized.*

> "when you go horizontal, it's really easy to lose track of your tabs"
>
> — [9:23](https://www.youtube.com/watch?v=9arM9b7JgOo&t=563s) &middot; *Small but real UI tradeoff for managing many parallel agent sessions.*

> "the way of using these terminals, usually it's more like a manager rather than a coder"
>
> — [9:23](https://www.youtube.com/watch?v=9arM9b7JgOo&t=563s) &middot; *Names the role shift that multi-agent development imposes on the human.*

> "when I when I code with these directly, um I usually feel like there's a bias, where it wants to say things are really working or whatever"
>
> — [10:07](https://www.youtube.com/watch?v=9arM9b7JgOo&t=607s) &middot; *States the self-assessment bias problem that motivates the manager layer.*

> "If this had been working on PR 294 by itself, I think it would have been like, "This PR is amazing. Like, we got to merge it, right?" But then this one was like, "No, like, there's another PR that should supersede it, and probably we should just close this PR.""
>
> — [10:07](https://www.youtube.com/watch?v=9arM9b7JgOo&t=607s) &middot; *Specific worked example of separated context producing a better judgment.*

> "that's kind of the benefit you get, where the manager has a different context um than the workers"
>
> — [10:07](https://www.youtube.com/watch?v=9arM9b7JgOo&t=607s) &middot; *Compresses the whole architecture argument into one sentence.*

> "that could double your token usage if you send the same work to both of them"
>
> — [13:30](https://www.youtube.com/watch?v=9arM9b7JgOo&t=810s) &middot; *Names the concrete cost of the staging-environment pattern.*

> "I think I would do local development and then I would run integration tests on the um sandbox or staging one, right? So I have two of them. And then once like everything's good, then I would merge the code and deploy to the production one."
>
> — [14:01](https://www.youtube.com/watch?v=9arM9b7JgOo&t=841s) &middot; *The recommended agent-environment promotion pipeline.*

> "I found uh GPT 54 to just use more tokens"
>
> — [14:29](https://www.youtube.com/watch?v=9arM9b7JgOo&t=869s) &middot; *Direct model comparison on token efficiency rather than quality.*

> "I use this until like this is getting low and then I just switch to MiniMax, which is not as good, but it kind of gets the job done. And then this is more about money than like preference"
>
> — [15:05](https://www.youtube.com/watch?v=9arM9b7JgOo&t=905s) &middot; *Frankly admits cost, not capability, drives day-to-day model routing.*

## Positions

- An orchestration layer like Open Claw is worth using over calling Claude Code directly, because it keeps spec/goal/history context separate from implementation context. ([5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s), confidence: stated)
- Loading CLAUDE.md, skills, and MCPs consumes roughly 25% of a coding agent's context on task-independent 'how to do the task' material. ([5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s), confidence: stated)
- The described workflow works about 70% of the time. ([0:37](https://www.youtube.com/watch?v=9arM9b7JgOo&t=37s), confidence: stated)
- The human's role in this loop is largely automatable — an agent could replace the speaker's own responses. ([2:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=139s), confidence: stated)
- Multiple agents running in git worktrees is the key enabler of parallelization. ([1:39](https://www.youtube.com/watch?v=9arM9b7JgOo&t=99s), confidence: stated)
- A coding agent evaluating its own PR is biased toward saying it works; a manager agent with different context gives a more reliable verdict. ([10:07](https://www.youtube.com/watch?v=9arM9b7JgOo&t=607s), confidence: stated)
- Agents became substantially more capable at browser testing over the last 6-12 months, to the point that flows like handling a pop-up and entering a password now work reliably. ([6:36](https://www.youtube.com/watch?v=9arM9b7JgOo&t=396s), confidence: stated)
- Developers should periodically re-audit which problems genuinely require a human, since agent capability improves every month or quarter. ([6:36](https://www.youtube.com/watch?v=9arM9b7JgOo&t=396s), confidence: stated)
- A Docker-style sandbox is unnecessary for personal use but would be warranted if running an externally-facing bot. ([12:49](https://www.youtube.com/watch?v=9arM9b7JgOo&t=769s), confidence: stated)
- Running local dev plus a staging agent increases token usage but buys reliability, and is worth the tradeoff. ([14:01](https://www.youtube.com/watch?v=9arM9b7JgOo&t=841s), confidence: stated)
- GPT 54 consumes more tokens than Codex 53 for comparable work, making it a worse cost choice. ([14:29](https://www.youtube.com/watch?v=9arM9b7JgOo&t=869s), confidence: stated)
- MiniMax is meaningfully worse than Codex 53 but adequate for a subset of work, so cost-tiered model routing is practical. ([15:05](https://www.youtube.com/watch?v=9arM9b7JgOo&t=905s), confidence: stated)
- Vertical tab layouts beat horizontal ones for managing many concurrent agent sessions. ([9:23](https://www.youtube.com/watch?v=9arM9b7JgOo&t=563s), confidence: stated)
- A notification-driven workflow — clearing agent notifications as they arrive — is a more efficient mode of work than watching agents run. ([9:23](https://www.youtube.com/watch?v=9arM9b7JgOo&t=563s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [context engineering](../concepts/context-engineering.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [reward hacking](../concepts/reward-hacking.md)

