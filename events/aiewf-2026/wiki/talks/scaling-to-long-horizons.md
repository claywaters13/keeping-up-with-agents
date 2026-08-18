---
title: "Scaling to Long Horizons"
type: "talk"
slug: "scaling-to-long-horizons"
track: "Data Quality"
org: "General Reasoning"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "2bvtay8wGYI"
duration_sec: 1087
word_count: 3230
speakers: ["Chengxi Taylor", "Ross Taylor"]
---

# Scaling to Long Horizons

*Program title: Scaling to Long-Horizons: Algorithms, Environments, Compute*

**Speakers:** [Chengxi Taylor](../speakers/chengxi-taylor.md), [Ross Taylor](../speakers/ross-taylor.md)

**Org:** General Reasoning

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 18m 07s

[Watch on YouTube](https://www.youtube.com/watch?v=2bvtay8wGYI)

## Summary

Ross Taylor (CEO, General Reasoning; formerly reasoning lead at Meta AI) and co-founder Chengxi Taylor pair a first-person history of the 2020–2023 LLM era with a technical agenda for long-horizon RL. Ross uses the Galactica-vs-ChatGPT collision as a natural experiment showing that a state-of-the-art base model is worthless as a product without RL, and explains why his team's early PPO-with-verifiable-rewards recipe on Llama 2 hit SOTA math results but never produced the reflective, inference-time-scaling behavior of o1/R1 — the missing ingredients were better base models, more RL compute, and longer context. Chengxi then argues that long-horizon tasks are the next frontier and walks through the concrete obstacles: scarce context windows, gradient variance that scales with trajectory length, sparse rewards and credit assignment, and the GPU-utilization/off-policy tradeoff in pipeline RL. He makes the case for value models (critics) as the unifying fix — variance reduction, trajectory-level fit with compaction, and bootstrapping partial episodes — while conceding they add bias and complexity versus GRPO. Worth watching for the insider account of Galactica's ideas (thinking tokens, data efficiency, multi-epoch training) and for a rare, specific treatment of what breaks when RL episodes run for weeks.

## Key Points

- Galactica and ChatGPT shipped two weeks apart on comparable base models, and the divergent outcomes served as a natural experiment proving that RLHF, not base model quality, is what turned LLMs into products.
- Galactica introduced several ideas that later became standard: data efficiency via a curated 105B-token corpus, multi-epoch training when the consensus was one epoch, and 'thinking tokens' as an internal working-memory process consuming inference compute before answering.
- Ross's team at Meta had a working recipe two years before R1 — continued pre-training on math/science, then PPO with verifiable rewards and a strong outcome reward model to initialize the value model — and got internal SOTA on math, but no reflective backtracking behavior.
- The explanation for that gap was the bitter lesson in pure form: better base models, more RL compute, and bigger context windows are what unlock emergent reasoning behavior, not a cleverer objective.
- Having a frontier base model earlier is an epistemic advantage, not just a product one — OpenAI's GPT-4-level model let them 'see further' and generate ideas others couldn't.
- Long-horizon RL faces three distinct optimization problems: gradient variance scaling with trajectory length, sparse rewards causing credit assignment failures, and variable-length trajectories.
- Value models are proposed as the answer — they reduce variance, operate at trajectory level (which fits context compaction), encourage batch diversity, and enable bootstrapping mid-episode — at the cost of value-model bias and having to train a second model alongside the policy.
- General Reasoning's Kelly Bench gave frontier models $100K to build ML models betting on a season of Premier League football; all of them lost money, which the speakers read as evidence the field over-indexes on short procedural coding tasks over open-ended, multi-agent, real-world ones.
- Pipeline RL trades off-policy staleness for GPU utilization; roughly eight steps of off-policyness is tolerable in their experience, but week-long inference in long-horizon settings blows past that and leaves GPUs idle unless you bootstrap with a value model.

## Notable Quotes

> "A good base model is not enough. So I took that lesson quite early on. So like I said, RLHF made LLMs products."
>
> — [3:03](https://www.youtube.com/watch?v=2bvtay8wGYI&t=183s) &middot; *The thesis of the first half, stated flatly.*

> "Like even at the time, like InstructGPT in 2022 had these pretty stunning results. Like a 1 billion parameter model with RLHF was outperforming 175 billion models."
>
> — [3:03](https://www.youtube.com/watch?v=2bvtay8wGYI&t=183s) &middot; *Concrete two-orders-of-magnitude number backing the RL-over-scale claim.*

> "it outperformed Palm, Chinchilla, GPT-3.5 with a lot less compute in scientific domains. It was state-of-the-art. So again, that also shows you how powerful RL is."
>
> — [4:17](https://www.youtube.com/watch?v=2bvtay8wGYI&t=257s) &middot; *The paradox at the center of the Galactica story — SOTA and still a failure.*

> "And Galactica said, "No. High quality, you know, curated data sets really matter." And that was a real driver of those results you just saw."
>
> — [5:21](https://www.youtube.com/watch?v=2bvtay8wGYI&t=321s) &middot; *Claims priority on the data-quality-over-quantity position.*

> "It sounds ridiculous now, but at the time the consensus was you don't do more than an epoch."
>
> — [5:21](https://www.youtube.com/watch?v=2bvtay8wGYI&t=321s) &middot; *Documents how fast a field consensus inverted.*

> "But, Galactica was really this first idea which said, "No, this is an internal working memory process. This is an internal thinking. You should be inside these tags, and you should spend the inference computer before you get to an answer, right?""
>
> — [5:50](https://www.youtube.com/watch?v=2bvtay8wGYI&t=350s) &middot; *A priority claim on the thinking-tokens / inference-time-compute framing.*

> "So, at the time we only had Llama 2 base models, terrible mathematics corpus, terrible results on math."
>
> — [6:51](https://www.youtube.com/watch?v=2bvtay8wGYI&t=411s) &middot; *Names the concrete constraint that made the early reasoning attempt fail.*

> "Number two, PPO with verifiable rewards. But, notice this isn't GRPO, right?"
>
> — [6:51](https://www.youtube.com/watch?v=2bvtay8wGYI&t=411s) &middot; *Pins down the actual unpublished recipe and its deliberate divergence from today's default.*

> "Like, better base models, more RL computes, bigger context windows, and that's all you need for this kind of emergent behavior."
>
> — [7:56](https://www.youtube.com/watch?v=2bvtay8wGYI&t=476s) &middot; *The talk's bitter-lesson punchline about why o1-style behavior appeared when it did.*

> "It also like says something like quite important about the sociology of like research because the fact that OpenAI had this model, you know, GPT-4 level model before anyone else, it allowed them to see further, right?"
>
> — [8:29](https://www.youtube.com/watch?v=2bvtay8wGYI&t=509s) &middot; *Frames compute access as an epistemic, not just competitive, advantage.*

> "Long horizon task is not just an engineering problem. It is a mindset."
>
> — [9:04](https://www.youtube.com/watch?v=2bvtay8wGYI&t=544s) &middot; *Chengxi's framing device, repeated as the closing line.*

> "If you take Fermat's Last Theorem as example, what it take for the mathematician was over 10 years time of reading paper, writing down thoughts in the scratch pad, or taking a walk to generate the creative ideas."
>
> — [9:49](https://www.youtube.com/watch?v=2bvtay8wGYI&t=589s) &middot; *Makes the context-scarcity argument vivid with a token-count comparison.*

> "So what it essentially does is generate the token until the end of the context window, summarize, and then on top of that generate more tokens."
>
> — [9:49](https://www.youtube.com/watch?v=2bvtay8wGYI&t=589s) &middot; *Clean definition of context compaction as an RL-trainable operation.*

> "The first is the gradient variance scales with the length. And the second is a sparse reward. And you have this credit assignment problem."
>
> — [10:42](https://www.youtube.com/watch?v=2bvtay8wGYI&t=642s) &middot; *Enumerates the specific optimization failures of long-horizon RL.*

> "As you can see, we gave all the frontier models a 100K to start. All of them lost."
>
> — [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s) &middot; *The headline empirical result from Kelly Bench.*

> "First, I believe now the AI industry is a little bit too biased towards coding and procedure task."
>
> — [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s) &middot; *A contestable position on where the field is misallocating effort.*

> "And second of all, not enough focus on open-ended task. We live in the real world with a lot of a complexity, uncertainty, and that's not fully captured by the current benchmark."
>
> — [13:51](https://www.youtube.com/watch?v=2bvtay8wGYI&t=831s) &middot; *States the benchmark critique that motivates their environment work.*

> "What the pipeline RL does is that you let the sequence to be generated and you start to train the model while there's a still more sequences being generated."
>
> — [14:36](https://www.youtube.com/watch?v=2bvtay8wGYI&t=876s) &middot; *Plain-language definition of pipeline RL for practitioners.*

> "But from the our experience, normally off-policy up to eight steps is okay. So, essentially, we made a trade-off between the off-policy and the GPU utilization."
>
> — [15:17](https://www.youtube.com/watch?v=2bvtay8wGYI&t=917s) &middot; *A specific empirical threshold others can test against.*

> "It's like a dopamine in human brain. And that allows you to train the model."
>
> — [16:01](https://www.youtube.com/watch?v=2bvtay8wGYI&t=961s) &middot; *Memorable analogy for value-model bootstrapping before episode end.*

> "But, here's another trade-off. While you utilize the GPU fully, you introduce the value model bias. So, there's always a bit of trade-off in those solutions."
>
> — [16:01](https://www.youtube.com/watch?v=2bvtay8wGYI&t=961s) &middot; *Concedes the cost of their own recommended approach.*

> "So, it's a place where host over 350 environments and with a single API endpoint."
>
> — [16:01](https://www.youtube.com/watch?v=2bvtay8wGYI&t=961s) &middot; *Concrete scale figure for their RL environment platform.*

## Positions

- A state-of-the-art base model is insufficient to make a useful product; RL post-training is the decisive ingredient. ([3:03](https://www.youtube.com/watch?v=2bvtay8wGYI&t=183s), confidence: stated)
- Galactica was the first LM to crack data efficiency (105B curated tokens vs. trillion-token corpora) and the first major empirical result for multi-epoch training. ([5:21](https://www.youtube.com/watch?v=2bvtay8wGYI&t=321s), confidence: stated)
- Galactica's thinking-token tags anticipated what DeepSeek/o1 did two years later by applying RL pressure to internal reasoning. ([6:21](https://www.youtube.com/watch?v=2bvtay8wGYI&t=381s), confidence: stated)
- Reflective, backtracking reasoning behavior did not emerge in 2023 because base models, RL compute, and context windows were too small — not because the objective was wrong. ([7:56](https://www.youtube.com/watch?v=2bvtay8wGYI&t=476s), confidence: stated)
- Early access to a frontier base model confers a research advantage: it lets a lab see further and generate ideas competitors cannot. ([8:29](https://www.youtube.com/watch?v=2bvtay8wGYI&t=509s), confidence: stated)
- A 1M-token context window is orders of magnitude short of what genuinely long-horizon intellectual work requires (tens to hundreds of billions of tokens). ([9:49](https://www.youtube.com/watch?v=2bvtay8wGYI&t=589s), confidence: stated)
- RL should be applied to the compaction step as well as the task itself. ([10:42](https://www.youtube.com/watch?v=2bvtay8wGYI&t=642s), confidence: stated)
- Value models are preferable to GRPO for long-horizon RL because they cut variance, work at trajectory level with compaction, and permit bootstrapping — despite added complexity and bias. ([11:31](https://www.youtube.com/watch?v=2bvtay8wGYI&t=691s), confidence: stated)
- Tools that let agents search prior trajectories or archives risk teaching the model to cheat by retrieving previous answers without reasoning. ([12:15](https://www.youtube.com/watch?v=2bvtay8wGYI&t=735s), confidence: stated)
- All frontier models lost money on Kelly Bench when given $100K to trade Premier League football matches over a one-year horizon. ([13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s), confidence: stated)
- The AI industry is over-indexed on coding and procedural tasks with only one or two valid solutions, which leaves little room for creativity. ([13:51](https://www.youtube.com/watch?v=2bvtay8wGYI&t=831s), confidence: stated)
- Current benchmarks fail to simulate multi-agent real-world environments where other players have differing goals. ([13:51](https://www.youtube.com/watch?v=2bvtay8wGYI&t=831s), confidence: stated)
- Off-policy staleness of up to about eight steps is acceptable in pipeline RL before quality degrades. ([15:17](https://www.youtube.com/watch?v=2bvtay8wGYI&t=917s), confidence: stated)
- Small, aligned, focused teams can produce frontier-relevant results even in the era of large-scale training. ([1:51](https://www.youtube.com/watch?v=2bvtay8wGYI&t=111s), confidence: implied)
- Solving humanity's largest problems requires patience and a long-horizon mindset rather than treating it purely as an engineering problem. ([9:04](https://www.youtube.com/watch?v=2bvtay8wGYI&t=544s), confidence: stated)

## Concepts

- [benchmark design](../concepts/benchmark-design.md)
- [context compaction](../concepts/context-compaction.md)
- [post-training](../concepts/post-training.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [reward design](../concepts/reward-design.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

