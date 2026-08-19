---
title: "agent tool design"
type: "concept"
slug: "agent-tool-design"
tier: "core"
maturity: "consolidating"
talk_count: 17
speaker_count: 18
---

# agent tool design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **17** talk(s) by **18** speaker(s)

**Definition:** Designing the tool surface an agent sees — naming, granularity, schemas, and affordances — so the model can use it reliably.

*Also referred to as: tool design, agent-native tool design, tool surface design, tool schema generation, tool surface scoping, typed sdk as constrained action surface, cli versus mcp tooling, tool use*

## State of Practice

The field has converged on a small, sharply differentiated tool surface: teams report better tool selection from two to five tools with non-overlapping functions than from large inventories, and Anthropic explicitly designs Claude Code to keep tool cardinality low so the model can tell tools apart. The second convergence is that a general programmable affordance — bash, a CLI, a REPL, a coding agent over structured data — outperforms a catalog of purpose-built function calls, because the model can write loops, slice large datasets, and construct its own context rather than paging it through hand-designed schemas; several teams reported that highly specified function-call tools worked on one dataset and broke on ten. Third, safety has moved out of the prompt and into the tool signature: partial application to lock arguments, a single typed SDK as the only mutation door, per-user tool scoping, and deterministic post-run validation, on the shared premise that the model may request but the system decides. Fourth, tool results are treated as claims, not facts — speakers independently reported agents declaring edits that never landed, and prescribe verification through a channel different from the one that acted. What remains genuinely open is transport (MCP servers and stores versus shell CLIs and code mode, with a reported 71-round-trip versus 7-turn gap on identical tasks) and how much unconstrained execution to grant. Prompt-level tool guidance is also being stripped: for frontier models, examples and 'do not do X' constraints are reported to hurt, and Claude Code's system prompt was cut 80%.

## Consensus

### Keep the tool surface small and make every tool functionally distinct from every other; large or overlapping inventories degrade tool selection.

Support: **5** talk(s)

> "we try to keep the cardality pretty low and make sure that every tool we add has a distinct function from every other tool so that Claude can very easily distinguish when to call each"
>
> — [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s)

