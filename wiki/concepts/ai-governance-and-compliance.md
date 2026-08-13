---
title: "ai governance and compliance"
type: "concept"
slug: "ai-governance-and-compliance"
tier: "supporting"
maturity: "contested"
talk_count: 14
speaker_count: 14
---

# ai governance and compliance

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **14** talk(s) by **14** speaker(s)

**Definition:** Organizational and regulatory control over AI systems — policy, approval, disclosure, and demonstrating conformance to auditors.

*Also referred to as: ai governance, ai code governance, eu ai act compliance, regulated environment compliance, agent governance and security posture, sox compliance for ai agents, predictive governance, ai disclosure policy*

## State of Practice

Governance has moved from a documentation exercise to a runtime engineering problem: speakers repeatedly argued that policy expressed as Confluence pages, PDFs, or prompt instructions is unenforceable, and that controls must be instrumented in the agent harness, in CI, in tool hooks, or in a shared output-veto service that every surface passes through by default. The scope of what needs governing has expanded past generated code to the whole agentic supply chain — skills, plugins, MCP servers, agent rules, hooks — with Nubank scanning 2,000+ skills and Snyk reporting that over a third of publicly shared skills carry malware or vulnerabilities. There is broad agreement that the system generating work cannot be the system validating it, and that a yes/no approval prompt on an opaque command is not meaningful oversight — an agent can satisfy its own 'ask for confirmation' instruction, and the EU AI Act's high-risk oversight requirement is about to make that gap legally material. The sharpest unresolved question is what the authority is made of: several speakers insist governance verdicts must be deterministic and traceable (regex vetoes, deterministic PR scores, static checks) because LLM judgments drift with temperature and model version and are not defensible to leadership, while others argue only a model can judge the spirit rather than the syntax of a constraint. Accountability and audit trail for AI-authored changes remain openly named as unsolved, with eBay predicting 2027 is when the industry conversation shifts from adoption to governance.

## Consensus

### Governance must be enforced as executable controls in the runtime path — harness hooks, CI steps, shared services — not as written policy that humans are trusted to follow.

Support: **5** talk(s)

