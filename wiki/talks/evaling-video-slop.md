---
title: "Evaling Video Slop"
type: "talk"
slug: "evaling-video-slop"
track: "Evals"
org: "Character.ai"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "b_PmGocP4rc"
duration_sec: 1393
word_count: 3764
speakers: ["Maor Bril"]
---

# Evaling Video Slop

**Speakers:** [Maor Bril](../speakers/maor-bril.md)

**Org:** Character.ai

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 23m 13s

[Watch on YouTube](https://www.youtube.com/watch?v=b_PmGocP4rc)

## Summary

Maor Bril of Character.ai argues that video generation quality has raced ahead of our ability to evaluate it, leaving teams to "squint" at outputs while frame-level metrics like CLIP score and LPIPS miss what actually matters. He walks through Character.ai's evolution from a slow, expensive committee-of-experts benchmark (frame metrics plus human-calibrated LLM judges) to a distilled small VLM that scores a 15-second video in about 3 seconds, cheap enough to sit inside the generation loop where drift can be caught and regenerated early. The most transferable lessons are methodological: train on pairwise A/B comparisons rather than absolute 1-10 scores, and score the specific axes you care about (story, pacing, physics, audio sync) rather than expecting them to emerge. He is candid about a failed V1 that scored "the vibe" instead of the axes — rating 9.2 on camera work for a static shot and praising the physics of hovering ghosts — and about the dataset fix (pairing real footage against AI footage with matched encoding) that risked producing an AI detector instead of a quality detector. Worth watching if you build or evaluate generative video, or want a concrete case study in distilling an expensive judge ensemble into a fast in-loop critic.

## Key Points

- Frame-level metrics like CLIP score and LPIPS check prompt adherence and inter-frame drift but cannot tell you whether the video told the story you meant to tell.
- Video should be evaluated as a storytelling medium along explicit axes — narrative, character consistency across shots, physics plausibility, pacing, and audio-visual sync.
- Foundation-model LLM judges are slow and prompt-sensitive: different phrasings of the same question get very different answers from the same model.
- Character.ai's first system combined frame metrics with LLM judges calibrated by human annotation, but it was too slow and expensive to run near user-facing generation.
- Catching drift early — at the starting-frame stage or on an individual six-second clip — is far cheaper than fixing it after a multi-minute video is assembled.
- The team distilled the expert committee into a small VLM (Qwen, chosen partly from prior post-training experience) that scores a 15-second video in ~3 seconds; a larger model scored better but the accuracy gain didn't justify the latency.
- Training on pairwise comparisons (A vs B) rather than absolute 1-10 ratings sidesteps the fact that human numeric scales don't align, while comparative judgments largely do.
- V1 failed because the data taught the model to score surface gloss and coherence rather than the named axes; the fix was pairing real footage against AI footage with identical encoding and identical annotation methodology on both sides to avoid overfitting into an AI detector.
- Character.ai moved from a fixed pipeline to an agentic workflow, giving the agent quality-validation tools so it can verify and repair its own output as user stories diverge from any single use case.
- The build-vs-frontier-model decision is unit economics: for a handful of videos a frontier judge is fine, but at thousands to tens of thousands per day the cost of serving a small distilled model wins.

## Notable Quotes

> "So, the hard part was never how to make video. The hard part was how do we generate um good enough video and how do we judge if the video is good enough?"
>
> — [1:01](https://www.youtube.com/watch?v=b_PmGocP4rc&t=61s) &middot; *States the talk's central reframing: generation is solved, judgment is not.*

> "If you think about what is video, video is a storytelling medium. Video is just another form on how we tell a story"
>
> — [3:06](https://www.youtube.com/watch?v=b_PmGocP4rc&t=186s) &middot; *The premise underlying his whole critique of frame-level metrics.*

> "The problem with them is that A, they're slow. B, they're only as good as your prompt and multiple people will prompt multiple ways and the same model may respond in a very very different way."
>
> — [3:43](https://www.youtube.com/watch?v=b_PmGocP4rc&t=223s) &middot; *Names the concrete tradeoffs of LLM-as-a-judge for video.*

> "the solution is actually actually to take all these committee of experts and distill it into one small model that is also very very fast, but it is able to give us a response that is not whether or not this video is slap or not, but why is it slap?"
>
> — [7:27](https://www.youtube.com/watch?v=b_PmGocP4rc&t=447s) &middot; *The core architectural move, plus the demand for diagnostic rather than scalar output.*

> "also tested a bigger model and the results were better, but it was significantly slower."
>
> — [8:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=494s) &middot; *An explicit accuracy-versus-latency tradeoff, resolved in favor of speed.*

> "The other very interesting realization we came to is don't score compare."
>
> — [9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s) &middot; *The single most portable methodological claim in the talk.*

> "if I show you two videos and I'll ask you which one of them is telling a better story, the grand majority will probably agree that B is telling a better story than A"
>
> — [9:47](https://www.youtube.com/watch?v=b_PmGocP4rc&t=587s) &middot; *The justification for pairwise labels over absolute scales.*

> "we trained on pairs, right? Um uh A versus B as opposed to 1 through 10. Now, we manufactured badness."
>
> — [9:47](https://www.youtube.com/watch?v=b_PmGocP4rc&t=587s) &middot; *Concrete training-data design, including deliberately synthesizing negatives.*

> "the frame you see here is from from a video that the model scored 9.2 on the camera work, and the camera didn't move."
>
> — [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s) &middot; *A specific, checkable failure case from the shipped V1.*

> "it says that the physics look great, but it said it on on ghosts hovering and people flying"
>
> — [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s) &middot; *Second concrete V1 failure showing the model rewarded gloss over the named axis.*

> "The reason it was wrong is because how we generated that data, right? It It um it scored the vibe as opposed to the the the axes."
>
> — [11:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=674s) &middot; *Diagnoses the failure as a dataset problem, not a model-capacity problem.*

> "if you start creating pairs of good is is is human-generated video and bad is AI uh uh video, then then there's a very big chance of of the model overfitting and becoming an AI detector as opposed to a um uh uh video quality detector."
>
> — [11:58](https://www.youtube.com/watch?v=b_PmGocP4rc&t=718s) &middot; *Names a subtle and generalizable label-leakage risk in preference-pair construction.*

> "the pipelines work great if you have a very very unique use case. But one once you put put put it in front of users, they'll have a very very distinct story that they want to tell with their own characters, with with their own images, and their own voice."
>
> — [13:24](https://www.youtube.com/watch?v=b_PmGocP4rc&t=804s) &middot; *His argument for agentic workflows over fixed pipelines once real users arrive.*

> "Be score the real axis that you care about. So if you care about storytelling, if you care about pacing, if you care about physics, score those axes. Don't expect them to miraculously appear."
>
> — [14:03](https://www.youtube.com/watch?v=b_PmGocP4rc&t=843s) &middot; *Second of the talk's takeaways, stated as a direct prescription.*

> "And put eval inside the generation loop, right? Especially if your goal is is is is to have a higher quality of generation, get the the eval as close to to the generation loop loop as possible."
>
> — [14:03](https://www.youtube.com/watch?v=b_PmGocP4rc&t=843s) &middot; *The structural recommendation that motivates the whole distillation effort.*

> "Lip syncing is an unsolved problem yet."
>
> — [16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s) &middot; *A frank admission of a remaining gap in the evaluation stack.*

> "will periodically have sessions where everyone spends 10 to 15 minutes just annotating videos."
>
> — [18:10](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1090s) &middot; *Describes the practical human-calibration ritual behind the judge alignment.*

> "If you do it for one or two, that's probably fine. If if you do it for thousands or tens of thousands per day, it adds up. So it's it's it's a matter of your your your unit economics."
>
> — [21:38](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1298s) &middot; *Frames the build-versus-frontier-judge decision as a volume-driven cost question.*

## Positions

- Frame-level metrics such as CLIP score and LPIPS are insufficient for video because they cannot judge whether the intended story was told. ([2:25](https://www.youtube.com/watch?v=b_PmGocP4rc&t=145s), confidence: stated)
- Video should be evaluated as a storytelling medium, along axes like narrative, pacing, physics, and character consistency. ([3:06](https://www.youtube.com/watch?v=b_PmGocP4rc&t=186s), confidence: stated)
- Frontier LLM judges for video are too slow and too prompt-sensitive to serve as the primary evaluator. ([3:43](https://www.youtube.com/watch?v=b_PmGocP4rc&t=223s), confidence: stated)
- Catching quality defects earlier in the pipeline (starting frames, individual clips) is substantially cheaper than correcting them after assembly. ([5:16](https://www.youtube.com/watch?v=b_PmGocP4rc&t=316s), confidence: stated)
- A distilled small VLM scores a 15-second video in about 3 seconds, fast enough to run near online generation. ([8:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=494s), confidence: stated)
- The larger evaluator model was more accurate, but its added value did not justify its slowness. ([9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s), confidence: stated)
- Relative comparison (A vs B) produces better-aligned judges than absolute 1-10 scoring, because humans do not agree on absolute scales but do agree on comparisons. ([9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s), confidence: stated)
- Evaluation models trained on naively generated data will learn surface gloss and coherence — 'the vibe' — rather than the axes you intended to measure. ([11:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=674s), confidence: stated)
- Pairing human footage against AI footage risks producing an AI detector rather than a quality detector unless encoding and annotation methodology are matched on both sides. ([11:58](https://www.youtube.com/watch?v=b_PmGocP4rc&t=718s), confidence: stated)
- Agentic workflows with quality-validation tools generalize better than fixed pipelines once real users bring their own characters, images, and voices. ([13:24](https://www.youtube.com/watch?v=b_PmGocP4rc&t=804s), confidence: stated)
- Audio-visual sync can be evaluated without semantic sound recognition, by correlating prompt-derived key frames with amplitude spikes at matching timestamps. ([16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s), confidence: stated)
- Lip sync evaluation remains unsolved, particularly for stylized characters whose mouth animation has no real correlation to speech. ([16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s), confidence: stated)
- At low volume the expensive committee-of-experts approach is fine; training and serving a distilled model only pays off at thousands to tens of thousands of videos per day. ([21:38](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1298s), confidence: stated)
- Taste is subjective enough that human judges must be sampled across randomized axes and continuously fed back to recalibrate the AI judges, rather than treated as a one-time labeling pass. ([18:55](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1135s), confidence: implied)

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

