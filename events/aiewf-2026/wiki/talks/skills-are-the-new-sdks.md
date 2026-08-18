---
title: "Skills are the New SDKs"
type: "talk"
slug: "skills-are-the-new-sdks"
org: "DataRobot"
video_id: "LC3-P7v3yoI"
duration_sec: 1599
word_count: 4247
speakers: ["Elvin Aghammadzada"]
---

# Skills are the New SDKs

**Speakers:** [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)

**Org:** DataRobot

**Duration:** 26m 39s

[Watch on YouTube](https://www.youtube.com/watch?v=LC3-P7v3yoI)

## Summary

Elvin Aghammadzada (DataRobot) argues that agent skills — progressively-disclosed markdown instruction bundles — are becoming the primary unit of software distribution, displacing SDKs and reducing the role of MCP. The talk's core technical premise is that context is a scarce budget: citing the "context rot" paper, he claims model performance degrades past roughly 25-40% of the context window, and that loading 15 MCP servers can burn 100,000+ tokens in tool definitions before a user says anything. Skills avoid this by exposing only ~100 tokens of front-matter metadata at runtime, loading the ~5K-token body only on activation, and scripts only when executed. He also makes a strategic case that enterprise moats are shifting from "friction" (high switching cost) to "fluency" (how quickly an agent harness can pick up your platform's operational knowledge), adding "teachability" to the enterprise procurement checklist. Worth watching for the moat framing and the concrete skills-vs-MCP decision rule; the closing caveats on prompt injection, lack of isolation, and unverified skill marketplaces are unusually candid.

## Key Points

- Longer context windows do not mean better performance — the speaker cites a "context rot" paper showing degradation begins after about 25% of the window is used, and treats 40% utilization as the boundary between a "smart zone" and a "dumb zone."
- Loading many MCP servers consumes context before the conversation starts: 15 MCP servers can cost over 100,000 tokens per session in tool definitions alone, whereas skills cost roughly 10x less thanks to progressive disclosure.
- Skills work in three levels: front matter (<100 tokens, always in the system prompt, acting like a database index), the markdown body (<5K tokens, loaded only on activation), and scripts (executed or read as examples, with only the output returned to context).
- Skills and MCP solve different problems — use skills when the hard part is reasoning or knowing how to think about a problem; use MCP when you need authentication, isolation, restricted-environment data access, or hosted compute the agent's machine can't provide.
- The enterprise moat is shifting from "friction moats" (defensive, built on switching cost, now eroding because agents can rewrite a million lines from Python to Rust) to "fluency moats" (offensive, built on how good the experience is), with teachability as a new procurement checklist item alongside security, compliance, and SLAs.
- Skills change the build model for domain agents: rather than building a separate supply-chain or manufacturing agent, you keep one good general-purpose agent as the engine and layer domain skills on top.
- Traffic to documentation sites from coding agents rose from 10% to 50% year over year, exposing a mismatch because docs are written for humans who can ask follow-ups while models cannot without a context engine around them.
- LLM-authored skills are a real risk area: recent research he cites found LLM-generated skills hurt performance by using more tokens and more reasoning time, and skill marketplaces still lack verification control the way NPM did a decade ago.
- Skills should be treated as software — versioned, evaluated, and tested — and a skill is only as good as the human who wrote it.

## Notable Quotes

> "there was a paper called context rot, and it proves that after 25% usage of the context window, so for example, for 1 million token, if you used 256K of it, the performance starts to degrade."
>
> — [1:39](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=99s) &middot; *The concrete empirical claim the whole talk's context-budget argument rests on.*

> "Typically this 40% is the smart zone where the LLM can potentially perform well. But if you would you are getting past this 40% context used it typically goes into a zone called dumb zone."
>
> — [10:13](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=613s) &middot; *Names the specific operating threshold he tells builders to design against.*

> "If it's connected to 15 MCP server, I'm pretty sure it's consuming over 100,000 tokens per session just in tool definitions itself."
>
> — [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s) &middot; *The quantified cost of the MCP-heavy approach he's arguing against.*

> "This is an interesting statistics that just from last year to this year, the traffic to documentation websites increased from 10% to 50% that's coming from coding agents."
>
> — [2:47](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=167s) &middot; *A reported number motivating why docs must be rewritten for machine readers.*

> "The challenge here is the fact that docs are written for humans, but models are expected in a different format."
>
> — [2:47](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=167s) &middot; *States the documentation-format mismatch in one line.*

> "Now, skills are creating an entirely different ecosystem where instead of creating a friction mode, they're actually creating fluency mode."
>
> — [5:01](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=301s) &middot; *The talk's central strategic thesis.*

> "Friction modes are typically defensive. So you're trying to make your experience in a sense that someone wouldn't switch. Now, fluency modes are offensive in a sense that you're making the whole experience really nice"
>
> — [5:48](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=348s) &middot; *Draws the defensive/offensive distinction that makes the moat framing checkable.*

> "So now we think that checklist really has a new item, a new guy in the room, which is the teachability."
>
> — [7:26](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=446s) &middot; *Introduces teachability as a procurement criterion — a concrete, contestable prediction.*

> "Both of them are from Anthropic. Both MCP and skills. So, they're not competing for a thing."
>
> — [15:31](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=931s) &middot; *Explicitly rejects the framing that skills replace MCP, before later partially walking it back.*

