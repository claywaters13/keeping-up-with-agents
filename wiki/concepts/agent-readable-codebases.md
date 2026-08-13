---
title: "agent-readable codebases"
type: "concept"
slug: "agent-readable-codebases"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 9
---

# agent-readable codebases

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **9** speaker(s)

**Definition:** Restructuring a repository and its documentation so agents can navigate and change it — the codebase as an interface for models.

*Also referred to as: agent-navigable codebases, agent-readable documentation, repo readiness for agents, architecture documentation for agents, codebase structure and hygiene, agent-generated documentation, monorepo architecture, codebase abstraction*

## State of Practice

The field has converged on treating the repository itself — not the prompt, not the model — as the primary lever on agent output. "Agent readiness" was given an operational definition at this conference: the density of deterministic validation loops (types, tests, compilers, evals, lint, CI) present in a codebase, with output quality of long-running agents held to be directly proportional to how well their work can be validated. A second, related move is treating abstractions and API boundaries as control surfaces rather than as ergonomics: tightening an API so an illegal agent action is structurally impossible is reported to beat instructing the agent not to take it (one team drove a data-leakage rate to zero this way). Practitioners also broadly agree that in-repo artifacts — architecture files, design docs, specs, glossaries, skills — outperform training individual engineers, because the repo is what every contributor and every agent shares; and correspondingly that badly-run repos (untagged PRs, no descriptions, no docs) cap what any frontier model can do there. What remains genuinely contested is whether prose docs are trustworthy agent context at all, whether the substrate (language, git, database) should be rebuilt for agents or consolidated onto what agents already write well, and whether a human must still read what ships.

## Consensus

### Agent output quality is set by what is embedded in the repo — structure, docs, config, validation — not by model capability or individual engineer skill, so an un-agent-ready codebase will not benefit from better models.

Support: **5** talk(s)

