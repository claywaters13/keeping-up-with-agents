---
title: "tool selection"
type: "concept"
slug: "tool-selection"
tier: "supporting"
maturity: "consolidating"
talk_count: 6
speaker_count: 7
---

# tool selection

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **6** talk(s) by **7** speaker(s)

**Definition:** The model picking the right tool from a catalog, and the accuracy and discovery problems that appear as catalogs grow.

*Also referred to as: tool selection accuracy, semantic tool selection, retrieval-augmented tool selection, dynamic tool discovery, tool search, tool catalog governance, long-horizon tool calling*

## State of Practice

The field now treats tool selection as a retrieval problem rather than a prompting problem: the catalog is a corpus, and the model should only ever see a small working set drawn from it per request. The failure curve is measured, not theoretical — Prosodica's benchmark puts naive full-catalog selection at ~78% accuracy at 10 tools, ~40% at 100, and 13.6% at 741, with 741 schemas costing ~127k tokens per request and pushing time-to-first-token past 5 seconds around 500 tools. Two mechanisms dominate the fix: an out-of-band embedding router that injects the top-K schemas (K=5 as the default starting point), or model-driven lazy discovery where tools are marked deferred and reached through a tool-search call, which is what Codex ships and what GPT-5.4 exposes natively alongside a hard 2%-of-context cap on the skill description block. Practitioners are converging on the claim that this is an accuracy fix, not just a cost fix — with all tools visible the model reaches for the wrong generic tool, an effect attributed to lost-in-the-middle attention over packed schemas. The open edges are who performs the selection (a router outside the model vs. the model searching a registry itself), and whether bad tool use is an architecture defect fixable at inference or a trained-in behavior that requires retraining — Mixedbread argues agents write keyword-stuffed queries because their training and the benchmarks reward that, and fixes it with SFT plus RL on trajectory rewards.

## Consensus

### Selection accuracy degrades as the tool catalog grows, and this is a property of catalog size rather than of individually badly-written tools.

Support: **3** talk(s)

> "At almost 100 tools, the accuracy drops to around 40%. Less than half of the tools that are called are the correct tools. And if it grows beyond that, like say for example, in over here, at 741 tools, the accuracy will be a mere 13.6%."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)

### The catalog may be arbitrarily large, but the set of tool schemas actually in context per request must be kept small — via just-in-time retrieval, semantic filtering, or deferred loading.

Support: **3** talk(s)

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)

### Selection quality is bounded by the text describing each tool — description wording and tool granularity are the control surface, not the selection algorithm.

Support: **3** talk(s)