Supporting talks: [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

### Give the agent a general programmable environment (bash, CLI, REPL, coding agent) so it can build and curate its own context, instead of adding purpose-built retrieval and inspection tools.

Support: **5** talk(s)

> "if you give it arms, like you give it the bash tool and ways to work with the environment, it can build and search its own context. And that's sort of like the insight that led to Claude Code"
>
> — [Field Guide to Fable](../talks/field-guide-to-fable.md), [5:14](https://www.youtube.com/watch?v=9fubhllmsBU&t=314s)

Supporting talks: [Field Guide to Fable](../talks/field-guide-to-fable.md), [Respect The Process](../talks/respect-the-process.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Enforce limits in the tool layer — locked arguments, a single typed entry point, scoped least-privilege grants — rather than instructing the model not to misbehave.

Support: **5** talk(s)

> "we frame it as constraining the effects, not the expression"
>
> — [Respect The Process](../talks/respect-the-process.md), [7:24](https://www.youtube.com/watch?v=CLttOU7n6sI&t=444s)

Supporting talks: [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Respect The Process](../talks/respect-the-process.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)

### Shape the tool surface around the model's native medium — text, structure, code — rather than around human interaction affordances like canvases, pixels, and GUI imitation.

Support: **4** talk(s)

> "You need to give the AI tools based on how it thinks, not in pixels, in language. Words, tokens, structure, that is its native medium."
>
> — [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [2:57](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=177s)

Supporting talks: [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [Respect The Process](../talks/respect-the-process.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### A tool's own success report is not evidence the effect happened; verify through a different channel than the one that performed the action.

Support: **3** talk(s)

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s)

Supporting talks: [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Respect The Process](../talks/respect-the-process.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

### Tool output should be split into a rendered, human-facing artifact and a separate model-facing payload, instead of one plain-text blob serving both.

Support: **4** talk(s)

> "So, there's two types of output, the ones that are shown in the UI, to put it simply, and the ones that are sent to the model."
>
> — [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [14:15](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=855s)

Supporting talks: [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [Respect The Process](../talks/respect-the-process.md)

## Disagreements

### Should tools be delivered to agents as MCP servers or as shell CLIs and code the agent writes itself?

| Position A | Position B |
|---|---|
| MCP is the right tool surface and is becoming table stakes: servers get listed in the ChatGPT/Claude/Cursor stores, are dynamically discovered from the registry, can return sandboxed UI widgets, and whether a product ships one is now a buying criterion — so invest in fixing MCP's rough edges (tool scoping, async tasks) rather than routing around it.<br>*[MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)* | Give the agent a CLI or let it write code over the data instead: success rates are comparable (~83%), but a CLI sequence runs a thousand times without a model in the loop, took 7 turns versus MCP's 71 round trips on the same task, and is reportedly up to 75x cheaper in tokens.<br>*[The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)* |

*Why it matters: The choice sets your per-task token cost and latency by roughly an order of magnitude, and determines whether your distribution comes from an app store listing or from shipping a binary. It also decides whether protocol-level work (tasks, elicitation, UI extensions) is on your critical path at all.*

### How much execution freedom should the tool surface grant — arbitrary code in a general-purpose environment, or a narrow curated set of capabilities?

| Position A | Position B |
|---|---|
| Hand the agent a real environment and let it express solutions however it wants: a bash tool, a Python REPL over the repo, a coding agent that writes loops and summarization scripts. Highly specified function-call tools do not scale past a handful of datasets, and constraining reasoning throws away the model's main advantage.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Respect The Process](../talks/respect-the-process.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Unconstrained code is the hazard: agents should not be able to read or write arbitrary files by default, sensitive standard-library calls should interrupt, and in the strongest version the agent should never run the loop at all — it emits a plan as a typed expression that a separate trusted executor type-checks and taint-analyzes before anything executes.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)* |

*Why it matters: This determines whether your agent runs in a general VM or behind a whitelist, and whether you can offer any pre-execution safety guarantee at all. Teams that gave agents a general VM reported it routing around instructions by using whatever runtimes it found there.*

### Should risky tool calls be gated by a human at call time, or pre-constrained so no approval prompt is needed?

| Position A | Position B |
|---|---|
| Interactive approval per call is slow and does not belong in automated pipelines; pre-bind the dangerous arguments (partial application so the model never sees the directory parameter), invest in evals and classifiers, and move toward removing the human from the loop entirely for non-core changes.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)* | Authority must be an explicit, scoped, expiring state bound to actor, session, run, tool, and arguments, with least privilege by default and just-in-time elevation — requestability is not authority, and an agent should not act absent a proof that the action is safe.<br>*[Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)* |

*Why it matters: It decides where the audit trail lives and whether autonomy is bought with prior engineering (evals, locked args) or with runtime friction. Get it wrong in the permissive direction and the failure mode is deleted production databases; get it wrong in the restrictive direction and long-running autonomous work is impossible.*

## Practical Guidance

**Do:**

- Start a coding agent at two tools — read file and edit file — and add a tool only when a specific failure demands it.
- Audit every new tool against the existing set: if the model could plausibly confuse it with an existing tool, merge or rename rather than ship it.
- Give the agent bash, a CLI, or a REPL over large structured data so it can write loops and summarization scripts instead of calling a bespoke tool per query.
- Prefer a CLI for any procedure you will run repeatedly — it can be programmed once and replayed with no model in the loop, versus MCP hitting the model every turn.
- Lock non-negotiable tool arguments with partial function application so the LLM cannot change them and does not even see that they exist.
- Route all state-mutating calls through one typed SDK that you can lint and error-check, and run a deterministic validation script on agent completion rather than trusting the agent's final message.
- Verify an action via a different sensory channel than the one that performed it — check the network response or the rendered screen, not the click's return value.
- Split tool output into what the widget renders for the user and what is sent to the model, so privacy-sensitive fields never reach the provider.
- Scope an MCP server's tool listing to the user who authorized the agent, with time-bounded permissions and just-in-time elevation for anything beyond the agent's job.
- Return renderable structure — HTML, or old-text/new-text for the client to diff — rather than plain text or pixel coordinates.
- Replace 'do not do X' instructions and few-shot examples with context for frontier models; Claude Code's system prompt shrank 80% this way, while older models still get the full prompt.
- Branch the agent loop on stop_reason so a token-exhausted, truncated response is not silently consumed as a complete answer.
- Grade the context you feed a tool by relevance the way rendering grades level-of-detail — distant or unfocused objects get a cheap placeholder.

**Avoid:**

- Loading one agent with a large tool inventory — the carpenter who shows up with plumbing, electrical, and carpentry tools and says he can do anything.
- Handing the agent a general-purpose VM with unvetted runtimes: one team saw it write Python because Python was on the box, after being instructed to write TypeScript.
- Trusting the agent's self-report of completed work — agents were observed gaslighting users, claiming edits that never landed.
- Building tools that make the model imitate human hands and eyes — Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops, canvas coordinates.
- Exposing the same full tool surface regardless of which user the agent is acting for.
- Leaving interactive permission prompts enabled when running a coding agent inside a CI pipeline.
- Designing stateful tool protocols with unfiltered list endpoints — MCP tasks V1's tasks/list forced a scan of a million tasks to find one, and its FIFO input_required handling meant only the first in-flight task could be answered.
- Round-tripping the model on every interaction when the target has a clock — a per-click model call loses reCAPTCHA v2 before the challenge finishes.
- Letting subagent output dump in full into the primary thread, crowding out the parent's context.

## Notable Outliers

- Claude Code's dedicated file-edit tool exists so the UI can deterministically show a nice file-writing surface, not because the model needs it — it could probably be removed today for experienced auto-mode users without harm. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s))
- Agents should never execute the agentic loop; they should return a program representing an expression of type IO A, which a trusted executor type-checks and taint-analyzes first — proof-carrying code applied to tool calls, requiring only elementary type-system machinery. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [16:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1002s))
- An identical task took MCP 71 round trips and 8 minutes versus a CLI's seven turns in under a minute, with Anthropic reporting CLI tool use up to 75x cheaper in token cost. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s))
- Replacing purpose-built function-call tools with a coding agent constrained by a typed SDK and a deterministic completion script moved internal eval pass rate from about 43% to 92%. ([Respect The Process](../talks/respect-the-process.md), [13:20](https://www.youtube.com/watch?v=CLttOU7n6sI&t=800s))
- Holding model and evaluation fixed across 106 tasks and changing only the harness produced scores from 52.4% to 76.2% — and the harness matters more for weaker models than stronger ones. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s))
- Tool design is closer to a biology than a physics — empirical and organic rather than governed by known rules. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [29:10](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1750s))

## All Talks

- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [Respect The Process](../talks/respect-the-process.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Erik Meijer](../speakers/erik-meijer.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [James Russo](../speakers/james-russo.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Ravi Madabhushi](../speakers/ravi-madabhushi.md)
- [Shashi](../speakers/shashi.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)

