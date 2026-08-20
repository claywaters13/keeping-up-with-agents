---
title: "rlhf and preference training"
type: "concept"
slug: "rlhf-and-preference-training"
tier: "supporting"
maturity: "contested"
talk_count: 8
speaker_count: 9
---

# rlhf and preference training

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **8** talk(s) by **9** speaker(s)

**Definition:** Training on human preference signals — pairwise comparisons, reward models, and the asymmetries they introduce.

*Also referred to as: reinforcement learning from human feedback, rlhf, preference data collection, pairwise preference training, user preference modeling, process reward models, reward model asymmetry, fine-tuning to human distributions*

## State of Practice

Preference training is universal in deployment and simultaneously under indictment. Essentially every shipped LLM is RLHF-tuned, but multiple speakers argued the objective itself — maximize a human rater's approval — is what produces overconfidence, hallucination, and collapse-to-the-mean 'slop', via a mode-dropping asymmetry in the reward model that makes wrong answers look right. The practical consequence is that reward specification, not model capability, is the binding constraint: capability follows measurability, so code and math (decomposable, executable, answer-keyed) advanced while design, video quality, finance, and pharma stalled — not because models are weak there but because nobody has decomposed those domains into gradeable ground truth. Teams that tried to shortcut this with prompted LLM-as-judge report reward hacking and 'vibe' scoring (a judge rating camera work 9.2 on a static shot, praising the physics of hovering ghosts); the working alternatives are pairwise-comparison judges trained on manufactured-bad data, or expert humans kept in the loop as the actual grader. The other live realization is that preference is plural: two designers, two analytics teams, or two survey respondents can hold incompatible-but-correct preferences, and averaging them into one reward signal reliably yields noise rather than a better target. Task and data design now dominate algorithm choice in practice — data beats compute and picking the right task beats data.

## Consensus

### Optimizing a preference proxy reliably teaches the model the proxy's surface (apparent confidence, gloss, 'the vibe') rather than the underlying quality you intended to reward.

Support: **6** talk(s)

