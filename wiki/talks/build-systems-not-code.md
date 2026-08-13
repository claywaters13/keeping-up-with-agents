---
title: "Build Systems, Not Code"
type: "talk"
slug: "build-systems-not-code"
org: "Agentic AI Foundation"
video_id: "ZD9-4fW2HhM"
duration_sec: 1178
word_count: 3006
speakers: ["Angie Jones"]
---

# Build Systems, Not Code

**Speakers:** [Angie Jones](../speakers/angie-jones.md)

**Org:** Agentic AI Foundation

**Duration:** 19m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=ZD9-4fW2HhM)

## Summary

Angie Jones argues that the fun of engineering hasn't been automated away — it has moved up a layer, from writing code to architecting agentic systems. Using a running example of "Relocation Scout," a house-hunting agent, she walks through the classical engineering disciplines that map directly onto agent design: systems thinking, workflow design, decomposition, separation of concerns, modularity, algorithmic thinking, contracts, state management, threat modeling, and maintainability. Her central practical claims are that giant prompts are the agentic equivalent of a god class, that deterministic work belongs in plain code rather than a model, and that you should not let a coding agent design your other agents because the result won't be maintainable. Worth watching if you're building agents beyond one-off prompts and want a concrete vocabulary for structuring them out of skills, sub-agents, schemas, scripts, and a queryable memory layer.

## Key Points

- An agent is a component inside a larger system of files, tools, humans, and other agents — not the system itself — so it should be designed with boundaries, dependencies, and failure modes like any other component.
- A goal is not a workflow: agents need an explicit path (gather, weigh, act) and every run should terminate by stopping, retrying, or escalating.
- The giant prompt is the agentic version of a god class; when four distinct jobs are crammed into one prompt, drift is the predictable result.
- Separation of concerns has direct agentic analogs — a reusable process becomes a skill, output format becomes a schema, exact computation becomes a script, and a meaty subtask becomes a sub-agent.
- Sub-agents are architecturally like functions: single-purpose, callable, and free of the parent session's context, which is why they perform well in scope.
- Use code for determinism, agents for judgment, and humans for authority; if a task has an exact answer, reach for code, because it's cheaper and more reliable.
- Agent output that another system must act on needs a structured contract written to a queryable memory layer, not free-form prose buried in a session.
- Idempotency must be enforced by the system rather than trusted to the model, since a retry can be reworded by the model into what looks like a brand-new task.
- Treat listing copy, forum threads, and reviews as untrusted input — evidence, not instructions — and wall high-consequence actions like emailing sellers or submitting offers behind human approval to reduce blast radius.
- Every level of the system should carry an agents file documenting workflow, policy, resources, and memory upkeep, so a fresh context can start cold; failure to update the system cleanly is a signal that maintainability needs work.

## Notable Quotes

> "Many of us who are coding with agents, we feel like this quiet sense of dread. Like they're kind of taking all of the fun parts of building and leaving us with the unglamorous work, but let me give you a little advice. Let them have it."
>
> — [0:00](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=0s) &middot; *frames the emotional premise the whole talk answers*

> "When you're building agents, not just using them to write code, you start getting into architecting agentic systems. And you realize that the building blocks are different, but the discipline is the same."
>
> — [0:41](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=41s) &middot; *the thesis in one sentence*

> "an agent is not the system, right? It's part of the system. And that system has files and tools, humans, even other agents."
>
> — [1:32](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=92s) &middot; *core systems-thinking reframe*

> "So, I often hear people say, "Just let your coding agent build it, right?" And I think that's a mistake."
>
> — [2:19](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=139s) &middot; *takes an explicit contrarian side others would dispute*

> "As much as we all love the slash goal command, an agent needs more than a goal, it needs a path."
>
> — [3:08](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=188s) &middot; *crisp statement of the workflow-design argument*

> "We call these code smells. Well, agentic systems, they have their own version of this. It's the giant prompts."
>
> — [3:47](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=227s) &middot; *names the central anti-pattern*

> "That's four different jobs crammed into a single prompt. And then you wonder why your agent is drifting and not sticking to the script."
>
> — [5:13](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=313s) &middot; *connects prompt bloat directly to observed agent drift*

> "Now, decomposition is about breaking the system apart. Separation of concerns is about putting each responsibility in the right place."
>
> — [5:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=358s) &middot; *clean distinction between two often-conflated disciplines*

> "Architecturally, they're sort of like functions, right? So, you give them one specific task to do. You call them when it needs to be done. And they can do it really well because that's all that they have in scope, right?"
>
> — [8:15](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=495s) &middot; *the clearest mental model for sub-agents in the talk*

