---
title: "Training Krea 2: What matters in generative model training"
type: "talk"
slug: "training-krea-2-what-matters-in-generative-model-training"
track: "Generative Media"
org: "Krea.ai"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "-tviRdpmHvs"
duration_sec: 1306
word_count: 4054
speakers: ["Sangwu Lee"]
---

# Training Krea 2: What matters in generative model training

*Program title: Training Krea 2 - What matters in generative model training.*

**Speakers:** [Sangwu Lee](../speakers/sangwu-lee.md)

**Org:** Krea.ai

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 21m 46s

[Watch on YouTube](https://www.youtube.com/watch?v=-tviRdpmHvs)

## Summary

Sangwu Lee of Krea walks through how the team trained Krea 2, their image foundation model, whose medium variant they open-sourced. His central argument is that once you lock in a diffusion-transformer architecture, essentially all remaining quality comes from data curation — and that the big labs' models (ChatGPT/GPT-image, Nano Banana Pro) buy their reliability by mode-collapsing toward boring, average outputs, so Krea deliberately optimized for fast, stylistically diverse generation that creatives can iterate against. Most of the talk is a concrete tour of the curation stack: OCR-plus-VLM captioning, hash then embedding deduplication over 2–10 billion images, distilling large-VLM filtering judgments into cheap SigLip classifiers, sparse autoencoders repurposed as an unsupervised tagging system, and Wikipedia PageRank to guarantee world-knowledge coverage — roughly 30–40 in-house classifiers and heuristics in total. He also lays out an LLM-shaped post-training pipeline (progressive 256→1K pre-training, mid-training, SFT, preference optimization, GRPO-style RL against reward servers, plus a trained prompt expander). Worth watching if you want a practitioner's view of what actually moves the needle in generative image training, especially the case against training on AI-generated data.

## Key Points

- Production models from the big labs achieve consistency by mode-collapsing — the reliable way to render a person is to render the most average person and center-frame them — so Krea traded some reliability for speed and stylistic diversity aimed at open-ended creative exploration.
- Architecture is largely a settled choice (a diffusion transformer operating in a compressed latent space); the overwhelming majority of the work and of the resulting quality comes from data curation.
- Krea deliberately avoided training on AI-generated images, because synthetic data is 'sticky' — it gets you a good model fast but locks in a recognizable ChatGPT/Nano Banana aesthetic.
- Conventional aesthetic and image-quality scores actively cut stylistic diversity (e.g. low-res CRT looks get filtered out), so Krea designed filters that preserve coverage rather than oversampling conventionally 'good' images.
- Images whose important attributes captioners consistently miss — like a painting that is framed on a white wall — are treated as bad data, because the omission becomes a systematic generation bias.
- Filtering at 2–10 billion images requires a two-tier approach: cheap pHash/MD5 dedup first, then embedding-based semantic dedup (SSCD, SigLip), with large-VLM filtering decisions distilled down into SigLip-sized classifiers so they can run over the full corpus.
- Sparse autoencoders trained on a vision model give an unsupervised tagging system whose sparse features (watermarks, signatures, blur, border artifacts) can be used directly as filtering or oversampling handles.
- The post-training pipeline mirrors LLM practice: progressive 256→1K resolution pre-training, mid-training/SFT to mold the distribution toward illustration, graphic design, photography and cinematics, preference optimization on pairwise data, and GRPO-inspired RL against reward servers for text rendering and anatomy.
- A separately trained small LLM prompt expander is now near-mandatory for production diffusion, because long detailed prompts sit closer to the training distribution; Krea is next pursuing multi-expert distillation, merging capability-specialized experts into one student.

## Notable Quotes

> "in order to get like good consistency, they have like kind of like significantly mode collapse their models"
>
> — [2:11](https://www.youtube.com/watch?v=-tviRdpmHvs&t=131s) &middot; *States the core diagnosis of frontier image models that motivates Krea's whole positioning.*

> "if you're trying to render a person, the easiest and most reliable way to like render a person is render the most boring average person that exists and then like put it in a center frame."
>
> — [2:11](https://www.youtube.com/watch?v=-tviRdpmHvs&t=131s) &middot; *Vivid, concrete illustration of how reliability optimization produces blandness.*

> "if you type like burning skull, Chat GPT-2 like is very consistent. All the outputs are like fine, but you know, there's barely any diversity."
>
> — [2:11](https://www.youtube.com/watch?v=-tviRdpmHvs&t=131s) &middot; *A named, checkable comparison against a specific competitor model.*

> "really like data is like quite everything that goes into the model. Like typically, you lock in your architecture and then you just a lot of work just goes into like just feeding the model like what it wants."
>
> — [5:13](https://www.youtube.com/watch?v=-tviRdpmHvs&t=313s) &middot; *The talk's central thesis about where model quality actually comes from.*

> "some people like think I know like low-resolution CRT videos are like a bad image, but some people like that kind of like aesthetics, so making sure that we have like good coverage"
>
> — [5:48](https://www.youtube.com/watch?v=-tviRdpmHvs&t=348s) &middot; *Names the tradeoff between quality filtering and stylistic coverage.*

> "we tried very hard to like remove any AI images like at all because it does like provide you a shortcut to to get you like a good model, but synthetic data is like so sticky to the model that once you like start training on AI image data, sure your model's good, but you kind of lose the point"
>
> — [7:27](https://www.youtube.com/watch?v=-tviRdpmHvs&t=447s) &middot; *The strongest and most contestable position in the talk — a flat rejection of synthetic training data.*

> "as a researcher it always slightly hurts my ego if all I'm doing is distillation"
>
> — [8:02](https://www.youtube.com/watch?v=-tviRdpmHvs&t=482s) &middot; *Candidly admits the anti-distillation stance is partly a values judgment, not only a technical one.*

> "when you try to generate a painting of whatever, it'll be always hanged on a wall, on a white wall, which is pulling that what the user wants."
>
> — [9:17](https://www.youtube.com/watch?v=-tviRdpmHvs&t=557s) &middot; *Shows exactly how a captioner's blind spot becomes a systematic generation bias.*

> "we need to use like like, I don't know, anywhere from like 2 to like 10 billion images. That's a lot of images to run like filters on."
>
> — [9:51](https://www.youtube.com/watch?v=-tviRdpmHvs&t=591s) &middot; *Reports the dataset scale that forces the tiered filtering architecture.*

> "we can like distill this data, this kind of like decision and like to like a very small like SigLip classifier. And then, you can base you have like a very like cheap classifier that is somewhat like reliable."
>
> — [10:34](https://www.youtube.com/watch?v=-tviRdpmHvs&t=634s) &middot; *The key cost-control technique for filtering billion-scale corpora.*

> "one thing that you can actually get out of SAE is a unsupervised tagging system"
>
> — [11:46](https://www.youtube.com/watch?v=-tviRdpmHvs&t=706s) &middot; *An unusual, practical repurposing of interpretability tooling for data curation.*

> "you can actually take the Wikipedia, the entire Wikipedia, and for each article or concept, you can compute the page rank of each of the concepts"
>
> — [13:17](https://www.youtube.com/watch?v=-tviRdpmHvs&t=797s) &middot; *Concrete, reproducible method for ensuring world-knowledge coverage in the dataset.*

> "I think we ended up having around like 30 to 40 like custom in-house classifier, like different heuristics and like filters that we've used."
>
> — [14:09](https://www.youtube.com/watch?v=-tviRdpmHvs&t=849s) &middot; *Quantifies the actual engineering surface area of the curation pipeline.*

> "most people like train start training at low resolution because that's where the model actually learns like text-to-image capabilities"
>
> — [15:29](https://www.youtube.com/watch?v=-tviRdpmHvs&t=929s) &middot; *Explains the rationale behind progressive resolution scheduling.*

> "you actually need to train a small LLM that takes in like user prompt and then outputs like a very long detail prompt because typically longer detail prompt they're more in distribution with your models like training data that tends to like make better images"
>
> — [17:33](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1053s) &middot; *Argues prompt expansion is now a required production component, with a distributional justification.*

> "we would like train experts that are like specialized in like photography text rendering and different capabilities and then kind of like merge all of these capabilities into a single student"
>
> — [17:33](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1053s) &middot; *Previews Krea's next research direction: multi-expert distillation.*

> "data is like eternal like you can if you have that's going to be valuable no matter what the hot new training paradigm is"
>
> — [18:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1106s) &middot; *Frames data as the durable asset relative to fast-churning modeling techniques.*

> "our thing that I like to do is steal a lot from LLM research so that I can just reuse their kernels and like research and like literature"
>
> — [18:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1106s) &middot; *Explicit methodological stance that diffusion work should track LLM research.*

> "I really like to, you know, simplify the stack so that we can get rid of VAEs and then text encoders and then just train a single clean transformer."
>
> — [19:52](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1192s) &middot; *A clear architectural bet about where image generation is headed.*

> "image generation, I think it's really like a proxy for like BLM like progress"
>
> — [20:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1226s) &middot; *Ties image model advances to vision-language model capability as the upstream driver.*

## Positions

- Frontier image models like GPT-image and Nano Banana Pro achieve their output reliability by significantly mode-collapsing, sacrificing stylistic diversity. ([2:11](https://www.youtube.com/watch?v=-tviRdpmHvs&t=131s), confidence: stated)
- Fast generation with knobs beats slow, highly reliable generation for creative users who don't yet know what they want. ([2:46](https://www.youtube.com/watch?v=-tviRdpmHvs&t=166s), confidence: stated)
- Once architecture is locked in, data curation is what actually determines model quality. ([5:13](https://www.youtube.com/watch?v=-tviRdpmHvs&t=313s), confidence: stated)
- Relying on standard aesthetic or image-quality scores to filter data unintentionally destroys stylistic diversity. ([5:48](https://www.youtube.com/watch?v=-tviRdpmHvs&t=348s), confidence: stated)
- Training on AI-generated images is a shortcut that permanently imprints a recognizable ChatGPT/Nano Banana aesthetic on the model, so it should be avoided entirely. ([7:27](https://www.youtube.com/watch?v=-tviRdpmHvs&t=447s), confidence: stated)
- A trained observer can tell when a model has been heavily distilled on ChatGPT or Nano Banana Pro outputs. ([8:02](https://www.youtube.com/watch?v=-tviRdpmHvs&t=482s), confidence: stated)
- Images whose key attributes captioning VLMs consistently fail to describe should be filtered out or undersampled, even when the image itself is fine. ([9:51](https://www.youtube.com/watch?v=-tviRdpmHvs&t=591s), confidence: stated)
- Running a large VLM directly over a billion-image corpus is an inefficient use of GPUs; the judgments must be distilled into a SigLip-sized classifier. ([11:46](https://www.youtube.com/watch?v=-tviRdpmHvs&t=706s), confidence: stated)
- Sparse autoencoders trained on vision models yield usable unsupervised tags for filtering artifacts like watermarks, signatures, and blur. ([12:33](https://www.youtube.com/watch?v=-tviRdpmHvs&t=753s), confidence: stated)
- Krea used roughly 30 to 40 custom in-house classifiers, heuristics, and filters over a 2–10 billion image corpus. ([14:09](https://www.youtube.com/watch?v=-tviRdpmHvs&t=849s), confidence: stated)
- Progressive resolution training from 256 to 1K works because semantics are learned at low resolution and structure and detail only later at high resolution. ([15:29](https://www.youtube.com/watch?v=-tviRdpmHvs&t=929s), confidence: stated)
- A trained prompt-expander LLM has become an almost essential component of production-grade diffusion systems. ([17:33](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1053s), confidence: stated)
- Methods with fewer hyperparameters to tune are preferable, because iteration speed matters more than squeezing out marginal quality. ([18:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1106s), confidence: stated)
- Diffusion research should deliberately borrow from LLM research to reuse its kernels and literature. ([18:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1106s), confidence: stated)
- The image generation stack should eventually shed VAEs and text encoders in favor of a single clean transformer. ([19:52](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1192s), confidence: stated)
- Now that VLMs can cheaply produce accurate bounding boxes and scene graphs, richer structured conditioning signals are a promising direction for image models. ([20:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1226s), confidence: stated)
- Progress in image generation is essentially a proxy for progress in vision-language models. ([20:26](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1226s), confidence: stated)

## Concepts

- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

