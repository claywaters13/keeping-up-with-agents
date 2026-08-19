---
title: "Designing Agents (The Floor Is the Frontier)"
type: "talk"
slug: "designing-agents-the-floor-is-the-frontier"
track: "Memory & Continual Learning"
org: "Raindrop"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "jHMiYtjoJfA"
duration_sec: 1185
word_count: 4051
speakers: ["Ben Hylak"]
---

# Designing Agents (The Floor Is the Frontier)

**Speakers:** [Ben Hylak](../speakers/ben-hylak.md)

**Org:** Raindrop

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 45s

[Watch on YouTube](https://www.youtube.com/watch?v=jHMiYtjoJfA)

## Summary

Ben Hylak, CTO and co-founder of Raindrop, argues that most of the value in improving production agents comes from raising the floor — eliminating the worst things an agent can do — rather than chasing ceiling capabilities or benchmark scores. He claims the prevailing eval discourse is stuck in the chatbot era: large hand-built eval sets break the moment you swap models or harnesses, and almost nobody actually delays a model upgrade to rewrite them. His prescription is that evals should live in the repo as code (unit/end-to-end tests), and that production issue detection should mirror ordinary telemetry: for every issue you must know when it started and what percent of users it affects. He closes with three tactical lessons from Raindrop's own work — clusters are not issues, code-mode classifiers over traces scale to production volume, and agents are bad at finding anomalies but good at investigating ones you found deterministically. Worth watching if you own a deployed agent and are unsure whether your eval investment is safety or theater; it is short, slide-light, and opinionated rather than a framework tour.

## Key Points

- Despite being programmed into a "continual learning" track, Hylak opens by asserting that essentially no real-world products or labs are actually shipping continual learning today.
- Large offline eval suites are fragile: they break when you change models or switch harnesses (he cites moving to Claude Code CLI invalidating ~80% of tool-call evals), so months invested in them mostly slows teams down.
- The practical test of whether an eval regime is real: would you actually delay adopting a new model by two weeks to update your evals? Most teams would say no, which reveals the evals as theater.
- Because the prompt is now the entire harness and codebase rather than a string, cloud-hosted prompt playgrounds have largely fallen out of use and evals should be written as code — tests run locally, e.g. Sentry's Vitest evals or what OpenAI calls macro evals.
- Floor raising (preventing the worst outcomes — recommending a competitor, deleting data, sending slop to a customer) matters more than ceiling capability because floor failures are what break user trust, and societal harms like sycophancy live on the floor side.
- For every production issue you need exactly two facts: when it started (which points at what changed) and what percent of users it affects (three users versus 100,000 is a different problem).
- The right approach depends heavily on user volume: at tens of millions of messages a day, experiments on a small free-tier sample are extremely valuable; with five or ten users, A/B tests are useless even if correctness is critical.
- Clustering traces is useful for one-off error analysis but doesn't scale as an issue-tracking primitive — clusters are hard to track reliably over time, you don't control boundaries, and semantically similar clusters can have completely different root causes.
- Code mode generalizes beyond MCP: write classifiers, run them in a sandbox against traces, and they scale to production volume.
- Agents are bad at anomaly detection but good at investigation — pull out deterministic signals like keyword frequency spikes first, then hand the agent something tractable to investigate.

## Notable Quotes

> "I think it's like notable that in the real world, there's really not that much continual learning, right?"
>
> — [0:01](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1s) &middot; *Opens by contradicting the premise of the track he was invited to speak in.*

> "Uh if you look at like the labs, if you look at like products that are in the real world, you really don't see a lot of continual learning."
>
> — [0:48](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=48s) &middot; *States the empirical claim behind the contrarian opening.*

> "you can do that uh but those evals like break as soon as you have a new model, as soon as you like switch harnesses"
>
> — [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s) &middot; *The core failure mode he attributes to big hand-built eval sets.*

> "the one thing I could promise you is that things are going to keep changing."
>
> — [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s) &middot; *The assumption that drives his whole argument against heavy eval investment.*

> "I think the whole thing here is like you want more safety but you you don't want theater"
>
> — [4:44](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=284s) &middot; *Names the tradeoff the talk is organized around.*

> "Do you actually delay it 2 weeks to update your evals or not, right? I I think most people would say no."
>
> — [5:17](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=317s) &middot; *A concrete, checkable test for whether a team's evals are real.*

> "the word eval is like uh more or less a meaningless word. It literally is just like you're evaluating something, right?"
>
> — [8:16](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=496s) &middot; *Direct swipe at the field's central term, motivating his benchmark-maxer/floor-raiser split.*

> "companies start borrowing like the language that like labs are using and like even copying similar benchmarks, but they're doing completely different things, right?"
>
> — [8:16](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=496s) &middot; *Explains why lab evaluation practice transfers badly to application teams.*

> "When the way that we start thinking about it with customers is something like this, which is like, are you a benchmark maxer or a floor raiser?"
>
> — [7:39](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=459s) &middot; *The framing device the rest of the talk hangs on.*

> "the floor is like what is the worst thing your agent can do? Like recommend a competitor or like delete a bunch of data"
>
> — [10:33](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=633s) &middot; *Defines the talk's title concept with concrete failure examples.*

> "I think that like the floor is very interesting because I think that that is the thing that like breaks user trust."
>
> — [10:33](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=633s) &middot; *The argument for prioritizing floor over ceiling.*

> "the prompt is actually like the whole thing now. It's like all the code. It's all It's your whole harness."
>
> — [11:57](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=717s) &middot; *Justifies why prompt playgrounds died and evals must become code.*

> "I actually don't know many companies that use some sort of like managed prompt like in the cloud anymore."
>
> — [11:57](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=717s) &middot; *An observation from Raindrop's customer base that contradicts a whole tooling category.*

> "what I think that means is the evals themselves actually should look a lot more like code. In other words, like a lot more like tests."
>
> — [11:57](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=717s) &middot; *The talk's main methodological prescription.*

> "for each issue, you really need to know two things. You need to know when it actually started, and you need to know how many people it affects."
>
> — [13:04](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=784s) &middot; *The two-fact requirement that his critique of clustering rests on.*

> "I think agents will have an infinite number of problems. That's sort of like the the great and terrible thing about them."
>
> — [14:06](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=846s) &middot; *Why triage, not exhaustive coverage, is the realistic goal.*

> "we have customers with millions of users and we have customers with like five."
>
> — [14:06](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=846s) &middot; *Grounds his claim that method must scale to user volume.*

> "if you have five or 10 users, like uh, I would not recommend, you know, experiments or AB tests"
>
> — [14:41](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=881s) &middot; *A specific negative recommendation tied to scale.*

> "the first one is that clusters are not issues. So, um, the sort of like naive approach that we've seen either customers or also, sometimes competitors, uh, take is like, well, you just take all the traces and you just cluster it"
>
> — [15:53](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=953s) &middot; *The most pointed of his three tactical lessons, aimed at a common tooling pattern.*

> "with clusters, it's very, very hard to reliably, uh, track over time."
>
> — [17:00](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1020s) &middot; *The technical reason clustering fails as an issue-tracking primitive.*

> "code mode actually really scales. Like you've heard about code mode in the context of MCPs. Um I highly recommend just uh trying to apply this to traces."
>
> — [17:48](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1068s) &middot; *Transfers a known pattern to a new domain, with a scale claim attached.*

> "Last lesson here is that agents are very, very bad at anomaly detection. So don't ask your agent to find anomalies. Uh ask it to investigate anomalies you've already found."
>
> — [18:30](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1110s) &middot; *A crisp capability boundary and the resulting architecture rule.*

## Positions

- Very little genuine continual learning exists in shipped products or at the labs today. ([0:01](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1s), confidence: stated)
- Large hand-built eval datasets break when you change models or harnesses — switching to Claude Code CLI can invalidate roughly 80% of tool-call evals. ([4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s), confidence: stated)
- Teams should not invest months building eval sets, because the rate of change in models and harnesses will obsolete them. ([4:44](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=284s), confidence: stated)
- Most teams would not delay a model upgrade by two weeks to update their evals, which shows the evals are not load-bearing. ([5:17](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=317s), confidence: stated)
- "Eval" has become a near-meaningless word because labs and application companies use it for fundamentally different activities. ([8:16](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=496s), confidence: stated)
- Application companies have different responsibilities from labs — encoding company-specific domain knowledge rather than general capability — so they should not copy lab benchmark practice. ([8:47](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=527s), confidence: stated)
- Floor failures, not ceiling limitations, are what break user trust and cause the societally worst outcomes such as sycophancy. ([10:33](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=633s), confidence: stated)
- Cloud-hosted prompt playgrounds and managed prompts are largely obsolete because the prompt is now the entire harness and codebase. ([11:57](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=717s), confidence: stated)
- Evals should be written and run as local tests in code (e.g. Sentry's Vitest evals, OpenAI's macro evals) rather than managed in a separate eval product. ([12:25](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=745s), confidence: stated)
- Effective agent issue tracking requires knowing when an issue started and what percent of users it affects; without both you cannot prioritize. ([13:04](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=784s), confidence: stated)
- At high volume (tens of millions of messages a day) experiments on a free-tier sample are highly valuable, but with five to ten users A/B tests should not be used. ([14:41](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=881s), confidence: stated)
- Clustering traces does not scale as an issue-detection method: clusters are hard to track over time, boundaries are uncontrollable, and one cluster can span unrelated root causes. ([16:26](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=986s), confidence: stated)
- Writing classifiers as code and running them in a sandbox over traces scales to production volume. ([17:48](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1068s), confidence: stated)
- Agents cannot reliably detect anomalies; deterministic signals such as keyword frequency should surface candidates and the agent should only investigate them. ([18:30](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1110s), confidence: stated)
- Most teams should not train their own frontier-level model and are better off waiting to incorporate new lab models into their product. ([7:39](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=459s), confidence: stated)
- The higher the user's own responsibility for correct operation (autocomplete vs. Devin vs. an AI doctor), the more the evaluation burden shifts onto the product builder. ([9:58](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=598s), confidence: implied)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [benchmark design](../concepts/benchmark-design.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [online evaluation](../concepts/online-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)

