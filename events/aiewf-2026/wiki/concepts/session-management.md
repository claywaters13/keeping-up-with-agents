---
title: "session management"
type: "concept"
slug: "session-management"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 14
---

# session management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** The lifecycle of an agent session as a portable object — persisting, resuming, forking, and sharing it across clients or users.

*Also referred to as: session persistence and resumption, agent session portability, session forking, trajectory forking, shared agent sessions across interfaces, context portability, multiplayer agent sessions*

## State of Practice

The field has converged on treating an agent session as a durable object that outlives the process, machine, and client that created it — the working definition several speakers arrived at independently is that the append-only event log (user inputs, model outputs, tool calls, results, permission decisions, failures) *is* the agent, and the running loop is disposable. Practically this means: model APIs are stateless so every turn is a replay of the log; the context window is a projection of the session rather than the session itself; and resumption, forking, and hand-off to another human or another vendor's agent are all log operations rather than process operations. Protocol work is standardizing the surface — ACP exposes newSession/loadSession/session-update notifications over JSON-RPC with ~40 client implementations, and making an existing agent compatible is roughly four functions. Production pressure is pushing execution off laptops into sandboxes with least-privilege credentials in vaults, and pushing the agent loop out of the tool-execution container (Anthropic measured 60% faster time-to-first-token at P50, >90% at P95, from that split alone). The live arguments are not about whether sessions should be durable but about who holds the log, whether compaction is good enough to make long-lived threads the primary abstraction, and whether the session or an external document is the real unit of state.

## Consensus

### Session state must be a durable artifact external to the agent process — not one process per agent pinned to a machine — so that a crashed worker, dead sandbox, or restarted host is an execution detail rather than a lost agent.

Support: **6** talk(s)

> "When the log is the state, you flip that model. One process can now advance thousands of agents."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### The same session, with identical state, should be attachable from any client or interface — Slack, editor, mobile, GitHub, or a different vendor's agent — rather than being bound to the tool that started it.

Support: **3** talk(s)

