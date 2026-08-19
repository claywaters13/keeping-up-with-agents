---
title: "session management"
type: "concept"
slug: "session-management"
tier: "supporting"
maturity: "frontier"
talk_count: 13
speaker_count: 15
---

# session management

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Supporting concept* &middot; discussed across **13** talk(s) by **15** speaker(s)

**Definition:** The lifecycle of an agent session as a portable object — persisting, resuming, forking, and sharing it across clients or users.

*Also referred to as: session persistence and resumption, agent session portability, session forking, trajectory forking, shared agent sessions across interfaces, context portability, multiplayer agent sessions*

## State of Practice

The field converged this year on treating an agent session as a durable, portable object rather than as a process or a chat window, but it has not converged on how. Three incompatible substrates were pitched: a standardized live wire protocol between client and agent (Zed's ACP, ~40 client implementations, four methods to adopt, stdio-only today), an append-only event log owned by the operator that any executor can advance (Omnara), and a managed harness where hosting, session state, sandboxing and credentials are outsourced to the provider (Anthropic's agentic surfaces stack). Everyone agrees the current baseline is broken in specific, cited ways: Claude Code and Codex write fire-and-forget JSONL to local disk, a pending permission prompt is lost if the process dies and resumes, OpenCode's SQLite state has documented corruption, and per-product memory silos force users and teams to rebuild context on every tool migration. The most concrete new capability demonstrated is cross-boundary resume — picking up a colleague's session on your machine with zero setup, forking a recorded computer-use trajectory to any moment, or running one branch on Claude and another on GPT — which reframes the session from disposable exhaust into the org's reusable asset. The live argument is over whether a long-lived compacted thread is a sound container at all, or whether decisions must be externalized into documents and logs that make the session itself stateless.

## Consensus

### A session must be resumable outside the process, machine, client, and vendor that created it — portability across boundaries is the design goal, not a nice-to-have.

Support: **5** talk(s)

> "I resume their session on my machine, I get the exact state, fully functional, zero setup, and then I just talk to my agent about the decisions we made"
>
> — [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s)

