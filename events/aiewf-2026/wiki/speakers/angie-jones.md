---
title: "Angie Jones"
type: "speaker"
slug: "angie-jones"
talk_count: 1
---

# Angie Jones

## Talks

- [Build Systems, Not Code](../talks/build-systems-not-code.md)

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

## Quotes

> "Many of us who are coding with agents, we feel like this quiet sense of dread. Like they're kind of taking all of the fun parts of building and leaving us with the unglamorous work, but let me give you a little advice. Let them have it."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [0:00](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=0s)

> "When you're building agents, not just using them to write code, you start getting into architecting agentic systems. And you realize that the building blocks are different, but the discipline is the same."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [0:41](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=41s)

> "an agent is not the system, right? It's part of the system. And that system has files and tools, humans, even other agents."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [1:32](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=92s)

> "So, I often hear people say, "Just let your coding agent build it, right?" And I think that's a mistake."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [2:19](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=139s)

> "As much as we all love the slash goal command, an agent needs more than a goal, it needs a path."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [3:08](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=188s)

> "We call these code smells. Well, agentic systems, they have their own version of this. It's the giant prompts."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [3:47](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=227s)

> "That's four different jobs crammed into a single prompt. And then you wonder why your agent is drifting and not sticking to the script."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [5:13](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=313s)

> "Now, decomposition is about breaking the system apart. Separation of concerns is about putting each responsibility in the right place."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [5:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=358s)

> "Architecturally, they're sort of like functions, right? So, you give them one specific task to do. You call them when it needs to be done. And they can do it really well because that's all that they have in scope, right?"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [8:15](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=495s)

> "Just because an agent can do something doesn't mean that it should, right? Some tasks are better handled by plain code."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [8:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=538s)

> "I promise you AI did not invent automation, right? We can use code while still using these systems."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [9:56](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=596s)

> "my rule of thumb here is if a task has an exact answer, reach for code. If it needs interpretation or judgment, that's when you can get the agent to do it, right?"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [9:56](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=596s)

> "So, use code for determinism, use agents for judgment, and then use humans for authority."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [10:43](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=643s)

> "defining the shape forces you to get really clear and specific. Because if you can't say what the output should look like, then you probably don't yet fully understand what you're asking the agent to produce."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [11:27](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=687s)

> "you have to design for idempotency, which is where you can run the same thing twice and the second run doesn't cause a mess."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [13:17](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=797s)

> "with the agents, they add a little trap here because you can't trust the model because its outputs can vary, right? So, a retry risks the agent actually like rewording the request just enough that it might look like a brand new task."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [13:17](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=797s)

> "So, we need to treat all of that as untrusted input and make it very clear to the agent that this is evidence, not instructions."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [15:41](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=941s)

> "those actions need to be walled behind like my approval, right? And when you draw that wall, what you've done is reduced the blast radius"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s)

> "This is one of the key reasons why I don't just have my coding agent design my other agents because I know it'll be thrown together in a way that's technically works, but it's not maintainable, right?"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s)

> "I design my agent so that even in a fresh context, they can jump right into the system and start cold, knowing exactly what to do."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [18:11](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=1091s)

> "So designing agents is software engineering. The primitives are different, but the discipline is the same."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [18:53](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=1133s)

