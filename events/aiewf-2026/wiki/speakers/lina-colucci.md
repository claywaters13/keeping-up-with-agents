---
title: "Lina Colucci"
type: "speaker"
slug: "lina-colucci"
role: "CEO"
company: "LemonSlice"
talk_count: 2
---

# Lina Colucci

**CEO &middot; LemonSlice**

Co-Founder and CEO of LemonSlice, an AI lab working to break the avatar Turing test. LemonSlice raised $10.5M seed from Matrix and YC and have the most advanced interactive avatar model in the world. Originally from Brazil, Lina is an ML researcher and artist - ballerina, musician, photographer, YouTuber. She previously founded and ran one of the leading ML consulting firms in the US, and has a PhD from MIT and Harvard.

[LinkedIn](https://www.linkedin.com/in/lina-colucci/)

## Talks

- [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md) (Generative Media)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md) (Generative Media)

## Scheduled Sessions

- **Voice agents with Realtime Video** &middot; Day 4 — Session Day 3 &middot; 1:55pm-2:15pm &middot; Track 1

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [context rot](../concepts/context-rot.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [latency budgets](../concepts/latency-budgets.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [vision-language models](../concepts/vision-language-models.md)
- [voice agents](../concepts/voice-agents.md)
- [world models](../concepts/world-models.md)

## Quotes

> "These are all audio engineering problems. They are not LLM problems because you can have the perfect model, perfect track but the experience still might feel broken if the turn taking is off."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [0:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=3s)

> "Both the scenarios, the LLM was identical. It was the same model. It was the same prompt, but the difference in the user experience is so different."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [1:34](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=94s)

> "because 200 milliseconds is how fast humans switch turns with each other in a conversation. And the implications are pretty brutal because at 800 milliseconds, things start to feel off. While at 1.5 seconds, your user just hang up on you"
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [2:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=138s)

> "But even there, best measured response time was 755 milliseconds. So, that's like almost 4x slower than how humans naturally take turns when talking."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [3:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=187s)

> "So, coming to Silero VAD, it's a small 300,000 parameter model. It takes in like a short term Fourier transform."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [5:13](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=313s)

> "And the one parameter that minimum silence millisecond is basically the entire user experience of level one. If you keep it very low, the agent is going to be snapping like it will cut people off while they're still, you know, thinking."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [6:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=361s)

> "If someone is pausing for 300 milliseconds or 400 milliseconds, VAD is seeing the same exact thing. It has no idea like whether the person is catching up their breath or whether they've completely finished their thought."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [7:24](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=444s)

> "And their P50 latency for Cartesiant is about 300, and it's about 250 for Deepgram Nova 3."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [9:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=541s)

> "However, the trade-off is with the transparency. Because when it is working, it works great. But when it misfires, or when it cuts someone off at the wrong moment, then you like have no way to figure out"
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [9:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=541s)

> "And it has about 58.9% recall and 68.4 percent precision. So, what this means is that about six out of 10 time when someone finishes a sentence, Smart Turn will be able to catch it quickly."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [9:43](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=583s)

> "There, they had reported a higher recall at 87.7%, but they haven't released the code, so you really cannot deploy it."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s)

> "Smart Turn is BSD-2 licensed, and it's a 8-MB small model. You can pip install it today as well."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [11:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=678s)

> "think about a normal conversation when someone says, "Yeah." Like, if they send an acknowledgement while you're speaking, you don't stop, right?"
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [12:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=721s)

> "So, today most of these systems stop every time, but this is a piece that's improving."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [12:43](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=763s)

> "LLM time to first byte, and this is generally the dominant bottleneck because in a typical API setup, you're looking at 500 to 650 ms depending on what model you're calling and from which cloud provider, which region."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [15:13](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=913s)

> "Now, the Quindos team had demonstrated about 500 ms total voice-to-voice by co-locating all models in the same GPU cluster."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [16:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=961s)

> "And the key insight to note here is that the STT, LLM, together eat about 2/3 of the is latency budget."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [16:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=961s)

> "But what matters more in voice than maybe anywhere else is that the P95 tail. Because GPT-4.1 was great at P50, but it spikes to 1.7 at P95."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [17:58](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1078s)

> "And it was even worse for Claude 3 that it hit over 4 seconds and because in a conversation you cannot average this out because one slow response and your entire flow is gone."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s)

> "which is the multi-turn trip because after 15 or 20 turn, sometime model starts ignoring parts of the system prompt. They might get to verbose, they go off spirit."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s)

