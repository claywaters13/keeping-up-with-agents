---
title: "Open Source Is Dead. Long Live Open Source."
type: "talk"
slug: "open-source-is-dead-long-live-open-source"
track: "Agentic Engineering"
org: "Cline"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "CoEIs6Xm8m8"
duration_sec: 1050
word_count: 2933
speakers: ["Saoud Rizwan"]
---

# Open Source Is Dead. Long Live Open Source.

**Speakers:** [Saoud Rizwan](../speakers/saoud-rizwan.md)

**Org:** Cline

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 17m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=CoEIs6Xm8m8)

## Summary

Cline founder Saoud Rizwan argues that the community half of open source — trusted contributors, third-party PRs, bug bounties — has been killed by AI slop and supply-chain risk, while the permissive-license, build-on-top-of-it half is becoming more important than ever, specifically in the form of open-weights models. He walks through the economics: runaway inference spend at enterprises, labs selling $200 subscriptions that deliver $8,000–$14,000 of API value to lock developers in, and an inevitable price-gouging endgame that he thinks will fail because buyers chase dollar-per-value, not features. He uses the Open Compute Project as the historical analogy: Facebook gave away its data center designs, the supply chain standardized on them, components commoditized, and Facebook's own costs collapsed. His technical claim is that raw model intelligence has plateaued in importance relative to context, tools, and verification scaffolding, illustrated by a head-to-head where GLM beat Opus on cost and code quality on a real Cline bug. He closes with a plea to American labs to release more open-weights models to keep mindshare from moving permanently to Chinese models, and a pitch for Cline's new open-weights subscription plan.

## Key Points

- The social layer of open source — cultivating trusted contributors through PR review — is collapsing under AI-generated slop, with Zig banning AI use outright, curl considering ending its decades-old bug bounty, tldraw auto-closing all external PRs, and GitHub shipping a feature to disable third-party pull requests entirely.
- Supply-chain risk makes depending on third-party code more dangerous than ever: LiteLLM, at ~3.5M downloads a day, was compromised for three hours via stolen PyPI publishing tokens, shipping a credential harvester and RCE backdoor that was caught only because the malware happened to crash Cursor.
- Enterprise inference spend is out of control — a CFO reportedly burned $500M on Claude in one month by not setting usage limits, and Uber exhausted its entire 2026 AI budget in four months at up to $2,000/user/month.
- The labs are subsidizing heavily and losing money — semianalysis found a $200 Claude plan yields ~$8,000 of API usage and a $200 Codex plan ~$14,000 — which Rizwan reads as a deliberate lock-in strategy ahead of eventual price gouging.
- He argues the lock-in strategy will fail because feature depth in a CLI agent doesn't hold customers; developers and businesses will migrate to whatever offers the best value per dollar once models are good enough.
- Raw intelligence lead matters less than the surrounding system: with good skills, rules, verification, and quality gates, a mediocre model can match a smarter one at the cost of more tokens, which are cheap.
- In a real bug fix from the Cline repo, GLM used twice the tokens at half the cost and cleaned up dead code and verified the build, while Opus finished faster but left type errors and broke the production build.
- The Open Compute Project is the template: giving designs away made the whole supply chain standardize, commoditized components, and drove Facebook's own costs down by billions — the industry standardizes on what it can build on, not on what's best.
- Rizwan asks American labs to release more open-weights models (not open research) as a mindshare defense, warning that if foreign open-weights models become the default standard, safety-focused Western labs lose control of the technology's direction.

## Notable Quotes

> "they value contributors more than they do the contributions"
>
> — [2:31](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=151s) &middot; *Names the exact thing AI breaks in open source — the apprenticeship function of code review.*

> "the primary goal for reviewing PRs and things isn't to add new code, but it's to help grow new contributors"
>
> — [2:31](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=151s) &middot; *Restates the Zig position that PR review is talent development, not throughput.*

> "his project is effectively being dodoed by AI generated bug reports"
>
> — [3:13](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=193s) &middot; *Concrete casualty report from curl, a load-bearing piece of internet infrastructure.*

> "it's gone so bad that GitHub added a feature to disable thirdparty pull requests altogether"
>
> — [3:13](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=193s) &middot; *The platform itself shipping an escape hatch is the strongest evidence for the talk's thesis.*

> "It's become more dangerous than ever to depend on third party software"
>
> — [4:01](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=241s) &middot; *States the supply-chain half of the argument in one line.*

> "It gets like three and a half million downloads a day. They were compromised for three hours"
>
> — [4:01](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=241s) &middot; *Blast-radius numbers for the LiteLLM compromise.*

> "the only reason this was even caught as quickly as it was was just pure luck"
>
> — [4:46](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=286s) &middot; *Admits detection was accidental, undercutting confidence in current supply-chain defenses.*

> "they accidentally spent $500 million on Claude in a single month because they didn't set the usage limits on their thousands of employees on their anthropic dashboard"
>
> — [5:28](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=328s) &middot; *The headline number for uncontrolled enterprise inference spend.*

> "a $200 plan for claude would give them about $8,000 worth of API usage"
>
> — [6:13](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=373s) &middot; *Quantifies the subsidy underlying the lock-in argument.*

