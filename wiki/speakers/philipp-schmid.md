---
title: "Philipp Schmid"
type: "speaker"
slug: "philipp-schmid"
role: "Staff Engineer"
company: "Google DeepMind"
talk_count: 1
---

# Philipp Schmid

**Staff Engineer &middot; Google DeepMind**

Philipp Schmid is a Staff Engineer at Google DeepMind working on Gemini and Gemma. His work focuses on helping developers build and benefit from AI responsibly.

[LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/)

## Talks

- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md) (Evals)

## Scheduled Sessions

- **Why Agents Should Have Their Own Sandbox** &middot; Day 3 — Session Day 2 &middot; 1:30pm-1:50pm &middot; Expo Stage 3 SW
- **Don't Ship Skills Without Evals** &middot; Day 3 — Session Day 2 &middot; 3:20pm-3:40pm &middot; Track 5
- **Agents Without Code: How Skills, YAML, and Filesystems Replaced Python** &middot; Day 4 — Session Day 3 &middot; 3:45pm-4:05pm &middot; Main Stage

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [context window management](../concepts/context-window-management.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "Everyone uses skills, no one has evals."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [0:01](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1s)

> "it's very hard to know if your skill is good or bad because like agents are really non-deterministic. So you might not know if your uh task fails because your skill is bad or if your task fails because it's way too challenging for the model."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [0:45](https://www.youtube.com/watch?v=0vphxNt4wyk&t=45s)

> "When you build an agent inside your application for consumer or customers, they have no idea about what a skill is. They don't start their prompt with use customer support skill to like help me refund or use refund skill to help me solve my problem."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [1:59](https://www.youtube.com/watch?v=0vphxNt4wyk&t=119s)

> "Capability skills teach models something they cannot do consistently at the moment."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [3:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=192s)

> "the better our model gets, the more likely it is that we can remove those skills. And Evals will tell us when we can retire skill and when not."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [3:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=192s)

> "skills on average improve the performance by roughly 15%"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:05](https://www.youtube.com/watch?v=0vphxNt4wyk&t=245s)

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s)

> "the description is the cost you always pay on every model invocation. So, on every model call, the description is part of the model context. So, you always pay that 100 200 tokens cost"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [7:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=461s)

> "If you have those type of use cases, you should not use skills. You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [8:49](https://www.youtube.com/watch?v=0vphxNt4wyk&t=529s)

> "I like to create five for like the happy path. So, when do I want to use that skill? Five when I don't want to use that skill just to make sure the model is not over triggering the skill and confusing itself."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [10:03](https://www.youtube.com/watch?v=0vphxNt4wyk&t=603s)

> "no-ops basically is an instruction which does nothing to change the agent's behavior. It's like before making an implementation easy to read."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [11:10](https://www.youtube.com/watch?v=0vphxNt4wyk&t=670s)

> "we created 117 test cases"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [12:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=748s)

> "the end result was that we improved the the performance up to like almost 90% for generating valid interactions API code with the latest Gemini models"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [12:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=748s)

> "most of the tests or evals for skills can be regex. It's like very amazing how good of regex you can write using coding agents."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [14:17](https://www.youtube.com/watch?v=0vphxNt4wyk&t=857s)

> "if a change happens to or like a diff to the skill file, the eval will be run, and there will also be a result, and the change will not be merged if it is not improving the test cases."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [16:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=988s)

> "we have seen 50% of the failures uh because the skill was not triggered correctly because the prompt of the user was not uh detailed enough"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s)

> "we don't want to test if the model loads the skill on like the first turn. We really want to test if it can achieve the task based on the prompt."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [18:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1102s)

> "coding agents are very good at finding or cheating. So, if you run inside uh your existing environment, it might look up previous chats or it might look up some other executions"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [18:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1102s)

> "agent harnesses behave differently and of course model behaves differently. So, maybe your skill is very good with a Gemini but very bad with Codex"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [18:57](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1137s)

> "If your um model is good enough that it doesn't need the skill anymore, keep that eval. You don't need to throw that eval away because you throw the skill away."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [19:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1181s)

> "run always evals with your skill loaded and without your skill loaded. Only that way you will know when you can retire skill or if a skill is really helpful for your performance."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [20:50](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1250s)

