---
title: "Claude Fable, Claude Tag, and Anthropic's Culture"
type: "talk"
slug: "claude-fable-claude-tag-and-anthropics-culture"
track: "Anthropic"
org: "Anthropic"
video_id: "uU5Gv2h8-9g"
duration_sec: 3090
word_count: 10422
speakers: ["Cat Wu", "Simon Willison", "Thariq Shihipar"]
---

# Claude Fable, Claude Tag, and Anthropic's Culture

**Speakers:** [Cat Wu](../speakers/cat-wu.md), [Simon Willison](../speakers/simon-willison.md), [Thariq Shihipar](../speakers/thariq-shihipar.md)

**Org:** Anthropic

**Track:** Anthropic &nbsp;|&nbsp; **Duration:** 51m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=uU5Gv2h8-9g)

## Summary

A fireside chat between Simon Willison and Anthropic's Cat Wu and Thariq Shihipar about how Claude Code, Claude Tag, and the Fable model generation have changed engineering practice inside Anthropic. The central claims are concrete and checkable: Claude Tag now lands 65% of the product engineering team's PRs, the Claude Code system prompt shrank by 80% for frontier models, and auto mode — hardened internally since January — has been red-teamed hard enough that they claim residual prompt-injection and exfiltration risk is below that of an average human reviewer. Along the way they argue that examples in prompts have become counterproductive for frontier models, that hard 'do not' constraints should be replaced with context, and that rewrites are now cheap enough to be a default rather than a mistake. There's also a practical account of how they removed humans from code review incrementally, using incident postmortems to grow an eval set. Worth watching for anyone building on Claude Code or trying to figure out how team-scale agent workflows and agent security actually work in practice.

## Key Points

- Claude Tag, Anthropic's multiplayer agent living in Slack, currently lands 65% of their product engineering team's PRs, with Claude Code reserved for the most complex interactive work.
- The Claude Code system prompt was cut by roughly 80% in tokens for frontier models (Opus 4.8 and Fable), and Anthropic now ships different system prompts per model because older models still need the long version.
- Few-shot examples now hurt more than they help on frontier models — the model is more creative than the examples supplied — and hard 'do not' constraints are being replaced with softer context because they conflict badly with later user instructions.
- Removing humans from code review was a six-plus-month incremental process: measure where automated review catches 100% of issues, drop human review only there, and add every incident-causing PR to an eval set to prevent regression.
- Anthropic maintains both external and larger internal eval suites so that a new model can be a drop-in replacement — Fable had to be strictly better than Opus 4.8 across the set before rollout.
- Auto mode works by running a Sonnet classifier over each tool/bash call plus conversation context, honoring dynamic per-request permissions and adjudicating escapes from the network sandbox.
- The skill shift for engineers is toward product taste and business sense, since idea-to-implementation has collapsed from six to twelve months down to roughly a week.
- Design and UX taste remains the clearest capability gap — models follow detailed behavioral specs but produce off paddings and an identifiable 'Opus aesthetic' rather than delightful interfaces.
- Claude Tag memory is currently a markdown file per Slack channel, shared across everyone in that channel, with session state able to write back to the main memory.

## Notable Quotes

> "claw tag currently lands 65% of our product PRs"
>
> — [7:57](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=477s) &middot; *The headline number of the talk, and the sharpest available data point on agent-authored code in production.*

> "cloud code is still the best place for your most complex tasks when you're interactively iterating with the agent"
>
> — [7:57](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=477s) &middot; *Names the division of labor between the two products rather than treating them as interchangeable.*

> "That means all of us need to have better taste on what is it that is worth building."
>
> — [4:17](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=257s) &middot; *States the skill-shift thesis compactly.*

> "It's down from six to 12 months to maybe even a week."
>
> — [4:17](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=257s) &middot; *Quantifies the idea-to-shipped compression they're building their org around.*

> "rewrites are now good"
>
> — [4:59](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=299s) &middot; *A direct reversal of longstanding software orthodoxy, stated without hedging.*

> "a codebase is a spec and maybe it's the only copy of the spec that you have"
>
> — [4:59](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=299s) &middot; *The conceptual justification for why rewrites became tractable.*

> "in general we are trying to move to a world where humans don't need to be in the loop"
>
> — [15:19](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=919s) &middot; *The most contestable position in the talk, stated as an explicit organizational goal.*

> "code review is catching a 100% of the issues there. So we actually don't need a human to be manually reviewing those."
>
> — [16:01](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=961s) &middot; *Gives the concrete decision rule for retiring human review on a file-by-file basis.*

> "we run the whole eval set and we make sure that for example Fable is strictly better than Opus 48 and that gives us the confidence to drop it in"
>
> — [16:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1014s) &middot; *Explains what evals are actually for in their workflow: model swap confidence, not scores.*

> "we were over constraining Claude, right? So I think the initial like maybe Opus 4ish kind of models wanted a lot of examples and uh removing examples was extremely helpful because it was just more creative than like uh you know the examples we gave it."
>
> — [21:38](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1298s) &middot; *Directly contradicts standard prompting advice, and Willison flags it as breaking his mental model.*

> "we try and give it more context and fewer like do not do this"
>
> — [22:16](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1336s) &middot; *The actionable rewrite rule that replaced hard constraints.*

> "whenever you give a prompt to the model, you should always think about the ways in which it could be misinterpreted by like a well-intentioned uh other user or human"
>
> — [24:14](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1454s) &middot; *A transferable prompt-review heuristic, not a Claude-specific one.*