> "the crazy part is is that the AI labs are losing money too"
>
> — [6:13](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=373s) &middot; *Frames current pricing as temporary and strategically motivated.*

> "every new feature and marketing push from these labs seem to be a new workflow to standardize on to use even more tokens and to be locked in even more"
>
> — [6:54](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=414s) &middot; *A pointed reading of lab product strategy that many would contest.*

> "they know that that's where they can set these sorts of traps and build their moat for the day that these models inevitably become a commodity"
>
> — [7:34](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=454s) &middot; *Explains the API-to-application-layer shift as moat-building against commoditization.*

> "developers and businesses will just jump to whatever offers them the best value for their dollars"
>
> — [7:34](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=454s) &middot; *The core counter-thesis: price beats features once models are good enough.*

> "we'll notice that although they've lagged behind the American closed source competitors, we're at an inflection point where raw intelligence lead doesn't matter as much anymore"
>
> — [8:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=505s) &middot; *The talk's central technical claim about diminishing returns on frontier intelligence.*

> "to get the best output from these models, it's more a problem of what context and tools you give the agent access to and less about its raw intelligence"
>
> — [8:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=505s) &middot; *Locates the leverage in harness design rather than model choice.*

> "even a mediocre model can produce similar results as a more intelligent model it just might take more tokens"
>
> — [8:59](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=539s) &middot; *The tradeoff stated explicitly: intelligence substituted with tokens plus scaffolding.*

> "GLM used twice as many tokens but only cost half as much."
>
> — [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s) &middot; *The measured result behind the open-weights argument.*

> "But GLM cleaned up dead code and verified that the build compiled before completing while Opus didn't. It left a bunch of type errors and it broke the production build."
>
> — [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s) &middot; *A specific, checkable head-to-head quality claim against a frontier model.*

> "defaulted to using GLM and Kimmy in their internal LLM gateway and that this has cut their AI spend by nearly half"
>
> — [10:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=625s) &middot; *External enterprise evidence (Coinbase) that the cost argument is already being acted on.*

> "the industry will adopt and standardize on something that they can build on top of even if it isn't the best thing"
>
> — [12:20](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=740s) &middot; *The distilled lesson of the Open Compute analogy and the talk's thesis in one sentence.*

> "what Facebook found was by giving these designs away they created the market that drove their own costs down and saved them billions of dollars down the road"
>
> — [11:37](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=697s) &middot; *The self-interested case for openness, not the altruistic one.*

> "when dollars are involved, the markets are extremely efficient and the absurd API costs that these closed labs charge just won't be worth it anymore for most knowledge work"
>
> — [13:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=824s) &middot; *The strongest form of the economic prediction, scoped to 'most knowledge work'.*

> "if the foreign models become the standard there won't be a reason to switch back to GPT or claude or Gemini no matter what the marginal improvements are and then we lose control over the development of this technology"
>
> — [14:28](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=868s) &middot; *The geopolitical stakes framing behind his ask of American labs.*

> "So I don't mean we need to open source our research. I think that's what gives us the lead."
>
> — [15:04](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=904s) &middot; *Draws a precise line between open weights and open research, preempting the obvious objection.*

## Positions

- The community and contribution side of open source is no longer worth cultivating, because software is cheap to build and third-party contributions carry supply-chain risk. ([4:01](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=241s), confidence: stated)
- Anthropic and OpenAI moved from API businesses into the application layer specifically to build a moat for when models commoditize. ([7:34](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=454s), confidence: stated)
- The subsidize-then-lock-in strategy will not work; buyers will switch to whichever option gives the best value per dollar regardless of feature parity. ([7:34](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=454s), confidence: stated)
- Open-weights models have reached the point where raw intelligence lead is no longer the decisive factor for most work. ([8:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=505s), confidence: stated)
- Intelligence is better placed in the system and guardrails around the model than in the model itself, reducing reliance on both the model and the developer's judgment. ([8:59](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=539s), confidence: stated)
- GLM outperformed Opus on a real Cline repo bug in cost and code quality, using 2x tokens at half the cost while Opus broke the production build. ([9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s), confidence: stated)
- Inference on a 1-trillion-parameter LLM will cost roughly 90% less by 2030, driven by ~$3T of capex and 100+ GW of new data center capacity. ([12:59](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=779s), confidence: stated)
- Industries standardize on whatever they can build on top of, even when it is not the best available option. ([12:20](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=740s), confidence: stated)
- American labs should release more open-weights models while keeping their research closed, since open weights enable copycats but not leapfrogging. ([15:04](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=904s), confidence: stated)
- If foreign open-weights models become the industry standard, safety investment by Anthropic and OpenAI loses influence over how the technology develops. ([14:28](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=868s), confidence: stated)
- Open source status was necessary for Cline's success, because it let developers inspect the code and trust it while spending heavily on API calls. ([0:53](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=53s), confidence: stated)
- Enterprises will increasingly build their own internal routing and tooling around cheaper models, accepting the loss of the newest features from tools like Claude Code. ([10:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=625s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [model portability](../concepts/model-portability.md)
- [model routing](../concepts/model-routing.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)

