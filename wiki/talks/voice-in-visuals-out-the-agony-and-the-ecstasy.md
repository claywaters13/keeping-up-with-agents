---
title: "Voice In, Visuals Out: The Agony and the Ecstasy"
type: "talk"
slug: "voice-in-visuals-out-the-agony-and-the-ecstasy"
org: "Forestwalk Labs"
video_id: "65X0pQ6Lmbg"
duration_sec: 785
word_count: 1935
speakers: ["Allen Pike"]
---

# Voice In, Visuals Out: The Agony and the Ecstasy

**Speakers:** [Allen Pike](../speakers/allen-pike.md)

**Org:** Forestwalk Labs

**Duration:** 13m 05s

[Watch on YouTube](https://www.youtube.com/watch?v=65X0pQ6Lmbg)

## Summary

Allen Pike of Forestwalk Labs argues that Karpathy's framing — voice as the preferred human input, visuals as the preferred output — is now technically feasible, and that the visuals-out half is the practical unlock. The core obstacle is latency: fully conversational voice-in/voice-out demands ~200ms round trips, which is nearly impossible across speech-to-text, inference, and network hops, whereas visual responses get a far more forgiving ~1 second envelope. Pike describes Forestwalk's agent that sits in live calls and takes action on spoken intent (e.g. filing a Linear issue mid-conversation) without interrupting the humans. He closes with three concrete engineering requirements: a genuinely fast model on a latency-prioritizing inference platform, eager inference every 1–2 seconds rather than waiting for silence, and aggressive prefix caching so ~90% of the context is stable across requests. Worth watching for anyone building real-time agentic UX and wanting specific latency budgets and observed provider numbers.

## Key Points

- Voice-in/visuals-out is now feasible because models can generate rich HTML, interactive controls, and illustrations via tool calling, raising the ceiling on what a response can be.
- Speech carries more words per minute than typing and also more meaning per word through tone, which is why humans escalate important communication to calls.
- Full voice-in/voice-out conversation requires ~200ms latency to support interruption and interjection, which is extremely hard across speech-to-text plus inference plus network.
- Switching the output modality to visuals buys a much more forgiving response envelope — roughly one second — without waiting for novel real-time architectures.
- Forestwalk built an in-call agent that acts on incidental spoken intent and responded within a second to a request to file a Linear issue.
- Model choice must account for the inference platform, not just model size: GPT-5 mini showed 5,000ms typical and 7,000ms P95 latencies, sometimes 10,000ms, while Haiku-class models were far better on P95.
- Heavy work should be handed off asynchronously to a larger model while the fast real-time model interleaves responses.
- Waiting for a second of silence before inferring blows the latency budget; sending inference every 1–2 seconds as the user speaks feels more seamless.
- Stable prefix caching — keeping the first ~90% of the context identical request to request and minimizing output tokens — is what makes fast turns affordable.

## Notable Quotes

> "he made an argument last month that voice is the human preferred input for AIs. But that we prefer visuals as the output."
>
> — [0:01](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=1s) &middot; *states the thesis the entire talk builds on*

> "The models that we have so far, the experiences that people most people have seen are both slow and dumb, which is like not a great combination."
>
> — [2:12](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=132s) &middot; *blunt diagnosis of why voice interfaces have a bad reputation*

> "When we're speaking, we have more words per minute than when we're typing. But we also convey more with each word."
>
> — [3:12](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=192s) &middot; *the bandwidth argument for voice input in one line*

> "There's a huge difference in between if you say to me okay versus if you say okay."
>
> — [3:12](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=192s) &middot; *concrete illustration that prosody carries information text loses*

> "the voice agent within a second responded that it had done so. And that feels perfectly natural when you get it really dialed in."
>
> — [4:16](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=256s) &middot; *the product demo moment that grounds the abstract latency claims*

> "It doesn't need to be voice. It is just taking action on your intent."
>
> — [5:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=302s) &middot; *reframes the design goal away from modality toward intent capture*

> "there's a huge barrier, a huge challenge to making this actually work and feel good. And that is the tyranny of latency."
>
> — [5:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=302s) &middot; *names the central obstacle the talk organizes around*

> "We we've known since the '60s that to have a computer react to us fast enough that it feels instant, it needs to react in about 100 milliseconds, a tenth of a second."
>
> — [5:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=302s) &middot; *grounds the latency budget in long-standing HCI research*

> "They ask Siri to do something, takes more than a second, we're off to something else mentally, right?"
>
> — [5:54](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=354s) &middot; *defines the upper bound of the attention envelope concretely*

> "We need to have a 200 millisecond latency or less if we want to have a fully conversive people are verbalizing something and they are interrupting or interjecting or agreeing"
>
> — [6:40](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=400s) &middot; *the hard number that makes voice-out impractical*

> "we don't need to wait for novel architectures. We can just switch to having voice in visuals out and then we benefit from the more forgiving visual response envelope that people have."
>
> — [7:24](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=444s) &middot; *the central practical recommendation of the talk*

> "it also has to be on an inference platform that prioritizes latency."
>
> — [9:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=542s) &middot; *distinguishes model size from serving characteristics*

> "in practice we were seeing latencies of 5,000 milliseconds, 7,000 P95, sometimes 10,000 millisecond latency for this small model."
>
> — [9:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=542s) &middot; *specific measured numbers naming a specific model*

> "Haiku is much better um in terms of of that that P95 latency."
>
> — [9:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=542s) &middot; *a direct comparative provider recommendation*

> "if there is a larger chunk of work that needs to get done, then that model then hands off or sends off an asynchronous message to a larger model that can think"
>
> — [9:51](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=591s) &middot; *describes the fast/slow model routing pattern*

> "you're you're blown your budget by a pretty wide margin just for waiting for silence."
>
> — [10:34](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=634s) &middot; *identifies turn detection as a hidden latency cost*

> "being willing to send inference every 1 or 2 seconds as they speak"
>
> — [10:34](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=634s) &middot; *the actionable alternative to silence-based turn taking*

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s) &middot; *quantifies the payoff from prefix caching*

