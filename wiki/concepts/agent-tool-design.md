---
title: "agent tool design"
type: "concept"
slug: "agent-tool-design"
tier: "core"
maturity: "consolidating"
talk_count: 14
speaker_count: 15
---

# agent tool design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **14** talk(s) by **15** speaker(s)

**Definition:** Designing the tool surface an agent sees — naming, granularity, schemas, and affordances — so the model can use it reliably.

*Also referred to as: tool design, agent-native tool design, tool surface design, tool schema generation, tool surface scoping, typed sdk as constrained action surface, cli versus mcp tooling, tool use*

## State of Practice

The field has moved decisively away from large inventories of purpose-built, tightly-specified function tools and toward small tool surfaces whose members are semantically distinct, plus one general code-execution affordance (bash, a REPL, a CLI, a typed SDK) that lets the model compose its own operations. Anthropic states it deliberately keeps tool cardinality low so Claude can distinguish when to call each, and reports that its file-edit tool now exists mostly for UI rendering rather than capability; a minimal coding agent is demonstrated with exactly two tools (read file, edit file). Tool descriptions themselves have followed the same compression: frontier models degrade when given in-prompt examples and hard 'do not do X' constraints, so the guidance is to supply context instead. The unresolved half of the design problem is the substrate — MCP (stores, apps returning sandboxed-iframe UI, async tasks, registry discovery) versus shell CLIs and code execution, where one talk cites 71 MCP round trips and 8 minutes against 7 CLI turns and under a minute, and Anthropic's own reported figure of up to 75x cheaper token cost. Across security, harness, and product talks, the tool layer — not the model — is where authority is enforced: constrain effects rather than expression, route mutations through one validated door, lock sensitive arguments so the model never sees them, and confirm outcomes through a channel other than the tool's own success report.

## Consensus

### Keep the tool surface small and make every tool functionally distinct from every other, because tool-selection reliability degrades with cardinality and overlap, not just with context length.

Support: **5** talk(s)

> "we try to keep the cardality pretty low and make sure that every tool we add has a distinct function from every other tool so that Claude can very easily distinguish when to call each"
>
> — [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s)

