---
title: "From Tokens to Cells: Foundation Models for Single-Cell Biology"
type: "talk"
slug: "from-tokens-to-cells-foundation-models-for-single-cell-biology"
org: "Altos Labs"
video_id: "-561cZmir5Q"
duration_sec: 1017
word_count: 2507
speakers: ["Akram Baharlouei"]
---

# From Tokens to Cells: Foundation Models for Single-Cell Biology

**Speakers:** [Akram Baharlouei](../speakers/akram-baharlouei.md)

**Org:** Altos Labs

**Duration:** 16m 57s

[Watch on YouTube](https://www.youtube.com/watch?v=-561cZmir5Q)

## Summary

Akram Baharlouei, an ML engineer at Altos Labs, gives an engineering-focused tour of foundation models for single-cell biology from the perspective of someone without a biology background. The talk motivates single-cell modeling through cellular reprogramming (Yamanaka factors), the 'virtual cell/virtual human' vision, and the declining productivity of drug development, then surveys the measurement modalities available (genomics, transcriptomics, proteomics, morphology) and explains why RNA-seq dominates foundation model training despite being noisy and heterogeneous. The core critical claim is that transformer-based single-cell models like scGPT, which treat cells as sentences and genes as tokens with BERT-style masking, compress data into latent vectors that lose information — and in the speaker's own NeurIPS benchmarking, simple linear models sometimes match or beat them despite far less compute. The talk argues that flow-matching models that predict the full distribution rather than the mean (their PrimeFlow work) perform better, and that progress is bottlenecked more on data quality and measurement realism than on scaling alone. Worth watching if you want a compact, honest status report on why cross-domain transfer of the LLM recipe to biology has underdelivered.

## Key Points

- Cellular reprogramming via the four Yamanaka transcription factors, discovered in 2006 and awarded the Nobel Prize in 2012, motivates the field — and partial reprogramming aims to change a cell's age without changing its type, with the first reprogramming medicine (OSK) reaching human testing around 2026.
- Drug development runs opposite to Moore's law: the number of drugs developed per year is declining, acceptance rates are around 5% or less, and the full pipeline takes up to 10 years and costs billions, so speedups must come across the whole pipeline rather than just the research stage.
- Of the single-cell modalities, RNA-seq dominates foundation model training because PCR-based technology scales — datasets reach tens of millions of cells, with 500-million and 1-billion-cell projects underway — while proteomics, arguably closer to biological function, remains very low throughput.
- Single-cell data is fundamentally noisy: two identical cells do not read the same, cellular changes happen in bursts rather than continuously, and sequencing captures only a snapshot of what is really a movie; batch effects across labs and machines add technical noise on top.
- Transformer-based models like scGPT treat each cell as a sentence and genes as tokens, using BERT-style masking with bidirectional attention to predict gene counts, then use the latent vector for cell type prediction and perturbation response modeling.
- Compressing single-cell data into a latent vector loses information, and the speaker reports that simple linear models are sometimes on par with or even outperform these expensive transformer models.
- Two NeurIPS benchmarking papers from the speaker's group — one on multimodal imaging plus RNA-seq, one on perturbation response — found these expensive-to-train models underperform relative to what foundation models achieve in language and imaging.
- Flow-matching models such as the group's PrimeFlow appear to do better because they match the data distribution rather than predicting the mean the way autoencoder-based models like CPA do, evaluated with MMD scores.
- The speaker's closing argument is that scaling data volume alone is insufficient — improving measurement quality and realism, alongside massive scaling, is what will enable generalization to unseen data.

## Notable Quotes

> "Altos Labs is a biotech startup and the goal is to restore cell health and resilience through cellular rejuvenation to inverse disease and disabilities that can happen throughout the life."
>
> — [0:12](https://www.youtube.com/watch?v=-561cZmir5Q&t=12s) &middot; *States the organizational mission that frames the entire talk.*

> "In 2006, Shinya Yamanaka discovered four transcription factors. There are four specific type of a proteins that when they were overexpressed in a cell"
>
> — [0:57](https://www.youtube.com/watch?v=-561cZmir5Q&t=57s) &middot; *Anchors the scientific premise the field is built on.*

> "For partial programming specifically is that we can also turn out that we can also only change the age of the cell. We don't have to change the type."
>
> — [1:51](https://www.youtube.com/watch?v=-561cZmir5Q&t=111s) &middot; *Names the specific mechanism behind rejuvenation as distinct from general reprogramming.*

> "the more we can model this living organisms. The better we are in understanding our body and the how we can treat medicine, we can develop drugs."
>
> — [3:40](https://www.youtube.com/watch?v=-561cZmir5Q&t=220s) &middot; *The core justification for the virtual cell research program.*

> "Basically, the number of drugs that developed each year is kind of declining, which is surprising with all the advances in technology, in AI."
>
> — [4:34](https://www.youtube.com/watch?v=-561cZmir5Q&t=274s) &middot; *Reports the counterintuitive productivity trend that motivates AI intervention.*

> "The whole pipeline it could take up to 10 years easily and then it cost it can cost billions."
>
> — [4:34](https://www.youtube.com/watch?v=-561cZmir5Q&t=274s) &middot; *Quantifies the cost structure the field is trying to attack.*

> "if we only look at like research and development, the models like you know, protein design and the stuff, we might like save like you know, few years here, but at the end maybe it's not going to help for the entire pipeline."
>
> — [5:29](https://www.youtube.com/watch?v=-561cZmir5Q&t=329s) &middot; *A tradeoff claim others might contest — that R&D-stage AI gains don't move the overall timeline.*

> "the problem is that proteomics is a very hard to measure and you know, there are ways to measure it but it's a very low throughput."
>
> — [7:03](https://www.youtube.com/watch?v=-561cZmir5Q&t=423s) &middot; *Explains why the field trains on RNA rather than the modality closer to function.*

> "So we have like usually data set for single cell RNA in the scale of like tens of tens of uh millions of cells to even like you know, I've heard 500 million cells and then kind of like even like there's a project 1 billion cells."
>
> — [7:45](https://www.youtube.com/watch?v=-561cZmir5Q&t=465s) &middot; *Concrete data-scale numbers for the domain.*

> "The nature of the data is if you measure two identical cell at the they don't read the same."
>
> — [8:27](https://www.youtube.com/watch?v=-561cZmir5Q&t=507s) &middot; *The single sharpest statement of why this data resists the LLM recipe.*

> "And what we are measuring with current uh single cell sequencing is like a snapshot. We're taking a snapshots from from a whole movie."
>
> — [9:12](https://www.youtube.com/watch?v=-561cZmir5Q&t=552s) &middot; *Memorable framing of the temporal limits of the measurement.*

> "they kind of like treat each uh, cell like a sentence and then genes like tokens."
>
> — [10:42](https://www.youtube.com/watch?v=-561cZmir5Q&t=642s) &middot; *The one-line statement of the token-to-cell analogy that titles the talk.*

> "And then what happens is when you, uh, compress this data, we're losing a lot of information. It doesn't preserve the, it doesn't preserve the information."
>
> — [12:24](https://www.youtube.com/watch?v=-561cZmir5Q&t=744s) &middot; *The mechanistic critique of latent-vector approaches.*

> "we see that sometimes, sometimes like, uh, maybe, uh, simple linear models are on par or like sometimes even outperforming this, uh, these, uh, models"
>
> — [12:24](https://www.youtube.com/watch?v=-561cZmir5Q&t=744s) &middot; *The talk's most contested empirical claim about foundation model value.*

> "even though these models are very expensive to train, uh, at the end they're not performing as well comparing to, you know, other domain language, uh, and and imaging."
>
> — [13:16](https://www.youtube.com/watch?v=-561cZmir5Q&t=796s) &middot; *Summarizes the benchmarking result and situates it against language and vision.*

> "it seems that these models they seem to do better. There is a better comparing to trans autoregressive-based models"
>
> — [14:02](https://www.youtube.com/watch?v=-561cZmir5Q&t=842s) &middot; *The positive methodological recommendation of the talk.*

> "Whereas other models like CPADR autoencoder-based is kind of like just mapping to the it's trying to predict the mean rather than understanding understanding the distribution."
>
> — [14:54](https://www.youtube.com/watch?v=-561cZmir5Q&t=894s) &middot; *Names the specific failure mode that distribution matching fixes.*

> "it's important that to work on quality of the data of the way that we are measuring this data to be a bit more realistic of the real organism than than just like you know scale the data the way it is."
>
> — [15:45](https://www.youtube.com/watch?v=-561cZmir5Q&t=945s) &middot; *The data-quality-over-data-scale position that closes the talk.*

## Positions

- The number of new drugs developed per year is declining despite advances in technology and AI, the inverse of Moore's law. ([4:34](https://www.youtube.com/watch?v=-561cZmir5Q&t=274s), confidence: stated)
- AI gains confined to the research and development stage of the drug pipeline will not meaningfully shorten the overall 10-year timeline; innovation is needed across the whole pipeline. ([5:29](https://www.youtube.com/watch?v=-561cZmir5Q&t=329s), confidence: stated)
- RNA-seq is the modality most used for single-cell foundation model training primarily because it is easier to measure and scale, not because it is the most biologically informative. ([7:45](https://www.youtube.com/watch?v=-561cZmir5Q&t=465s), confidence: stated)
- Proteomics would arguably be more valuable than transcriptomics because proteins do most of the functional work in the body, but it is too low-throughput to train on. ([7:03](https://www.youtube.com/watch?v=-561cZmir5Q&t=423s), confidence: stated)
- Two measurements of identical cells do not produce the same reading, making single-cell data intrinsically heterogeneous in a way text data is not. ([8:27](https://www.youtube.com/watch?v=-561cZmir5Q&t=507s), confidence: stated)
- Compressing single-cell data into a latent vector destroys information, which is why transformer-based single-cell models underperform. ([12:24](https://www.youtube.com/watch?v=-561cZmir5Q&t=744s), confidence: stated)
- Simple linear models sometimes match or outperform compute-expensive transformer-based single-cell foundation models. ([12:24](https://www.youtube.com/watch?v=-561cZmir5Q&t=744s), confidence: stated)
- Single-cell foundation models perform worse relative to their training cost than foundation models in language and imaging domains, a view the speaker says is shared in the community. ([13:16](https://www.youtube.com/watch?v=-561cZmir5Q&t=796s), confidence: stated)
- Flow-matching models currently outperform autoregressive and autoencoder-based models on single-cell data because they match the full distribution rather than predicting the mean. ([15:45](https://www.youtube.com/watch?v=-561cZmir5Q&t=945s), confidence: stated)
- Progress requires both massive data scaling and improved measurement quality; scaling existing low-quality data alone will not produce models that generalize to unseen data. ([16:29](https://www.youtube.com/watch?v=-561cZmir5Q&t=989s), confidence: stated)
- Quantum computing may eventually be a natural fit for the high-dimensional multi-state nature of single-cell data, but classical AI is what is available now. ([10:00](https://www.youtube.com/watch?v=-561cZmir5Q&t=600s), confidence: implied)

## Concepts

- [agentic science](../concepts/agentic-science.md)
- [benchmark design](../concepts/benchmark-design.md)
- [long-context processing](../concepts/long-context-processing.md)

