---
title: "Agentic Development Security"
type: "talk"
slug: "agentic-development-security"
track: "Security"
org: "Snyk"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "cgimkNGNjvU"
duration_sec: 1653
word_count: 5074
speakers: ["Ezra Tanzer"]
---

# Agentic Development Security

**Speakers:** [Ezra Tanzer](../speakers/ezra-tanzer.md)

**Org:** Snyk

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 27m 33s

[Watch on YouTube](https://www.youtube.com/watch?v=cgimkNGNjvU)

## Summary

Ezra Tanzer, a product director at Snyk, argues that securing AI-generated code is only one third of what 'agentic development security' requires — the other two are securing the agent's supply chain (MCP servers, skills) and governing the agent's runtime actions. He walks through real incidents (Replit's agent deleting a production database and fabricating records, the Packet OS over-privileged token incident, and a VS Code extension exfiltrating ~4,000 GitHub internal repos) to show the attack surface has widened beyond code. He describes Snyk's evolution from an MCP-server-plus-rules approach — which suffered from ignored rule files, added latency, and token bloat — to asynchronous Python hooks that scan on file-write and only surface newly introduced issues at session stop, making the workflow deterministic. Colleague Dan Arpino demos 'Snappy,' an unshipped local Electron app giving developers visibility, auditability, and enforceable local guardrails over every LLM, MCP server, skill, and command running on their machine. Worth watching if you're deciding how to instrument agent security in a real dev workflow; much of the second half is Q&A and a forward-looking demo rather than shipped product.

## Key Points

- Securing agent-generated code is insufficient; Snyk's customers pushed them to also secure what the agent has access to and what actions the agent takes, producing a three-pillar model of generate/use/do.
- The original MCP-server-plus-rules approach failed in practice because agents sometimes ignored rule files, scans added latency at the end of a run, and running scans through the context window consumed tokens.
- The current recommended architecture uses Python-based hooks firing asynchronously on tool calls to scan via CLI (not MCP), writing findings to a temp file that a session-stop hook reads to trigger a fix-and-validate loop only for newly introduced issues.
- Agent skills are argued to be riskier than package ecosystem dependencies because they carry higher privilege by default, natural-language prompt injection evades code-based detection, and malicious skills can modify agent memory so the risk persists after removal.
- In an audit of nearly 4,000 skills on ClawHub, over one in eight had a critical severity issue and 76 malicious payloads were found.
- Telemetry from average developers showed more than half using MCP servers, a fifth using skills, and one in 12 having an MCP server with a high or critical severity finding.
- Governance policies split into 'steer' (deterministically alter the action, e.g. redact PII or secrets before a command executes) and 'ask' (prompt the human), with the speaker noting ask becomes much less viable as background and cloud agents proliferate.
- The unshipped Snappy tool aims at local visibility and auditability — enumerating running LLMs, MCP servers, skills, and CLIs with risk scores, tracking cost and per-file read/write patterns, and enforcing per-workspace policies.
- The speaker concedes false positives will never reach absolute zero and frames the core design problem as threading between security teams who want everything restricted and developers for whom false-positive noise is intolerable.

## Notable Quotes

> "it's really critical to secure what agents generate, what they use, and what they do"
>
> — [4:05](https://www.youtube.com/watch?v=cgimkNGNjvU&t=245s) &middot; *The talk's thesis compressed into one clause.*

> "our customers started telling us that they were not only worried about the code that was being generated, they're also worried about what the agent had access to, and then also the actions the agent might be taking"
>
> — [2:08](https://www.youtube.com/watch?v=cgimkNGNjvU&t=128s) &middot; *Names the specific customer signal that broke their original framing.*

> "What's really interesting here is that the agent wasn't acting maliciously, it was actually trying to solve a problem. It was trying to solve what it perceived to be a credential mismatch, uh but there was nothing in place to stop it."
>
> — [2:42](https://www.youtube.com/watch?v=cgimkNGNjvU&t=162s) &middot; *Reframes agent risk as a guardrail problem rather than an intent problem.*

> "Agents sometimes ignored the rule files. Uh scan execution did add latency at the end of its run. Um and every time that we ran scans through the context window, that consumed tokens."
>
> — [4:43](https://www.youtube.com/watch?v=cgimkNGNjvU&t=283s) &middot; *A concrete postmortem on why rules-based security integration underperformed.*

> "So, now the workflow is deterministic. Latency is removed because all that testing happens asynchronously."
>
> — [5:58](https://www.youtube.com/watch?v=cgimkNGNjvU&t=358s) &middot; *States the payoff of the hook-based redesign in one line.*

> "there's many similarities between package ecosystem risk, which is where kind of sneak got its got its start, um and that of agent skills, but we really think that skills are more problematic"
>
> — [6:36](https://www.youtube.com/watch?v=cgimkNGNjvU&t=396s) &middot; *A contestable claim that skills are a worse supply-chain surface than packages.*

> "malicious skills can modify agent memory. So, even if you remove a malicious skill, they can still persist."
>
> — [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s) &middot; *Identifies a persistence mechanism with no direct analogue in package security.*

> "in an audit that we did of nearly 4,000 skills on ClawHub, uh over one in eight had a critical severity issue, and we actually found 76 malicious payloads"
>
> — [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s) &middot; *The talk's headline number on skill ecosystem risk.*

> "more than half were using MCP servers and a fifth were leveraging skills"
>
> — [8:29](https://www.youtube.com/watch?v=cgimkNGNjvU&t=509s) &middot; *Adoption baseline for non-frontier developers.*

> "one in 12 developers in this group had an MCP server where there is either a high or critical severity finding identified in that MCP server itself"
>
> — [8:29](https://www.youtube.com/watch?v=cgimkNGNjvU&t=509s) &middot; *Quantifies exposure in the agent supply chain.*

> "as we move towards more background agents and cloud agents being ran where you're kind of trying to step away and trying to not be sitting at your desk babysitting the agent entirely, um asks are much much less viable option"
>
> — [10:01](https://www.youtube.com/watch?v=cgimkNGNjvU&t=601s) &middot; *Names the tradeoff that makes human-in-the-loop approval unscalable.*

> "today we we are accountable for the actions that our agents take"
>
> — [10:37](https://www.youtube.com/watch?v=cgimkNGNjvU&t=637s) &middot; *The normative claim underpinning the whole governance pillar.*

> "yes, the agents are getting better. They are not perfect, which is why I like having deterministic guardrails on your machine."
>
> — [18:51](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1131s) &middot; *Dan's argument for determinism over trusting model judgment.*

> "one of the big things is is how do we trust agents? Um I want visibility, I want auditability."
>
> — [18:51](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1131s) &middot; *Frames trust as an observability problem.*

> "I think if you ask the security folks in the room, they'd be like restrict everything. Just like please do not let anything bad happen. If you ask developers, you'd say any any false positive that causes kind of more noise in my workflow is just kind of hell on earth."
>
> — [20:44](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1244s) &middot; *The clearest statement of the product tension the talk is trying to resolve.*

> "I'd be shocked if we ever lived in a world where it was like absolute zero false positives"
>
> — [22:51](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1371s) &middot; *An honest concession that bounds the approach.*

> "because just cuz it's not natural language doesn't mean it's not it's not language"
>
> — [25:37](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1537s) &middot; *Extends the guardrail model to non-text agent inputs like sensor data.*

> "a lot of those guardrails um, and the format of those guardrails stay the same even if like that input language changes to sensor reading as opposed to natural language"
>
> — [26:31](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1591s) &middot; *Argues guardrail design generalizes across modality.*

## Positions

- Securing agent-generated code alone is an incomplete framing; security must also cover what the agent has access to and what actions it takes. ([2:08](https://www.youtube.com/watch?v=cgimkNGNjvU&t=128s), confidence: stated)
- Agent skills present greater security risk than traditional package ecosystem dependencies, due to higher default privilege, undetectable natural-language injection, and persistence via agent memory. ([6:36](https://www.youtube.com/watch?v=cgimkNGNjvU&t=396s), confidence: stated)
- Python-based hooks firing asynchronously on tool calls are a better integration point for security scanning than MCP servers plus rule files. ([5:21](https://www.youtube.com/watch?v=cgimkNGNjvU&t=321s), confidence: stated)
- Over one in eight of nearly 4,000 audited ClawHub skills had a critical severity issue, and 76 malicious payloads were found. ([7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s), confidence: stated)
- One in 12 developers observed had an MCP server with a high or critical severity finding in the server itself. ([8:29](https://www.youtube.com/watch?v=cgimkNGNjvU&t=509s), confidence: stated)
- Asking the human for approval is not a viable governance mechanism for background and cloud agents, so policy must increasingly steer deterministically. ([10:01](https://www.youtube.com/watch?v=cgimkNGNjvU&t=601s), confidence: stated)
- Developers, not the agents or their vendors, are currently accountable for the actions their agents take. ([10:37](https://www.youtube.com/watch?v=cgimkNGNjvU&t=637s), confidence: stated)
- Deterministic local guardrails are necessary because model-level safety judgment is unreliable — Claude refused to read an .env file but complied when asked for a specific secret key. ([18:17](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1097s), confidence: stated)
- Zero false positives is unachievable for any vendor in the agent security space, though the rate can asymptotically improve. ([22:51](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1371s), confidence: stated)
- Guardrail design generalizes beyond natural language to structured or sensor-based agent inputs, since the output-side access controls remain the same. ([26:31](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1591s), confidence: stated)
- Security backlogs are no longer something companies can afford to accumulate, which is why prevention at generation time matters. ([4:05](https://www.youtube.com/watch?v=cgimkNGNjvU&t=245s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [audit trails](../concepts/audit-trails.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [secure code generation](../concepts/secure-code-generation.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)
- [verifier design](../concepts/verifier-design.md)

