---
title: "Neil Zeghidour"
type: "speaker"
slug: "neil-zeghidour"
role: "Co-founder & CEO"
company: "Gradium"
talk_count: 1
---

# Neil Zeghidour

**Co-founder & CEO &middot; Gradium**

Neil Zeghidour is the co-founder and CEO of Gradium. Neil founded Gradium after a decade of building and leading frontier generative audio teams at Meta and Google DeepMind. Being frustrated by slow and brittle voice assistants , he built the engineering teams that developed the first neural audio codecs and introduced the first audio LLMs, such as AudioLM, at Google. He later created Kyutai to launch Moshi, the world's first real-time, full-duplex conversational AI , and Hibiki, the first simultaneous speech-to-speech translation system. Today, Gradium is focused on helping developers build natural, real-time voice agents by providing ultra-low latency streaming APIs that transition these breakthroughs from the research lab to production.

## Talks

- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md) (Claws & Personal Agents)

## Scheduled Sessions

- **Your Voice Agent is Just a Walkie-Talkie** &middot; Day 2 — Session Day 1 &middot; 12:05pm-12:25pm &middot; Track 6
- **Everybody Gets a Digital Clone! (Part 1 of 3)** &middot; Day 2 — Session Day 1 &middot; 1:30pm-1:50pm &middot; Track 4
- **Everybody Gets a Digital Clone! (Part 2 of 3)** &middot; Day 2 — Session Day 1 &middot; 1:55pm-2:15pm &middot; Track 4
- **Everybody Gets a Digital Clone! (Part 3 of 3)** &middot; Day 2 — Session Day 1 &middot; 2:25pm-2:45pm &middot; Track 4
- **Voice is the universal interface** &middot; Day 4 — Session Day 3 &middot; 11:40am-12:00pm &middot; Expo Stage 3 SW

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [context compaction](../concepts/context-compaction.md)
- [durable execution](../concepts/durable-execution.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [small language models](../concepts/small-language-models.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)
- [voice agents](../concepts/voice-agents.md)

## Quotes

> "Because our budget was never IQ, it's millisecond."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s)

> "When a voice agent pause for even a second, your brain says it's dead."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s)

> "The AI model need to start talking in about 950 milliseconds."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s)

> "A frontier model that think for a full second has already lost the room, no matter how good the answer is."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s)

> "So, we made the model small and took the hardest part jobs away from it."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s)

> "What's left for the model is one thing it's really good at, talking."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s)

> "But that is actually precisely the problem. Because the reasoning can take couple of seconds and those seconds are really valuable when you are building voice applications."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [1:38](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=98s)

> "So all of the thinking is extracted into a state machine."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [1:38](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=98s)

> "So everything when it comes to what happens next, when it comes to what needs to be displayed, when it comes to how to actually answer a question, it's all done outside of the model."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [2:27](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=147s)

> "Same question, but now you see that the answer comes in about 900 milliseconds."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [3:11](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=191s)

> "by removing all of the thinking, all of the logic, all of the reasoning from the model and actually putting it within the code, we actually saves a lot of time and allows us to use smaller models which are cost effective and actually better at real-time voice applications"
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [3:11](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=191s)

> "A small model like the Haiku 4.5, if it doesn't have any scaffolding, tend to drift on long structure and really needs strict rules in order to be able to stay organized."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

> "So the scaffolding piece is the price. But the good thing is you pay it once and in code, right? Not on every single turn."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

> "In those cases, the model is the smallest part of the system."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:53](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=293s)

