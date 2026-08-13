---
title: "least-privilege agent permissions"
type: "concept"
slug: "least-privilege-agent-permissions"
tier: "supporting"
maturity: "contested"
talk_count: 21
speaker_count: 24
---

# least-privilege agent permissions

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **21** talk(s) by **24** speaker(s)

**Definition:** Restricting which tools, data, and credentials an agent can reach to the minimum its task requires, and keeping secrets out of its context.

*Also referred to as: least privilege for agents, agent tool permissions, tool access control, fine-grained access control, permission granularity, over-broad agent permissions, credential isolation*

## State of Practice

The field has converged on a blunt operational fact: an agent will use every permission it holds, so the API key you hand it is the ceiling on your blast radius, not the plan. The dominant pattern presented was to stop handing agents human credentials and instead give them their own identity plus narrowly delegated authority — per-tool-call tokens obtained via RFC 8693 token exchange, audience-bound to a single MCP server, expiring in minutes, never stored — with policy evaluated *before* the credential is minted so a denied action leaves nothing to leak or replay. A parallel school argues the credential layer is the wrong place to fight and that containment wins: keep secrets in a vault decrypted only at tool-execution time (the model never sees a token), give the agent no write credentials at all and push git push / PR creation / CI triggering into a deterministic wrapper, and run the whole thing in a micro VM because the sandboxes shipped with Codex and Claude Code are worthless the moment the agent has a Docker socket. Everyone agrees prompt injection is unsolved and that human-in-the-loop approval is not an access control — approvers are consent-fatigued, and a skill that merely instructs the agent to 'ask for confirmation' gets confirmed by the agent itself. The supply chain around the agent (skills, plugins, MCP servers, hooks) is now treated as dependency surface to be scanned and allow-listed, and the boring infrastructure layer underneath — auth off by default on clusters — is where breaches actually land. Nobody claims a settled control layer; the honest summary from the survey talk is that current tooling is the toolkit you'd use to manage an intern.

## Consensus

### An agent will exercise every permission it holds, so credentials must be scoped to the specific task rather than issued as broad, long-lived, 'kitchen sink' keys.

Support: **5** talk(s)

> "agents want to be helpful. they're going to use all the permissions that they have access to in order to get the job done."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Human-in-the-loop approval is not an access control; it fails to consent fatigue, and an in-prompt 'ask for confirmation' instruction can be satisfied by the agent itself.

Support: **3** talk(s)

