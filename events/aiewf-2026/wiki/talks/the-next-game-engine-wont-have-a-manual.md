---
title: "The Next Game Engine Won't Have a Manual"
type: "talk"
slug: "the-next-game-engine-wont-have-a-manual"
track: "Generative Media"
org: "Nereu"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "VBCDhRrvlYo"
duration_sec: 1172
word_count: 3187
speakers: ["Arturo Nunez"]
---

# The Next Game Engine Won't Have a Manual

**Speakers:** [Arturo Nunez](../speakers/arturo-nunez.md)

**Org:** Nereu

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 19m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=VBCDhRrvlYo)

## Summary

Arturo Nunez, a former Unity engineer of nearly a decade, argues that bolting LLMs onto existing game engines is the wrong abstraction: the assistant ends up speaking the engine's vocabulary (meshes, rigid bodies, colliders, sliders) and reinvents the same boilerplate every time. His tool, Nereu, instead exposes an "asset tag system" (ATS) derived from entity-component-system design, where everything is an asset and users attach intent tags — character, drivable, animated, double jump — in the language players already use to describe games. He demos building a playable scene (robot character, WASD movement, rain particles, follow camera) purely by description, and explains the engineering behind it: vision models auto-tagged 6–7,000 assets, and scene context is assembled using a level-of-detail analogy, sending full tag data for nearby objects and thin summaries for distant ones. Notably, he rejects one-shotting entire games as a goal — the assistant exists to unstick people so they learn game design, not code. Worth watching for the ATS/ECS framing and the LOD-style context assembly, both transferable beyond game dev.

## Key Points

- Existing engines force the developer — and any LLM sitting on top of them — to think in engine vocabulary (mesh, renderer, animator, rigid body, collider, audio source) when nearly all of that is boilerplate shared by every character in every game.
- Nereu's asset tag system (ATS) is an adaptation of entity-component-system data-oriented design: assets carry intent tags, and systems query for tags like vehicle, player, or drivable to drive behavior, so the same systems are recycled across all games.
- The interaction language is the language of playing games ('move with WASD', 'double jump', 'when you collect a coin increase the score'), not code, so the LLM does not need to re-derive a follow-camera implementation on every request.
- The engine deliberately ships without a scripting system, on the theory that most users should never need one; it is JavaScript in the browser, so extension remains possible for those who want it.
- Scene context is assembled using the game-dev level-of-detail idea: objects near what the user is editing get full tag values, distant objects get a one-line summary, which keeps context from exploding on scenes with ~100 objects.
- A vision model was run over screenshots to auto-tag a library of roughly 6,000–7,000 3D assets, since manual labeling at that scale was infeasible.
- Tool definitions are fed to the assistant as they are built, and the development loop is deliberately subtractive — dropping settings and features that observed users never touch in order to keep the engine simple.
- Nunez explicitly does not want to one-shot whole games; the assistant's job is to unstick people so they finish something they can share and learn game design along the way.
- He treats world-model-generated games as a different medium rather than a replacement for engines, citing 60 fps at 4K plus real-time physics simulation as still far off.

## Notable Quotes

> "I worked at Unity, a game engine company for almost 10 years. So, I saw a lot of people building games and struggling with the same things over and over."
>
> — [3:55](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=235s) &middot; *Establishes the credential and the specific pattern-recognition the whole thesis rests on.*

> "You need to know programming, 3D modeling, rendering, music, animation, and so many other things, you either have a huge team that complement each other, or if it's just you, or you have a small team, people need to wear multiple hats."
>
> — [5:27](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=327s) &middot; *Names the concrete skill surface that makes game development inaccessible.*

> "if it's not fun, honestly, people won't play it. And I think fun should be for the player, but also for the developers."
>
> — [6:14](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=374s) &middot; *States the value judgment driving the tool's design priorities.*

> "Now, there are powerful engines, Unreal, Unity, and there are powerful LLMs and agents, but I think still it's hard. It's hard because I think we're just building a bridge between two worlds, and it's not optimal"
>
> — [6:55](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=415s) &middot; *The central critique of the LLM-plus-existing-engine approach.*

> "I've seen the the demos, and the LLM reinvents the wheel every single time."
>
> — [7:35](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=455s) &middot; *Sharpest statement of the failure mode he designed around.*

> "by default, the context is on the game engine uh rather than on the game design part, and I think we should flip that idea."
>
> — [7:35](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=455s) &middot; *The talk's thesis in one sentence.*

> "most of that is just boilerplate that every single game out there has or every character in every single game out there has, but somehow developers need to understand and read the descriptions of those components"
>
> — [8:27](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=507s) &middot; *Justifies why the abstraction can be raised without losing generality.*