> "If your descriptions are weak, embeddings will end up being weak. Write descriptions in the words users actually use and include intent, action, and key entities along with it."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [24:44](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1484s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

## Disagreements

### Should the small working set be chosen for the model by an external router, or should the model discover tools itself through a search call?

| Position A | Position B |
|---|---|
| Pre-select outside the model: embed the request, run a vector search over tool descriptions, and inject only the top-K (K≈3-5) schemas before the model ever sees a choice — the model never knows the rest of the catalog exists.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* | Let the model pull: mark tools as deferred so they are absent from context but reachable through a tool-search call the model issues when it needs one, and at the ecosystem level let the client search a live registry for a connector it does not yet have.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* |

*Why it matters: Pre-selection caps latency and tokens deterministically but silently loses any task whose right tool falls outside K, and it requires you to own the routing index; model-driven search preserves recall on multi-tool and unanticipated tasks but adds a round trip and hands selection authority to the model and to whoever ranks the registry.*

### When an agent picks the wrong tool or misuses it, is the defect in the harness architecture or in the model's trained behavior?

| Position A | Position B |
|---|---|
| It is an architecture and code problem: failures that appear as tools are added mean the context is asking the model to solve the wrong problem, and the fixes are code changes — routing, registry clearing between turns, pre-tool-call hooks — not prompt or model changes.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* | It is trained-in behavior: agents write keyword-stuffed 'caveman' queries and emit malformed tool calls because coding-agent training and BM25-favoring benchmarks taught them to, so the fix is retraining on trajectory-level rewards or continual learning against production rollouts.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* |

*Why it matters: One camp's remedy is a focused sprint of retrieval plumbing any team already running RAG can do; the other's requires an RL or distillation pipeline and a data flywheel. Choosing wrong means either endlessly tuning a router around a behavior baked into the weights, or funding training to fix something a 1,000-token context change would have solved.*

## Practical Guidance

**Do:**

- Cap the tool/skill description block as an explicit fraction of the context window — Codex uses 2% and progressively truncates descriptions past it.
- Mark rarely-used tools as deferred so they are reachable through tool search instead of preloaded into every request (supported natively since GPT-5.4).
- Put a semantic router in front of the catalog once you pass ~50 tools in production; below 20 tools, load statically and skip the router.
- Start at K=5 retrieved tools, then run your test set at K=3, 5, and 10 and ship the smallest K that hits your accuracy target.
- In multi-turn conversations, actively clear tools from the registry and re-add them on each invocation — semantic filtering alone does not bound context growth across turns.
- Write tool descriptions in the vocabulary users actually use, including intent, action, and key entities, since the embedding is only as good as the description.
- Expose several differentiated tools (wide semantic search vs. grep) so each maps to one retrieval intent, rather than one generic search tool.
- Instruct the model to write 'one concise sentence describing what it wants to find' instead of 'write a search query,' which breaks the trained BM25 keyword-stuffing reflex.
- Conform tool interfaces to what the model was trained on — apply_patch for edits, ripgrep for search, PowerShell on Windows — and ship the binary with the harness if the host lacks it.
- Give the agent a persistent REPL for computer-use style work so it can script repeated interactions, instead of a one-action-per-call tool API.
- Route aggregation, counting, and relationship-traversal questions to a graph or structured query tool; vector top-k will return a sample and the model will present it as fact.
- Enforce hard constraints in code (a pre-tool-call hook) and use server-registered runtime steering for soft rules that should let the agent adjust and continue.
- Separate execution from validation across agents (executor / validator / critic) so a tool error cannot be rationalized into a confident success response.

**Avoid:**

- Shipping the entire catalog in every request — 741 tools is ~127k tokens per call and, at 100k requests/day, billions of tokens spent only to describe tools.
- Assuming that failures appearing as you add tools are a prompt-quality problem; at scale it is lost-in-the-middle attention over packed schemas.
- Leaving near-duplicate generic tools visible — with all 29 tools in view the model sometimes picks the wrong generic one, so removing wrong tools matters as much as surfacing right ones.
- Defaulting to a large K 'to be safe' — pay for recall you have measured, not recall you hope for.
- Using blocking hooks for soft rules; they are all-or-nothing, stop the agent, and force the user to retry.
- Letting one agent act and validate in the same loop — there is no second opinion and errors surface as success.
- Writing long essay-style goal prompts; the loop only terminates when the model can verify the goal, so goals must be concrete and checkable.
- Treating prompt-stated rules as constraints — they are processed as probabilistic text, and only code executes logic.
- Tuning tool selection against BEIR/NanoBEIR-style entity queries, which structurally favor BM25 and mis-train agent query behavior.

## Notable Outliers

- Tool selection is escaping the process boundary: Claude already searches the MCP registry for a connector when an assigned task has no matching tool, making store placement a distribution channel rather than a packaging detail. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [24:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1492s))
- The retrieval bottleneck, not reasoning, is what caps agent performance — Codex with default tools scores 9 points on BrowseComp Plus against a 93% oracle, and swapping only the search tool closes the gap to three points with the same reasoning model. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s))
- Tool-call formatting itself degrades under training at scale: at 120B parameters with 50-100 tool calls per episode, eval accuracy swings widely, run-to-run variance explodes, and malformed tool calls start appearing. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [12:49](https://www.youtube.com/watch?v=zL1kLftVTlo&t=769s))
- At ~1,000 tokens/sec inference the tool-call loop is network-bound, not inference-bound, which is why the Responses API moved to a persistent WebSocket transmitting only changed items instead of SSE over HTTP. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- Splitting a tool's output between what the widget renders and what the model sees lets MCP apps operate in domains where sending the data to an LLM provider is not acceptable at all. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [14:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=892s))

## All Talks

- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)

## Speakers

- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Ronak Malde](../speakers/ronak-malde.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)

