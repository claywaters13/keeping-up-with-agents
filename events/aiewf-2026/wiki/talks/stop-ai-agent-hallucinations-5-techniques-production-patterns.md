---
title: "Stop AI Agent Hallucinations: 5 Techniques + Production Patterns"
type: "talk"
slug: "stop-ai-agent-hallucinations-5-techniques-production-patterns"
org: "AWS"
video_id: "vJukHCIv7Ck"
duration_sec: 3319
word_count: 7194
speakers: ["Elizabeth Fuentes Leone"]
---

# Stop AI Agent Hallucinations: 5 Techniques + Production Patterns

**Speakers:** [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)

**Org:** AWS

**Duration:** 55m 19s

[Watch on YouTube](https://www.youtube.com/watch?v=vJukHCIv7Ck)

## Summary

Elizabeth Fuentes (AWS Developer Advocate) argues that most agent hallucinations and token waste are fixed in code, not in prompts, and walks through five techniques with live before/after demos on a 29-tool travel agent built with Strands: semantic tool selection, GraphRAG, multi-agent validation via Strands' swarm class, neuro-symbolic guardrails implemented as pre-tool-call hooks, and runtime steering with the agent-control library. Each section shows the same model, tools, and prompt producing a wrong answer without the technique and a correct one with it — filtering 29 tool schemas down to three cuts per-call context from ~3,000 tokens to under 300, a Cypher query returns a computed aggregate where vector RAG averages three sampled chunks, and a Python rule blocks a booking the prompt-only agent happily confirms. The core position is that prompt rules are probabilistic suggestions the model can ignore, so hard constraints belong in code that intercepts tool calls, while soft rules should steer the agent to self-correct rather than hard-block the user. She closes by mapping each local pattern onto Amazon Bedrock AgentCore (Gateway, policies, runtime, DynamoDB-backed steering rules) for production. Worth watching if you want concrete, framework-level implementations rather than prompt-engineering advice; the demos are unpolished and live, and the tools are deliberately dummy.

## Key Points

- Every tool schema sent to the model costs roughly 17–200 tokens depending on parameter count, so a 29-tool agent burns about 3,000 tokens of context per call before the user's message is even considered.
- Semantic tool selection embeds tool descriptions in a vector store, retrieves the top-3 matches for each query, and injects only those tools — dropping token usage from thousands to fewer than 300 while also improving accuracy because the model can no longer pick a confusable generic tool.
- With conversation memory, filtering alone is insufficient: tools accumulate across turns, so Strands' tool registry must be cleared and re-populated each invocation (swap-tools) to keep context bounded.
- Vector RAG structurally cannot answer aggregation, counting, or multi-hop questions because it only sees top-k chunks — it estimates from a sample and presents the estimate as fact; a knowledge graph with a model-generated Cypher query returns a computed, verifiable result and honestly returns zero for 'hotels in Antarctica'.
- A single agent validating its own output in the same loop offers no separation of concerns: it rationalizes tool errors into confident success messages, which a three-agent executor/validator/critic swarm catches and surfaces as an explicit failure.
- Rules written in the system prompt or tool description are read as text and are probabilistic suggestions; the same rule implemented as a Strands BeforeToolCallEvent hook in Python cannot be escaped, and the demo shows identical model/tools/prompt producing opposite outcomes.
- Hooks are all-or-nothing and force the user to retry, so soft constraints are better handled by runtime steering (the agent-control library), which nudged the agent to split a 50-guest booking into two rooms instead of failing.
- Steering rules live on a local server registered via API (DynamoDB in the production architecture), so changing a rule takes effect on the next call, whereas changing a hook means editing code and redeploying the whole agent.
- Each local pattern has a managed AWS counterpart — AgentCore Gateway does tool indexing and routing, AgentCore policies enforce rules before tool execution, and AgentCore Runtime hosts any framework with memory and CloudWatch observability.

## Notable Quotes

> "Each one is a code change, not a prompt change."
>
> — [0:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=0s) &middot; *The thesis of the whole talk in one sentence.*

> "Each tool schema is about 17 or 200 tokens, depending of how many parameters it has."
>
> — [4:18](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=258s) &middot; *Concrete per-tool cost number that grounds the token-waste argument.*

> "has 29 tools, that adds up to somewhere around 3,000 tokens per call, just for the tool description."
>
> — [4:18](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=258s) &middot; *Quantifies the fixed context tax of a mid-size tool catalog.*

> "With this filter, the model sees only three most relevant tools. Tokens usage drops from thousands to fewer than 300."
>
> — [5:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=328s) &middot; *The headline result for semantic tool selection.*

> "So, for each question, it is spend around 2,000 tokens."
>
> — [10:49](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=649s) &middot; *Measured baseline from the unfiltered agent.*

> "And when all the 29 tools are visible, the model sometimes pick the wrong one. And with the filtering, those generic tools uh only appears in the query actually match them."
>
> — [16:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=960s) &middot; *Names the accuracy mechanism, not just the cost saving.*

> "So, you register your tools once and it find the right one for each request. It's the same principle but without infrastructure to manage."
>
> — [17:53](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1073s) &middot; *The managed-service tradeoff she offers for the DIY vector index.*

> "Vector search always returns something even when nothing is truly relevant. And the agent only sees the top end chunks of your all data at a time. It cannot aggregate, count, or traverse relationship across all the full data set. So, it estimates."
>
> — [18:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1130s) &middot; *The clearest statement of RAG's structural failure mode for quantitative questions.*

> "So, the graph run that query across all the data. And the model gets back a compute verified results, not a sample."
>
> — [19:54](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1194s) &middot; *States the computed-vs-sampled distinction that motivates GraphRAG.*

> "They are currently no hotel listed in Antarctica. Of course, because it create a cyber query, the cyber query and it receive zero. So, it no, it give me a honest answer."
>
> — [27:04](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1624s) &middot; *Live demo evidence that a structured query yields an honest null where RAG hedges.*

> "Sometimes an agent fails, and nobody find out. It calls a tool, and the tool returns an error, and the agent does not surface that error. It generate a confidence success response instead."
>
> — [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s) &middot; *Defines the silent-failure problem multi-agent validation targets.*

> "The agent acts and validate its own output in the same loop. There's no separation, no second opinion."
>
> — [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s) &middot; *The architectural reason self-validation fails.*

> "And now the same request through the swarm, the executor gets the error, the validator catches, the critic rejects this, and the user never see a fabricator response."
>
> — [34:58](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2098s) &middot; *Describes the concrete handoff chain and its user-visible payoff.*

> "Because prompts probably are suggestions, not constraints. The model process them as a text. Not as a logic it has to execute. It's probabilistic. Only code execute logic."
>
> — [35:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2151s) &middot; *The strongest and most contestable claim in the talk.*

> "A rule in the code the model can not escape it. Neuro-symbolic guardians rules put the rules in the code."
>
> — [36:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2210s) &middot; *States the guarantee that code-level enforcement buys you.*

> "So, what we have what we have here is same model, same tools, same prompt. And the different that outcome because the rules are in Python knowing the prompt."
>
> — [44:27](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2667s) &middot; *Isolates the variable — the A/B result that carries the argument.*

> "So, the hooks are all or nothing. They block everything or approve. But sometimes you want the agent to adjust and keep going."
>
> — [44:27](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2667s) &middot; *Names the limitation of her own previous technique.*

> "Hooks blocks unconditionally. The agent is stop and the user has to retry. For a hard constraint, that is exactly what you want. But sometimes the rule is soft."
>
> — [45:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2728s) &middot; *The hard-vs-soft constraint distinction that separates techniques four and five.*

> "rules are registered on a local server via API. You open the agent without touching the agent code because the agent picks them up immediately."
>
> — [46:29](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2789s) &middot; *The operational, not behavioral, argument for steering over hooks.*

> "So, it's the reservation have been split into two rooms. So, it took that it in self."
>
> — [50:08](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=3008s) &middot; *The self-correction result that distinguishes steering from blocking.*

## Positions

- All five hallucination-reduction techniques are implemented as code changes, not prompt changes. ([0:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=0s), confidence: stated)
- A single tool schema costs roughly 17 to 200 tokens depending on parameter count, and 29 tools add about 3,000 tokens to every call. ([4:18](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=258s), confidence: stated)
- Filtering tools by semantic search to the top three drops per-query tool context from thousands of tokens to under 300. ([5:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=328s), confidence: stated)
- Filtering tools also improves accuracy, because with all 29 tools visible the model sometimes picks the wrong generic tool. ([16:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=960s), confidence: stated)
- In a multi-turn conversation, semantic filtering alone does not bound context; tools must be actively cleared from the registry and re-added each invocation. ([13:15](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=795s), confidence: stated)
- Vector search always returns something even when nothing relevant exists, and cannot aggregate, count, or traverse relationships across a full dataset. ([18:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1130s), confidence: stated)
- For aggregation and counting questions, the LLM computes over the three retrieved chunks and presents that estimate as fact, which breaks once the corpus exceeds top-k. ([24:43](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1483s), confidence: stated)
- A graph query returns a computed, verified result rather than a sample, and also consumes fewer output tokens because the query engine does the arithmetic instead of the model. ([23:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1431s), confidence: stated)
- An agent that acts and validates in the same loop provides no real check — it rationalizes tool errors into confident success responses. ([28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s), confidence: stated)
- A three-agent executor/validator/critic chain catches fabricated confirmations that a single agent reports as success. ([34:58](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2098s), confidence: stated)
- Rules written in prompts are processed as probabilistic text and are suggestions rather than constraints; only code executes logic. ([35:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2151s), confidence: stated)
- With the same model, tools, and prompt, moving rules from the prompt into a Python pre-tool-call hook changes the outcome from wrong to correct. ([44:27](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2667s), confidence: stated)
- Hooks are the wrong tool for soft rules because they block unconditionally and force the user to retry. ([45:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2728s), confidence: stated)
- Use hooks for hard constraints and runtime steering for soft rules. ([51:05](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=3065s), confidence: stated)
- Changing a hook rule requires changing code and redeploying the agent, whereas steering rules registered on a server take effect on the next call with no redeploy. ([46:29](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2789s), confidence: stated)
- Neo4j's knowledge-graph pipeline can build the graph from raw text files using an LLM, removing the need to construct it by hand. ([27:46](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1666s), confidence: stated)
- The entire stack can be run locally for free using a local sentence-transformer for embeddings, files as a vector store, and Ollama for the model. ([7:12](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=432s), confidence: stated)
- AgentCore Gateway provides the same tool-routing and vector-based selection as the hand-built index, without infrastructure to manage. ([17:53](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1073s), confidence: stated)
- Enforcing rules in code before tools run is the same thing AgentCore policies does at the structural level, managed for you in production. ([44:27](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2667s), confidence: stated)
- The demo tools are dummy tools and are not suitable for production use. ([9:22](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=562s), confidence: stated)

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