> "no matter how wrong the models are, they will look right because of the asymmetry within the reward model in RLHF"
>
> — [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [8:07](https://www.youtube.com/watch?v=cJ0EOzey--o&t=487s)

Supporting talks: [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### What a domain can be trained on is set by what can be decomposed and verified in it, not by model capability — so the bottleneck in subjective domains is the measurement problem.

Support: **4** talk(s)

> "One is that capability follows measurability. So if we can solve the measurability problem or at least part of it, then we can solve a big portion of these domains."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [2:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=163s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### Task design and data curation dominate the choice of training algorithm; the algorithmic machinery is the easy, commoditized part.

Support: **4** talk(s)

> "I actually think that the full stack is that data matters more than compute and doing the right task matters way more than data."
>
> — [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s)

Supporting talks: [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)

### Preference is genuinely multi-valued — averaging labels across unmodeled raters or teams destroys signal instead of resolving it.

Support: **3** talk(s)

> "And that doesn't mean either of those things are wrong or it doesn't mean that the best answer is the average of what two people might like."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [10:45](https://www.youtube.com/watch?v=lCBf9slCanI&t=645s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### A prompted frontier LLM-as-judge is not adequate as the primary evaluator of subjective quality — it is prompt-sensitive, slow, and hackable.

Support: **3** talk(s)

> "The problem with them is that A, they're slow. B, they're only as good as your prompt and multiple people will prompt multiple ways and the same model may respond in a very very different way."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [3:43](https://www.youtube.com/watch?v=b_PmGocP4rc&t=223s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)

## Disagreements

### Is RLHF the foundation to keep building on, or a detour whose objective must be replaced?

| Position A | Position B |
|---|---|
| Preference post-training is what turned base models into products and remains the highest-leverage lever available today — a good base model is not enough, and RLHF fine-tuning on expert preference is the current gold standard for domain edge (accepting that each new base model forces a redo).<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* | RLHF is an unexpected detour that is excellent at pleasing a human in the loop and structurally bad at automation; its overconfidence and hallucination are by construction, so the next paradigm is neither RLHF nor RLVR but optimization for calibrated decision-making with a different API shape.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: It decides whether a team's post-training budget goes into collecting more preference data against the existing objective, or into building calibration/decision-quality targets that the current reward-model tooling does not express.*

### When prompted LLM judges fail on subjective quality, do you replace them with a trained judge or with human experts?

| Position A | Position B |
|---|---|
| Train the judge: collect human pairwise comparisons across randomized axes and distill a committee of experts into one small fast model, or fine-tune on human survey data — alignment then generalizes even to groups never seen in training.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)* | Keep the human as the grader: human judgment is still at a much higher level than any LLM judge for subjective work, models cannot verify themselves where there are no answer keys, and rubrics-as-rewards degenerates into an echo chamber where the AI grades itself into agreement.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* |

*Why it matters: One path amortizes expert cost into a model that can run inside the generation loop; the other treats expert time as a permanent recurring cost and the proprietary dataset it produces as the moat.*

### Should conflicting human preferences be aggregated into one reward signal or preserved as a distribution?

| Position A | Position B |
|---|---|
| Preserve pluralism: attach preferences to per-rater vectors, route requests to the metric definition the specific team or individual uses, and measure distribution shape rather than only correlation to the average — models that match the mean routinely muddle the variation.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)* | Aggregate: on well-posed relative comparisons the grand majority of humans do agree, so a committee of expert annotators can be collapsed into a single distilled scalar judge that scores every user's output.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md)* |

*Why it matters: Aggregation is what makes a single cheap judge (and a single reward model) possible; preserving the distribution requires identity-conditioned routing and per-rater modeling that essentially no production stack has today.*

### Is keeping a human in the loop a temporary scaffold or the correct end state for high-stakes domains?

| Position A | Position B |
|---|---|
| Temporary: guardrails and harness scaffolding should get progressively thinner as model capability improves, and the stack should be redesigned for reliability and full automation rather than for assisting a human.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* | Not yet reachable: in finance and pharma the right model is AI-in-the-loop, where the expert makes every decision and AI only compresses their time, because current models are text statistics rather than world models and cannot do the causal reasoning these decisions require.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* |

*Why it matters: It determines whether preference data is collected to eventually remove the expert or to permanently accelerate them — which changes what you reward (task outcome vs. expert-time saved) and what the product is allowed to decide.*

## Practical Guidance

**Do:**

- Train preference judges on pairwise A-vs-B comparisons rather than absolute 1-10 scores, since humans do not agree on absolute scales but do agree on comparisons.
- Score the specific axes you care about (narrative, pacing, physics, character consistency) explicitly — do not expect them to emerge from a holistic quality score.
- Manufacture 'bad' examples inside your own generation pipeline so the judge learns quality rather than becoming an AI-vs-human detector; match encoding and annotation methodology on both sides of every pair.
- Decompose a subjective target (e.g. 'on brand') into codified elements first, then grade outputs against that decomposed ground truth rather than against the original reference artifact, so novel-but-valid solutions are not penalized.
- Keep per-rater preference vectors instead of one averaged label, and route requests to the metric or definition belonging to the requesting individual or team.
- Treat human annotation as continuous recalibration — recurring sessions sampled across randomized axes — not a one-time labeling pass.
- For synthetic-persona work, elicit free text and map it to the scale via semantic similarity to human-written anchors, and validate with both a correlation metric and a distribution-shape metric against known human ground truth.
- Run error analysis over observability logs before any weight-touching technique; it is the cheapest and highest-ROI improvement available.
- Hire the domain expert before you start iterating, and involve them across query scoping, source curation, decomposition, and final judgment.
- Keep RL tasks inside a difficulty window — too easy or too hard yields no training signal.
- Surface infrastructure errors to the model instead of resetting the environment, so recovery becomes a native learned action.
- Penalize dangerous or unintended intermediate actions, not just the final outcome — a trajectory can reach 'done' having sent a resignation letter to the CEO.
- For long-horizon RL, prefer value models over GRPO (lower variance, trajectory-level with compaction, bootstrapping), and cap off-policy staleness at roughly eight steps in pipeline RL.
- Log every user correction event and feed it back into the agent's context as a first-class loop.
- Distill a judge committee into a small model only when volume justifies it — at one or two videos a day the expensive committee is fine; at thousands per day the unit economics flip.

**Avoid:**

- Averaging preference labels across raters you have not modeled — it washes out into noise, and in LLM personas averaging two orderings collapsed to 50/50.
- Prompting an LLM judge to assess holistic quality or brand adherence directly; it invites reward hacking and 'vibe' scoring.
- Rubrics-as-rewards without human grounding — it becomes an echo chamber where the AI grades itself into agreement.
- Reaching for a bigger model, a longer context window, or more knowledge bases when the real defect is that no source of truth is ranked.
- Adding demographic detail to a persona on the assumption that more detail is more accurate — it can amplify model bias and move results further from reality.
- Re-running synthetic samples on unchanged inputs to boost statistical significance; it sharpens your estimate of the model, not the forecast.
- Outcome-only reward on computer-use trajectories.
- Giving agents tools that search prior trajectories or archives — it teaches retrieval of previous answers instead of reasoning.
- Hand-maintained .md files and skills as the context substrate; enterprise definitions and KPIs change faster than they can be updated.
- Assuming large volumes of cheap labels beat a small volume of expensive high-taste data in subjective domains.
- Using RLHF-trained models for decisions with real stakes to your business, on the assumption that confident output means correct output.

## Notable Outliers

- Expert disagreement is diagnostic, not uniformly bad: disagreement on objective attributes like alignment signals bad data, while disagreement on style or aesthetics is valuable signal about genuine preference variation. ([Ending AI Slop](../talks/ending-ai-slop.md), [14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s))
- There is a hard ceiling on preference-alignment accuracy set by human self-inconsistency — one study measured humans as only about 80% consistent with themselves. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Roughly 100% of LLMs in usage today are RLHF-trained, and Claude Code is not a new era — it is still part of the same RLHF assistance era. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [8:51](https://www.youtube.com/watch?v=cJ0EOzey--o&t=531s))
- The specificity of an expert's language is a measurable proxy for the value of that data point, and tying expert commentary to the exact code component producing a visual materially reduces label noise. ([Ending AI Slop](../talks/ending-ai-slop.md), [12:53](https://www.youtube.com/watch?v=lCBf9slCanI&t=773s))
- Given $100K each to trade Premier League matches over a one-year horizon, every frontier model lost money. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- Sutton's bitter lesson holds in games but not in reality — in reality data beats compute and choosing the right task beats data. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s))
- In creative and design domains the most likely output is by definition not the optimal one, so a reward that pulls toward the mode is producing slop by construction. ([Ending AI Slop](../talks/ending-ai-slop.md), [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s))

## All Talks

- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Speakers

- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)

