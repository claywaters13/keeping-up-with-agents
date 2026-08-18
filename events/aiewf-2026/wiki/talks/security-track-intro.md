---
title: "Security Track Intro"
type: "talk"
slug: "security-track-intro"
track: "Software Factories"
org: "Snyk"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "2xJoimgoqBg"
duration_sec: 256
word_count: 672
speakers: ["Manoj Nair"]
---

# Security Track Intro

*Program title: Security Track intro*

**Speakers:** [Manoj Nair](../speakers/manoj-nair.md)

**Org:** Snyk

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 4m 16s

[Watch on YouTube](https://www.youtube.com/watch?v=2xJoimgoqBg)

## Summary

A four-minute track-opening keynote from Snyk's Randall Degges framing the state of AI security ahead of the World's Fair's first dedicated security track. He argues generative AI's real promise is shipping quality software faster, but three obstacles stand in the way: AI-generated code carrying security flaws (which he treats as unremarkable, since humans do the same), the much harder problem of deploying autonomous agents you can trust unsupervised in production, and geopolitics restricting model access. His framing is that all three collapse into one goal — using AI fearlessly with security by default. The talk is mostly a signpost to the security track sessions (Nvidia, Anthropic, Keycard, Snyk) rather than a technical deep dive; watch it only for the framing.

## Key Points

- Degges frames the appeal of generative AI not as novelty but as the ability to build better-quality software more quickly and ship it to real users.
- He treats AI-generated security vulnerabilities as a solved-in-principle, non-alarming problem: humans generate security issues when they write code, and models do too, so security belongs in the development lifecycle either way.
- The harder unsolved problem, in his view, is deploying autonomous agents to production with enough confidence that you can sleep without worrying they go off the rails and harm your business or users.
- He names geopolitics as a third, underrated barrier to moving fast, citing access to Fable being pulled and the inability to use OpenAI's GPT-5.6.
- He explicitly connects model-access restrictions to security, arguing the core unsolved problem in the space is being able to use AI fearlessly and have it be secure by default.
- The talk announces the first-ever security track at the AI Engineer World's Fair, running a full day in room 2005 on the second floor.
- Track speakers come from Nvidia, Anthropic, Keycard, and Snyk, with Degges emceeing the day.

## Notable Quotes

> "even though I've been in the security space, the thing that makes me excited in these recent years with the rise of generative AI is being able to build better quality software more quickly"
>
> — [0:01](https://www.youtube.com/watch?v=2xJoimgoqBg&t=1s) &middot; *States the speaker's framing that security is in service of shipping speed, not opposed to it.*

> "when you're building software using AI, uh there's always the risk that the code the AI generates might have a security issue. Everybody knows that. It's nothing new, right?"
>
> — [0:55](https://www.youtube.com/watch?v=2xJoimgoqBg&t=55s) &middot; *Deliberately deflates the most-discussed AI security concern as old news.*

> "everyone kind of intuitively knows that when humans write code, we generate security issues."
>
> — [0:55](https://www.youtube.com/watch?v=2xJoimgoqBg&t=55s) &middot; *The symmetry argument that underpins his dismissal of AI-code-vulnerability panic.*

> "When AI models write code, turns out they also generate security issues. And so having security as part of your development life cycle is just like a core part of like modern engineering work, no questions at all."
>
> — [1:38](https://www.youtube.com/watch?v=2xJoimgoqBg&t=98s) &middot; *Names the practical conclusion: nothing new is required, just existing lifecycle security.*

> "when you're trying to deploy actual autonomous agents into production, how do you do that in a way that allows you to go to sleep easily and not worry that the agents you deployed are going to go off the rails"
>
> — [1:38](https://www.youtube.com/watch?v=2xJoimgoqBg&t=98s) &middot; *Frames agent deployment trust as the genuinely open problem.*

> "And that's a much more difficult problem to solve."
>
> — [1:38](https://www.youtube.com/watch?v=2xJoimgoqBg&t=98s) &middot; *Explicit ranking of agent safety above code-generation security in difficulty.*

> "the final thing that I think is a barrier to us, you know, really innovating and moving quickly is almost geopolitics at this point"
>
> — [2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s) &middot; *An unusual claim for a security talk — treats model access policy as an engineering constraint.*

> "how many people were kind of annoyed when access to Fable got pulled? Show of hands. Yeah, a whole lot of people, right?"
>
> — [2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s) &middot; *Concrete, dated example of the geopolitical access problem he's describing.*

> "How many people are a little annoyed they can't use the brand new Open AI GPT-5.6 model right now? Yes, a lot of people."
>
> — [2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s) &middot; *Second specific access-restriction datapoint anchoring the talk in mid-2026.*

> "fundamentally, the biggest problem that I feel we have to still solve in our space is being able to use AI fearlessly and have it be secure by default"
>
> — [2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s) &middot; *The thesis sentence of the talk.*

> "right after this keynote, downstairs on the second floor, in room 2005, we're going to be running the first security track at the World's Fair for the entire day"
>
> — [3:03](https://www.youtube.com/watch?v=2xJoimgoqBg&t=183s) &middot; *The announcement the talk exists to deliver, and a marker that security was new to this conference.*

> "We have presenters from Nvidia, Anthropic, Keycard, where Ali works, uh Sneak, of course."
>
> — [3:03](https://www.youtube.com/watch?v=2xJoimgoqBg&t=183s) &middot; *Names the organizations shaping the track's agenda.*

## Positions

- AI models generate security issues in code just as human developers do, so this is not a novel or especially alarming risk. ([1:38](https://www.youtube.com/watch?v=2xJoimgoqBg&t=98s), confidence: stated)
- Security must be a core part of the modern development lifecycle regardless of whether code is written by humans or AI. ([1:38](https://www.youtube.com/watch?v=2xJoimgoqBg&t=98s), confidence: stated)
- Safely deploying autonomous agents into production is a substantially harder problem than securing AI-generated code. ([1:38](https://www.youtube.com/watch?v=2xJoimgoqBg&t=98s), confidence: stated)
- Geopolitics — specifically restricted access to frontier models like Fable and GPT-5.6 — is now a real barrier to innovation and speed for AI engineers. ([2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s), confidence: stated)
- Model access restrictions are fundamentally a security problem, not merely a policy or commercial one. ([2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s), confidence: stated)
- The biggest remaining unsolved problem in AI engineering is being able to use AI fearlessly with security by default. ([2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s), confidence: stated)
- Generative AI's primary value to engineers is shipping higher-quality software to users faster, rather than any other capability. ([0:01](https://www.youtube.com/watch?v=2xJoimgoqBg&t=1s), confidence: implied)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [output guardrails](../concepts/output-guardrails.md)
- [secure code generation](../concepts/secure-code-generation.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