> "Just because an agent can do something doesn't mean that it should, right? Some tasks are better handled by plain code."
>
> — [8:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=538s) &middot; *states the algorithmic-thinking position plainly*

> "I promise you AI did not invent automation, right? We can use code while still using these systems."
>
> — [9:56](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=596s) &middot; *memorable pushback against model-for-everything design*

> "my rule of thumb here is if a task has an exact answer, reach for code. If it needs interpretation or judgment, that's when you can get the agent to do it, right?"
>
> — [9:56](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=596s) &middot; *an actionable, checkable heuristic*

> "So, use code for determinism, use agents for judgment, and then use humans for authority."
>
> — [10:43](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=643s) &middot; *the talk's most quotable allocation rule*

> "defining the shape forces you to get really clear and specific. Because if you can't say what the output should look like, then you probably don't yet fully understand what you're asking the agent to produce."
>
> — [11:27](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=687s) &middot; *argues schemas are a design tool, not just plumbing*

> "you have to design for idempotency, which is where you can run the same thing twice and the second run doesn't cause a mess."
>
> — [13:17](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=797s) &middot; *names the reliability property agentic retries need*

> "with the agents, they add a little trap here because you can't trust the model because its outputs can vary, right? So, a retry risks the agent actually like rewording the request just enough that it might look like a brand new task."
>
> — [13:17](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=797s) &middot; *explains why model nondeterminism breaks naive retry logic*

> "So, we need to treat all of that as untrusted input and make it very clear to the agent that this is evidence, not instructions."
>
> — [15:41](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=941s) &middot; *compact prompt-injection defense principle*

> "those actions need to be walled behind like my approval, right? And when you draw that wall, what you've done is reduced the blast radius"
>
> — [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s) &middot; *ties human approval gates to a security rationale*

> "This is one of the key reasons why I don't just have my coding agent design my other agents because I know it'll be thrown together in a way that's technically works, but it's not maintainable, right?"
>
> — [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s) &middot; *the talk's sharpest and most debatable claim*

> "I design my agent so that even in a fresh context, they can jump right into the system and start cold, knowing exactly what to do."
>
> — [18:11](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=1091s) &middot; *gives a concrete test for agentic maintainability*

> "So designing agents is software engineering. The primitives are different, but the discipline is the same."
>
> — [18:53](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=1133s) &middot; *the closing restatement of the thesis*

## Positions

- Letting a coding agent design your other agents is a mistake, because it will produce something that technically works but is not maintainable — typically a giant prompt with poor separation of concerns. ([2:19](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=139s), confidence: stated)
- A goal alone is insufficient for an agent; the workflow must define the path, and every run must terminate in one of three ways — stop, retry, or escalate. ([3:08](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=188s), confidence: stated)
- Giant prompts are the agentic equivalent of code smells like god classes and bloated services, and they are the cause of agent drift. ([3:47](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=227s), confidence: stated)
- Tasks with an exact answer (commute calculation, deduplication) should be handled by plain code, which is cheaper and more reliable than a model. ([9:56](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=596s), confidence: stated)
- Responsibility should be allocated as code for determinism, agents for judgment, and humans for authority. ([10:43](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=643s), confidence: stated)
- Free-form text output is acceptable only when a human is the sole reader; any output another system consumes should follow a structured contract. ([11:27](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=687s), confidence: stated)
- Idempotency must be enforced at the system level rather than relying on the model, because model outputs vary enough that a retry can look like a new task. ([14:06](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=846s), confidence: stated)
- Agentic systems need a lint pass to stay healthy and to detect half-completed runs. ([14:06](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=846s), confidence: stated)
- All externally sourced content — listing copy, forum threads, anonymous reviews — must be treated as untrusted evidence rather than instructions. ([15:41](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=941s), confidence: stated)
- High-consequence actions such as emailing sellers, booking tours, or submitting offers should require human approval rather than running autonomously. ([16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s), confidence: stated)
- A well-designed agentic system can be updated successfully by any harness; difficulty updating it is a signal that maintainability needs improvement. ([18:11](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=1091s), confidence: stated)
- Not everything should be modularized — some instructions are local to a workflow and abstracting them costs more than it saves. ([8:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=538s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent skills](../concepts/agent-skills.md)
- [durable execution](../concepts/durable-execution.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [structured output contracts](../concepts/structured-output-contracts.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)
- [task decomposition](../concepts/task-decomposition.md)

