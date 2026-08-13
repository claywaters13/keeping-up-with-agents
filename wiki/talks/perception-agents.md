---
title: "Perception Agents"
type: "talk"
slug: "perception-agents"
track: "Autoresearch"
org: "Amazon AGI Lab"
day: "Day 3 — Session Day 2"
room: "Main Stage"
video_id: "2JX6JYyQG4Y"
duration_sec: 1304
word_count: 2872
speakers: ["Antje Barth"]
---

# Perception Agents

**Speakers:** [Antje Barth](../speakers/antje-barth.md)

**Org:** Amazon AGI Lab

**Track:** Autoresearch &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 21m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=2JX6JYyQG4Y)

## Summary

Antje Barth of Amazon AGI Lab argues that computer-use agents have solved capability — clicking, typing, tool calls, workflow chaining — but not reliability, and that reliability arrived first in coding only because code is verifiable. Most knowledge work lives 'in the seams' between applications where no unit test can confirm success, which is why end-to-end agent workflows still break. Her proposed fix is the 'perception agent': an agent that reads the rendered screen the way a human collaborator would, sharing context rather than needing a bigger brain, and reacting in real time instead of in prompt-response turns. Amazon has open-sourced the first two pieces of a perception agent harness — a Chrome-extension annotation tool that lets you point at screen elements instead of writing long descriptions, and a verification tool that checks an agent's work against a design.md spec via visual checks and simulated user flows. The talk includes a live-ish demo where a wearable's meeting transcript is piped into the agent as design instructions, then auto-verified. Watch it for the framing of verification as the bottleneck for non-code work, plus a concrete look at pixel-level (not API-level) agent grounding.

## Key Points

- Agents can reliably perform individual steps but fail end-to-end because the real work lives in the seams between five different systems that nobody owns.
- The industry has largely solved adding capabilities to models; the unsolved problem is reliability, and without reliability there is no trust.
- A 60-80% success rate sounds acceptable but is unusable in practice — an agent that deletes a database one in four times will never be used again; you need reliability 'in the nines'.
- Coding became reliable first specifically because code is verifiable: you can run it, test it, and check it, so reliability showed up where verification was possible.
- Verification breaks down for knowledge work — whether a report landed or a design is on brand has no unit test — and this is a wide-open field.
- What agents lack is not a bigger brain but shared context: looking at the same screen as the human drastically reduces explanation overhead.
- Perception agents complete the perceive-plan-act loop borrowed from robotics by reading the rendered screen (layout, state, what changed) rather than scraping the code behind the page.
- Working off rendered pixels rather than APIs matters because most software people use daily exposes no API at all.
- Pointing at an element is a more precise, less lossy input signal than writing a long text description of the change you want.
- Amazon AGI Lab has open-sourced two harness pieces — annotation (tell the agent what you want) and verification (agent checks its own work against design specs via visual checks and automated user-flow walkthroughs).

## Notable Quotes

> "Just a year ago, the hard problem was getting an agent to find a button and click it on a screen, especially screens it had never seen before. Now, agents can drive browsers and they're starting to also drive desktop apps."
>
> — [0:01](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=1s) &middot; *Sets the baseline of what's now considered solved.*

> "The agent can use every single tool you give it, but it still can't do the full work."
>
> — [1:26](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=86s) &middot; *Names the capability/completion gap precisely.*

> "the real work lives within the seams of all of those different applications, of all of those different steps you have to take. And this is mostly where it all falls apart."
>
> — [1:26](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=86s) &middot; *The 'seams' framing is the reusable diagnosis.*

> "We taught computers to use computers."
>
> — [2:23](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=143s) &middot; *Compact characterization of the current computer-use paradigm.*

> "this is all capabilities and we mostly figured out how to add capabilities to models."
>
> — [2:23](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=143s) &middot; *A strong, contestable claim about where the field stands.*

> "Now the next hard part is really reliability and without reliability we cannot really build up trust in those systems."
>
> — [3:30](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=210s) &middot; *States the reliability-before-trust dependency the rest of the talk builds on.*

> "if your agent one in four times deletes a database, you will never touch that agent again, right? So when you need this reliability, you really need to be it in the nines."
>
> — [3:30](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=210s) &middot; *Concrete reliability bar with a memorable failure case.*

> "why was coding first solved? It's because code is verifiable. You can run it, you can test it, you can check it and you can be for sure that it worked. So reliability showed up in the first place you can actually verify the answer."
>
> — [5:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=355s) &middot; *The causal argument at the center of the talk.*

> "Did the report I created land? Is the design on brand? Did it get it what I actually meant? So there is no unit test that can answer those questions."
>
> — [5:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=355s) &middot; *Makes the verification gap concrete for non-code work.*

