---
title: "scaling laws"
type: "concept"
slug: "scaling-laws"
tier: "supporting"
maturity: "contested"
talk_count: 11
speaker_count: 11
---

# scaling laws

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **11** talk(s) by **11** speaker(s)

**Definition:** Predictable relationships between compute, data, parameters, and capability, and how compute is allocated across the training stack.

*Also referred to as: data scaling laws, compute allocation across the training stack, compute allocation between pre-training and post-training, post-training compute, capability density, impact per parameter, training corpus saturation*

## State of Practice

The conference treated the classic compute/data/parameter scaling curve as a description of a regime the field has largely exited. The repeated claim is that pre-training parameter count has hit an architectural ceiling — sub-13B models climbing leaderboards, a 27B dense model beating Llama 405B, a reported 'densing law' of ~50% fewer parameters per unit capability every 3.5 months — while the marginal compute dollar has migrated to mid-training, post-training, RL environments, and test-time compute. The sharpest technical claim is that data curation does not shift the scaling curve but changes its exponent, with concrete numbers attached: matching Qwen 3.5 4B on 145x less training compute, ~35x fewer flops per correct answer, mid-training data making an unchanged post-training harness 2-3x more effective, and a full open-frontier-competitive model for under $20M including failed runs. The structural consequence people care about is who gets to compete: post-training and agentic compute do not need co-located GPU fleets, so the constraint shifts from hardware hoarding to curation recipes and tacit training knowledge held by fewer than ~5,000 people. Cutting against all of this is a minority position that scale, not ideas, is still the only real driver — and that the remaining axis is compute applied to private context rather than to public pre-training corpora. Measurement is the weak link everyone acknowledged: benchmaxing, Git-history mining, and evals saturating at 90% mean the reported capability curves overstate real gains.

## Consensus

### Pre-training parameter scale is no longer the most productive place to spend marginal compute; the budget is shifting to mid-training, post-training, and RL.

Support: **5** talk(s)

> "pre-training size in particular is not your most lucrative axis of scale."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s)

Supporting talks: [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### Data quality, not compute, is the binding constraint, and curation acts as a multiplier on compute rather than a constant-factor improvement.

Support: **5** talk(s)

> "if you choose your data correctly you can actually bend the scaling laws itself you can change the exponent"
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

### Capability per parameter is improving fast enough that newer, smaller models routinely displace older, much larger ones.

Support: **3** talk(s)

> "It's that newer, more efficient models are beating older, less efficient ones."
>
> — [The Desktop Frontier](../talks/the-desktop-frontier.md), [4:26](https://www.youtube.com/watch?v=XV2oYi7kojc&t=266s)

Supporting talks: [The Desktop Frontier](../talks/the-desktop-frontier.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### Because the dominant axis of scale no longer requires co-located mega-clusters, the set of actors who can compete near the frontier is widening.

Support: **3** talk(s)

> "Like if pre-training scale isn't going to dominate performance, it actually really greatly changes who can create the best recipes for innovation, because pre-training compute typically has to be co-located."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s)

Supporting talks: [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)

### Public benchmarks are a broken instrument for measuring scaling returns — they saturate, get contaminated, and must be continuously replaced with held-out sets.

Support: **3** talk(s)

> "if you're looking at an eval and all the models are scoring like 90% probably time to retire that eval and try to get something more difficult"
>
> — [Recursive Model Improvement](../talks/recursive-model-improvement.md), [8:24](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=504s)

Supporting talks: [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

## Disagreements

### Is raw scale still the primary driver of capability, or has the current architecture reached its size ceiling so that returns now come from data, task selection, and post-training?

| Position A | Position B |
|---|---|
| Scale is what drives progress, not new algorithms or ideas; observed trends like the Meter task-length curve are pure artifacts of scaling, and for a fixed corpus compute is the only remaining axis to push.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md)* | The architecture is saturated — no frontier lab will supersize a pre-training run again under it; the original scaling laws were wrong, and data quality and choice of task now beat compute as levers.<br>*[Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)* |

*Why it matters: It determines whether a team's next dollar buys GPUs and a bigger hero run or buys curation, environments, and post-training staff. It also decides whether incumbents with co-located clusters keep a durable moat.*

### Does synthetic data provide a continued scaling axis once real tokens run out, or does it hit a hard ceiling?

| Position A | Position B |
|---|---|
| Rephrasing-based synthetic generation avoids model collapse because all information originates in the source document, so the trained model can surpass the rephrasing model; synthetic data is the way forward for pre-training.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)* | Any approach that fixes a generated dataset and trains on it saturates — a 'data wall in the synthetic sense' — and specific synthetic steps like rewriting and task augmentation failed to move metrics in practice.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* |

*Why it matters: If synthetic data has a fixed upper bound, self-improving curricula that make their own training harder are mandatory rather than optional; if not, corpus rephrasing is a straightforward way to keep spending compute productively.*

### Should teams get domain capability by training their own specialized model, or by anchoring a general frontier model at inference time?

| Position A | Position B |
|---|---|
| Train your own: curation plus SFT beats the public Pareto frontier at a fraction of the compute, post-training simultaneously improves compliance, latency, and throughput, and owning a model hedges against rising frontier API costs and subsidy withdrawal.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)* | Specialization via weights degrades the model: biomedically fine-tuned models underperformed their general-purpose bases through catastrophic forgetting, and naive finetuning on your own corpus drives loss to near zero while generation collapses — put the material in context instead.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: The two paths have opposite cost structures and opposite audit properties — one buys inference savings and control at the cost of a training pipeline and possible capability loss, the other keeps provenance inspectable but pays frontier token prices forever.*

