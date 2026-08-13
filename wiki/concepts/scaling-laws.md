---
title: "scaling laws"
type: "concept"
slug: "scaling-laws"
tier: "supporting"
maturity: "contested"
talk_count: 10
speaker_count: 10
---

# scaling laws

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **10** talk(s) by **10** speaker(s)

**Definition:** Predictable relationships between compute, data, parameters, and capability, and how compute is allocated across the training stack.

*Also referred to as: data scaling laws, compute allocation across the training stack, compute allocation between pre-training and post-training, post-training compute, capability density, impact per parameter, training corpus saturation*

## State of Practice

The conference's working consensus is that the original compute-parameters-data curve has stopped being the interesting one: pre-training size is treated as a saturated axis under current architectures, and the live question is how compute is allocated across pre-training, mid-training, post-training, RL, and inference. Data quality is repeatedly described not as a constant-factor win but as something that changes the exponent of the curve — Datology claims curation alone matched a Qwen 3.5 4B-class VLM with 145x less training compute, and Bespoke reports a curation recipe whose downstream metrics scale with curated dataset size. RL has been promoted from a post-hoc alignment step to the dominant consumer of the compute budget, which reframes the base model as a prior supplying atomic skills for RL composition rather than an archive of web text (web text fell from ~85% of GPT-3's mix to ~15% in MAI Thinking 1). A second scaling law is doing real work here: the 'densing' trend of roughly 50% fewer parameters for equivalent capability every 3.5 months, which is why a 27B dense model now beats Llama 405B and why efficiency, not size, is where practitioners expect gains. The unresolved core is saturation: every approach that fixes a dataset and trains on it plateaus, so the frontier bet is on self-improvement loops that make training data harder as the model improves. Meanwhile a minority position holds that scale is still the only thing that ever drove progress and that everything else is a story told by people without 200,000 GPUs.

## Consensus

### Pre-training parameter count is no longer the most productive axis of scale; the returns have moved to post-training, RL, and mid-training on the same or smaller checkpoints.

Support: **5** talk(s)

> "pre-training size in particular is not your most lucrative axis of scale."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s)

Supporting talks: [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### Data quality and curation, not raw compute, is the binding constraint — it acts as a multiplier on compute rather than an additive improvement.

Support: **5** talk(s)

> "if you choose your data correctly you can actually bend the scaling laws itself you can change the exponent"
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)

### Capability per parameter is improving fast enough that newer efficient models beat older much larger ones, so equivalent capability keeps migrating down to smaller footprints.

Support: **3** talk(s)