> "So, it's like an entire complete package of what an agent can become. Essentially, Copilot could be a skill."
>
> — [17:40](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1060s) &middot; *The most expansive claim about what skills subsume, from the co-presenter.*

> "the skills we didn't know quite how powerful were we were until we had 85,000 of them out there"
>
> — [19:02](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1142s) &middot; *Reports ecosystem scale and admits the capability was discovered, not designed.*

> "I don't have access to a GPU on my computer that is sufficient in order to do a significant operations or to do semantic search across 400 terabytes of documents. In those cases, I still need a robust hosted MCP server."
>
> — [19:02](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1142s) &middot; *The clearest statement of where MCP remains necessary.*

> "it turns out that current agents doesn't need a lot of tools. If you go into the way Codex or cloud code is developed, you will see that there's only like a handful of tools that's being run."
>
> — [19:45](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1185s) &middot; *His strongest argument against tool proliferation, grounded in how shipped agents are built.*

> "So, this is the first one, less than 100 tokens."
>
> — [21:09](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1269s) &middot; *Quantifies the front-matter cost that makes progressive disclosure cheap.*

> "The second one, on activation, which is typically less than 5K tokens. The level three is what third one is, which is scripts."
>
> — [21:48](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1308s) &middot; *Completes the three-level token budget of a skill.*

> "So, there is 26 plus platforms that support this, right now. Like cloud code, code X, code pilots, Gemini CLI, and others."
>
> — [22:38](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1358s) &middot; *Ecosystem breadth is the load-bearing evidence for 'skills are the new SDKs'.*

> "they published that actually the LM generated skills hurts the performance of LM in a sense that it uses more tokens."
>
> — [24:09](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1449s) &middot; *A counterintuitive finding that cuts against fully automating skill authoring.*

> "One of the advantages of MCP in the sense that the isolate the process for your MCP and your agent, but everything happens on your laptop, on your agent, on your environment."
>
> — [24:54](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1494s) &middot; *Names the security tradeoff skills make that MCP does not.*

> "And last one here is about the fact that these marketplaces still lack the verification control. Just like how NPM was scary 10 years ago"
>
> — [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s) &middot; *The supply-chain analogy that frames skill marketplaces as immature.*

> "Context is a budget. Context is almost like a limited resource that we need to carefully filter information. Definitely the longer context doesn't mean better."
>
> — [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s) &middot; *The one-line summary of the talk's engineering thesis.*

> "A skill is only as good as the human who wrote it based on our experience."
>
> — [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s) &middot; *A blunt limit on skill autonomy, stated from practice.*

> "skills are software which can take weeks to build so that we should actually start versioning them, evaluating and testing them, and actually writing good skills."
>
> — [26:20](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1580s) &middot; *The actionable closing prescription.*

## Positions

- Model performance begins to degrade after roughly 25% of the context window is used, per the context rot paper. ([1:39](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=99s), confidence: stated)
- Past 40% context utilization an agent enters a 'dumb zone', so builders should keep baseline system prompt plus tool definitions under 40% before any user turn. ([10:13](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=613s), confidence: stated)
- Connecting an agent to 15 MCP servers consumes over 100,000 tokens per session in tool definitions alone. ([13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s), confidence: stated)
- Skills impose roughly 10x less context overhead than the equivalent MCP setup because of progressive disclosure. ([13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s), confidence: stated)
- Enterprise moats are shifting from friction (high switching cost) to fluency (quality of agent experience), because coding agents have made porting codebases cheap. ([5:01](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=301s), confidence: stated)
- Teachability — how fast a new agent harness can absorb a platform's operational knowledge — is becoming a standard enterprise evaluation criterion alongside security, compliance, and SLAs. ([7:26](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=446s), confidence: stated)
- Vendors should build one general-purpose agent engine and deliver domain specialization through skills rather than building separate per-domain agents. ([24:09](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1449s), confidence: stated)
- Skills and MCP are complementary rather than competing, since both come from Anthropic and address different layers. ([15:31](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=931s), confidence: stated)
- A skills folder can replace MCP for most use cases provided you have a good base reasoning model, since production agents like Codex and Claude Code ship with only a handful of tools. ([19:45](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1185s), confidence: stated)
- MCP remains necessary specifically for authentication, process isolation, restricted-environment data access, and compute the agent's local machine cannot provide. ([19:02](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1142s), confidence: stated)
- LLM-generated skills degrade LLM performance by consuming more tokens and more reasoning time than human-written ones. ([24:09](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1449s), confidence: stated)
- Skills executing on the agent's own machine with no isolation is a genuine security weakness relative to MCP's separate server process. ([24:54](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1494s), confidence: stated)
- Skill marketplaces today are as unsafe as NPM was ten years ago because they lack verification controls. ([25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s), confidence: stated)
- The LLM and agent ecosystem has not yet had its 'React moment' — no standard philosophy exists for systematically building long-running agent systems. ([8:45](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=525s), confidence: stated)
- Skills should be treated as software artifacts subject to versioning, evaluation, and testing rather than as disposable prompt files. ([26:20](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1580s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [context engineering](../concepts/context-engineering.md)
- [context rot](../concepts/context-rot.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)
- [token efficiency](../concepts/token-efficiency.md)