> "if your code base isn't agent ready, you won't see any of the success of the most capable AI systems in the world today"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [15:21](https://www.youtube.com/watch?v=wpOA-UXynoM&t=921s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Content Is Code](../talks/content-is-code.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### The density of deterministic verification signals in a codebase — types, compilers, tests, evals — is what gates how much autonomy an agent can be given.

Support: **4** talk(s)

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### Codebase abstractions and API boundaries are the real control surface on agent behavior: tightening the interface so a bad action is impossible works better than instructing the agent to avoid it.

Support: **4** talk(s)

> "We then tighten the obstruction to a more strict API where the test data couldn't reach the training and the data leakage rate just dropped to zero."
>
> — [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s)

Supporting talks: [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)

### Written artifacts checked into the repo — architecture files, design/taxonomy docs, specs, glossaries — are first-class agent inputs and must be held to a higher quality bar than the code itself.

Support: **5** talk(s)

> "And we have a very simple rule in our team. Code can be slop, writing cannot."
>
> — [fighting slop with slop](../talks/fighting-slop-with-slop.md), [2:38](https://www.youtube.com/watch?v=AMiyLItEtLA&t=158s)

Supporting talks: [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Content Is Code](../talks/content-is-code.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)

## Disagreements

### Should agents be pointed at prose documentation as ground truth about a codebase, or only at the source code?

| Position A | Position B |
|---|---|
| Maintained prose is essential agent context: docs, skills, cleanly documented specs, and hand-written markdown glossaries are what let agents navigate a repo, and reading a maintained glossary is cheaper and more reliable than having the agent parse the artifact itself.<br>*[Content Is Code](../talks/content-is-code.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* | Docs, READMEs, and architecture files will drift and lie; only the source code and its execution trace can be trusted. Keep a single tiny model-agnostic architecture.md containing nothing that changes within months or years, and enforce everything else through the type system.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md)* |

*Why it matters: It decides whether you fund a documentation-maintenance practice (and pay its drift cost) or invest that budget in tracing, typing, and semantic code-search tooling. Getting it wrong means agents confidently act on stale prose, or that you starve them of context they actually needed.*

### Should the language and tooling substrate be rebuilt for agents, or should teams consolidate onto the language agents already write best?

| Position A | Position B |
|---|---|
| Existing languages were optimized for human productivity and readability, which is the wrong objective now; the correct response is new agent-first languages (with inferred error types, exhaustive compiler proofs, zero-cost full execution tracing) plus new git and new databases — and the language need not even be human-readable.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | Consolidate on TypeScript, because coding agents already default to it, next-generation training will be fed more TypeScript, NPM is the richest ecosystem, and a single Zod schema removes the cross-service type-sync boundary that other stacks force.<br>*[A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)* |

*Why it matters: It is the difference between betting a codebase on compounding model quality in an existing ecosystem versus paying a rewrite/embedding cost for stronger machine-checkable invariants. The two paths imply opposite hiring, tooling, and dependency decisions over the next few years.*

### Must a human still read and understand the code agents write before it ships?

| Position A | Position B |
|---|---|
| Yes — understanding is the durable bottleneck even after correctness checking is automated, because it is the prerequisite for creative participation; gate sending code for team review on being able to pass a quiz about what the agent wrote, and treat review throughput as a real constraint worth investing in.<br>*[Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* | No — code review is not a necessary control if invariants are enforced by tooling and a strong type system; one team does zero code reviews, and within roughly a year generated code will ship unread the way compiler assembly output does.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* |

*Why it matters: It determines whether the scaling investment goes into explanation, shared agent-conversation spaces, and review capacity, or into type systems, tracing, and verification harnesses. Teams that pick wrong either bottleneck on human review or lose the ability to reason about their own system.*

## Practical Guidance

**Do:**

- Define agent readiness concretely as the count of deterministic validation loops in the repo (types, tests, compile, lint, evals), and treat raising that count as the unlock for autonomy.
- Keep one small, model-agnostic architecture.md rather than a tool-specific CLAUDE.md, containing only invariants that will not change for months or years.
- Tighten API boundaries so disallowed agent behavior is structurally impossible — e.g. an interface where test data cannot reach training code — instead of asking the agent not to do it.
- Let each repo's champion choose its agent configuration and let teams with similar repo shapes (web, mobile, monorepo) converge naturally, rather than mandating one setup top-down.
- Point an agent at the ~30-40% of agent-readiness fixes that are low-hanging fruit and let it fix them automatically; budget human workflow change for the remaining ~60%.
- Require a written design/taxonomy doc before engineers join a prototype, including domain context, data representations, and the explicit type contract between the ML repo and the product repo.
- Check in a hand-maintained markdown glossary of a project's content so agents read that instead of the rendered page.
- Build a machine-readable model of every service and how they connect before attempting multi-agent parallelism, and give each agent its own isolated cloud workspace.
- Gate sending code to teammates for review on being able to pass a quiz about what your agent wrote.
- Merge clean, tagged PRs with accurate descriptions that distinguish features, bug fixes, and reverts — downstream content and change-log generation depend on the diff being trustworthy.
- Use stacked diffs so slices can be reviewed asynchronously by the specific subject-matter expert each slice needs.
- Move agent conversations and plans into shared commentable spaces rather than leaving them in individual local terminals, since understanding is a team-level property.

**Avoid:**

- Standardizing which AI coding tool engineers use; standardize codebase invariants instead.
- Making the AI strategy depend on every individual leveling themselves up — it will never produce broad impact.
- Assuming a better model will compensate for a repo with no documentation, no skills, and no PR hygiene.
- Mandating AI code reviewers before the repo is ready and the reviewers are good enough — it just antagonizes engineers.
- Publishing or importing skills that were generated without regard for their contents or structure.
- Running real multi-agent parallelism on local developer machines.
- Letting ML researchers sink time into the persistence layer; have them document how far they got and hand it off as the first software-engineering task.
- Building a demonstration deployment so far ahead of the org's current practice that it gets dismissed as a theme park rather than copied.
- Using grep in agent tooling — ripgrep supersedes it, and a semantic describe tool supersedes both.
- Adding interactive figures by default to explanations; used untastefully they are slop and a crutch.
- Delegating every bug fix to an agent — you forfeit the peripheral feel for the system that debugging it yourself produces.

## Notable Outliers

- A team ships with zero code reviews, no standardization on how engineers use AI, and mandatory parallel work — the type system, not review, is the center of truth that keeps invariants out of the codebase. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [0:01](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1s))
- The agent-oriented programming language we need does not have to be human-readable at all; take inspiration from Lean and very strongly typed languages and make writing code deliberately harder. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [17:17](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1037s))
- In auto-research the codebase abstraction is literally the model architecture and the eval is the loss function — and abstraction is currently the more underrated of the two. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [11:06](https://www.youtube.com/watch?v=iCj_ATyThvc&t=666s))
- Structure, not taste, is the expensive scarce input — clean PRs, tagging, descriptions, knowing what was reverted — and essentially no organization actually does it. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))
- Because generating code is nearly free, writing throwaway software whose only purpose is to help you understand other software is now an everyday technique. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [14:49](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=889s))

## All Talks

- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Content Is Code](../talks/content-is-code.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)

## Speakers

- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Deepak Pathak](../speakers/deepak-pathak.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

