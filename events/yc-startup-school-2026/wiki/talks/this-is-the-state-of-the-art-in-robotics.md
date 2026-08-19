---
title: "This is the State of the Art in Robotics"
type: "talk"
slug: "this-is-the-state-of-the-art-in-robotics"
org: "Physical Intelligence"
video_id: "cRZNwgvcWUg"
duration_sec: 3498
word_count: 11230
speakers: ["Chelsea Finn"]
---

# This is the State of the Art in Robotics

**Speakers:** [Chelsea Finn](../speakers/chelsea-finn.md)

**Org:** Physical Intelligence

**Duration:** 58m 18s

[Watch on YouTube](https://www.youtube.com/watch?v=cRZNwgvcWUg)

## Summary

Chelsea Finn, co-founder of Physical Intelligence, argues that robotics is finally crossing from cool demos into deployable usefulness, and that the gating factor is reliability under long-term autonomy rather than raw task variety. She contrasts physical AI with recommender-style ML, where a human filters the model's mistakes: robots act directly on the world, so they need far lower error rates before they are useful at all. The talk gives a concrete recipe — a robot-efficient RL loop with human interventions to kill dead-end trajectories plus a general-purpose value function, yielding ~2x throughput and >90% espresso success — and adds multi-timescale memory (10s of compressed video plus text summaries) to enable 10-15 minute non-repetitive tasks like cleaning a kitchen. She then presents PI0-7, a single out-of-the-box generalist model that matches or beats task-specific fine-tuned specialists and shows compositional generalization, including folding clothes on a robot platform with zero folding data. Worth watching if you want a grounded, numbers-backed picture of where robot foundation models actually stand and what the remaining bottlenecks (speed, reliability, embodied data) are.

## Key Points

- Physical AI faces a stricter reliability bar than prior deployed ML because the robot acts on the world directly rather than making a recommendation a human can override, so mistakes are not absorbed by a user in the loop.
- Naively porting PPO/GRPO-style RL to robots is infeasible: a million one-minute trajectories would cost roughly 700 robot-days, because each rollout consumes real hardware time rather than data-center compute.
- Two efficiency fixes make robot RL practical — humans teleoperate interventions to rescue or terminate dead-end trajectories, and a single general-purpose value function amortizes value estimation across many tasks instead of rolling out a prompt 10-50 times.
- The RL post-training stage delivered about 2x throughput over SFT and pushed espresso-making past 90% success, validated by running a latte policy continuously for 13 hours.
- Most state-of-the-art robot foundation models have no memory at all; naive video context would cost half a million tokens for 10 seconds, so Physical Intelligence uses compressed short-term video memory plus text summaries for minutes-to-hours horizons, enabling 10-15 minute multi-step kitchen cleaning.
- Finn maps robotics onto the generalist-AI timeline: it sat at the 2014 'pretrain-then-finetune' stage until recently and, with PI0-7, has moved into the GPT/DALL-E era of out-of-the-box models with compositional generalization.
- A single pre-trained PI0-7 model matches or outperforms fine-tuned RL and SFT specialists on the same tasks, and generalizes compositionally to a rarely-seen appliance (air fryer) and to a very different industrial robot arm with no folding data collected on it.
- Ablations show diverse data matters far more than data volume, and metadata prompting flips low-quality data from harmful to helpful — without it, adding the last 20% of low-quality data decreases performance; with it, performance increases.
- Finn expects no single ChatGPT-style moment for robotics because physical distribution is inherently slower, even though model capabilities are approaching that level, and she advises small teams to start from an open-source generalist policy like PI0/PI0-5 and fine-tune immediately.
- There is no substitute for on-robot experience: human video and web data help, but watching Roger Federer does not teach you tennis, and robots likewise need data on their own platform.

## Notable Quotes

> "And in all of these applications, the customer is making a decision based off of the recommendation of the AI model more or less."
>
> — [3:33](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=213s) &middot; *Names the structural difference between every profitable ML deployment so far and physical AI.*

> "Uh and this means that they're going to be far more useful when they're operating fully autonomously. And as a result, this requires us to develop physical AI systems that make far fewer mistakes than the machine learning systems that have been deployed thus far."
>
> — [4:52](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=292s) &middot; *The talk's core thesis about why robotics has a higher reliability bar.*

> "a year ago Whimo passed the uh quarter of a million weekly autonomous rides suggesting that it is really possible to develop a machine learning based system that can uh operate in a trustworthy and autonomous way uh directly in the physical world"
>
> — [4:52](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=292s) &middot; *Cites the one existence proof that the reliability bar is reachable.*

> "what would be even better is if the AI system itself can iterate on the scenario in which you want it to have higher reliability where it on its own automatically seeks out places where it needs more data, where it needs more supervision."
>
> — [7:26](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=446s) &middot; *States the case for automated self-improvement over human data-tuning loops.*

> "This is even shorter than the espresso task that I talked about. This would correspond to 700 robot days um to get high reliability for that task."
>
> — [8:17](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=497s) &middot; *Quantifies why language-model RL scale does not transfer to hardware.*

> "we took this policy and we ran it not just once, but we ran it for 13 hours straight."
>
> — [14:05](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=845s) &middot; *Concrete durability test, not a cherry-picked demo clip.*

> "around a 2x throughput just from the RL stage itself showing how we can get much greater reliability from reinforcement learning"
>
> — [16:06](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=966s) &middot; *The headline number for the RL post-training recipe.*

> "So, you might be surprised to hear that most state-of-the-art foundation models for robotics have no memory or no context."
>
> — [17:23](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1043s) &middot; *A field-level gap most audiences would not guess.*

> "Even if you subsample to one frame per second, you're still going to be passing in 10,000 tokens into your model which at least right now is prohibitively expensive for these models and that's still only 10 seconds of memory."
>
> — [18:48](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1128s) &middot; *Puts a number on why robot memory is a hard engineering problem.*

> "And with this sort of kind of memory at multiple different time scales, we're able to enable robots to do tasks that can operate for 10 or 15 minutes at a time completely autonomously."
>
> — [20:14](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1214s) &middot; *The payoff of the memory architecture, stated as a horizon length.*

> "But if you have to fine-tune a model, you actually aren't getting a general purpose model um for the things that you want it to do because you have to fine-tune it for each individual thing."
>
> — [25:23](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1523s) &middot; *Defines the bar she sets for calling a robot model 'general purpose'.*

> "You don't need pictures of avocado chairs in your data set in order to generate something like this."
>
> — [26:37](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1597s) &middot; *Crisp statement of why compositional generalization buys data efficiency.*

> "we see that the across the board the single PIO like pre-trained PIO7 model matches or outperforms the fine-tuned specialists that were developed with reinforcement learning post-training for those downstream tasks"
>
> — [30:36](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1836s) &middot; *The central empirical claim: generalist beats specialist on the specialist's own task.*

> "if we remove the diver most diverse data um from the model training uh shown in like the grayish color, we find that the performance on held out tasks decreases dramatically"
>
> — [35:06](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2106s) &middot; *Ablation result isolating diversity, not volume, as the driver of generalization.*

> "without metadata prompting when you add lower quality data from 80% data to 100% data the performance actually decreases which is perhaps not too surprising because you're adding lowquality data to your data mixture"
>
> — [35:47](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2147s) &middot; *Reports the tradeoff that metadata conditioning is what makes low-quality data safe to include.*

> "I think that the distribution channel for physical models is going to be slower uh unfortunately because you actually need a physical robot there"
>
> — [39:22](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2362s) &middot; *Her answer to the 'ChatGPT moment for robotics' question, and a caution for founders.*

> "I mean at the very least I actually think that just starting with a generalist policy and then fine-tuning it even like right off the bat uh can be really effective."
>
> — [40:58](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2458s) &middot; *Direct build advice for small teams choosing between bespoke and generalist models.*

> "I think that learning about uncertainty is really useful in the startup environments in being at the frontier of AI because we don't know now like no one knows what the best route is to make these models more and more powerful."
>
> — [44:00](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2640s) &middot; *Her argument for the PhD's transferable value to founders.*

> "Uh and so in general with machine learning, you want train to match test."
>
> — [46:07](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2767s) &middot; *The principle behind her answer on what robotics' internet-scale dataset must look like.*

> "It's useful to watch Roger Federer play tennis. But the um but the actual experience on robot platforms will be a critical component of developing an analogous data set for robotics."
>
> — [47:55](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2875s) &middot; *Takes a side on the human-video-vs-robot-data debate.*

> "Uh, and yeah, I think it's either you need to figure out how to make the data faster or you need to figure out how to be faster than the data."
>
> — [53:45](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=3225s) &middot; *Frames the robot-speed bottleneck as a data problem in one line.*

> "Um the robot essentially had learned this sort of equivariance between his left hand and his right hand so that it could actually transfer uh behaviors from one hand to another."
>
> — [55:21](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=3321s) &middot; *The emergent-capability anecdote she found most surprising all year.*

## Positions

- Physical AI must make far fewer mistakes than deployed recommendation-style ML systems, because the robot acts on the world directly instead of a human making the final decision. ([4:52](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=292s), confidence: stated)
- Scaling language-model RL directly to robots is impractical: one million one-minute trajectories would take roughly 700 robot-days. ([8:17](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=497s), confidence: stated)
- Human teleoperated interventions on dead-end trajectories, plus an amortized general-purpose value function, are the two changes that make RL data-efficient enough for real robots. ([12:39](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=759s), confidence: stated)
- RL post-training roughly doubles throughput over SFT and gets espresso-making above 90% success. ([16:06](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=966s), confidence: stated)
- Most state-of-the-art robotics foundation models have no memory or context and operate only on current sensor observations. ([17:23](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1043s), confidence: stated)
- Memory is not needed for short repetitive motor skills but is critical for multi-step long-horizon tasks. ([18:11](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1091s), confidence: stated)
- A single pre-trained generalist model (PI0-7) matches or outperforms task-specific fine-tuned specialists, including RL post-trained and SFT ones. ([30:36](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=1836s), confidence: stated)
- Data diversity matters more than data volume: removing the most diverse subset collapses held-out task performance while removing a random 20% barely hurts. ([35:06](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2106s), confidence: stated)
- Metadata prompting reverses the sign of low-quality data's effect — without it added low-quality data hurts performance, with it performance improves. ([35:47](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2147s), confidence: stated)
- Robotics will not have a single ChatGPT-style adoption moment because physical distribution is inherently slow, even though comparable capability is a few years out. ([40:23](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2423s), confidence: stated)
- Small teams should start from an open-source generalist policy and fine-tune immediately rather than scaling bespoke per-task models; the main exception is severely compute- or connectivity-constrained deployments. ([41:42](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2502s), confidence: stated)
- Human video and web data cannot substitute for on-robot experience; the robot needs data collected on its own platform. ([47:55](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2875s), confidence: stated)
- Predicting future subgoal images ('imagination') measurably helps but is not clearly a critical component, since the model performs surprisingly well without it. ([51:59](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=3119s), confidence: stated)
- Robot speed is bottlenecked by slow human teleoperation data, so progress requires either faster demonstration data or policies that exceed the speed of their data. ([53:45](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=3225s), confidence: stated)
- The choice of action space (joint targets vs. gripper pose vs. torques) is not currently a bottleneck for robot performance. ([50:33](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=3033s), confidence: stated)
- Open-source robotics models will likely thrive because frontier labs benefit from ecosystem building, though embodied data and hardware costs may make it play out differently than for language models. ([49:29](https://www.youtube.com/watch?v=cRZNwgvcWUg&t=2969s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [capability elicitation](../concepts/capability-elicitation.md)
- [physical ai](../concepts/physical-ai.md)

