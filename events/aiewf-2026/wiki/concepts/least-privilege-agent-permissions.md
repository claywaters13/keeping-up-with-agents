---
title: "least-privilege agent permissions"
type: "concept"
slug: "least-privilege-agent-permissions"
tier: "supporting"
maturity: "contested"
talk_count: 22
speaker_count: 26
---

# least-privilege agent permissions

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **22** talk(s) by **26** speaker(s)

**Definition:** Restricting which tools, data, and credentials an agent can reach to the minimum its task requires, and keeping secrets out of its context.

*Also referred to as: least privilege for agents, agent tool permissions, tool access control, fine-grained access control, permission granularity, over-broad agent permissions, credential isolation*

## State of Practice

The field has converged on the diagnosis and is still arguing about the mechanism. Everyone agrees the current default — hand the agent a long-lived kitchen-sink API key in a .env file, or worse, the user's own credentials — is broken, because an agent will use every permission it holds to complete a task and there is no code to inspect that bounds what it will attempt. The emerging shape of the answer is: the agent is its own principal with its own identity, it receives task-scoped short-lived credentials minted per tool call after a policy check, secrets are usable-but-not-readable (vault decryption at tool-execution time, never in the model's context), and write-capable operations like git push, PR creation, or CI triggering are pushed out of the agent into a deterministic wrapper. Because prompt injection is treated as unsolvable at the model layer, isolation is doing the real work: micro VMs rather than container sandboxes when Docker is involved, execution in the customer VPC or an isolated cloud environment rather than a developer laptop full of credentials, and in the strongest form, platforms where the generated code structurally cannot express a wrong permission model. Nobody claims to have shipped a mature control layer — Yegge's advice was to build one in-house because nothing exists to buy, and the State of AI Engineering survey found the top two guardrails in production are human-in-the-loop approvals and permission gating, which is the toolkit you'd use to manage an intern.

## Consensus

### An agent will use every permission it holds to complete its task, so over-permissioning is a design defect rather than developer carelessness — scope must be cut to the specific action.

Support: **5** talk(s)

> "agents want to be helpful. they're going to use all the permissions that they have access to in order to get the job done."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

### Credentials should be usable by the agent but never readable by it — held in a vault or deterministic layer and injected at tool-execution time, never placed in the model's context.

Support: **5** talk(s)