> "when you're building ungoverned AI apps, that AI governance cannot live in a confluence page or PDF"
>
> — [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [14:40](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=880s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### The system that produces the work must not be the system that certifies it — independent validation, whether a separate scanner, an adversary agent, or a human reviewer, is structurally required.

Support: **5** talk(s)

> "Can, you know, the generator and the validator be the same? And our point is, you know, in some of the data you'll show for all kinds of reasons why not"
>
> — [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [3:22](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=202s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

### A yes/no confirmation prompt on an opaque action does not constitute human oversight; the human must be given the plan, the reasoning, or the cost before approving.

Support: **4** talk(s)

> "people sometimes will add the instruction like you need to ask for confirmation but the AI may ask confirmation for itself. So from your perspective there is a human in the loop but for the AI perspective there is has been a confirmation"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [12:33](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=753s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Probabilistic model judgment is not a sufficient basis for a compliance verdict — deterministic checks must anchor the decision because LLM verdicts vary with temperature and model version.

Support: **4** talk(s)

> "The first three layers are instruction, the fourth is permission. And that's the whole distinction. Instructions are probabilistic. Permission is deterministic."
>
> — [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [17:51](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1071s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

### Skills, plugins, MCP servers, and agent rules are supply-chain dependencies and belong under the same scanning, versioning, and ownership regime as third-party code.

Support: **3** talk(s)

> "It still have the traditional part, but it will it also includes skills, plugins, MCP servers, agent rules and much more things to be acting as supply chain"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [2:08](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=128s)

Supporting talks: [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### Accountability for AI-authored changes must land on a named human, and the audit trail for it does not exist yet in most organizations.

Support: **3** talk(s)

> "who is accountable when an AI authored change causes an incident? Where is the audit trail?"
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

## Disagreements

### Should AI governance controls hard-block the workflow, or surface risk without ever gating it?

| Position A | Position B |
|---|---|
| Controls should inform and never block — post the risk score as a comment on every PR but let it merge, and treat security as guardrails alongside development rather than a gate, because acceleration will always beat friction.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* | Controls must be load-bearing: skills get blocked before marketplace distribution, a missing brand identity throws rather than defaults, and the agent's default on a constraint/task collision is halt-and-explain rather than route around.<br>*[We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* |

*Why it matters: This determines whether a governance program is a dashboard or a control plane — and whether it can be presented to an auditor as an enforced conformance mechanism at all. Non-blocking controls preserve velocity but produce no guarantee; blocking controls produce evidence but require the org to accept stalled work.*

### Can a model be the authority that judges whether an AI system complied, or must the verdict be deterministic?

| Position A | Position B |
|---|---|
| The verdict must be deterministic and traceable to a computation: LLM-judged scores shift when the model changes and aren't defensible to leadership, regex vetoes beat probabilistic classifiers, and frontier models found the same vulnerability in only 50% of five repeated runs at a 40% F1 versus a static check.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)* | Deterministic rules only catch syntax; judging whether a worker agent violated the spirit of a constraint requires an equal-power adversary agent, and a hybrid where an LLM supplies context around deterministic scanning catches what either alone misses.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)* |

*Why it matters: If verdicts must be deterministic, whole classes of violation — the agent that stayed inside its authorization the entire time — are structurally undetectable and must be prevented by design instead. If model judgment is admissible, you inherit run-to-run variance in your compliance record and must version-pin the judge.*

### Where should AI security and compliance budget actually go — conventional infrastructure hygiene, or AI-specific risk?

| Position A | Position B |
|---|---|
| Almost everything breaking in production is ordinary misconfiguration: auth off by default on Ray clusters, 78% of 50 audited ML setups with at least one critical mistake, and vulnerabilities that are all known classes. Spend on infra compromise, insider threat, and memory-safe rewrites rather than model-level attack research.<br>*[Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* | The agentic layer is a genuinely new surface: repos hold roughly 3x more agentic components than models, a third of shared skills carry malware, model safety properties are non-monotonic across attack types, and existing string-matching runtime tools are not equipped for non-deterministic workloads.<br>*[Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Notion's Token Town](../talks/notions-token-town.md)* |

*Why it matters: It decides whether an AI governance program is a re-run of cloud security fundamentals with existing tooling and staff, or a new discipline needing new instrumentation at the harness and skill-registry layer. Getting it wrong means spending on the category where breaches aren't landing.*

### Should every AI-authored change still pass a human reviewer, or should automated validation absorb the volume?

| Position A | Position B |
|---|---|
| Human review is non-negotiable and must hold AI PRs to the same standard with no exceptions — the human author writes the PR body and confirms the tests assert intended behavior — because unreviewed code becomes grounding for tomorrow's agent output, and in finance you cannot assign accountability to the model.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* | Human review is the bottleneck and will not survive: within 6-12 months most shipped code will be reviewed by AI, and autonomy should instead be gated by the density of deterministic validation loops so the signal-to-deploy flow is uninterrupted by a human.<br>*[The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)* |

*Why it matters: This is the load-bearing assumption behind every AI-era SDLC control: if human review is mandatory, throughput is capped by reviewer headcount you won't get funded; if validation loops replace it, the entire compliance story rests on test and verifier coverage that most codebases don't have.*

## Practical Guidance

**Do:**

- Compute PR risk scores from a fully deterministic formula (cross-file spread, test-to-code ratio, cross-team blast radius), post it as a comment on every PR, and calibrate the weights by backfilling the last 200 merged PRs against your own reviewers' experience
- Route every skill, plugin, MCP server, and agent rule through an internal marketplace gated by a hybrid deterministic + LLM scanner, run locally by the developer and re-enforced in CI because you cannot prove they ran the latest version locally
- Emit scanner findings as SARIF into the existing vulnerability management program, and deliver them in the same pull request that uploads the skill
- Invoke security tooling deterministically from hooks or skills rather than relying on the developer to prompt for it
- Make the final output guard a shared service every surface passes through by default, and tune it toward false positives — a false positive is a double-checked response, a false negative is a hallucinated number shipped to a client
- Grade shell-command risk per command rather than treating all shell access as equally dangerous, and drop low-context weak signals that generate more noise than value
- Require the human author to write the PR body and to confirm the tests assert what the code should do — that is the moment accountability attaches
- In multi-tenant systems, make a missing identity field throw rather than silently default
- Disclose that the system is AI in its first response unprompted, mark AI-generated content explicitly, show the action plan plus a rough time and cost estimate before executing, and always expose a prominent abort control and version history
- Version company context like code — approvers, maintainers, contributors, dependency tracking — and route self-improving skills' learnings through a human approve/reject step, since each evolution breaks downstream dependents
- Secure the infrastructure layer first (auth on by default, verified service-to-service identity instead of network-as-trust-boundary, network segmentation, data at rest) and budget 5-10% security overhead as the production floor
- Select models per use case against distinct safety tests, since a model perfectly resistant to decision override can be 100% vulnerable to PII extraction
- Set the agent's default on a constraint/task collision to halt and explain, and require that the energy to remove a constraint come from outside the agentic loop

**Avoid:**

- Publishing AI governance as Confluence pages or PDFs and expecting conformance
- Using an LLM as the scoring authority for anything you must defend to leadership — the same artifact scores differently after a model change
- Accepting a prompt instruction to 'ask for confirmation' as evidence of a human in the loop
- Presenting a yes/no approval on an opaque command as meaningful human oversight, particularly under the EU AI Act's high-risk requirements
- Severity-based triage that closes out lows and mediums, since agents can chain low-severity findings into working exploits
- Reporting PR count, PR size, or cycle time as AI adoption health — they measure the speed of production, not the speed of trust
- Blocking merges on the review-debt score itself, or letting the agent write the PR body
- Blanket real-time malicious-input detection on every request (15-30% latency overhead); reserve it for higher-risk systems
- Assuming your single internal marketplace is a durable chokepoint — teams will spin up others, so scan for new marketplaces proactively
- Claiming any AI tool is 100% hallucination-free or marketing your model as more trustworthy than competitors
- Shipping a blank 'ask AI' box, an unabortable process, or non-deterministic output with no version history
- Committing to a single model provider for a volume discount — optionality is the leverage, and without the ability to walk you are stuck
- Waiting for a better model to solve agentic security

## Notable Outliers

- A yes/no approval prompt on an opaque command will not satisfy the EU AI Act's meaningful-human-oversight requirement for high-risk AI, which begins taking effect within weeks — 'A sandbox diagram with a yes no LGTM ain't going to cut it.' ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [15:36](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=936s))
- An agent persuading a human to remove a control — e.g. talking them into installing a Chrome extension — counts as the agent supplying the energy to defeat its own constraint, with the human acting as its tool. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- More than a third of publicly shared agent skills contain malware or vulnerabilities, and repos contain roughly three times more agentic components than models. ([Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [8:23](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=503s))
- An audit of 50 real production ML setups found at least one critical security mistake in 78% of them, and most teams believe they are at maturity level three when they are actually at level one or two. ([Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [8:32](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=512s))
- 2027 will be the year the industry conversation shifts from AI coding adoption to governance and accountability; meanwhile median PR review time is already up 441.5% and 31% more PRs merge with no review at all. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s))
- Compliance should become a continuous intelligence function rather than a periodic review — a cross-document correlation framework cut false positives 76% and manual audit effort ~40% across 3M records in 4 jurisdictions. ([AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [15:16](https://www.youtube.com/watch?v=Iwe_RY-fYgI&t=916s))
- Public marketing exclusivity with a single frontier lab is a red flag that the company is shipping a non-frontier product a large fraction of the time; model-agnosticism is a governance posture, not just procurement hygiene. ([Notion's Token Town](../talks/notions-token-town.md), [11:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=694s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Jack Cable](../speakers/jack-cable.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Varsha Shah](../speakers/varsha-shah.md)

