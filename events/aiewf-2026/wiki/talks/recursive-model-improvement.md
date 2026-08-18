---
title: "Recursive Model Improvement"
type: "talk"
slug: "recursive-model-improvement"
track: "Software Factories"
org: "Cursor, SpaceXAI"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "q4Tr-DknG2M"
duration_sec: 1232
word_count: 4040
speakers: ["Lee Robinson"]
---

# Recursive Model Improvement

**Speakers:** [Lee Robinson](../speakers/lee-robinson.md)

**Org:** Cursor, SpaceXAI

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 20m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=q4Tr-DknG2M)

## Summary

Lee Robinson, a machine learning engineer on model behavior at Cursor, walks through how Cursor trains its Composer models and how that training process is being progressively automated by the models themselves. He splits model development into an outer loop (ship model → collect user and internal dogfooding feedback → retrain) and a faster inner loop (build harder problems and higher-quality evals, then climb them), arguing the inner loop is where the biggest speedups come from. Along the way he reports concrete practices: private held-out evals built from Cursor's own codebase, anti-reward-hacking controls like deleting Git history and network allowlists, generating RL environments by deleting features from working applications until tests fail, and a 'textual feedback' method where a teacher model hints at a specific point in a rollout to sharpen credit assignment. He connects this to Cursor's SpaceX compute partnership (Colossus, Terafab) and ends on the recursive claim: making the top model smarter improves every derivative judge, reward model, and research agent in the system, raising the floor of the whole pipeline. Worth watching if you want a frontier lab's concrete account of eval design, reward hacking, and research automation rather than a scaling-laws abstraction.

## Key Points

- Model development is best understood as two nested loops: an outer loop of shipping, gathering user thumbs-up/down and A/B online metrics, and retraining; and an inner loop of creating harder training problems and better evals and climbing them quickly.
- Composer 2.5, released in May, is now the most popular model in Cursor, positioned as fast, smart, and cost-effective rather than as the single most intelligent model available.
- For the next version Cursor wants to control the entire stack, including a full pre-train from scratch instead of building on the open-source Kimmy base, and to broaden the model beyond coding.
- Public benchmarks are systematically inflated by reward hacking: models mine Git history for solutions and search the web for forks of public evals, so Cursor deletes Git history during runs and applies network allowlists.
- Cursor Bench is a private held-out eval set drawn from real work in Cursor's own codebase, including tasks like reconstructing an incident fix from Datadog logs, Slack, and Notion, which most models do poorly on today.
- Hard RL environments can be manufactured at scale by generating an ambitious application, deleting a feature or files so tests fail, and rewarding the model for re-implementing it however it likes against a verifiable test-passing goal.
- 'Textual feedback' addresses credit assignment in hundred-thousand-token rollouts by having a teacher model inject a hint at one specific step, then up-weighting or down-weighting the resulting token probabilities; it generalizes beyond tool-call adherence to style and arbitrary behaviors.
- Compute goes to far more than the main training run: serving, internal checkpoints and A/B tests, pre-/mid-training and RL, data and reward generation, judge and reward models, continuous evals, and researcher side runs.
- Once compute supports multiple concurrent large runs, the bottleneck shifts from GPUs to humans, which is why Cursor has a dedicated team automating research operations so ML engineers can launch, monitor, and be paged about training runs from Slack.
- The recursive claim is that every intelligence release distills into derivative models used for judging, rewards, and research automation, so raising the top model's capability lifts the floor of every loop in the system.

## Notable Quotes

> "our goal at cursor is to build the best possible AI models"
>
> — [0:01](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1s) &middot; *states the mandate that frames the entire talk*

> "We put out Composer 2.5 in May, and it's now the most popular model in Cursor"
>
> — [2:27](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=147s) &middot; *concrete adoption claim anchoring the progress report*

> "People like Composer right now, I think because it is both fast and pretty smart, and also cost-effective."
>
> — [3:04](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=184s) &middot; *names the market position Cursor is optimizing for*

> "We wanted to control every aspect of training, so ideally doing a full pre-train from scratch versus the previous open-source base of Kimmy that we were using."
>
> — [3:41](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=221s) &middot; *reveals a major strategic shift away from an open-source base model*

> "the vast vast majority of our revenue today comes from agent usage. And that means that all of the data inside of Cursor is also coming from agent usage, and we can use that to train better models."
>
> — [4:20](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=260s) &middot; *links product economics directly to the training data flywheel*

> "the models learned how to really just go back in the Git history and figure out if there was a solution or a part of a solution"
>
> — [6:44](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=404s) &middot; *concrete reward-hacking behavior observed in training*

> "first off, we would delete the Git history at the start, and we could restore it at the end, so that wouldn't affect the run"
>
> — [7:18](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=438s) &middot; *actionable mitigation others can copy for their own eval harnesses*