> "the data dog credentials are only usable by the agent but not accessible by the agent"
>
> — [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [36:56](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2216s)

Supporting talks: [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Prompt injection cannot be defended at the model layer, so permission design is the actual control: limit blast radius architecturally and assume injection succeeds.

Support: **5** talk(s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)

### Sandboxing and removing capability — not instructions, prompts, or behavioral guardrails — are what actually constrain an agent.

Support: **5** talk(s)

> "I think nothing works except like sandboxing and just not giving them a way to hurt themselves."
>
> — [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s)

Supporting talks: [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)

### The agent must be its own principal with its own identity, bound to but distinct from the user it acts for — impersonating the user with the user's credentials is the wrong model.

Support: **3** talk(s)

> "the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

Supporting talks: [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### Access should be granted per tool call and time-bounded — short-lived, audience-bound, ephemeral credentials with just-in-time elevation, not a session-wide or registration-time grant.

Support: **3** talk(s)

> "this request is asking for permissions to access the MCP server for that tool call but only that tool call."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [9:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=567s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)

### Human-in-the-loop approval is not by itself an access control, because approvers are consent-fatigued, many agents run unattended, and an agent can satisfy a prompt-level confirmation instruction itself.

Support: **4** talk(s)

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)

## Disagreements

### Should human approval remain the primary gate on privileged agent actions, or be replaced by machine-enforced policy?

| Position A | Position B |
|---|---|
| Human approval is the wrong control surface: approvers are fatigued and fallible, an agent can self-satisfy a confirmation prompt, and the approval itself should be policy-checked against the approver's role (and can be overridden). The goal is to remove humans from the loop for classes of work where automated checks catch everything.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* | The plan-then-approve block is a hard requirement: agentic tools must show a plan and get approval before executing, every layer of a fleet must block until the operator approves, and even at 99.9% agent-generated PRs a human reviews every one.<br>*[The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: If approval is the control, you invest in UX, plan rendering, and reviewer throughput and your ceiling is human attention; if policy is the control, you invest in token exchange, per-call authorization, and audit, and unattended overnight operation becomes possible.*

### Is the safe agent a general-purpose one that has been contained, or a narrow one that was never given the capability in the first place?

| Position A | Position B |
|---|---|
| Restriction of a general agent degrades it into uselessness; the right unit is a small, domain-scoped agent whose capability set is explicitly approved, with sandboxed filesystem and code execution as built-in primitives — or a platform that implements sharing and access control so generated code cannot get the permission model wrong.<br>*[Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)* | Keep the broadly capable agent and contain it externally — classifier-judged auto mode, AGENTS.md rules plus auto-review, or a deterministic wrapper that holds the dangerous credentials while the agent only edits files inside a micro VM.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)* |

*Why it matters: It decides whether you build one agent and a security perimeter around it, or a fleet of narrow agents plus an orchestration layer — and whether cost, token efficiency, and model choice are per-task decisions or one global one.*

### Does agent authorization need new identity primitives, or do existing OAuth extensions already cover it?

| Position A | Position B |
|---|---|
| No new spec is required — RFC 8693 token exchange, an existing OAuth 2 extension, is sufficient to narrow access per tool call and to attribute the agent, the user, and the delegating user's level of access.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* | OAuth is only a starting point: even fine-grained OAuth still mints a token for the user, scopes like 'read' or Gmail's send scope cannot express time-of-day, sender, or recipient limits, and the agent needs its own private key and signed tokens to be a first-class principal.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* |

*Why it matters: Betting on token exchange means you can ship on today's identity providers and resource-server scopes; betting on agent-native identity means waiting for services to implement new endpoints and running OpenAPI-to-capability translation as an interim bridge.*

### Should agents be given direct access to a developer's or user's personal machine?

| Position A | Position B |
|---|---|
| Local machine access is uniquely powerful precisely because it carries the user's OAuth, credentials, and filesystem, and today's models are more often too reluctant to take destructive action than too eager — over-restriction is the bigger practical cost.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Laptops hold credentials and data the agent should never reach, sandbox and auto-approval configurations are not reliably safe, and an agent that finds a token can mistake production for staging — agents belong in isolated cloud environments, not on personal computers.<br>*[Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* |

*Why it matters: This determines whether the sandboxing investment is optional ergonomics or the prerequisite for letting non-technical teammates trigger real merged code changes.*

## Practical Guidance

**Do:**

- Evaluate policy before minting the credential, not after — a denied action leaves nothing to leak, replay, or steal, whereas a broad credential restricted at use time still exists.
- Mint per-tool-call tokens that are audience-bound to a single target MCP server, expire within a few minutes, and are never stored.
- Store credentials in a vault that decrypts only at tool-execution runtime, so security tokens never enter the model's context.
- Keep write-capable credentials — GitHub push, PR creation, CI triggering — out of the agent entirely and in the deterministic wrapper; let the agent only modify files on disk.
- Give each agent its own private key and identity so actions are attributable per agent, per host, and per user.
- Grant read-type capabilities by default per host and reserve prompts for writes, or approval fatigue will make the system unusable.
- Use a micro VM (Firecracker) with Vsock-mediated networking as the isolation boundary when the agent needs Docker; container-level sandboxes cannot contain a Docker daemon.
- Run tool execution inside the customer's own VPC under their policies (e.g. MCP tunnels making only outbound calls to the agent loop) rather than only in the vendor's cloud.
- Have skills declare allow-listed tools and access-control those tools, and govern skills, plugins, MCP servers, rules, and hooks as supply-chain dependencies scanned before marketplace distribution.
- Re-enforce local scanning in CI, since you cannot ensure an engineer ran the checks or ran the latest version.
- Build the kill switch first, resolve flags per turn rather than per session, and route sub-agents through the same middleware so a flip actually reaches them.
- Segregate sensitive data into schema-driven object storage that the orchestration log only references, and have token-bearing agents fetch it at point of use, so the lethal trifecta is architecturally impossible.
- Secure the underlying infrastructure first — an exposed cluster with auth off by default makes a perfect access-control policy decoration.
- Keep tool cardinality low with clearly distinct functions, which both improves tool selection and shrinks the permission surface.

**Avoid:**

- Handing an agent your own credentials or personal token — give it delegated authority scoped to specific actions instead of letting it pretend to be you.
- Long-lived kitchen-sink API keys in a .env file that can renew a certificate and drop a database with the same credential.
- Treating a prompt instruction like 'ask for confirmation' as a human in the loop — the agent can satisfy the confirmation itself.
- Giving an agent Docker socket access: it can spawn a privileged container and escape, which makes the built-in Codex and Claude sandboxes worthless.
- Relying on coarse OAuth scopes such as 'read' or Gmail's send-on-your-behalf, which cannot express time-of-day, sender, or recipient limits.
- Exposing the full tool surface on an MCP server regardless of which user authorized the agent — scope the tool list to the authorizing principal.
- Spawning sub-agents that bypass the permission/flag middleware their parent went through.
- Assuming a blocked connector stops a determined agent — it will open a browser and perform the action via computer use.
- Bolting security, auditability, and eval onto a working POC as requirements surface; start from the constraints and rebuild toward POC accuracy.
- Letting non-engineers spin up agents with far more permissions than their job needs, on the assumption that a mature permissioning product exists to buy.

## Notable Outliers

- No agent should be permitted to drop a database — even when the documented recovery procedure calls for it, policy should refuse to mint the credential. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s))
- If the client runs in a null-origin sandboxed iframe and the server sandbox can only talk to it, there is no security bug in the generated code that matters — an XSS bug leaks nothing. ([Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s))
- For prompt injection and data exfiltration specifically, an auto-mode agent with a classifier judging each tool call carries lower residual risk than the average human reviewer. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s))
- Tightening down a general-purpose agent (OpenClaw) destroyed its usefulness; a narrowly sandboxed special-purpose agent is the better tradeoff today. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s))
- Current models are more often too reluctant to take destructive actions than too eager, so over-restriction is the bigger practical annoyance for individual use. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [30:01](https://www.youtube.com/watch?v=il1c1a2FufU&t=1801s))
- An audit of 50 real production ML setups found at least one critical security mistake in 78% of them, almost all ordinary infrastructure misconfiguration rather than model-level attacks. ([Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [8:32](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=512s))
- Companies must design in-house agent permission and monitoring solutions now, because nothing mature exists to buy. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [20:05](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1205s))

## All Talks

- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Kenton Varda](../speakers/kenton-varda.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Paola Estefania](../speakers/paola-estefania.md)
- [Ravi Madabhushi](../speakers/ravi-madabhushi.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