Supporting talks: [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

### Give the agent a general code-execution affordance (bash, REPL, CLI, scripts) so it can compose and batch its own operations, rather than enumerating fine-grained bespoke tool calls for each operation.

Support: **5** talk(s)

> "if you give it arms, like you give it the bash tool and ways to work with the environment, it can build and search its own context. And that's sort of like the insight that led to Claude Code"
>
> — [Field Guide to Fable](../talks/field-guide-to-fable.md), [5:14](https://www.youtube.com/watch?v=9fubhllmsBU&t=314s)

Supporting talks: [Field Guide to Fable](../talks/field-guide-to-fable.md), [Respect The Process](../talks/respect-the-process.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)

### Safety belongs in the tool layer as a constraint on effects — a single validated entry point, locked arguments, scoped permissions — not in instructions asking the model to behave.

Support: **6** talk(s)

> "we frame it as constraining the effects, not the expression"
>
> — [Respect The Process](../talks/respect-the-process.md), [7:24](https://www.youtube.com/watch?v=CLttOU7n6sI&t=444s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)

### A tool's own success report is not evidence the action landed; the harness must confirm the effect through a different channel than the one that performed it.

Support: **3** talk(s)

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s)

Supporting talks: [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Respect The Process](../talks/respect-the-process.md)

## Disagreements

### Should agent capability be exposed as MCP servers/protocol tools, or as CLIs and code the agent executes directly?

| Position A | Position B |
|---|---|
| Skip the protocol layer: hand the agent shell CLIs, a REPL, or code it can write and re-run without a model in the loop. Capability parity is roughly equal (~83% task success either way), but CLIs win on reuse, latency, and token cost, and highly-specified function-call tools stop scaling past a handful of entities as schemas eat context and get hallucinated. Canvas-style MCPs (Figma, PowerPoint) are the wrong shape entirely because they make the agent imitate human interaction.<br>*[The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Respect The Process](../talks/respect-the-process.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)* | MCP is the tool surface worth investing in: apps now return sandboxed-iframe UI, three major clients run self-serve stores that drive real traffic, shipping an MCP server is becoming a purchasing criterion, and the async tasks spec is being fixed rather than abandoned. Standardized protocols (MCP, ACP) are what let a tool be written once and reused across every client, and per-user tool scoping is a protocol-layer fix.<br>*[MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)* |

*Why it matters: It decides whether you spend engineering effort on JSON-RPC servers, schemas, and store submissions, or on scripts and a sandbox — and it sets your per-task cost and latency floor, which matters concretely for anything on a clock (a captcha round, an interactive edit loop).*

### Can an agent be allowed to execute tool calls under runtime guardrails, or must every action be provably safe before it runs?

| Position A | Position B |
|---|---|
| Autonomous execution is acceptable when the blast radius is bounded: a classifier judging the tool call plus conversation context, a typed SDK as the only door with a deterministic validation pass at completion, or arguments locked by partial application so the model cannot change or even see them. Anthropic claims auto mode's residual prompt-injection and exfiltration risk is below that of an average human reviewer and is moving to remove humans from the loop for non-core changes.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Respect The Process](../talks/respect-the-process.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* | Agents are dangerous until proven safe. The agent should not run the agentic loop at all: it should emit a plan reified as a program expression, which is then type-checked, taint-analyzed, and proof-carried before a separate trusted executor runs it. Absent deterministic, fine-grained, time-bounded control over what the agent can do, you have no security posture — 'praying is not a strategy.'<br>*["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* |

*Why it matters: The two camps build incompatible tool layers: one ships tools that execute immediately behind probabilistic judges and typed wrappers, the other ships tools that return inspectable programs and defers all side effects to a separate executor. It also determines whether an LLM-as-judge is an acceptable gate or a category error, since safety may not be formally specifiable at all.*

### Should an agent's tool surface be fixed and curated at build time, or discovered and expanded dynamically at runtime?

| Position A | Position B |
|---|---|
| Fix it and keep it tiny — one or two tools and a single job per agent, distinct functions only. Failures trace directly to too many unrelated tools and concepts sharing context, and a large inventory is the 'carpenter who shows up with plumbing tools' anti-pattern.<br>*[Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* | The client should search a registry at runtime and pull in the right connector when no existing tool fits the assigned task — Claude already does this, and being the connector that gets selected is the distribution opportunity.<br>*[MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* |

*Why it matters: If dynamic discovery wins, tool design becomes a discoverability and description-quality problem competing in a registry; if the curated-minimum view wins, every added tool is a liability you must justify against selection accuracy.*

## Practical Guidance

**Do:**

- Give each agent one or two tools and a single job; specialize rather than building a do-everything inventory
- Audit every new tool against existing ones for functional overlap — if the model could plausibly confuse two tools, merge or rename them
- Start a coding agent from the irreducible pair (read file, edit file) and add tools only for what the surrounding client cannot already do
- Expose capability as a CLI or script sequence the agent can write once and run a thousand times without hitting the model each turn, especially where latency is bounded by an external clock
- Give the agent a REPL or sandbox so it can write loops and summarization scripts over large structured data instead of paging it through bespoke tool calls
- Route all state-mutating calls through a single typed SDK that lints and checks errors, and run a deterministic orchestration/validation script on agent completion rather than trusting the agent's own final state
- Lock sensitive tool arguments via partial function application so the model cannot change them and never learns the argument exists
- Verify an action's effect through a different sensory channel than the one that performed it (check the network or the screen, not the click's return value)
- Emit structured, human-reviewable artifacts from the deterministic execution step so non-engineer users never have to read agent-written code to approve work
- Write tool and system prompts as context rather than negative constraints; drop in-prompt examples for frontier models, which are more imaginative than the examples
- Scope the tool surface to the user who authorized the agent, time-bound permissions to the agent's operating window, and default to least privilege with just-in-time elevation
- Give the agent its own client ID and delegated on-behalf-of access rather than letting it act as the user
- Pick an output medium the model natively generates — HTML and structured text over pixels and coordinates
- Return an alternate text payload alongside any UI widget so clients without widget support don't starve the model of information
- Branch on stop_reason in the agent loop instead of consuming the first response, so token exhaustion doesn't silently produce truncated output
- Make every external boundary resolve to a terminal state: success, failure, timeout, cancel, or max attempts
- Make credentials usable by the agent without being accessible to it

**Avoid:**

- Handing an agent a large tool inventory and expecting reliable selection — this is the carpenter who shows up with plumbing, carpentry, and electrical tools
- Building highly-specified function-call tools per entity type; they work on one graph and break on a few, with the agent hallucinating schema as context fills
- Surfacing every tool the user or application supports regardless of who authorized this specific agent run
- Treating a tool's success response as proof the work landed — agents will report edits they never made
- Giving the agent a general-purpose VM with arbitrary tooling installed; it will route around your instructions using whatever it finds (writing Python when told to write TypeScript)
- Round-tripping the model on every individual interaction in a loop with an external deadline — the challenge expires before the agent finishes
- Hard 'do not do X' constraints in prompts, which collide with later user instructions and confuse frontier models
- Letting subtask output dump into the primary thread's context, and filling a million-token window because it exists
- Designing stateful protocol endpoints (a tasks/list with no filter) that force a scan of a million tasks to find one
- Making agents imitate human interaction patterns — canvas manipulation, screenshot-and-replace loops, pixel coordinates
- Defaulting to plain text output for artifacts that are meant to be used
- Leaving interactive permission prompts enabled when the agent runs in a CI pipeline
- Building your own AI Slackbot — the prompt-injection attack surface is too large

## Notable Outliers

- The dedicated file-edit tool exists for UI rendering reasons, not model capability, and could probably be deleted today for experienced auto-mode users without harm. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s))
- Tools should not return an opaque IO value at all — the model should return a program representing the computation, so compiler techniques (data flow, type checking, taint analysis) can prove it safe before a separate executor runs it. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [16:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1002s))
- Tool design is closer to biology than physics — an empirical, organic discipline rather than one with known rules. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [29:10](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1750s))
- A CLI and an MCP server hit ~83% task success equally, but the same task took MCP 71 round trips and 8 minutes versus 7 turns and under a minute for the CLI, with Anthropic reporting up to 75x cheaper token cost. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s))
- Splitting tool output between what the widget renders and what the model receives lets you build agent tools in privacy-sensitive domains where the data can never reach the LLM provider. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [14:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=892s))
- Amazon's add-to-cart button silently ignores untrusted JavaScript clicks with no error or failure signal, so the tool appears to succeed while nothing happened. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [11:16](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=676s))
- Intermediate languages for agent plans need not be human-readable, since machines generate, consume, and prove them. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s))
- Changing only the harness — model and eval held constant across 106 tasks — moved scores from 52.4% to 76.2%, and the effect is larger for weaker models. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s))

## All Talks

- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [Respect The Process](../talks/respect-the-process.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Erik Meijer](../speakers/erik-meijer.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [James Russo](../speakers/james-russo.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Ravi Madabhushi](../speakers/ravi-madabhushi.md)
- [Shashi](../speakers/shashi.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)