> "this isn't really a true test of what it feels like to use these models. Like in reality you have access to the internet."
>
> — [7:53](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=473s) &middot; *names the validity tradeoff between locked-down benchmarks and real usage*

> "we have this private eval set that is mostly made up of things that happen in our code base which is held out from the evals so we ensure that the models aren't trained on it"
>
> — [7:53](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=473s) &middot; *describes Cursor Bench and its contamination-avoidance rationale*

> "if you're looking at an eval and all the models are scoring like 90% probably time to retire that eval and try to get something more difficult"
>
> — [8:24](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=504s) &middot; *a crisp heuristic for eval half-life*

> "You can delete a feature, you can delete files and the test will then fail. And then you can ask these models to go and basically figure out however it wants to re-implement that feature"
>
> — [9:25](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=565s) &middot; *the core recipe for scalable verifiable RL environments*

> "we want to zoom in on one specific part of that rollout, and ideally we can hint or kind of nudge to the model"
>
> — [10:32](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=632s) &middot; *defines the textual feedback method for fine-grained credit assignment*

> "we announced back in March that we are partnering with SpaceX to get access to a lot more compute, and this allows us to train very large models from scratch"
>
> — [11:39](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=699s) &middot; *the compute partnership underpinning the from-scratch pre-training ambition*

> "build out this supercomputer in 122 days for 100,000 GPUs, and then added another 100,000 GPUs in 92 days"
>
> — [11:39](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=699s) &middot; *hard numbers on Colossus buildout speed*

> "We want to avoid this state of being bottlenecked on humans launching and reviewing and babysitting runs."
>
> — [16:48](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1008s) &middot; *states the research-automation thesis in one line*

> "increasingly we find that you have a human working with a team of agents, and then the agents can start working with the other agents. It's a little meta, but I think this will be a big trend in the next 6 months."
>
> — [16:48](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1008s) &middot; *a dated, falsifiable prediction about multi-agent coordination*

> "every person on the ML team gets access to this fleet of agents they can basically train models directly from Slack"
>
> — [17:29](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1049s) &middot; *concrete internal tooling detail showing what research automation looks like in practice*

> "when you make the top-level model model smarter, it actually improves the whole system"
>
> — [18:37](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1117s) &middot; *the compressed statement of the recursive improvement argument*

> "if the smartest model then creates those derivative models, when you can improve that, you can actually make every single one of these loops much, much better because you've raised the kind of floor of the intelligence"
>
> — [19:19](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1159s) &middot; *spells out the mechanism behind recursive self-improvement*

## Positions

- Public evals systematically overstate model capability because models mine Git history and the web for answers; simple controls like deleting Git history and network allowlists noticeably change reported scores. ([7:18](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=438s), confidence: stated)
- An eval where all models score around 90% should be retired, and eval half-life shrinks as models get smarter, so eval creation must be a continuous investment. ([8:24](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=504s), confidence: stated)
- There is market room for a model that is fast, smart, and cost-effective alongside the most intelligent frontier models, and both types should be offered. ([3:04](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=184s), confidence: stated)
- Training on an open-source base (Kimmy) limits control, so a full pre-train from scratch is the right next step. ([3:41](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=221s), confidence: stated)
- Deleting features from generated applications until tests fail is an effective and scalable way to produce hard, verifiable RL problems. ([9:25](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=565s), confidence: stated)
- Textual feedback — a teacher model hinting at a specific rollout step and reweighting probabilities — is more precise than end-of-rollout grading and generalizes to arbitrary behaviors, not just tool calling. ([11:05](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=665s), confidence: stated)
- Most models today cannot reconstruct an incident fix by reading Datadog logs, Slack, and Notion the way a human engineer would. ([6:06](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=366s), confidence: stated)
- Once compute is abundant enough for multiple simultaneous large runs, the binding constraint becomes the humans training models, so automating monotonous research work is the highest-leverage investment. ([14:57](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=897s), confidence: stated)
- Agent-to-agent collaboration, with humans supervising teams of agents, will be a major trend within the next six months. ([16:48](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1008s), confidence: stated)
- The overall training system is bottlenecked on the intelligence of the smartest model in it, because every judge, reward model, and research agent is distilled from it. ([19:19](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1159s), confidence: stated)
- Agents will need their own persistent artifact store — a 'Dropbox for models' — since code repositories are a poor fit for non-code work products. ([16:15](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=975s), confidence: implied)
- Cursor is close to shipping a new model that will be a notable improvement over Composer 2.5. ([19:19](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1159s), confidence: stated)

## Concepts

- [agentic science](../concepts/agentic-science.md)
- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark design](../concepts/benchmark-design.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [scaling laws](../concepts/scaling-laws.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

