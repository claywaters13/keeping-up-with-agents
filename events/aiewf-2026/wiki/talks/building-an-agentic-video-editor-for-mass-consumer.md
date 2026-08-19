---
title: "Building an Agentic Video Editor for Mass Consumer"
type: "talk"
slug: "building-an-agentic-video-editor-for-mass-consumer"
track: "Generative Media"
org: "Reelful"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "pPj_tjlvYjA"
duration_sec: 764
word_count: 1672
speakers: ["Ekaterina Deyneka"]
---

# Building an Agentic Video Editor for Mass Consumer

**Speakers:** [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)

**Org:** Reelful

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 12m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=pPj_tjlvYjA)

## Summary

Kate Deyneka, founder and CEO of Reelful, walks through the architecture of an agentic video editor aimed at ordinary consumers rather than professional editors. Her core argument is that editing real personal footage is a harder agentic problem than generating video from scratch: a blank canvas lets the agent do anything, while editing forces it to judge which moments are best, what to cut, and how to assemble messy or incomplete footage into something that reads as professionally made. She maps the pipeline — media understanding and transcription, a user-approved creative plan, a sandbox where an agent with taste-encoding skills (cut rules, font pairs, B-roll generation) writes a Remotion composition as React code, then a verification layer that catches errors and forces re-iteration — and notes the infrastructure is nearly identical to an agentic app builder. The second half is about distribution rather than architecture: mobile-first, directional templates instead of prompting, and a conventional timeline editor for touch-ups, because the hard part is hiding a complex agentic workflow from mass consumers. Worth watching if you want a concrete case study of agent-writes-code applied to a non-code artifact, or if you're thinking about consumer UX on top of multi-step agent pipelines.

## Key Points

- Editing existing real footage is a harder agentic problem than generation, because the agent must decide which moments are best and what to omit rather than working from a blank canvas.
- The infrastructure for an agentic video editor closely mirrors an agentic app builder: prompt UI, a remote sandbox, an agent with tools and skills, and an artifact — a code base in one case, a video composition in the other.
- Reelful's pipeline runs media understanding and speech transcription first, then produces a creative plan the user approves or regenerates before any editing begins.
- Editorial taste is encoded as agent skills — cut rules for selecting moments, font pairings, and B-roll generation guidance — which is where the company's craft lives.
- Videos are produced as Remotion compositions, i.e. React code, specifically because agents are strong at writing code and this converts video assembly into a code-generation task.
- A dedicated verification layer checks the composition is clean, well-defined, and renderable, and sends the agent back to re-iterate when it isn't.
- Consumer delivery is treated as a separate problem from the pipeline: mobile-first so people can edit while walking or driving, and the complexity is deliberately hidden from users.
- Because prompting for video is hard for consumers, Reelful offers directional templates (speak-to-camera, add B-rolls, add voiceover) that work with no prompt at all, plus a conventional timeline editor for small manual fixes after agentic generation.

## Notable Quotes

> "I never posted them online because video editing is hard."
>
> — [0:01](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=1s) &middot; *States the consumer pain point that motivates the entire product in one line.*

> "as a user, you just drop in your media, photos and videos, and provide some context."
>
> — [0:59](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=59s) &middot; *Defines the input contract for agentic video editing.*

> "the agent will go, understand your media, uh find the right moments, assemble everything together, generate captions, music, voiceover, b-rolls, uh and give you a ready-to-share clip."
>
> — [0:59](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=59s) &middot; *Enumerates the full scope the agent is expected to cover autonomously.*

> "At RealFull, we're focusing on editing real footage. So, we do not generate a lot of content."
>
> — [3:42](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=222s) &middot; *A clear positioning choice against the generative-video default.*

> "We are expecting you to provide your real life, your personal content, and we will edit it for you. And actually, this is a more complex problem because if the agent has a blank blank canvas, it can do whatever they can."
>
> — [3:42](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=222s) &middot; *The talk's central contrarian claim: editing is harder than generation.*

> "in the editing case, the agent has to figure out which moments are the best. Uh what to omit, what to use, how to organize everything together."
>
> — [4:41](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=281s) &middot; *Names the specific judgment burden that makes editing hard for an agent.*

> "sometimes footage can be messy or incomplete, and agent still has to deliver a very polished result, professionally made, so that ideally the viewers of this content don't get if it is like AI or human edited."
>
> — [4:41](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=281s) &middot; *Sets an explicit quality bar — output indistinguishable from human editing.*