> "it's only our uh most frontier models that have this 80% token decrease and the older models actually still have the full system prompt"
>
> — [24:53](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1493s) &middot; *Concrete number plus the tradeoff it imposes on multi-model deployments.*

> "we try to keep the cardality pretty low and make sure that every tool we add has a distinct function from every other tool so that Claude can very easily distinguish when to call each"
>
> — [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s) &middot; *States their actual bar for adding tools, relevant to anyone designing a tool surface.*

> "tool design is more of an art maybe or like a biology"
>
> — [29:10](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1750s) &middot; *Honest admission that this part of the stack resists evaluation.*

> "the reason that we had a dedicated file edit tool was so that we could deterministically know that quad was making a file so we could show people this nice UI"
>
> — [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s) &middot; *Reveals a tool that exists for UI reasons, not model reasons — and that they'd remove it today.*

> "almost every single person uses auto mode. It is the best way to do longunning work in quad code while being safe."
>
> — [31:14](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1874s) &middot; *Anthropic's own recommendation, against Willison's admitted YOLO-mode habit.*

> "for the main categories of risks that we're concerned about like prompt injection, data exfiltration, um the risks are far lower than the average human reviewer"
>
> — [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s) &middot; *The strongest security claim made, with the walk-back from 'every attack mitigated' visible around it.*

> "there's a sonet classifier that is judging the tool and also the context of the conversation, your instruction"
>
> — [32:42](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1962s) &middot; *The only mechanical description of how auto mode actually works.*

> "please you probably shouldn't build your own AI Slackbot, you know, like there's so many attack vectors"
>
> — [35:16](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2116s) &middot; *A blunt build-versus-buy recommendation grounded in the injection surface of feedback channels.*

> "the data dog credentials are only usable by the agent but not accessible by the agent"
>
> — [36:56](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2216s) &middot; *Crisply states the credential-injection pattern Willison calls obviously right.*

> "we don't negotiate against ourselves"
>
> — [45:17](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2717s) &middot; *The cultural principle they nominate as most worth stealing.*

> "I wanted to have better design and UX taste."
>
> — [43:31](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2611s) &middot; *The named capability gap, from the person shipping the product.*

> "the limiting factor actually tends to be that it takes a long time for customers to build really high quality evals. And so I think the tooling is less of the constraint"
>
> — [49:35](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2975s) &middot; *Explains why Anthropic hasn't shipped eval tooling despite demand.*

> "how it works right now in cloud tag is a markdown file per channel"
>
> — [50:49](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=3049s) &middot; *Answers the audience's memory-architecture question with the actual unglamorous implementation.*

## Positions

- Claude Tag lands 65% of Anthropic's product engineering team's PRs. ([7:57](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=477s), confidence: stated)
- The Claude Code system prompt was reduced by 80% in tokens, but only for frontier models; older models still receive the full prompt. ([24:53](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1493s), confidence: stated)
- Including examples in a system prompt now degrades frontier-model output because the model is more creative than the examples provided. ([21:38](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1298s), confidence: stated)
- Hard negative constraints ('do not do X') in system prompts are harmful because they conflict with later user instructions and confuse the model; context should replace them. ([22:16](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1336s), confidence: stated)
- Rewrites, long considered the worst thing a software team could do, are now a good idea provided you have a strong test suite. ([4:59](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=299s), confidence: stated)
- Anthropic has rewritten Bun in Rust and runs Claude Code on it internally, though it has not shipped externally. ([5:52](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=352s), confidence: stated)
- Humans should be removed from the code review loop for non-core changes, and this is achievable through months of eval and infrastructure investment rather than overnight. ([15:19](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=919s), confidence: stated)
- For prompt injection and data exfiltration specifically, auto mode's residual risk is lower than that of an average human reviewer. ([31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s), confidence: stated)
- Anthropic has mitigated essentially every attack found by its commissioned red teams against auto mode, and will publish the evals. ([31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s), confidence: stated)
- Companies should not build their own AI Slackbots because the prompt-injection attack surface is too large. ([35:16](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2116s), confidence: stated)
- A new model is only rolled in after the full eval suite shows it is strictly better than the incumbent. ([16:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1014s), confidence: stated)
- The value of engineering execution skill is falling relative to product taste and business sense, except in infrastructure work where detail still dominates. ([4:17](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=257s), confidence: stated)
- The file edit tool exists for UI rendering reasons rather than model capability, and could probably be removed today for experienced auto-mode users without harm. ([30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s), confidence: stated)
- Eval tooling is not the bottleneck for customers building evals; the skill of writing high-quality evals is. ([49:35](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2975s), confidence: stated)
- Current models lack design and UX taste, defaulting to existing app design best practices rather than inventing the new interaction patterns frontier AI products need. ([44:06](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2646s), confidence: stated)
- Claude Tag's accuracy depends on Slack channels being public, so organizations should default to public channels. ([45:17](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2717s), confidence: stated)
- Keeping tool cardinality low with clearly distinct functions produces better model tool-selection than a large tool surface. ([30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s), confidence: stated)
- The reliability of Claude Code's minimized prompt depends on frontier-level model judgment, which models from a year ago did not have. ([24:53](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1493s), confidence: implied)

## Concepts

- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [token efficiency](../concepts/token-efficiency.md)