### As models improve, does the binding constraint become the scaffolding around the model or the intelligence of the model itself?

| Position A | Position B |
|---|---|
| The limiting factor will be harness adaptability, not model strength; carefully built harnesses go stale within a month as models improve past them.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)* | The whole system is bottlenecked on the smartest model in it, since every judge, reward model, and research agent is distilled from it; post-training is a more powerful reliability lever than prompting or harness changes.<br>*[Recursive Model Improvement](../talks/recursive-model-improvement.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* |

*Why it matters: It decides whether engineering headcount goes into multi-agent coordination and emergent scaffolding or into training data, environments, and model quality.*

## Practical Guidance

**Do:**

- Derisk a large run by training small models on properly curated data with simulated token scarcity — this predicts large-model performance at 50-100x less compute
- Sample multiple answers per question (e.g. 16x on the same question) rather than collecting proportionally more questions answered once
- When domain-adapting, keep most of the mid-training mix representative of the pre-training distribution — this prevented catastrophic forgetting entirely while still capturing the domain gain
- Repeat high-quality data rather than adding low-quality data, up to a threshold
- Pull post-training-shaped data (chat SFT, agentic traces, long context) back into pre-training so the model learns downstream task shapes from the start
- Fix MoE expert load imbalance by mixing the data better early, not by cranking the load-balancing coefficient during SFT
- Test teachers empirically before distilling — some Qwen models beat Claude models as teachers in Open Thoughts Agents
- Select documents deliberately for rephrasing; random document selection produces poor synthetic data
- Add structural tags to prompt-response pairs when fine-tuning on imbalanced data to stop the model hallucinating specific numbers
- Instrument large runs with tensor core utilization and InfiniBand metrics, and pull any GPU running above ~78°C out of the pool immediately
- Checkpoint every 20-30 minutes on a fast parallel filesystem, and buy a commercial one rather than running Ceph
- Give training jobs strictly higher scheduling priority than production inference, and relocate inference to other clusters or rented capacity rather than blocking the run
- Delete Git history and apply a network allowlist during eval runs, and maintain a private held-out eval set drawn from your own codebase

**Avoid:**

- Assuming more pre-training parameters buys performance under an architecture that is already at its size ceiling
- Plain next-token-prediction finetuning on your private corpus — loss goes to ~0.0001, generation collapses, and no useful generalization appears
- Treating any fixed dataset as an indefinite scaling axis; unless the model is underparameterized it will learn all of it and stop improving
- Trusting GPU utilization as a training-efficiency metric — use tensor core utilization instead
- Running multi-node pre-training with no InfiniBand metrics when most failures at scale are cross-node communication failures
- Swapping nodes reactively after every crash; the same machines and code often run 12-24 hours after a series of hourly failures
- Budgeting 'hundreds of millions of dollars' as the price of a competitive custom model
- Reading published benchmark scores at face value given benchmaxing and models mining Git history and the web for answers
- Assuming answer filtering, synthetic rewriting, or task augmentation will help — they did not move metrics, while synthetic question generation did
- Enforcing behavior through a long list of prompt rules, which blows up latency where post-training would not

## Notable Outliers

- Curation alone, with no post-training, pushed a VLM past the public Pareto frontier and matched Qwen 3.5 4B using 145x less training compute, with ~35x fewer flops per correct answer at inference. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [7:47](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=467s))
- Capability density follows a 'densing law' of roughly 50% fewer parameters for equivalent capability every 3.5 months. ([The Desktop Frontier](../talks/the-desktop-frontier.md), [4:26](https://www.youtube.com/watch?v=XV2oYi7kojc&t=266s))
- Fewer than roughly 5,000 people in the world know how to train frontier models at scale, and that tacit knowledge is itself an exploitable search space for automated research. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s))
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude tracking language similarity. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- The original scaling laws were incorrect, and Sutton's bitter lesson holds in games but not in reality — data beats compute and choosing the right task beats data. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s))
- Web text has fallen from ~85% of GPT-3's training mix to ~15% in MAI Thinking 1, with code now the dominating subset. ([The Base Model Is Dead](../talks/the-base-model-is-dead.md), [6:46](https://www.youtube.com/watch?v=xbPriQWXtWM&t=406s))
- Training runs failed far more often than Meta's published failure-rate estimates predicted, frequently lasting under 8 hours. ([Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [3:49](https://www.youtube.com/watch?v=byn9PURoBNY&t=229s))
- A model competitive with the open frontier can be trained for under $20 million total, including salaries, compute, and every failed attempt. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [The Desktop Frontier](../talks/the-desktop-frontier.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Gabriel Jorge Menezes](../speakers/gabriel-jorge-menezes.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Varun Singh](../speakers/varun-singh.md)