> "everything is just an asset. Everything has to be rendered on screen."
>
> — [8:27](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=507s) &middot; *Compact statement of the uniform data model underlying ATS.*

> "this system comes from something that we're calling the ATS or asset tax system. Comes from the idea from game development called the entity component system data oriented design"
>
> — [9:03](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=543s) &middot; *Names the architecture and its lineage — the most reusable idea in the talk.*

> "We don't have a scripting system in there. That's on purpose. But it's just JavaScript and runs on the on the browser."
>
> — [11:14](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=674s) &middot; *A deliberate, contestable design tradeoff stated plainly.*

> "I don't think we need this feature. I haven't seen a lot of users using those things. So, let's get rid of them in order to simplify the the engine."
>
> — [13:28](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=808s) &middot; *Describes a subtractive development loop that runs counter to typical engine feature growth.*

> "I've used uh also vision models mostly to tag the the assets that we have because it's like six or 7,000 assets. I could not manually tag them all"
>
> — [14:01](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=841s) &middot; *Reports the scale that forced automated labeling.*

> "And if we feed the entire scene to the LLM, the context grows a lot."
>
> — [14:41](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=881s) &middot; *Sets up the context-assembly problem the LOD technique solves.*

> "Something that's too far away from the camera, I'm just going to maybe just put a cube and the user won't be able to to tell because it's so far away. So, we're using something similar to assemble the context."
>
> — [15:32](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=932s) &middot; *The clearest articulation of borrowing level-of-detail rendering as a context-pruning strategy.*

> "I don't want us to one-shot games that nobody is going to play and I don't see the point in in that."
>
> — [16:18](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=978s) &middot; *A direct rejection of the dominant vibe-coding demo pattern.*

> "the idea is that we allow people to make games and experience that and have fun and share that those games with their families and friends"
>
> — [16:18](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=978s) &middot; *States the actual success criterion he is optimizing for.*

> "And of course, that they learn along the way the language of making games, the language of game design, not necessarily the coding or programming."
>
> — [17:09](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=1029s) &middot; *Distinguishes the literacy the tool teaches from programming literacy.*

> "I think that's going to be a different medium even if we call them video games."
>
> — [17:09](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=1029s) &middot; *Takes a position on world models that other speakers at the event would likely dispute.*

> "Games for instance in these days they have to render 60 frames per second. And doing that at 4K resolutions in real time uh with a with a world model, I think it's still far away."
>
> — [17:52](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=1072s) &middot; *Attaches concrete performance numbers to the world-model skepticism.*

## Positions

- Putting an LLM on top of an existing game engine is suboptimal because it forces the user to speak engine and code vocabulary, and the model reinvents standard implementations like a follow camera every single time. ([6:55](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=415s), confidence: stated)
- The agent's context should be anchored on game design rather than on the game engine — the default should be flipped. ([7:35](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=455s), confidence: stated)
- Most of what a character needs in a conventional engine (renderer, animator, rigid body, collider, audio source) is boilerplate common to every game, so users should not have to understand those components or their hundreds of sliders. ([8:27](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=507s), confidence: stated)
- Describing assets with intent tags, in an ECS-derived asset tag system, is sufficient to author games because systems can query tags and reuse the same behavior across all games. ([9:03](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=543s), confidence: stated)
- Omitting a scripting system from the engine is the correct choice for most users, even though the browser JavaScript runtime leaves extension possible. ([11:14](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=674s), confidence: stated)
- Composing games down into tags and systems — covering genres, alternate descriptions of the same game, and mood-driven concerns like post-processing and lighting — is the hard part of the work, not the AI integration. ([11:57](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=717s), confidence: stated)
- Features and settings that observed users do not use should be removed to simplify the engine. ([13:28](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=808s), confidence: stated)
- Feeding the entire scene to the LLM is wasteful; context should be graded by proximity and editing focus, the way level-of-detail grades rendering quality. ([15:32](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=932s), confidence: stated)
- One-shotting complete games is not a worthwhile goal for this tool; the assistant should get people unstuck so they finish and share games instead. ([16:18](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=978s), confidence: stated)
- Games generated by world models will constitute a different medium from engine-built games, and real-time 4K rendering at 60 fps with physics simulation remains far off for them. ([17:52](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=1072s), confidence: stated)
- You do not need to be a professional game developer to make games, just as AI coding assistants removed the requirement to be a programmer to build software. ([6:14](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=374s), confidence: stated)
- The game industry has drifted toward producing and selling more at the expense of the craft, and enjoying the process should matter more than the end product. ([5:27](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=327s), confidence: stated)

## Concepts

- [agent tool design](../concepts/agent-tool-design.md)
- [context engineering](../concepts/context-engineering.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)
- [vision-language models](../concepts/vision-language-models.md)
- [world models](../concepts/world-models.md)

