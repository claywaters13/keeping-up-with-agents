---
title: "Elizabeth Fuentes Leone"
type: "speaker"
slug: "elizabeth-fuentes-leone"
role: "Developer Advocate"
company: "Amazon Web Services"
talk_count: 1
---

# Elizabeth Fuentes Leone

**Developer Advocate &middot; Amazon Web Services**

Elizabeth Fuentes Leone is a Developer Advocate at AWS, helping developers build production-ready AI applications. With a background spanning data analytics, machine learning, and developer education, she specializes in making complex AI concepts accessible through hands-on tutorials, open-source projects, and live demos.

[LinkedIn](https://www.linkedin.com/in/lizfue/)

## Talks

- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)

## Scheduled Sessions

- **Agent Speedrun: Idea → Code → Deploy → Observe, Fix → Ship** &middot; Day 1 — Workshop Day &middot; 11:05am-12:05pm &middot; Track 9
- **The Infinite Context Window Is a Myth: Context Engineering for AI Agents** &middot; Day 3 — Session Day 2 &middot; 3:20pm-3:40pm &middot; Expo Stage 3 SW

## Concepts

- [agentic loop design](../concepts/agentic-loop-design.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [graph rag](../concepts/graph-rag.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [output guardrails](../concepts/output-guardrails.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [token efficiency](../concepts/token-efficiency.md)
- [tool selection](../concepts/tool-selection.md)

## Quotes

> "Each one is a code change, not a prompt change."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [0:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=0s)

> "Each tool schema is about 17 or 200 tokens, depending of how many parameters it has."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [4:18](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=258s)

> "has 29 tools, that adds up to somewhere around 3,000 tokens per call, just for the tool description."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [4:18](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=258s)

> "With this filter, the model sees only three most relevant tools. Tokens usage drops from thousands to fewer than 300."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [5:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=328s)

> "So, for each question, it is spend around 2,000 tokens."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [10:49](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=649s)

> "And when all the 29 tools are visible, the model sometimes pick the wrong one. And with the filtering, those generic tools uh only appears in the query actually match them."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [16:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=960s)

> "So, you register your tools once and it find the right one for each request. It's the same principle but without infrastructure to manage."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [17:53](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1073s)

> "Vector search always returns something even when nothing is truly relevant. And the agent only sees the top end chunks of your all data at a time. It cannot aggregate, count, or traverse relationship across all the full data set. So, it estimates."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [18:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1130s)

> "So, the graph run that query across all the data. And the model gets back a compute verified results, not a sample."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [19:54](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1194s)

> "They are currently no hotel listed in Antarctica. Of course, because it create a cyber query, the cyber query and it receive zero. So, it no, it give me a honest answer."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [27:04](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1624s)

> "Sometimes an agent fails, and nobody find out. It calls a tool, and the tool returns an error, and the agent does not surface that error. It generate a confidence success response instead."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s)

> "The agent acts and validate its own output in the same loop. There's no separation, no second opinion."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s)

> "And now the same request through the swarm, the executor gets the error, the validator catches, the critic rejects this, and the user never see a fabricator response."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [34:58](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2098s)

> "Because prompts probably are suggestions, not constraints. The model process them as a text. Not as a logic it has to execute. It's probabilistic. Only code execute logic."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [35:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2151s)

> "A rule in the code the model can not escape it. Neuro-symbolic guardians rules put the rules in the code."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [36:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2210s)

> "So, what we have what we have here is same model, same tools, same prompt. And the different that outcome because the rules are in Python knowing the prompt."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [44:27](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2667s)

> "So, the hooks are all or nothing. They block everything or approve. But sometimes you want the agent to adjust and keep going."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [44:27](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2667s)

> "Hooks blocks unconditionally. The agent is stop and the user has to retry. For a hard constraint, that is exactly what you want. But sometimes the rule is soft."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [45:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2728s)

> "rules are registered on a local server via API. You open the agent without touching the agent code because the agent picks them up immediately."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [46:29](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2789s)

> "So, it's the reservation have been split into two rooms. So, it took that it in self."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [50:08](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=3008s)

