---
title: "We Gave an Agent Production Code Access and Then Tried to Sleep at Night"
type: "talk"
slug: "we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night"
track: "Security"
org: "Form3"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "LqLoYksJ6do"
duration_sec: 1316
word_count: 4022
speakers: ["Moritz Johner"]
---

# We Gave an Agent Production Code Access and Then Tried to Sleep at Night

**Speakers:** [Moritz Johner](../speakers/moritz-johner.md)

**Org:** Form3

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 56s

[Watch on YouTube](https://www.youtube.com/watch?v=LqLoYksJ6do)

## Summary

Moritz Johner of Form3 describes Patch Pilot, an in-house agentic system that remediates CVEs across thousands of repositories and container images, and the security architecture that made Infosec comfortable with it running in production. His central argument is that any coding agent with production credentials is a supply chain actor and should be governed with the same guardrails as a human engineer. The design splits the system into a deterministic Go orchestrator that holds the dangerous capabilities (GitHub write, CI triggering) and agent invocations that only mutate files on disk, deliberately shrinking the blast radius of prompt injection. He also covers why off-the-shelf agent sandboxes fail once you hand an agent a Docker socket, and why they moved to Firecracker micro VMs with Vsock-mediated network policy. Worth watching if you're deciding what an agent should and shouldn't be allowed to do in a regulated production environment.

## Key Points

- Dependabot and Renovate only see manifests, so CVEs living in base-image OS packages or in binaries downloaded during a Docker build are invisible to them.
- Dependency patching is a reasoning problem, not just a version-bump problem: bumping the Go runtime can force a linter bump, which introduces new lint rules that break the codebase.
- Patch Pilot has two layers — a deliberately boring deterministic Go orchestrator that discovers vulnerable OCI images and maps them to source repositories, and spawned agents that handle reasoning tasks like diagnosing CI failures.
- The CVE remediation agent only modifies files on the filesystem; committing, pushing, opening PRs, and triggering CI are all done by the deterministic layer, so the agent never holds those credentials.
- The agent is instructed to make the smallest effective change that fixes the specific CVE rather than bumping everything to latest, since gratuitous upgrades add risk.
- Every agent invocation ends with a short retrospective (what went well, what went wrong, what tools and context were missing), which is aggregated across PRs as a stand-in for the agent observability tooling that doesn't yet exist.
- Prompt injection is treated as unsolvable, so mitigation is blast-radius limitation plus prompt steering about untrusted directories (vendor dirs, CI logs) and a purpose-built eval repository containing planted injection attempts.
- Giving an agent the Docker socket defeats any in-process sandbox — it can spawn a privileged container and escape — so they moved to Firecracker micro VMs with the Docker socket inside its own kernel and all network traffic forced through a Vsock to a host process that applies policy.
- Sandboxing tooling exists (micro sandbox, sandbox-as-a-service vendors, Kubernetes agent sandbox SIG, open sandbox) but is still beta and short of enterprise features.

## Notable Quotes

> "A useful coding agent is a supply chain actor, whether you plan for that or not. That's the thesis of this talk, basically."
>
> — [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s) &middot; *The talk's explicit thesis, stated as such.*

> "we pushed to production, and eventually Infosec um came around the corner ask a very reasonable question, is this automation, or is it a supply chain incident waiting to happen?"
>
> — [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s) &middot; *Frames the entire security review that motivated the architecture.*

> "It's not agents are dangerous, or agents are fine. It's the moment where you give an agent um production credentials in order to like be useful, it really becomes a supply chain actor, just like an engineer in your department."
>
> — [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s) &middot; *Refuses both extremes of the agent-safety debate and locates the risk in credential grant.*

> "at our scale, we have thousands of repositories and it really is a backlog that never empties and you close 10 issues today and you know next week 20 more will arrive"
>
> — [0:01](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1s) &middot; *Quantifies the scale problem that justifies automation.*

> "the vulnerable thing isn't necessarily the thing that these tools can see. For instance, the CVE might live in an OS package that you use in your base image. It's not in your Dockerfile."
>
> — [0:52](https://www.youtube.com/watch?v=LqLoYksJ6do&t=52s) &middot; *The concrete gap in existing patching tools.*

> "So, you don't really have a like a patching problem, you also have like a reasoning problem that you um need to address here."
>
> — [2:09](https://www.youtube.com/watch?v=LqLoYksJ6do&t=129s) &middot; *The core justification for using an agent rather than a script.*

> "this deterministic part is very boring on purpose. It's very simple. And inside that, we spawn agents."
>
> — [4:08](https://www.youtube.com/watch?v=LqLoYksJ6do&t=248s) &middot; *States the architectural principle in one line.*

> "It shouldn't just, you know, bump the dependencies to the latest and greatest version. That's just that interest introduces unnecessary risk, which we want to avoid."
>
> — [6:07](https://www.youtube.com/watch?v=LqLoYksJ6do&t=367s) &middot; *A minimal-change patching policy others might disagree with.*

> "the CVE remediation agent actually just modifies files on the file system. It doesn't commit, it doesn't push, it doesn't create a PR, it doesn't watch the CI itself."
>
> — [6:07](https://www.youtube.com/watch?v=LqLoYksJ6do&t=367s) &middot; *The precise capability boundary that defines their security model.*

> "It kind of LLMs LLMs kind of tend to just revert the previous changes that it did. So, we got to tell it to not do this."
>
> — [7:27](https://www.youtube.com/watch?v=LqLoYksJ6do&t=447s) &middot; *A specific, reusable failure mode of agents fixing their own CI breakage.*

> "at the end of every agent invocation, we ask the agent to do a very short and simple retrospective. What went well, what went wrong, what tools are missing, and what kind of context would help the next time it would be invoked."
>
> — [8:06](https://www.youtube.com/watch?v=LqLoYksJ6do&t=486s) &middot; *A concrete, transferable observability technique.*

> "The dangerous ones, the get up right access, um and trigger UCI is something that we did not give the agent. Instead, we pushed um that functionality out to the deterministic part"
>
> — [11:53](https://www.youtube.com/watch?v=LqLoYksJ6do&t=713s) &middot; *The central design decision, stated directly.*

> "there was like 70,000 lines of code that were changed in that small PR. Um that's really like a lot of changes that come in just by bumping a couple of dependencies."
>
> — [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s) &middot; *Reports a number showing why prompt injection surface is unavoidably large.*

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s) &middot; *Explicit position on prompt injection defense.*

> "there um, unknown, um, injection vectors which we aren't aware of yet. Um, so that's why, you know, we still have to pray a little bit. But at least we don't like build the whole system on on hope."
>
> — [13:59](https://www.youtube.com/watch?v=LqLoYksJ6do&t=839s) &middot; *Honest statement of residual risk, rare in vendor-adjacent talks.*

> "Sandboxes look great on a slide. You just draw a box, put the agent in it and you feel secure, right?"
>
> — [13:59](https://www.youtube.com/watch?v=LqLoYksJ6do&t=839s) &middot; *Sets up the sandbox critique that follows.*

> "naturally you give it that Docker socket. At that point, it's more or less game over for you, um, because the agent can then simply just spawn a privileged container, escape out of it"
>
> — [14:40](https://www.youtube.com/watch?v=LqLoYksJ6do&t=880s) &middot; *Names the specific escape path that broke their first design.*

> "We run it like that in production at some point. Um, it didn't feel good. We moved off of that"
>
> — [14:40](https://www.youtube.com/watch?v=LqLoYksJ6do&t=880s) &middot; *Admits they shipped the insecure version before fixing it.*

> "the existing agent that we have today with Codex and Cloud, they come with their own sandbox, but in my opinion, it's worthless, especially when you give it um a a Docker socket access."
>
> — [17:19](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1039s) &middot; *A sharp, contestable claim about mainstream coding agents.*

> "the gap isn't the tool doesn't exist. All the tools do exist, but most of them are still in the beta phase."
>
> — [19:21](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1161s) &middot; *Summarizes the state of the agent-sandboxing ecosystem.*

> "the blast radius of an agent is an architecture decision."
>
> — [20:25](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1225s) &middot; *The talk's one-line takeaway.*

> "that choice, what's that what's deterministic and what's agentic, that really is, you know, your security model in this case."
>
> — [21:04](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1264s) &middot; *Reframes an engineering split as the security boundary itself.*

## Positions

- Any coding agent given production credentials is a supply chain actor and must be subject to the same guardrails as a human engineer. ([2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s), confidence: stated)
- Manifest-based patching tools like Dependabot and Renovate structurally cannot fix CVEs that live in base images or build-time downloaded binaries. ([0:52](https://www.youtube.com/watch?v=LqLoYksJ6do&t=52s), confidence: stated)
- Dependency patching requires reasoning, not just version bumping, because patches cascade into linter upgrades and codebase changes. ([2:09](https://www.youtube.com/watch?v=LqLoYksJ6do&t=129s), confidence: stated)
- Agents should never hold write credentials (GitHub push, PR creation, CI triggering); those belong in a deterministic layer. ([11:53](https://www.youtube.com/watch?v=LqLoYksJ6do&t=713s), confidence: stated)
- Prompt injection cannot be solved, only contained by limiting blast radius. ([12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s), confidence: stated)
- The built-in sandboxes shipped with Codex and Claude are worthless once the agent has Docker socket access. ([17:19](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1039s), confidence: stated)
- Giving an agent a Docker socket is equivalent to giving it host compromise, since it can spawn a privileged container and escape. ([14:40](https://www.youtube.com/watch?v=LqLoYksJ6do&t=880s), confidence: stated)
- Existing Linux sandboxing primitives (landlock, bubblewrap, seccomp, Kaniko, buildkit) do not compose well with containers and cannot contain a Docker daemon. ([15:18](https://www.youtube.com/watch?v=LqLoYksJ6do&t=918s), confidence: stated)
- Micro VMs (Firecracker) with Vsock-mediated networking are currently the right isolation boundary for agents that need Docker. ([15:56](https://www.youtube.com/watch?v=LqLoYksJ6do&t=956s), confidence: stated)
- Agents should be instructed to make the smallest effective change that fixes the specific CVE, because bumping to latest introduces unnecessary risk. ([6:07](https://www.youtube.com/watch?v=LqLoYksJ6do&t=367s), confidence: stated)
- The agent sandboxing tooling ecosystem exists but is still beta and not ready for enterprise deployment. ([19:58](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1198s), confidence: stated)
- Micro sandbox would be the right choice for building this system today, over rolling your own micro VM plumbing. ([18:37](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1117s), confidence: stated)
- Asking agents for a per-invocation retrospective is a workable substitute for the agent observability tooling that does not yet exist. ([8:44](https://www.youtube.com/watch?v=LqLoYksJ6do&t=524s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)