> "So, what we really wanted was to be able to work with the same session from every relevant interface."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [3:28](https://www.youtube.com/watch?v=OL7kfezynJM&t=208s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)

### Sessions are a multiplayer unit: handing a live session to another engineer — with full materialized state and zero setup — is more valuable than handing over the artifact the session produced.

Support: **3** talk(s)

> "I resume their session on my machine, I get the exact state, fully functional, zero setup, and then I just talk to my agent about the decisions we made"
>
> — [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s)

Supporting talks: [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

### Session transcripts are the raw material for memory and self-improvement, not disposable exhaust — a batch process should distill them back into durable structured context that improves later sessions.

Support: **5** talk(s)

> "you're going to stop treating the log as this exhaust from the system, and you're going to treat it as the system itself"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [14:10](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=850s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)

### Sessions need branch/fork/rollback semantics, not just linear resume — you should be able to re-enter a run at an arbitrary earlier point and continue along a different path.

Support: **3** talk(s)

> "Every run that we record can be forked through any moment in its trajectory to give you the state of the computer at that moment."
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)

## Disagreements

### Who should own and host the session log — the managed agent provider, or the team running the agent?

| Position A | Position B |
|---|---|
| Session management is undifferentiated infrastructure alongside hosting, sandboxing, credentials, and observability; teams should take it from the harness vendor and own only system prompts, skills, tools, and domain context.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* | Log lock-in is the deepest and most durable form of vendor lock-in — deeper than model, API, or tool lock-in, because a log cannot be wrapped or adapted away. Teams should self-host their logs, and the continuity layer should sit above the agent as an agent-agnostic meta-harness or an external context layer, precisely because agent tooling churns roughly annually.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: This decides whether switching models or agent vendors is an adapter-and-schema migration or a total loss of accumulated organizational context; one talk described migrating across five agent stacks in twelve months and losing trapped context at every hop.*

### Is compaction good enough to make one long-lived thread the primary session abstraction?

| Position A | Position B |
|---|---|
| Compaction now works well enough that the old advice to start a fresh thread after a long conversation is obsolete; threads five weeks old with hundreds of subagents still behave correctly, and scheduled automation should post heartbeats back into the existing thread rather than spawning new ones.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Compaction is inherently lossy and throws information away; it should be treated as a best-effort fork resumed as a new log with the raw log retained. Related: state should be extracted as atomic facts or pushed into durable docs rather than accumulated in a thread and squeezed.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: If compaction is trustworthy, the thread is the session and persistence is a UX problem; if it is lossy, every product needs raw-log retention plus a separate distillation path, and 'resume' has to mean replay-from-log rather than reload-the-summary.*

### Is the session itself the durable unit of state, or should the session be treated as stateless action against an external document?

| Position A | Position B |
|---|---|
| The session is the state — persist and resume the full session object (intent, repos, PRs, traces, permission state) so a human or another agent can continue it mid-stream; pooling sessions across an org gives an agent more context than any individual has.<br>*[A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | Separate agent-as-action from doc-as-state: decisions go into a durable shared document up front, which makes agents effectively stateless and removes the need to resume anything. Per-agent memory is an anti-pattern that causes context sprawl and prevents a single version of truth; extracting decisions ahead of time beats having an LLM summarize sessions afterward, which risks picking the wrong things.<br>*[Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* |

*Why it matters: It determines where engineering effort goes: durable log infrastructure with fork/resume semantics, versus a versioned, reviewed context store that agents read from and that nobody needs to resume. The second camp argues the first reproduces per-agent memory silos at session granularity.*

## Practical Guidance

**Do:**

- Persist an append-only event log of every user input, model output, tool call, tool result, permission decision, and failure; treat the context window, UI, debug view, and audit trail as projections of it.
- Split the agent loop from tool execution into separate containers so first-token reasoning does not block on sandbox setup — measured at 60% faster TTFT at P50 and >90% at P95.
- Implement newSession and loadSession over a client-agent protocol (ACP is JSON-RPC over stdio, ~4 functions, ~15 minutes to retrofit an existing agent) so any client can attach to a session.
- Read files through the client's proxied filesystem rather than native fs APIs, since the client may hold unsaved buffer state the agent must see.
- Keep the raw log when compacting and resume the compacted summary as a new forked log rather than overwriting history.
- Materialize enough state — intent, repos, PRs, traces — that another person can resume the session on their own machine with zero setup.
- Store credentials in a vault decrypted only at tool-execution time so security tokens never enter the session transcript or model context.
- Run sessions in isolated cloud sandboxes with least-privilege access instead of on developer laptops holding production tokens.
- Feed session transcripts plus current memory state through a periodic batch distillation process that edits memory for subsequent sessions.
- Give users version history, an always-available prominent stop control, and visible control over what the session remembers and forgets.
- Route scheduled automation and heartbeats back into an existing thread rather than creating a new thread per run.
- Benchmark agents and harnesses on your own repository rather than trusting SWE-bench-style public results when choosing what backs your sessions.

**Avoid:**

- Assuming a pending permission prompt survives process death — Claude Code drops it on resume and leaves the agent paused, which is unacceptable in production.
- Relying on fire-and-forget JSONL writes to local disk (Claude Code, Codex SDK mode) or on SQLite state with known corruption issues as your only session persistence.
- One process per agent with sticky sessions, which forces state migration and coordination overhead the log-centric design removes entirely.
- Conflating the context window with the session — traditional harnesses make them one and the same, which breaks recovery and observability.
- Giving each agent its own memory system: it produces context sprawl, divergent learning, and no single version of truth, and makes failures untraceable between model, agent, and context.
- Leaving your only copy of the session log on a provider's infrastructure; if a provider owns your log, the provider owns your agent.
- Putting the agent loop and tool execution in the same container, which couples their failure domains.
- Carrying forward harness workarounds written for an older model's limitations — they become pure overhead, adding latency and invalidating the cache incorrectly.
- Treating chat as durable state: it is isolated, ephemeral, and encourages accepting the agent's recommendation without thinking; plan mode is still just a rich chat message.
- Assuming a Slack bot solves portability — it moves the agent from trapped on a laptop to trapped in Slack.
- Shipping widget or UI-only session output without alternate model-visible content, which starves the model on clients that do not render it.

## Notable Outliers

- Once the log is the agent, different branches of the same session can run on different providers — one on Claude, one on GPT, one on an open-weight model — because provider migration is only an adapter and schema problem, not an identity problem. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [8:04](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=484s))
- Memory should be portable across agent products, so a session begun in Claude can be continued in Codex mid-stream. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s))
- Compaction is now good enough that threads five weeks old containing ~400 subagents still know what they need to do. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [3:29](https://www.youtube.com/watch?v=il1c1a2FufU&t=209s))
- Once state lives in the doc and agents are stateless, 'declaring agent bankruptcy' stops being a thing you ever do. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [16:38](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=998s))
- Session permissions in a shared/group agent should be enforced by per-user LoRA adapters over a shared memory layer rather than by access-control code — whether something is private depends on the room, not the data. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s))
- Pooling sessions across every developer in an organization gives the agent more context than any single developer possesses, because it crosses developer boundaries. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Speakers

- [Arjun Singh](../speakers/arjun-singh.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Victor Savkin](../speakers/victor-savkin.md)

