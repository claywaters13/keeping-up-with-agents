---
title: "What's Next After RLHF?"
type: "talk"
slug: "whats-next-after-rlhf"
track: "Posttraining & Midtraining"
org: "TypeSafe AI"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "cJ0EOzey--o"
duration_sec: 1084
word_count: 3191
speakers: ["Diogo Almeida"]
---

# What's Next After RLHF?

*Program title: What's next after RLHF?*

**Speakers:** [Diogo Almeida](../speakers/diogo-almeida.md)

**Org:** TypeSafe AI

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 18m 04s

[Watch on YouTube](https://www.youtube.com/watch?v=cJ0EOzey--o)

## Summary

Diogo Almeida, a co-author on InstructGPT/RLHF, ChatGPT, and GPT-4, argues that the apparent contradiction in AI today — superhuman benchmark scores alongside failure at mundane business tasks — has one simple explanation: RLHF optimizes for human preference, so today's models are excellent at tasks whose goal is to please a human in the loop and structurally bad at tasks whose goal is to remove the human. He claims Claude Code is not a new era but the tail end of the same assistance era, since it is still RLHF-shaped, and that hallucination and overpromising are features of the reward model's asymmetry rather than bugs to patch. He points to SaaS being essentially unchanged since 2019 — with chatbots bolted on — as evidence that AI is 'assistance native' and that we are automating the writing of software without making software any more expressive. His answer to 'what's next' is real automation via a post-training objective that is neither RLHF nor RLVR but calibrated decision-making, which is what his stealth startup TypeSafe is building. Worth watching for the assistance-vs-automation frame and the insider's critique of what RLHF locked in; light on technical detail, since he repeatedly defers the deeper mechanics.

## Key Points

- The split between 'AI is going insanely well' and 'AI is a bubble generating no value' is best explained by task type: models excel where the objective is to please a human in the loop and fail where the objective is to run unattended.
- RLHF's optimization target — human preference — is why essentially every LLM requires a human in the loop; the humans were literally put into the training loop by design.
- Overpromising and confident hallucination are structural consequences of the reward model's asymmetry, not incidental defects: a model that doesn't know will still err toward whatever scores well with a human rater.
- The speaker claims Claude Code belongs to the assistance era rather than starting a new one, because it is still RLHF-trained; a purely RLVR-trained coding agent would look very different.
- Businesses have converged on a defensive pattern — never use AI for decisions with stakes, and push the costs of failure onto the user rather than the business — which the speaker calls horrible but accurate.
- SaaS software has barely changed since 2019 apart from bolted-on chatbots; AI has made software cheaper to write without making it smarter or more expressive.
- The speaker inverts Sutton's bitter lesson for real-world systems: data matters more than compute, and choosing the right task to optimize matters far more than data.
- Each post-training branch has its own North Star — RLHF targets human preference, RLVR targets pure correctness — and TypeSafe is pursuing a third target, calibrated decision-making, with a different API shape from either.

## Notable Quotes

> "But what makes me somewhat unique here is that I'm one of the few people at OpenAI who actually hates on chat GPT."
>
> — [0:49](https://www.youtube.com/watch?v=cJ0EOzey--o&t=49s) &middot; *Establishes the insider-critic posture the whole talk rests on.*

> "how can we be solving like, you know, unsolved math problems, but still customer service requires like humans in the loop in order to actually like make decisions?"
>
> — [3:38](https://www.youtube.com/watch?v=cJ0EOzey--o&t=218s) &middot; *States the central puzzle the talk sets out to resolve.*

> "And on the other side, all of these tasks that seem way more basic, the goal is to not have remove the human loop."
>
> — [4:08](https://www.youtube.com/watch?v=cJ0EOzey--o&t=248s) &middot; *The core assistance-vs-automation distinction in the speaker's own words.*

> "lesson one for my talk is that today's AI, everything inherited from our LHF, is incredible at the human in the loop stuff, but not for automation tasks."
>
> — [4:42](https://www.youtube.com/watch?v=cJ0EOzey--o&t=282s) &middot; *The talk's first explicit thesis statement.*

> "This is a longer side, but the lesson basically every business has learned is do not use AI for decisions with stakes to your business."
>
> — [5:23](https://www.youtube.com/watch?v=cJ0EOzey--o&t=323s) &middot; *A blunt claim about deployment practice that others might contest.*

> "A common pattern is make sure that all of the costs are to the user and not to your business."
>
> — [5:23](https://www.youtube.com/watch?v=cJ0EOzey--o&t=323s) &middot; *Names an uncomfortable incentive structure in current AI product design.*

> "As far as I can tell by usage, 100% roughly of LLMs are trained with RLHF."
>
> — [5:59](https://www.youtube.com/watch?v=cJ0EOzey--o&t=359s) &middot; *A concrete quantitative claim about the field's uniformity.*

> "And the simple answer is we literally put them in the loop."
>
> — [6:44](https://www.youtube.com/watch?v=cJ0EOzey--o&t=404s) &middot; *The punchline of the diagnosis, from someone who helped build the loop.*

> "by construction, every RLHF model will always have a big difference between human preference and results, even if the results are good, because the main objective you're optimizing for is for human preference."
>
> — [6:44](https://www.youtube.com/watch?v=cJ0EOzey--o&t=404s) &middot; *Frames overpromising as a mathematical guarantee rather than a bug.*

> "If it doesn't know, it will err on the side of doing what it thinks is best for human preference."
>
> — [7:26](https://www.youtube.com/watch?v=cJ0EOzey--o&t=446s) &middot; *Compact mechanism for sycophancy and hallucination.*

> "But what you really want if you want automation is for it to just like not give a about the humans and just do the task correctly in a calibrated way."
>
> — [7:26](https://www.youtube.com/watch?v=cJ0EOzey--o&t=446s) &middot; *States the alternative objective function the speaker is arguing for.*

> "no matter how wrong the models are, they will look right because of the asymmetry within the reward model in RLHF"
>
> — [8:07](https://www.youtube.com/watch?v=cJ0EOzey--o&t=487s) &middot; *Ties the reliability problem to a specific training-time asymmetry.*

> "it's not Claude code because Claude code is still part of that assistance era."
>
> — [8:51](https://www.youtube.com/watch?v=cJ0EOzey--o&t=531s) &middot; *The talk's most contrarian and checkable claim.*

> "kind of like the craziest part of software in my opinion is that all of the SaaS basically has not changed since 2019."
>
> — [10:03](https://www.youtube.com/watch?v=cJ0EOzey--o&t=603s) &middot; *Empirical claim offered as evidence that AI is assistance-native.*

> "And we used to think that software would get a lot smarter, not just cheaper to write, which is kind of the direction we're going down right now."
>
> — [10:39](https://www.youtube.com/watch?v=cJ0EOzey--o&t=639s) &middot; *Names the tradeoff the speaker thinks the industry accepted without noticing.*

> "We're entering the golden age of just-in-time software, but I actually think that this is like a like a double-edged sword."
>
> — [10:39](https://www.youtube.com/watch?v=cJ0EOzey--o&t=639s) &middot; *Directly pushes back on a popular optimistic framing from Garry Tan.*

> "What we're doing is we're just automating the writing of the software. But then it its expressibility is the same."
>
> — [11:55](https://www.youtube.com/watch?v=cJ0EOzey--o&t=715s) &middot; *Crisp statement of what the speaker thinks AI coding tools fail to deliver.*

> "Our core question is what if the AI stack was redesigned for reliability and automation?"
>
> — [12:37](https://www.youtube.com/watch?v=cJ0EOzey--o&t=757s) &middot; *States what TypeSafe is actually building toward.*

> "to me what the like Sutton's bitter lesson is that algorithms matter more than compute. This is true in games, but not true in reality."
>
> — [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s) &middot; *Explicitly disputes a canonical piece of ML orthodoxy.*

> "I actually think that the full stack is that data matters more than compute and doing the right task matters way more than data."
>
> — [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s) &middot; *His replacement hierarchy for what drives progress.*

> "RLHF is optimizing for human preference. RLVR is optimizing for like log error rates of pure correctness, but we are doing a third thing that is optimized for calibrated decision-making"
>
> — [16:08](https://www.youtube.com/watch?v=cJ0EOzey--o&t=968s) &middot; *The clearest technical positioning of the new approach against existing ones.*

## Positions

- The divide between AI's benchmark successes and its real-world failures is explained by whether a task's goal is to please a human in the loop or to remove the human entirely. ([4:08](https://www.youtube.com/watch?v=cJ0EOzey--o&t=248s), confidence: stated)
- Roughly 100% of LLMs in usage today are trained with RLHF. ([5:59](https://www.youtube.com/watch?v=cJ0EOzey--o&t=359s), confidence: stated)
- Claude Code does not represent a new era after ChatGPT; it is part of the same RLHF-driven assistance era. ([8:51](https://www.youtube.com/watch?v=cJ0EOzey--o&t=531s), confidence: stated)
- Overpromising and overconfidence are by design in RLHF models, not correctable defects, because the reward model rewards apparent confidence. ([6:44](https://www.youtube.com/watch?v=cJ0EOzey--o&t=404s), confidence: stated)
- Hallucination is intrinsic to optimizing for human preference, via a mode-dropping asymmetry in the reward model analogous to GANs. ([14:35](https://www.youtube.com/watch?v=cJ0EOzey--o&t=875s), confidence: stated)
- Pre-training is not the problem; pre-trained models are already highly intelligent and the failure is in how that intelligence is unearthed. ([13:54](https://www.youtube.com/watch?v=cJ0EOzey--o&t=834s), confidence: stated)
- SaaS software has not meaningfully changed since 2019 despite the LLM era, apart from chatbots being latched on. ([10:03](https://www.youtube.com/watch?v=cJ0EOzey--o&t=603s), confidence: stated)
- AI is currently automating the writing of software without increasing software's expressiveness, which is the wrong direction. ([11:55](https://www.youtube.com/watch?v=cJ0EOzey--o&t=715s), confidence: stated)
- Sutton's bitter lesson — that algorithms matter more than compute — holds in games but not in reality; data beats compute and task choice beats data. ([15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s), confidence: stated)
- The next post-training paradigm is neither RLHF nor RLVR but optimization for calibrated decision-making, with a different API shape from both. ([17:04](https://www.youtube.com/watch?v=cJ0EOzey--o&t=1024s), confidence: stated)
- The amount of real work currently automated by LLMs is a rounding error despite their intelligence. ([12:37](https://www.youtube.com/watch?v=cJ0EOzey--o&t=757s), confidence: stated)
- RLHF was a weird, unexpected detour rather than the main path for the field. ([11:55](https://www.youtube.com/watch?v=cJ0EOzey--o&t=715s), confidence: implied)
- The original scaling laws were incorrect. ([13:22](https://www.youtube.com/watch?v=cJ0EOzey--o&t=802s), confidence: stated)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [generative ui](../concepts/generative-ui.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [post-training](../concepts/post-training.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [scaling laws](../concepts/scaling-laws.md)

