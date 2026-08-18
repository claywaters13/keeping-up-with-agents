---
title: "Sumaiya Shrabony"
type: "speaker"
slug: "sumaiya-shrabony"
talk_count: 1
---

# Sumaiya Shrabony

## Talks

- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [audit trails](../concepts/audit-trails.md)
- [entity resolution](../concepts/entity-resolution.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [structured output contracts](../concepts/structured-output-contracts.md)

## Quotes

> "If you build long enough, specially alone, you will start building something completely different. Something that looks suspiciously like CICD. Except worse, because you're building it from scratch, one failure at a time."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [0:00](https://www.youtube.com/watch?v=WLXxTaPagA8&t=0s)

> "And the most useful thing I learned from building this was not how to build better prompts. It was recognizing the five controls I was rebuilding badly and what you can do instead."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [0:00](https://www.youtube.com/watch?v=WLXxTaPagA8&t=0s)

> "But here's the thing that matters for this talk, not the content. What matters is that this system has seven handoffs."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [0:49](https://www.youtube.com/watch?v=WLXxTaPagA8&t=49s)

> "Every single handoff is the place where the system can lie to you. And if you're building the system alone, nobody catches the lies except you, usually after the damage is done."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [1:39](https://www.youtube.com/watch?v=WLXxTaPagA8&t=99s)

> "One skill changes its output schema, so three skills downstream break. You decided to add a validation at the boundary because of it. You just reinvented contract testing."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [2:24](https://www.youtube.com/watch?v=WLXxTaPagA8&t=144s)

> "The reason the title says worst version isn't because agents are software builds, it's because you end up needing the exact same operational guarantees."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [2:24](https://www.youtube.com/watch?v=WLXxTaPagA8&t=144s)

> "The dangerous failure in an agent system is never a bad output. A bad output is very easy to fix."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [3:17](https://www.youtube.com/watch?v=WLXxTaPagA8&t=197s)

> "That is the agent equivalent of shipping because the code compiled, but the tests never run."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [3:17](https://www.youtube.com/watch?v=WLXxTaPagA8&t=197s)

> "This is why agent demos are misleading. They always show you the happy path."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [4:58](https://www.youtube.com/watch?v=WLXxTaPagA8&t=298s)

> "Claim bearing content cannot ship without a verification trail. "Trust me" is not a verifier."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [6:40](https://www.youtube.com/watch?v=WLXxTaPagA8&t=400s)

> "If your agent system makes claims about data, about users, about anything, and you don't have a validation chain, you're shipping unverified assertions with a professional looking wrapper."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [6:40](https://www.youtube.com/watch?v=WLXxTaPagA8&t=400s)

> "If your system keeps generating near duplicates, your system looks automated, even if every individual piece is technically fine. Your audience notices before you do."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [7:35](https://www.youtube.com/watch?v=WLXxTaPagA8&t=455s)

> "That audit record is boring, but when a scheduled run fails at 2:00 a.m., the final artifact alone is not enough. You need to know which gate failed."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [7:35](https://www.youtube.com/watch?v=WLXxTaPagA8&t=455s)

> "You don't need a platform. You don't need a framework. You don't need the ecosystem to catch up. What you need are a few boring gates."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [8:23](https://www.youtube.com/watch?v=WLXxTaPagA8&t=503s)

> "In software, we learned not to deploy only because code exists. In agent systems, we need to learn not to ship just because the artifacts look complete."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [9:13](https://www.youtube.com/watch?v=WLXxTaPagA8&t=553s)

> "Pick the most expensive handoff. Not the most complex, most expensive. The one where bad data can cost you the most."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

> "A gate which logs only warnings is not a gate. It's a suggestion. The gate needs to block the artifact from moving forward."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

> "That's the difference between an impressive demo and an operable system. Before you add another agent, add one boundary."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

