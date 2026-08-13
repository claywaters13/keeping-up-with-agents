---
title: "Moritz Johner"
type: "speaker"
slug: "moritz-johner"
role: "Staff Engineer"
company: "Form3"
talk_count: 1
---

# Moritz Johner

**Staff Engineer &middot; Form3**

Staff Engineer at Form3, focused on Kubernetes, security, and platform engineering. One of the creators and maintainers of external-secrets.

[LinkedIn](https://www.linkedin.com/in/moritz-johner/)

## Talks

- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md) (Security)

## Scheduled Sessions

- **We Gave an Agent Production Code Access and Then Tried to Sleep at Night** &middot; Day 2 — Session Day 1 &middot; 11:40am-12:00pm &middot; Track 5

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

## Quotes

> "A useful coding agent is a supply chain actor, whether you plan for that or not. That's the thesis of this talk, basically."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s)

> "we pushed to production, and eventually Infosec um came around the corner ask a very reasonable question, is this automation, or is it a supply chain incident waiting to happen?"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s)

> "It's not agents are dangerous, or agents are fine. It's the moment where you give an agent um production credentials in order to like be useful, it really becomes a supply chain actor, just like an engineer in your department."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s)

> "at our scale, we have thousands of repositories and it really is a backlog that never empties and you close 10 issues today and you know next week 20 more will arrive"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [0:01](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1s)

> "the vulnerable thing isn't necessarily the thing that these tools can see. For instance, the CVE might live in an OS package that you use in your base image. It's not in your Dockerfile."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [0:52](https://www.youtube.com/watch?v=LqLoYksJ6do&t=52s)

> "So, you don't really have a like a patching problem, you also have like a reasoning problem that you um need to address here."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [2:09](https://www.youtube.com/watch?v=LqLoYksJ6do&t=129s)

> "this deterministic part is very boring on purpose. It's very simple. And inside that, we spawn agents."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [4:08](https://www.youtube.com/watch?v=LqLoYksJ6do&t=248s)

> "It shouldn't just, you know, bump the dependencies to the latest and greatest version. That's just that interest introduces unnecessary risk, which we want to avoid."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [6:07](https://www.youtube.com/watch?v=LqLoYksJ6do&t=367s)

> "the CVE remediation agent actually just modifies files on the file system. It doesn't commit, it doesn't push, it doesn't create a PR, it doesn't watch the CI itself."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [6:07](https://www.youtube.com/watch?v=LqLoYksJ6do&t=367s)

> "It kind of LLMs LLMs kind of tend to just revert the previous changes that it did. So, we got to tell it to not do this."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [7:27](https://www.youtube.com/watch?v=LqLoYksJ6do&t=447s)

> "at the end of every agent invocation, we ask the agent to do a very short and simple retrospective. What went well, what went wrong, what tools are missing, and what kind of context would help the next time it would be invoked."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [8:06](https://www.youtube.com/watch?v=LqLoYksJ6do&t=486s)

> "The dangerous ones, the get up right access, um and trigger UCI is something that we did not give the agent. Instead, we pushed um that functionality out to the deterministic part"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [11:53](https://www.youtube.com/watch?v=LqLoYksJ6do&t=713s)

> "there was like 70,000 lines of code that were changed in that small PR. Um that's really like a lot of changes that come in just by bumping a couple of dependencies."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

> "there um, unknown, um, injection vectors which we aren't aware of yet. Um, so that's why, you know, we still have to pray a little bit. But at least we don't like build the whole system on on hope."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [13:59](https://www.youtube.com/watch?v=LqLoYksJ6do&t=839s)

> "Sandboxes look great on a slide. You just draw a box, put the agent in it and you feel secure, right?"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [13:59](https://www.youtube.com/watch?v=LqLoYksJ6do&t=839s)

> "naturally you give it that Docker socket. At that point, it's more or less game over for you, um, because the agent can then simply just spawn a privileged container, escape out of it"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [14:40](https://www.youtube.com/watch?v=LqLoYksJ6do&t=880s)

> "We run it like that in production at some point. Um, it didn't feel good. We moved off of that"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [14:40](https://www.youtube.com/watch?v=LqLoYksJ6do&t=880s)

> "the existing agent that we have today with Codex and Cloud, they come with their own sandbox, but in my opinion, it's worthless, especially when you give it um a a Docker socket access."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [17:19](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1039s)

> "the gap isn't the tool doesn't exist. All the tools do exist, but most of them are still in the beta phase."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [19:21](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1161s)

> "the blast radius of an agent is an architecture decision."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [20:25](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1225s)

> "that choice, what's that what's deterministic and what's agentic, that really is, you know, your security model in this case."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [21:04](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1264s)