> "we want to the first 90% of the context window if we can to be the same from request to request, and then just use that final 10%"
>
> — [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s) &middot; *a concrete architectural ratio to design context around*

## Positions

- Voice is the preferred human input for AI and visuals are the preferred output, per Karpathy's argument, which the speaker endorses. ([0:01](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=1s), confidence: stated)
- Fully conversational voice-in/voice-out requires 200ms or less end-to-end latency. ([6:40](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=400s), confidence: stated)
- Visual responses have a more forgiving latency envelope of about one second, so voice-in/visuals-out is achievable today without novel architectures. ([7:24](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=444s), confidence: stated)
- GPT-5 mini's real-world latency (5,000ms typical, 7,000ms P95, sometimes 10,000ms) makes it unusable for real-time interaction despite being a small, cheap model. ([9:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=542s), confidence: stated)
- A Haiku-class model or a smaller open-source model is the right choice for the real-time responding layer. ([9:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=542s), confidence: stated)
- Waiting for a second of silence before triggering inference is the wrong design; inference should fire every 1-2 seconds while the user is still speaking. ([10:34](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=634s), confidence: stated)
- Prefix caching can yield up to 90% cheaper and faster inference when the context prefix is stable. ([11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s), confidence: stated)
- Most LLM applications, whether long-running or frequently running agents, are converging on a stable-prefix caching architecture. ([11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s), confidence: stated)
- Model size alone does not determine response speed; the serving platform's latency prioritization matters as much or more. ([9:02](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=542s), confidence: implied)

## Concepts

- [context window management](../concepts/context-window-management.md)
- [generative ui](../concepts/generative-ui.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [voice agents](../concepts/voice-agents.md)