> "Then, we are providing a creative plan for the user so that they can approve if they like it or not, what they want to change or maybe regenerate, uh, and we create this plan before actually starting editing."
>
> — [5:33](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=333s) &middot; *Describes a plan-approval checkpoint placed before expensive execution.*

> "and this is where our taste and craft, uh, live, actually."
>
> — [6:22](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=382s) &middot; *Locates the product's differentiation in the skills layer, not the model.*

> "Remotion is a framework, open-source open-source framework, uh, to create videos as code, as React code."
>
> — [7:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=432s) &middot; *Names the concrete representation that makes video agent-writable.*

> "Because, uh, agents are really good at writing code and therefore we can use them to create videos with this remotion framework."
>
> — [7:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=432s) &middot; *The explicit reasoning for choosing a code representation over a timeline API.*

> "Of course agent can make mistakes and that's why we develop this verification layer to make sure that all the the composition is clean, is well defined, everything will be rendered and if there are there are some problems then the agent will reiterate on the composition."
>
> — [7:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=432s) &middot; *Describes the correctness loop that makes the code-generation approach viable.*

> "It's like very complex workflow and ideally we don't want our users to even know anything about it."
>
> — [8:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=492s) &middot; *Frames the consumer product philosophy: hide the agent entirely.*

> "this is even maybe a bigger problem how to deliver this complex agentic workflow to mass consumer."
>
> — [8:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=492s) &middot; *Claims distribution/UX is a harder problem than the pipeline itself.*

> "So we decided to go mobile first so that users can edit videos videos while driving, walking or maybe lifting weights."
>
> — [8:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=492s) &middot; *Concrete platform decision derived from the consumer thesis.*

> "Also, I know that prompting videos can sometimes be also challenging. That's why we create directional templates."
>
> — [8:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=492s) &middot; *Identifies prompting itself as a consumer barrier and names the mitigation.*

> "So a lot of people are already sort of using regular video editors and that's why we want to provide this experience as well."
>
> — [9:14](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=554s) &middot; *Justifies keeping a familiar manual editor alongside the agent.*

> "User first generates a video agentically, but if they want to tweak it, for example, remove a second or maybe correct some word in the captions, they can go into building editor and edit it a little bit."
>
> — [9:14](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=554s) &middot; *Spells out the agent-first, human-refine interaction model.*

> "basically all these videos they were assembled only using agent, no regular video editor, and I already posting them on social media."
>
> — [10:41](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=641s) &middot; *The demo claim — end-to-end agentic output shipped to real social feeds.*

## Positions

- Editing real user footage is a harder agentic problem than generating video from scratch, because a blank canvas imposes no constraints while editing requires selecting and omitting from fixed material. ([3:42](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=222s), confidence: stated)
- An agentic video editor is infrastructurally near-identical to an agentic app builder — same prompt UI, sandbox, agent-with-tools pattern, differing mainly in the artifact produced. ([2:58](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=178s), confidence: stated)
- Representing video as React/Remotion code is the right substrate for agents because code generation is what current agents are strongest at. ([7:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=432s), confidence: stated)
- Agents reliably make mistakes in composition generation, so a separate verification layer plus re-iteration is a required part of the pipeline rather than an optimization. ([7:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=432s), confidence: stated)
- Delivering the complex agentic workflow to mass consumers is a bigger problem than building the workflow itself. ([8:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=492s), confidence: stated)
- Editorial taste — cut rules, font pairings, B-roll conventions — should be encoded as agent skills, and that skills layer is the real source of product differentiation. ([6:22](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=382s), confidence: stated)
- Consumers cannot be expected to prompt effectively for video, so template-driven direction should replace free-text prompting as the default entry point. ([8:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=492s), confidence: stated)
- A fully agentic editor still needs a conventional timeline editor, because users expect a familiar surface for small corrections. ([9:14](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=554s), confidence: stated)
- Showing the user a creative plan for approval before execution is worth the extra step in a consumer product. ([5:33](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=333s), confidence: implied)
- The quality bar for agentic editing is output that viewers cannot distinguish from human-edited video. ([4:41](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=281s), confidence: stated)

## Concepts

- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent skills](../concepts/agent-skills.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [vision-language models](../concepts/vision-language-models.md)

