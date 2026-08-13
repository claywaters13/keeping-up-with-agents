---
title: "Teaching AI to Find Real Vulnerabilities"
type: "talk"
slug: "teaching-ai-to-find-real-vulnerabilities"
track: "Post-training"
org: "Bugcrowd"
video_id: "ZFxh7sqbUZo"
duration_sec: 1637
word_count: 5001
speakers: ["David Brumley"]
---

# Teaching AI to Find Real Vulnerabilities

**Speakers:** [David Brumley](../speakers/david-brumley.md)

**Org:** Bugcrowd

**Track:** Post-training &nbsp;|&nbsp; **Duration:** 27m 17s

[Watch on YouTube](https://www.youtube.com/watch?v=ZFxh7sqbUZo)

## Summary

David Brumley argues that the way we teach frontier models to hack should mirror how elite human hackers learn: a ladder of tasks graded along two axes, target difficulty (toy programs → CTFs → hardened real-world targets) and exploitation difficulty (find the bug → crash it → arbitrary read/write → full code execution). His central methodological claim is that existing cybersecurity benchmarks are broken because they assume one vulnerability per program: models reward-hack by repeatedly finding the easiest bug, and benchmarks that hand the model a backtrace stunt its reasoning. He proposes the 'audit task' — ask for all vulnerabilities with proofs, uniquify crashes by stack backtrace with a deterministic grader, and score multiplicative precision and recall — which allows open-world grading on real open-source code including bugs you didn't know existed. The talk's payoff is an experiment on 41 verified V8 (Chrome JavaScript engine) vulnerabilities showing that crash-triggering no longer distinguishes models (95% for top models, ~50% even for weaker ones), but full sandbox escape does: 73% and 68% for the two strongest models versus 0% for others, with at least one exploit taking a route human Chrome experts thought impractical. Worth watching if you build RL environments, design evals with deterministic oracles, or care about where autonomous offensive capability actually stands.

## Key Points

- Cybersecurity is an unusually good fit for reinforcement learning because tasks form a natural difficulty ladder and each rung has a deterministic oracle for success.
- Environments should be designed along two axes at once: target difficulty (toy → CTF/synthetic → hardened real targets) and exploitation difficulty (locate bug → trigger crash → arbitrary read/write → arbitrary code execution).
- LLM-as-a-judge fails for security grading because models nearly always claim their hack succeeded; graders must be deterministic and must not be the model under training.
- Benchmarks that assume a single known vulnerability are structurally broken — real programs have many, so the model just re-finds the easiest one and its learning trajectory flattens.
- Hand-curating single-bug environments doesn't work even with enormous budgets: 50% of DARPA's Cyber Grand Challenge hand-curated challenges contained unknown exploitable bugs, and AIxCC saw 18 unintended bugs found.
- Benchmarks that hand the model a backtrace pointing at the vulnerable function remove the need to reason about the program and stunt reasoning capability.
- The proposed 'audit task' flips the prompt to 'find all vulnerabilities,' uniquifies proofs by stack backtrace, and scores multiplicative precision and recall so the model is rewarded for breadth but penalized for spamming non-exploits.
- Asking for a working exploit rather than a bug report is what separates hallucination from real discovery, and separates bug-finding from security — crashing a program isn't hacking it.
- On 41 expert-verified V8 CVEs, crash-triggering saturates across models while full out-of-sandbox arbitrary code execution sharply separates them (73% / 68% versus 0%).
- Evidence against memorization: one model exploited a CVE via a novel path (reversing JavaScript's math.random to forge a pointer) that experts believed impractical, and succeeded on x86 where the team's own expert doubted exploitability.

## Notable Quotes

> "What we found in cybersecurity is that is flawed. The LLMs will always say they were successful hacking."
>
> — [7:31](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=451s) &middot; *Direct rejection of LLM-as-a-judge for this domain, from empirical experience.*

> "you don't want to just ask, "Can you find the vulnerability?" because then you won't be able to distinguish between an LLM hallucination and a real vulnerability"
>
> — [8:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=518s) &middot; *States the core design rule: demand an executable witness, not an assertion.*

> "hacking is really a ladder. And this is what actually matches cybersecurity so well to reinforcement learning."
>
> — [4:50](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=290s) &middot; *The talk's organizing thesis in one line.*

> "there's an assumption that the program only has one vulnerability. I don't know about you, but it's very rare to find a program for which you know there's only one vulnerability."
>
> — [10:00](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=600s) &middot; *Names the flawed assumption underlying current cyber benchmarks.*

> "So the LLM no longer has to reason about the program and that will stunt its reasoning capability."
>
> — [11:17](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=677s) &middot; *Explains why hint-giving benchmarks actively harm capability growth.*

> "This was DARPA spent $60 million designing a contest trying to come up with problems that were well defined and well scoped and they accidentally added additional bugs and 50% of those were ones that were actually exploited."
>
> — [12:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=758s) &middot; *Concrete, expensive proof that curating single-bug environments is infeasible.*

> "This is again a very large DARPA program that ran last year in DEF CON where 18 of the bugs found were unintended ones."
>
> — [13:17](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=797s) &middot; *Second independent data point on unintended vulnerabilities in curated contests.*

> "It also means that there's no LLM as a judge, because let's face it, you can't judge trust the LLM that you're teaching to be a judge."
>
> — [16:19](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=979s) &middot; *Compact statement of the circularity problem in self-graded RL.*

> "don't define the task by a single bed, let the program define the task"
>
> — [16:55](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1015s) &middot; *The speaker's own stated TLDR for benchmark design.*

> "Crashing a program is different than hacking it. You can't go steal someone's IP by simply crashing a program."
>
> — [18:08](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1088s) &middot; *The tradeoff at the heart of the second half: measurable proxy versus real capability.*

> "if you could give Chrome to an LLM and it could come up with a zero-day, you would essentially be able to hack nation-states at that point"
>
> — [19:33](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1173s) &middot; *Frames the stakes of the chosen high-value target.*

> "GPT and GPT 5.5 and Mythos both achieved 95%. They were able to trigger a vulnerability 39 out of 41 times."
>
> — [21:32](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1292s) &middot; *Reports the number showing crash-based benchmarks have saturated.*

> "If you were looking at the old benchmarks, the message would be 50% of the time Kimmy succeeds in hacking, but that's because their definition of hacking was broken. It was simply crashing it."
>
> — [21:32](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1292s) &middot; *Shows how a bad oracle produces a badly misleading headline result.*

> "Mythos was a quite surprising able to do this 73% of the time. So, 30 out of the 41 examples, Mythos was able to do this sort of full control flow hijack."
>
> — [22:12](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1332s) &middot; *The headline capability number for full exploitation on a hardened target.*

> "One of the things that Mythos was able to do was reverse JavaScript's math.random and use that to forge a pointer for a return-oriented program out of the Uber cage exploit."
>
> — [22:53](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1373s) &middot; *Specific technical evidence of novel, non-memorized exploit strategy.*

> "At the end of this, the work was on par with a human elite researcher."
>
> — [23:31](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1411s) &middot; *The strongest capability claim in the talk, stated flatly.*

> "If we're going to publish these benchmarks and we believe in open science, but the models are creating actually interesting exploits for high-value targets. What do you do as far as the open science part of this? We don't have an answer."
>
> — [24:58](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1498s) &middot; *Honest statement of the disclosure dilemma created by capable exploit-generating models.*

> "We're able to do this at scale where some of our the companies that we work with we're providing up to 10,000 reinforcement learning environments per month"
>
> — [25:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1538s) &middot; *Quantifies the scale of RL environment supply going to frontier labs.*

## Positions

- LLM-as-a-judge is unreliable for grading cybersecurity tasks because models consistently claim their hacks succeeded; graders must be deterministic. ([7:31](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=451s), confidence: stated)
- Existing cyber benchmarks such as Cybex, CyberGym, and Bounty Bench are flawed because they assume a single vulnerability per program and only check for a crash. ([10:00](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=600s), confidence: stated)
- Giving the model a backtrace identifying the vulnerable function stunts its reasoning capability because it no longer has to reason about the program. ([11:17](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=677s), confidence: stated)
- Hand-curating benchmark programs with exactly one known vulnerability is infeasible; 50% of DARPA's Cyber Grand Challenge challenges contained unintended exploitable bugs and AIxCC had 18 unintended bugs found. ([12:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=758s), confidence: stated)
- The audit task formulation — asking for all vulnerabilities with proofs and scoring multiplicative precision and recall — prevents both easiest-bug reward hacking and proof spamming. ([15:08](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=908s), confidence: stated)
- Triggering a crash is not hacking; only control-flow hijack or sandbox escape counts as real exploitation. ([18:08](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1088s), confidence: stated)
- Crash-triggering no longer distinguishes frontier models — top models hit 95% (39/41) on V8 CVEs — so it is a saturated metric. ([21:32](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1292s), confidence: stated)
- Full arbitrary code execution does distinguish models: 73% and 68% for the two strongest versus 0% for Gemini and Kimi. ([22:12](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1332s), confidence: stated)
- The top model's V8 exploits are not memorized, evidenced by a novel math.random-reversal route and success on x86 where internal experts believed it infeasible. ([24:21](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1461s), confidence: stated)
- Frontier model exploitation on hardened targets is now on par with an elite human security researcher. ([23:31](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1411s), confidence: stated)
- Publishing full benchmark transcripts becomes ethically fraught once models produce weaponized exploits for high-value targets that were never public. ([24:58](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1498s), confidence: stated)
- Mining genuine zero-days for RL environments is necessary to rule out memorization as an explanation for model performance. ([25:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1538s), confidence: stated)
- Teaching models to hack should follow the same graduated-difficulty write-up-and-practice methodology that produces elite human hackers. ([2:37](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=157s), confidence: stated)
- Building good cybersecurity RL training requires a genuine domain expert to build the oracles and audit transcripts for memorization and reward hacking — it is not otherwise mysterious. ([26:19](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1579s), confidence: stated)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [benchmark contamination](../concepts/benchmark-contamination.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [verifier design](../concepts/verifier-design.md)