> "people sometimes will add the instruction like you need to ask for confirmation but the AI may ask confirmation for itself. So from your perspective there is a human in the loop but for the AI perspective there is has been a confirmation"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [12:33](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=753s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

### Prompt injection has no reliable technical fix at the model layer, so the only available defense is limiting what the agent can reach when it happens.

Support: **4** talk(s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)

### Secrets must be usable by the agent without being visible to it: credentials belong in a vault or deterministic execution layer and should never enter the model's context.

Support: **4** talk(s)

> "the data dog credentials are only usable by the agent but not accessible by the agent"
>
> — [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [36:56](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2216s)

Supporting talks: [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### Agents should execute in an isolated sandbox rather than on a developer's machine, because the laptop's ambient credentials and filesystem are themselves the over-privileging.

Support: **5** talk(s)

> "it finds a token on your laptop that it can use and it thinks it's working with staging, but actually it's production and now it just deleted everything."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [11:05](https://www.youtube.com/watch?v=OL7kfezynJM&t=665s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### The agent must be its own principal with its own identity, acting on behalf of a user under delegated authority, rather than impersonating the user with the user's credentials.

Support: **3** talk(s)

> "the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

Supporting talks: [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### Restrict the tool surface itself — allow-listed tools per skill, per-user tool scoping on MCP servers, agents that structurally cannot do more than their job — rather than relying on runtime approval of a maximally capable agent.

Support: **3** talk(s)

> "In a world that would be powered by smaller domain-specific agents, those agents can't do everything. They can only do the things that are already explicitly approved for them to do."
>
> — [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [19:34](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1174s)

Supporting talks: [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

## Disagreements

### Should least privilege be achieved by scoping credentials for a general-purpose agent, or by replacing it with narrow agents that structurally lack the capability?

| Position A | Position B |
|---|---|
| Keep the powerful general agent and constrain it at the authorization layer: per-tool-call token exchange, policy evaluated before minting, classifiers and auto-review in the loop.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Restricting a general-purpose agent destroys its usefulness; deploy narrow, domain-specific, capability-limited agents whose approved action set is fixed at design time, and skip permission dialogs entirely.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* |

*Why it matters: One path invests in identity infrastructure, policy engines and token exchange that a single agent calls at runtime; the other invests in fleets of small isolated agents and an orchestration layer. The engineering budgets and failure modes barely overlap.*

### Should agents hold scoped credentials at all, or should privileged operations be moved out of the agent into deterministic code?

| Position A | Position B |
|---|---|
| Give the agent short-lived, audience-bound, task-scoped tokens minted per tool call after policy evaluation — the agent acts, but only within the narrowed grant.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* | The agent should hold no write credentials whatsoever; it only edits files or proposes changes, while push, PR creation, CI triggering and sharing/access control live in a deterministic layer or the platform, so a compromised agent has nothing to spend.<br>*[We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* |

*Why it matters: It decides where the security review happens — in an authorization server and policy language, or in the architectural split between what is agentic and what is deterministic. As one speaker put it, that split is the security model.*

### Are the sandboxes and auto-approval modes shipped with today's coding agents adequate protection?

| Position A | Position B |
|---|---|
| Yes for most work: auto mode plus a classifier is the safest way to run long tasks, and AGENTS.md rules plus auto-review suffice for individual use, with models already erring toward being too reluctant to act.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | No: built-in sandboxes are worthless once the agent has Docker socket access, and relying on a correctly configured YOLO mode on a laptop full of credentials is hope, not a control — micro VMs with mediated networking are the real boundary.<br>*[We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* |

*Why it matters: If vendor defaults are adequate, teams ship agents today with configuration; if not, every team needs isolation infrastructure the speakers themselves describe as still in beta, which pushes production agent adoption out by quarters.*

## Practical Guidance

**Do:**

- Mint downstream access tokens per tool call, not per session, audience-bound to the single target MCP server, expiring within a few minutes, and never stored
- Evaluate policy before the credential is minted rather than issuing a broad credential and restricting its use, so a denied action leaves nothing to leak, replay, or steal
- Store credentials in a vault decrypted only at tool-execution runtime so the model never sees a security token
- Keep dangerous write capabilities — GitHub push, PR creation, CI triggering — out of the agent entirely and in the deterministic wrapper around it
- Give each agent its own private key and identity so actions are attributable per agent, per host, and per user, with the user it reports to always recorded
- Check the human approver's role against policy too, so an approval from someone without the role is overridden
- Build the kill switch first, resolve flags per turn rather than per session, and force sub-agents through the same middleware as their parent
- Default autonomy to 'suggest' for everything, earn auto-approve per surface, and make auto-execute opt-in per tool
- Time-bound agent permissions to its operating window and require just-in-time elevation for anything broader
- Have skills declare allow-listed, access-controlled tools, and route third-party skills through an internal marketplace that scans them with both deterministic checks and LLM review before distribution
- Run agents needing Docker inside micro VMs (Firecracker) with Vsock-mediated networking, or let tool execution run inside the customer's own VPC via outbound-only tunnels
- Secure the boring infrastructure first — cluster auth, network segmentation, service-to-service verified identity — since access control policy is decoration if the cluster underneath is open

**Avoid:**

- Handing an agent your own credentials or a personal API key that can do everything the certificate-renewal job needed plus drop the database
- Treating an in-prompt 'ask for confirmation' instruction as a human in the loop
- Giving an agent Docker socket access — it can spawn a privileged container and escape, making the surrounding sandbox meaningless
- Assuming a blocked connector stops the agent; a determined one will open a browser and perform the action manually via computer use
- Letting a parent agent with flags correctly applied spawn child agents that bypass the flag middleware, so a flipped kill switch never reaches them
- Relying on OAuth scopes like 'read' or Gmail's send-on-your-behalf, which cannot express time-of-day, sender, or recipient restrictions
- Exposing the same MCP tool surface to the agent regardless of which user authorized it
- Building your own AI Slackbot, given the prompt-injection attack surface
- Believing your team is at security maturity level three when the audit evidence puts most teams at level one or two

## Notable Outliers

- No agent should be permitted to drop a database, even when the documented recovery runbook calls for exactly that step. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s))
- If the platform implements sharing and access control and the client runs in a null-origin sandboxed iframe talking only to an isolated server sandbox, there is no security bug the generated code can have that matters. ([Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s))
- For prompt injection and data exfiltration specifically, an auto-mode agent's residual risk is already lower than that of an average human reviewer. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s))
- Behavioral techniques for taming agents simply do not work — only sandboxing and removing the means to cause harm do. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s))
- 78% of 50 audited production ML setups had at least one critical security mistake, and the breaches come from ordinary infrastructure misconfiguration rather than model-level attacks. ([Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [8:32](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=512s))
- A determined agent blocked from a connector will route around it with computer use — opening Chrome and clicking send — which makes connector-level blocking an incomplete control. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [54:37](https://www.youtube.com/watch?v=il1c1a2FufU&t=3277s))
- Companies must design in-house agent permission and monitoring systems now, because nothing mature enough to buy exists. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [20:05](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1205s))

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
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Cat Wu](../speakers/cat-wu.md)
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
- [Simon Willison](../speakers/simon-willison.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