> "Because when agents cut people off incorrectly, then users are more likely to request for a human in the loop uh support."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [20:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1203s)

> "And on infrastructure running all of this in production is also hard because five systems that all scale differently and can also fail differently."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [21:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1263s)

> "So, definitely this is just a a quick demo, but in practice, you would probably combine both the turn detection model and the silence detection."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [29:12](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1752s)

> "And Lemon Slice is on a mission to break the Avatar Turing test. What we mean by this is making an Avatar that is indistinguishable from a human on a video call."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [0:01](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1s)

> "So, our bet here is in the long term we think most interactions between AI and humans will have a visual visual layer."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [4:07](https://www.youtube.com/watch?v=z1dqv74SpUs&t=247s)

> "Essentially what we do is we take these world models and we focus them on humans."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [4:55](https://www.youtube.com/watch?v=z1dqv74SpUs&t=295s)

> "even though it's harder to get the initial model working, it's harder to train the model, it's harder to deploy the model. Once you have a model, you get all of these nice emergent properties"
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [4:55](https://www.youtube.com/watch?v=z1dqv74SpUs&t=295s)

> "most audio encoders today are trained on basically audiobooks, which is very monotone, very simple, don't have a lot of emotions. So, if you want to have a very expressive model, you can't use those audio encoders"
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [9:13](https://www.youtube.com/watch?v=z1dqv74SpUs&t=553s)

> "usually video models are bidirectional, so they can look into the past, but they actually also can look into the future"
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [10:01](https://www.youtube.com/watch?v=z1dqv74SpUs&t=601s)

> "we basically train a model with an attention mask so that the model can only look into the past. So, when you do inference, it never can see the future because the future doesn't exist because like you haven't given it those inputs yet."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [10:38](https://www.youtube.com/watch?v=z1dqv74SpUs&t=638s)

> "let's say 30 steps. You spend 30 steps like removing the noise to generate the beautiful beautiful videos. And what we need to do is go from like 30 steps, bring it out to one step."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [11:22](https://www.youtube.com/watch?v=z1dqv74SpUs&t=682s)

> "So now you're looking in the past, you're looking at the error, you're adding more error to it, and then just the error compounds over time."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [11:58](https://www.youtube.com/watch?v=z1dqv74SpUs&t=718s)

> "Like the teddy avatar is generating continuously non-stop frame by frame for 8 hours straight with like no reset throughout the entire process. We have another one that's going to be generating for 16 hours straight."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s)

> "we've been able to make the models small enough and efficient enough so that the costs are about the same as a voice model."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [13:20](https://www.youtube.com/watch?v=z1dqv74SpUs&t=800s)

> "I feel like the model hardness is something that is often overlooked but is actually super important and super hard."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [14:11](https://www.youtube.com/watch?v=z1dqv74SpUs&t=851s)

> "you have to orchestrate this perfectly in a way that like the video always remains real time. There is never any stutter that happens inside of the video."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [14:56](https://www.youtube.com/watch?v=z1dqv74SpUs&t=896s)

> "It has the capabilities to do this. It's just not controllable enough to like make it real time with the conversation and not deterministic enough to to make it useful with the conversation."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [18:05](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1085s)

> "So I strongly believe that in the end uh there'll be a single model um that is the EQ layer for AI."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [18:46](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1126s)

> "What we're not saying is that this EQ model will be very intelligent. Uh it'll be very it'll have very high EQ and it'll be very good at like interacting with people"
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [19:38](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1178s)

> "but I feel strongly that within two or three years you'll be seeing these kinds of end-to-end EQ models coming on the market."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [20:32](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1232s)

> "we're uh in the process of figuring out our own version of the Turing test for these avatars, which will just include real people."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [23:09](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1389s)

> "Again, like the cost of this is at the same level as an audio model in terms of what we charge for it."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [25:06](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1506s)

> "I think there'll also be very cool architectural updates to to move to more of like a token approach instead of a diffusion approach that will make video like this type of video generation way cheaper."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [25:48](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1548s)

> "Now the way this is used, just for for kind of everybody's information, is we're mostly the API layer. So, we provide an API. People bring their own LLM. People bring their own usually like voices."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [7:40](https://www.youtube.com/watch?v=z1dqv74SpUs&t=460s)

> "the funny thing is he was scheduled to be there for, you know, a quick minute, one interaction, and he actually stayed for 10 minutes."
>
> — [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [3:28](https://www.youtube.com/watch?v=z1dqv74SpUs&t=208s)

