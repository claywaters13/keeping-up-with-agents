---
title: "Maor Bril"
type: "speaker"
slug: "maor-bril"
role: "Chaos Catalyst"
company: "Character.ai"
talk_count: 1
---

# Maor Bril

**Chaos Catalyst &middot; Character.ai**

Maor is a Principal Software Engineer at Character.ai, where he builds the agentic platform behind Stories, Streams, and the AI Social Feed (16M+ MAU). He open-sourced claude-agent-sdk-go and JudgeJudy, the multimodal eval harness that gates every AgentX release. Before Character.ai he led the Datastores org at Coinbase and shipped infrastructure at Netflix, Google, and VMware (via the Arkin acquisition). Twenty years of building systems that run in production. He writes about agentic systems and AI engineering on LinkedIn.

[LinkedIn](https://www.linkedin.com/in/maorbril)

## Talks

- [Evaling Video Slop](../talks/evaling-video-slop.md) (Evals)

## Scheduled Sessions

- **Evaling Video Slop** &middot; Day 3 — Session Day 2 &middot; 1:55pm-2:15pm &middot; Track 5

## Concepts

- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [benchmark contamination](../concepts/benchmark-contamination.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [vision-language models](../concepts/vision-language-models.md)

## Quotes

> "So, the hard part was never how to make video. The hard part was how do we generate um good enough video and how do we judge if the video is good enough?"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [1:01](https://www.youtube.com/watch?v=b_PmGocP4rc&t=61s)

> "If you think about what is video, video is a storytelling medium. Video is just another form on how we tell a story"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [3:06](https://www.youtube.com/watch?v=b_PmGocP4rc&t=186s)

> "The problem with them is that A, they're slow. B, they're only as good as your prompt and multiple people will prompt multiple ways and the same model may respond in a very very different way."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [3:43](https://www.youtube.com/watch?v=b_PmGocP4rc&t=223s)

> "the solution is actually actually to take all these committee of experts and distill it into one small model that is also very very fast, but it is able to give us a response that is not whether or not this video is slap or not, but why is it slap?"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [7:27](https://www.youtube.com/watch?v=b_PmGocP4rc&t=447s)

> "also tested a bigger model and the results were better, but it was significantly slower."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [8:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=494s)

> "The other very interesting realization we came to is don't score compare."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s)

> "if I show you two videos and I'll ask you which one of them is telling a better story, the grand majority will probably agree that B is telling a better story than A"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [9:47](https://www.youtube.com/watch?v=b_PmGocP4rc&t=587s)

> "we trained on pairs, right? Um uh A versus B as opposed to 1 through 10. Now, we manufactured badness."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [9:47](https://www.youtube.com/watch?v=b_PmGocP4rc&t=587s)

> "the frame you see here is from from a video that the model scored 9.2 on the camera work, and the camera didn't move."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s)

> "it says that the physics look great, but it said it on on ghosts hovering and people flying"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s)

> "The reason it was wrong is because how we generated that data, right? It It um it scored the vibe as opposed to the the the axes."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [11:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=674s)

> "if you start creating pairs of good is is is human-generated video and bad is AI uh uh video, then then there's a very big chance of of the model overfitting and becoming an AI detector as opposed to a um uh uh video quality detector."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [11:58](https://www.youtube.com/watch?v=b_PmGocP4rc&t=718s)

> "the pipelines work great if you have a very very unique use case. But one once you put put put it in front of users, they'll have a very very distinct story that they want to tell with their own characters, with with their own images, and their own voice."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [13:24](https://www.youtube.com/watch?v=b_PmGocP4rc&t=804s)

> "Be score the real axis that you care about. So if you care about storytelling, if you care about pacing, if you care about physics, score those axes. Don't expect them to miraculously appear."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [14:03](https://www.youtube.com/watch?v=b_PmGocP4rc&t=843s)

> "And put eval inside the generation loop, right? Especially if your goal is is is is to have a higher quality of generation, get the the eval as close to to the generation loop loop as possible."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [14:03](https://www.youtube.com/watch?v=b_PmGocP4rc&t=843s)

> "Lip syncing is an unsolved problem yet."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s)

> "will periodically have sessions where everyone spends 10 to 15 minutes just annotating videos."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [18:10](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1090s)

> "If you do it for one or two, that's probably fine. If if you do it for thousands or tens of thousands per day, it adds up. So it's it's it's a matter of your your your unit economics."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [21:38](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1298s)