Supporting talks: [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### The durable substrate is an append-only event log of the session (inputs, model outputs, tool calls, results, permissions, failures); model context, UI, audit and compaction are all views derived from it.

Support: **4** talk(s)

> "underneath every serious database is a log. And that log is the durable sequence of changes. Everything else is a view."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [3:18](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=198s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### The executor is disposable and should be treated as fallible infrastructure: one-process-per-agent on a developer laptop is the wrong deployment shape for production sessions.

Support: **3** talk(s)

> "And if an agent is a running process, that's extremely terrifying. But if the agent is the log, it's simply an execution detail."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [12:28](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=748s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### The trajectory of a session is worth as much as its output — sessions should be replayable, forkable and mineable as organizational assets, not discarded when the task ends.

Support: **5** talk(s)

> "the value is not just what the agent produced, it's also the log, which indicates how it got there"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [8:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=525s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)

### Binding memory and context to the session (or to a single agent product) is a dead end; context has to outlive any individual session, framework, or vendor.

Support: **4** talk(s)

> "Each of these products is trying to build its own memory of me. None of these memories are shared with each other. So I have to rebuild context within every single product from scratch."
>
> — [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [17:43](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1063s)

Supporting talks: [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

## Disagreements

### Is a long-lived, compacted thread a sound container for ongoing work, or must session state be externalized into durable artifacts?

| Position A | Position B |
|---|---|
| Stay in one thread indefinitely — compaction is now good enough that five-week-old threads with hundreds of sub-agents still know what to do, and scheduled automations should heartbeat back into the existing thread rather than opening a new one.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Compaction throws information away, so the thread cannot be the state: retain the raw log and treat any compacted continuation as a best-effort lossy fork, extract atomic facts instead of compacting on overflow, and hold decisions in a durable doc so every agent starts stateless.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: It decides whether you invest in thread-management UX (pinning, renaming, inter-thread messaging) or in log persistence, forking, and doc-as-state infrastructure. It also determines whether 'agent bankruptcy' is a real failure mode you must design around or an artifact of bad session hygiene.*

### Should teams outsource session persistence to a managed agent platform, or own the session state themselves?

| Position A | Position B |
|---|---|
| Hosting, session management, sandboxing, credentials and observability are undifferentiated infrastructure; developers should own only system prompts, skills, tools and domain context and let the harness supply the rest.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* | Whoever owns the log owns the agent — log lock-in is deeper than model or API lock-in, memory must be built in-house rather than outsourced, and teams should stay model- and harness-agnostic because the best option changes weekly.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: Managed session infrastructure buys measured wins (60% faster P50 time-to-first-token from decoupling the loop from tool containers) at the cost of a migration path; self-owned logs preserve the ability to swap providers mid-session but require building durability, forking and compaction yourself.*

### Does session portability come from standardizing the live client-agent protocol or from standardizing the persisted session object?

| Position A | Position B |
|---|---|
| Standardize the wire protocol: implement four JSON-RPC methods and any client can drive any agent, with the client owning terminals, diffing, and a proxied filesystem — sessions are created per client thread and the agent keeps its own state.<br>*[Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)* | Standardize the state itself: materialize the full session as a portable object — log, repos, PRs, traces — so it can be handed to another person, another machine, or another vendor's agent mid-stream, independent of any live connection.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: The protocol approach makes sessions interchangeable across UIs but not across time or machines — ACP is stdio-only with no remote transport yet — while the state approach makes sessions durable and shareable but leaves every client rendering them differently.*

### Should sessions be pooled across an organization by default, or gated by who is in the room?

| Position A | Position B |
|---|---|
| Pool them: crossing developer boundaries gives the agent more context than any single developer has, and replaying a respected engineer's session beats every implementation being bespoke.<br>*[A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | Gate them: whether information is public or private depends on the room it was shared in, not the data, so permissions belong in the memory layer itself (per-user adapters over shared memory) and the user must retain visible, final say over what is remembered.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* |

*Why it matters: A shared session pool is the single biggest context multiplier on offer, but if permission scoping is bolted on afterward the pool becomes an exfiltration surface — and retrofitting per-room privacy onto an already-merged corpus is far harder than designing for it.*

## Practical Guidance

**Do:**

- Persist an append-only event history — every user input, model output, tool call, tool result, permission and failure — and resume from it rather than from in-process state.
- Treat compaction as a lossy fork resumed as a new log, and keep the raw log around.
- Decouple the agent loop from the tool-execution container so first-token reasoning does not block on container setup (measured: 60% faster TTFT at P50, >90% at P95).
- Make the same session, with identical context, reachable from Slack, desktop/mobile and GitHub instead of adding a Slack bot on top of a laptop-bound agent.
- To make an existing agent client-portable, implement ACP's four methods; read files through the client's proxied filesystem so unsaved buffer state is visible, and send old text plus new text so the client renders the diff.
- Record trajectories so any run can be forked at an arbitrary moment to recover the state of the machine at that point.
- Run a periodic batch pass over session transcripts plus current memory state to extract and reorganize what the next day's sessions start with.
- Externalize the decisions that matter into a durable doc up front rather than asking an LLM to summarize the session afterward.
- Move sessions into isolated cloud sandboxes with least-privilege access instead of running them on laptops holding production credentials.
- Keep security credentials in a vault decrypted only at tool-execution time so the model never sees them in session context.
- Give users version history and a visible, revocable record of what the session remembered, with an always-available stop control.

**Avoid:**

- Fire-and-forget JSONL writes to local disk as the only persistence layer — a failed write silently loses the session.
- Resuming into a state where a pending permission prompt has been dropped and the agent sits paused forever.
- One process per agent with sticky sessions pinned to a machine; it forces state migration and coordination overhead that log-centric design removes.
- Letting the provider hold the only copy of the log — model, API and tool lock-in can be wrapped or swapped, log lock-in cannot.
- Treating the context window and the session as the same object.
- Giving each agent its own memory system, which produces context sprawl and no single version of truth.
- Hardcoding business context into agents, which loses it at every framework migration (Relevance → Google ADK → Glean → Claude Code → Codex in ~12 months).
- Making the human the memory layer by starting every session from a blank slate and re-explaining the same change per repo.
- Reading files with native fs APIs from inside an ACP agent, which misses unsaved client buffers.
- Spawning a new thread per scheduled automation when a heartbeat into the existing thread would preserve continuity.

## Notable Outliers

- The deepest form of vendor lock-in is not model or API lock-in but log lock-in — whoever owns your session log owns your agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- Threads five weeks old containing roughly 400 sub-agents still work fine — the advice to start fresh after ~20 messages is obsolete. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [3:29](https://www.youtube.com/watch?v=il1c1a2FufU&t=209s))
- Every recorded computer-use run can be forked at any moment in its trajectory to recover the exact state of the computer at that moment. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s))
- Pooling sessions across developer boundaries gives the agent more context than any single developer possesses — effectively photographic memory of the organization. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s))
- One process can advance thousands of agents once the log rather than the runtime holds the state. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s))
- ACP has reached roughly 40 client implementations but still runs only over standard IO — remote transport does not exist yet. ([Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [17:36](https://www.youtube.com/watch?v=HsxQICTLF84&t=1056s))
- A separate branch of the same session can run on Claude while another runs on GPT and another on an open-source model, because provider migration is only an adapter and schema problem. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [8:04](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=484s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)
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
- [Shlok Khemani](../speakers/shlok-khemani.md)
- [Victor Savkin](../speakers/victor-savkin.md)

