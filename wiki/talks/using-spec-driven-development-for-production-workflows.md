---
title: "Using Spec-Driven Development for Production Workflows"
type: "talk"
slug: "using-spec-driven-development-for-production-workflows"
org: "AWS"
video_id: "IddXPepIAS4"
duration_sec: 1067
word_count: 3287
speakers: ["Erik Hanchett"]
---

# Using Spec-Driven Development for Production Workflows

**Speakers:** [Erik Hanchett](../speakers/erik-hanchett.md)

**Org:** AWS

**Duration:** 17m 47s

[Watch on YouTube](https://www.youtube.com/watch?v=IddXPepIAS4)

## Summary

Erik Hanchett, a senior developer advocate at AWS, makes the case for spec-driven development: writing requirements, design, and task documents in markdown before any code is generated, with the human reviewing each artifact in between. His central framing is that coding agents behave like over-eager interns who will 'go off the rails' given leeway, so the specs exist to constrain and guide them rather than to satisfy process for its own sake. He walks through the three-document flow (requirements in EARS format, a design doc with mermaid diagrams, then a task list), shows it in AWS's Kiro IDE, and stresses that the same workflow can be done manually with any assistant or with GitHub's open-source Spec Kit. Secondary threads cover the Goldilocks problem of how much context to put in agents.md/steering files, using skills as on-demand instruction files, pulling requirements from Jira/Asana via MCP, and property-based tests generated against the requirements. Worth watching if you want a concrete, tool-agnostic picture of the spec-first agent workflow; it is introductory and partly a Kiro demo, so skip it if you already run this pattern.

## Key Points

- Spec-driven development means structured specifications — requirements and design documents in markdown — are created and human-reviewed before any code is written.
- The justification is behavioral, not bureaucratic: coding assistants act like eager interns who go off the rails with too much leeway, and the specs are the guardrails.
- Frontier models improving and adding planning modes does not remove the need for explicit documents, because requirements and paradigms keep shifting and the model needs project-specific context.
- Context volume is a real tradeoff: agents.md, CLAUDE.md, or Kiro steering docs should hit a 'Goldilocks zone' rather than being stuffed with everything.
- The human stays accountable — you are the code reviewer of everything generated, and you must read the requirements and design docs for hallucinations and inconsistencies before implementation.
- The flow is not Kiro-specific: you can prompt any assistant for requirements, then design, then an implementation task list, or use GitHub's open-source Spec Kit.
- Spec-driven development works on legacy codebases, not just greenfield — Hanchett has seen years-old apps accumulate dozens of spec files — though small changes may not be worth the ceremony.
- Kiro's task lists can include property-based tests written against the requirements and design documents, run with fast-check in TypeScript over many generated values.
- MCP servers let you pull product-manager-authored requirements out of Jira or Asana directly into the spec-generation step, which Hanchett cites as MCP's strongest use here.
- A practical tip: after the task list is generated, ask the agent to reorder the top four tasks into an MVP so you see something working before implementing the rest.

## Notable Quotes

> "So, what we're doing is we are writing these markdown files, we're writing the specifications and the design document before any of the code is written."
>
> — [0:41](https://www.youtube.com/watch?v=IddXPepIAS4&t=41s) &middot; *The working definition of the practice, in the speaker's own words.*

> "I kind of like to think about our coding assistants, our large language models that we're using every day as sort of like AI interns. You need to really prompt them, you really need to push them the right way"
>
> — [0:41](https://www.youtube.com/watch?v=IddXPepIAS4&t=41s) &middot; *The central analogy the whole argument rests on.*

> "So, you really need to guide them. Because if you give them just a little bit of of leeway, they will go off the rails. And really the spec-driven development helps guide them in the right direction."
>
> — [1:27](https://www.youtube.com/watch?v=IddXPepIAS4&t=87s) &middot; *States the causal claim: specs are a control mechanism, not documentation.*

> "But there's nothing better than actually having those documents created and having you be in the middle before it jumps into the net that next part with it creating code."
>
> — [3:32](https://www.youtube.com/watch?v=IddXPepIAS4&t=212s) &middot; *His answer to 'can't planning mode do this already?' — a position others contest.*

> "Now, I told you before that spec-driven development gives you a lot of context that gets fed into that large language model, but sometimes you have too much of a good thing."
>
> — [3:32](https://www.youtube.com/watch?v=IddXPepIAS4&t=212s) &middot; *Names the tradeoff against his own recommendation.*

> "I would be very careful not to put too much information or too little information in that. Kind of like that Goldilocks zone of information is what you need."
>
> — [4:16](https://www.youtube.com/watch?v=IddXPepIAS4&t=256s) &middot; *Concrete guidance on sizing steering/agents.md files.*

> "Skills are like instruction files that you can give to your coding agents that are ran on demand."
>
> — [4:53](https://www.youtube.com/watch?v=IddXPepIAS4&t=293s) &middot; *Compact definition of skills and how they compose with the spec flow.*

> "You need to be the code reviewer of all the code that's generated through this process."
>
> — [5:38](https://www.youtube.com/watch?v=IddXPepIAS4&t=338s) &middot; *The human-in-the-loop obligation stated flatly.*

> "because at the end of the day, if something goes wrong, you are the person that are going to be blamed for it, not the agent."
>
> — [5:38](https://www.youtube.com/watch?v=IddXPepIAS4&t=338s) &middot; *Grounds review in accountability rather than code quality.*

> "I think right now it's switching. Most people are starting to use CLIs more often than IDEs."
>
> — [7:08](https://www.youtube.com/watch?v=IddXPepIAS4&t=428s) &middot; *An empirical claim about tooling adoption from someone shipping both.*

> "When we released this, it actually went a little bit viral. We got tens of thousands of downloads."
>
> — [7:48](https://www.youtube.com/watch?v=IddXPepIAS4&t=468s) &middot; *Reported number on Kiro's launch.*

> "But I don't want this to be a half-hour pitch for Kiro. You can do this process spec-driven development without Kiro and there's a few few ways."
>
> — [8:24](https://www.youtube.com/watch?v=IddXPepIAS4&t=504s) &middot; *Explicitly decouples the practice from the product.*

> "Now, you're probably thinking is this spec only good for greenfield brand new projects? And I would say absolutely not. I've seen existing apps that are years old have dozens and dozens of these different spec files in them."
>
> — [9:44](https://www.youtube.com/watch?v=IddXPepIAS4&t=584s) &middot; *Directly rebuts the most common objection to spec-first workflows.*

> "these are really good for when you're doing in-depth features, when you need your project needs a little more upfront planning, uh and you just want to build things in a structured way."
>
> — [10:19](https://www.youtube.com/watch?v=IddXPepIAS4&t=619s) &middot; *Scopes where the overhead pays off.*

> "Now, this is at the point I would highly recommend, if you're trying this at home, to stop and go in and update it with your knowledge and expertise and taste to exactly what you're looking for. Because it's only as good as what you put in."
>
> — [11:34](https://www.youtube.com/watch?v=IddXPepIAS4&t=694s) &middot; *Pinpoints the single highest-leverage human intervention in the flow.*

> "Uh it also has something called property-based tests in them, which are tests that are against the requirements document and design document."
>
> — [12:12](https://www.youtube.com/watch?v=IddXPepIAS4&t=732s) &middot; *Links verification back to the spec artifacts, closing the loop.*

> "I tell it, "Please take the top four tasks, put them at the top, and create an MVP for me first." So that way I can actually see it working."
>
> — [12:12](https://www.youtube.com/watch?v=IddXPepIAS4&t=732s) &middot; *Actionable technique any listener can copy.*

> "I really think MCP is still maturing. There's a lot uh a long road ahead for it, especially with some of the security stuff it's doing. I would keep an eye out for MCP"
>
> — [13:36](https://www.youtube.com/watch?v=IddXPepIAS4&t=816s) &middot; *Takes a side in the 'is MCP dead' debate.*

> "It uses fast check in this TypeScript in the node world to do these tests which actually run dozens if not hundreds of times with different values to make sure that it's uh these requirements are satisfied correctly"
>
> — [15:26](https://www.youtube.com/watch?v=IddXPepIAS4&t=926s) &middot; *Specifies the actual testing implementation, not just the concept.*

## Positions

- Writing specification and design documents before code produces higher-quality output from coding assistants, not just faster output. ([0:00](https://www.youtube.com/watch?v=IddXPepIAS4&t=0s), confidence: stated)
- Coding assistants left unguided will go off the rails, so explicit up-front documents are needed as guardrails. ([1:27](https://www.youtube.com/watch?v=IddXPepIAS4&t=87s), confidence: stated)
- Better frontier models and built-in planning/thinking modes do not eliminate the need for human-reviewed spec documents. ([2:52](https://www.youtube.com/watch?v=IddXPepIAS4&t=172s), confidence: stated)
- Putting too much information into agents.md or steering files is harmful; there is a Goldilocks amount of context. ([4:16](https://www.youtube.com/watch?v=IddXPepIAS4&t=256s), confidence: stated)
- The human, not the agent, is accountable for generated code and must personally review both the code and the spec documents. ([5:38](https://www.youtube.com/watch?v=IddXPepIAS4&t=338s), confidence: stated)
- More people are now using CLI coding assistants than IDE-based ones. ([7:08](https://www.youtube.com/watch?v=IddXPepIAS4&t=428s), confidence: stated)
- Spec-driven development is a workflow, not a product feature — it can be done manually with any assistant or with GitHub's open-source Spec Kit. ([8:24](https://www.youtube.com/watch?v=IddXPepIAS4&t=504s), confidence: stated)
- Spec-driven development applies to existing legacy codebases, not only greenfield projects. ([9:44](https://www.youtube.com/watch?v=IddXPepIAS4&t=584s), confidence: stated)
- Small changes and quick fixes may not justify the spec workflow and are better handled by vibe coding. ([10:19](https://www.youtube.com/watch?v=IddXPepIAS4&t=619s), confidence: stated)
- Generated design and requirements documents should always be hand-edited by the developer before implementation, since output quality is bounded by input quality. ([11:34](https://www.youtube.com/watch?v=IddXPepIAS4&t=694s), confidence: stated)
- Property-based tests derived from the requirements and design documents are worth generating and running to verify tasks were implemented correctly. ([12:12](https://www.youtube.com/watch?v=IddXPepIAS4&t=732s), confidence: stated)
- MCP is not dead; it is still maturing and remains valuable, particularly for pulling ticket and requirements data from tools like Jira or Asana into the spec flow. ([13:36](https://www.youtube.com/watch?v=IddXPepIAS4&t=816s), confidence: stated)
- Requirements and design can be authored in either order — starting from the design document first is a legitimate variant of the flow. ([11:34](https://www.youtube.com/watch?v=IddXPepIAS4&t=694s), confidence: stated)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [context window management](../concepts/context-window-management.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)
- [spec-driven development](../concepts/spec-driven-development.md)
- [task decomposition](../concepts/task-decomposition.md)
- [verifier design](../concepts/verifier-design.md)