> "It's that newer, more efficient models are beating older, less efficient ones."
>
> — [The Desktop Frontier](../talks/the-desktop-frontier.md), [4:26](https://www.youtube.com/watch?v=XV2oYi7kojc&t=266s)

Supporting talks: [The Desktop Frontier](../talks/the-desktop-frontier.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### Training on any fixed dataset saturates, so continued compute scaling requires a mechanism that makes the training problems progressively harder as the model improves.

Support: **3** talk(s)

> "whatever you do, you have to define the data set, and then you train on the data set, and eventually things saturate. So, even if it's like really hard, unless your model is under parameterized, eventually it will learn all the data."
>
> — [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [16:11](https://www.youtube.com/watch?v=WiqDvX6isc4&t=971s)

Supporting talks: [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)

## Disagreements

### If you are compute-limited, is the correct response to acquire more compute or to invest in data and task selection?

| Position A | Position B |
|---|---|
| Scale is what drives progress; compute is the only remaining scaling axis once data is fixed, and the visible capability trends (e.g. the METR task-length curve) are artifacts of scaling rather than of algorithmic insight. Buying and co-locating compute is therefore the move.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)* | Compute is downstream of data: curation changes the exponent, not the intercept, and the right task choice beats data which beats compute. A team hitting a compute wall should spend on curation, not GPUs — Datology claims a model competitive with the open frontier for under $20M all-in.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)* |

*Why it matters: This determines whether a serious model effort needs a nine-figure cluster commitment or a data team, and whether 'we can't afford to train' is a real constraint or a category error.*

### Does synthetic data extend the data scaling axis, or does it just relocate the wall?

| Position A | Position B |
|---|---|
| Synthetic data is the way forward for pre-training. Rephrasing-based generation avoids collapse because all information originates in the source document, so the trained model can surpass the rephrasing model, and synthetic question generation was one of the few curation steps that empirically worked.<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* | Synthetic generation from a corpus hits a synthetic data wall: you eventually learn everything derivable from the source set, and synthetic continued pretraining additionally overwrites pretrained knowledge and forces you to re-post-train. It is a one-time transfer, not an axis you can keep pushing compute into.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: If synthetic data is a genuine axis, the data wall is a non-event and curation pipelines are the whole game; if it is a one-time transfer, teams need self-improvement loops with escalating difficulty instead of bigger generation runs.*

### Does frontier capability still require frontier-scale, co-located capital?

| Position A | Position B |
|---|---|
| Yes — controlling every aspect of training means a full pre-train from scratch on dedicated infrastructure (100,000 GPUs in 122 days, then another 100,000 in 92), and the whole training system is bottlenecked on the intelligence of the single smartest model, since every judge, reward model, and research agent is distilled from it.<br>*[Recursive Model Improvement](../talks/recursive-model-improvement.md)* | No — agentic and post-training compute do not require hoarding co-located GPUs, capability density is halving parameter counts every few months, and a domain-competitive model is a high-six-figure to low-eight-figure project. The advantage shifts to whoever has the best recipe or owns their own hardware.<br>*[Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)* |

*Why it matters: It decides whether the set of organizations that can produce frontier-relevant models stays at a handful of labs or widens to anyone with a curation pipeline and a rack, and whether enterprises should build or keep renting subsidized tokens.*

### What should a base model be trained to be — a repository of world knowledge, or a prior for RL?

| Position A | Position B |
|---|---|
| Pre-training remains the mechanism for genuine knowledge acquisition and cannot be replaced by later-stage tricks; the failure of current models is that they lack private/personal knowledge, not that pre-training is misdirected.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* | Because RL now dominates the compute budget, supervised next-token prediction exists to build useful representations for RL. The base model only needs exposure to the atomic skills RL will later compose, and post-training-shaped data (SFT, agentic traces, long context) should be pulled forward into pre-training.<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)* |

*Why it matters: It changes the pre-training data mix by an order of magnitude — whether you optimize for breadth of world knowledge or for the specific skill atoms and interaction shapes your RL environments will exercise.*

## Practical Guidance

**Do:**

- Derisk a large run with small-scale runs on properly curated data using simulated token scarcity — Datology reports this predicts large-model performance at 50-100x less compute.
- Sample multiple answers per question (they used 16x) rather than collecting proportionally more questions answered once.
- Run staged ablations per curation step and keep only what moves metrics; synthetic question generation worked, while answer filtering, synthetic rewriting, and task augmentation did not.
- Repeat high-quality data rather than adding low-quality data, up to some repetition threshold.
- Keep most of the mid-training mix representative of the pre-training distribution when doing domain adaptation — this prevented catastrophic forgetting entirely while still making the unchanged post-training harness 2-3x more effective.
- Design pre-training, mid-training, and post-training as one system rather than handing off between independent teams; MoE expert load imbalance during SFT is a symptom of pre/post distribution mismatch, not something to fix by cranking the load-balancing coefficient late.
- Treat SFT as the source of most agent post-training gains and reserve RL for the last few percentage points, since RL is compute-intensive.
- Make test-time compute adaptive to task difficulty instead of spending the same compute on every query.
- Generate hard verifiable RL problems programmatically — e.g. delete features and files from generated applications until tests fail, then have the model re-implement them.
- Retire any eval where all models score ~90%, and hold out a private eval set drawn from your own codebase; delete Git history and apply network allowlists during agentic evals since models will mine both for answers.

**Avoid:**

- Assuming a stronger model is a better distillation teacher — Bespoke found some Qwen models outperformed Claude models as teachers.
- Plain next-token-prediction finetuning on a private corpus: loss goes to ~0.0001, generation collapses, and no useful generalization appears.
- Believing customizing a competitive model costs hundreds of millions of dollars — Datology puts it at under $20M including salaries, all compute, and every failed attempt.
- Treating benchmark numbers as capability signal when benchmaxing is widespread and public evals leak into training.
- Enforcing behavior with an ever-growing list of prompt rules — it blows up latency, and post-training on the same requirement improved compliance, latency, and throughput simultaneously.
- Fine-tuning on an imbalanced dataset without structural tags on prompt-response pairs, which lets the model hallucinate specific numbers instead of learning the response form.
- Assuming a fixed harness you build today will still be relevant next month — the model may improve enough not to need the scaffolding.
- Building an automated architecture/hyperparameter search without co-optimizing data quality; the returns do not appear until data quality is controlled for.

## Notable Outliers

- Capability density follows a 'densing law': roughly 50% fewer parameters needed for equivalent capability every 3.5 months, projecting GLM 5.2-class intelligence onto a single 32GB RTX 5090 within ~18 months. ([The Desktop Frontier](../talks/the-desktop-frontier.md), [4:26](https://www.youtube.com/watch?v=XV2oYi7kojc&t=266s))
- The original scaling laws were simply incorrect, and Sutton's bitter lesson holds in games but not in reality — data beats compute and task choice beats data. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s))
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude tracking language similarity — at only 8% multilingual tokens. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- Fewer than ~5,000 people worldwide know how to train frontier models at scale, which makes that tacit knowledge an exploitable search space for automated research agents that already beat in-house research staff at 60%+ win rates. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s))
- The entire training system is bottlenecked on the intelligence of its single smartest model, because every judge, reward model, and research agent is distilled from it — so raising the top model raises the floor of every loop at once. ([Recursive Model Improvement](../talks/recursive-model-improvement.md), [19:19](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1159s))
- Post-training data bought from Scale, Surge, and Mercor is public data by definition, because it is content the model could tell any user — so it cannot close the private-knowledge gap. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [5:45](https://www.youtube.com/watch?v=WiqDvX6isc4&t=345s))
- Language models will not follow AlphaGo's trajectory of RL fully overtaking supervised learning, because human language is too broad a distribution to learn through RL alone. ([The Base Model Is Dead](../talks/the-base-model-is-dead.md), [14:48](https://www.youtube.com/watch?v=xbPriQWXtWM&t=888s))
- H100 prices reversed a multi-year decline and are now ~40% up from their lows, and OpenAI has started selling token futures — access to frontier APIs may become capacity-limited rather than business-limited. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [1:23](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=83s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
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
- [Jack Morris](../speakers/jack-morris.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Varun Singh](../speakers/varun-singh.md)