> "How do you make an agent reliable when there's no way to verify the answer that easily? And that's a field that is still wide open."
>
> — [6:56](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=416s) &middot; *Explicitly frames the open research problem.*

> "So this is what the agent these days is missing. You don't necessarily need a bigger brain. What you need is this shared context."
>
> — [7:51](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=471s) &middot; *Takes a side against scale-first framing.*

> "if they fire off actions, what they usually do, they move on. They don't watch what happens or recover if one step didn't succeed or something goes sideways."
>
> — [8:37](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=517s) &middot; *Names the specific behavioral defect perception agents target.*

> "a robot perceives what's around it and it plans what to do and then acts. So this loop here from perceiving to planning to acting, this is actually what we also would need on a screen."
>
> — [9:24](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=564s) &middot; *Sources the architecture directly from robotics.*

> "The agent has to take in the screen the way you do, not scrape the code behind the page, but what's actually rendered, the layout, the state, what just changed"
>
> — [9:24](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=564s) &middot; *The key technical commitment: pixels over DOM.*

> "what we actually would need, think about it, is an agent that can react while you're still working."
>
> — [11:02](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=662s) &middot; *Argues against the turn-taking chatbot rhythm.*

> "an agent that perceives what you perceive and understands what you mean. We call them perception agents."
>
> — [11:02](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=662s) &middot; *The definition of the talk's titular concept.*

> "A perception agent can read the rendered screen so it can confirm its own output instead of just firing off those actions and then hoping."
>
> — [12:04](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=724s) &middot; *Ties perception directly back to self-verification.*

> "it doesn't need an API or backend process. And that's important because it works off the rendered interface. It sees the same pixels and the structure you see. And most of today's software people use every day don't expose APIs at all."
>
> — [12:04](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=724s) &middot; *The strongest practical argument for pixel-level grounding.*

> "This is a much more precise signal and less lossy than text. and the agent can act exactly on what you marked."
>
> — [12:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=775s) &middot; *States the annotation-over-prose tradeoff explicitly.*

> "we just recently launched the first two pieces of our perception agent harness open source. There's two pieces. There is annotation which you can use to tell it what you want. And then the second piece, the verification part gives the agent the capability to check its own work."
>
> — [12:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=775s) &middot; *The concrete artifact being shipped.*

> "there is no back and forth anymore because you captured exactly what you saw on screen and the agent can see the same thing."
>
> — [14:38](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=878s) &middot; *Claims annotation eliminates prompt iteration.*

> "it does two kinds of checks. Then it does a visual check, which is really cool. So everything is on brand, for example. it's the right layout. The other part is also checking user flows."
>
> — [15:26](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=926s) &middot; *Specifies what the verification tool actually does.*

> "perception can also be listening in the room to what you're discussing."
>
> — [17:03](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=1023s) &middot; *Extends perception beyond screens to ambient audio.*

> "we're building out the rest in the open because these patterns can only get better if more people are using them, building on top of them, breaking things."
>
> — [19:14](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=1154s) &middot; *States the rationale for open-sourcing the harness.*

## Positions

- Adding capabilities to models is largely a solved problem; reliability is the next hard problem. ([2:23](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=143s), confidence: stated)
- Agent reliability must reach 'the nines' — 60-80% end-to-end success is not usable for real work. ([3:30](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=210s), confidence: stated)
- Coding was the first domain where agents became reliable because code is verifiable by running and testing it. ([5:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=355s), confidence: stated)
- Most knowledge work has no verification mechanism analogous to a unit test, and making agents reliable without verification is an unsolved, wide-open problem. ([6:56](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=416s), confidence: stated)
- Agents don't need larger models to handle messy work; they need shared context with the human. ([7:51](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=471s), confidence: stated)
- Agents should read the rendered screen rather than scrape the underlying page code. ([9:24](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=564s), confidence: stated)
- Most software people use every day exposes no API, so API-based agent integration cannot cover real workflows. ([12:04](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=724s), confidence: stated)
- Pointing at on-screen elements is a more precise and less lossy input signal than natural-language descriptions. ([12:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=775s), confidence: stated)
- The turn-taking prompt-and-wait chatbot interaction pattern is a limitation to be moved past, not the endpoint for agent UX. ([11:02](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=662s), confidence: implied)
- An agent that can verify its own work against explicit design rules removes the need for humans to manually click through QA checks. ([16:16](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=976s), confidence: stated)

## Concepts

- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [spec-driven development](../concepts/spec-driven-development.md)
- [verifier design](../concepts/verifier-design.md)
- [voice agents](../concepts/voice-agents.md)

