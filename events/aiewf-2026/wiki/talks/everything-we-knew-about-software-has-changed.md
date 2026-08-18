---
title: "Everything we knew about software has changed"
type: "talk"
slug: "everything-we-knew-about-software-has-changed"
track: "Claws & Personal Agents"
org: "@t3dotgg ​"
day: "Day 2 — Session Day 1"
room: "Track 1"
video_id: "xUnRQ9vLXxo"
duration_sec: 961
word_count: 3235
speakers: ["Benjamin Guo", "Rob Cheung"]
---

# Everything we knew about software has changed

*Program title: Everyone Gets A Software Company*

**Speakers:** [Benjamin Guo](../speakers/benjamin-guo.md), [Rob Cheung](../speakers/rob-cheung.md)

**Org:** @t3dotgg ​

**Track:** Claws & Personal Agents &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 16m 01s

[Watch on YouTube](https://www.youtube.com/watch?v=xUnRQ9vLXxo)

## Summary

Theo Browne argues that the jump from Sonnet 3.5 to Opus 4.5 to Mythos represents three distinct eras — reliable tool calling, long-running tasks, and now self-orchestration — and that the bottleneck has shifted from the models to developers' own ambition. Because the models improve faster than we do, he says the response isn't to get better but to build bigger: the tiers of what counts as a side project, a startup, and a too-big idea have each shifted down one level. Getting there requires discarding inherited developer identity and habits — terminal worship, language tribalism, sunk-cost attachment to code — which he frames as software engineering's 'skeuomorphic phase,' analogous to pre-iOS 7 apps that mimicked physical objects instead of being useful. He closes with a strategy argument: startups no longer have to win on depth alone, because breadth is now buildable, and products architected for user extension (Slack being the accidental example) let users fill their own gaps. Worth watching for the tier-shift framing and the 'your product is now a markdown file' provocation; it's a mindset talk, not a technical how-to.

## Key Points

- Browne frames recent models as eras rather than increments: Sonnet 3.5 made tool calls reliable enough for day-to-day code work, Opus 4.5 sustained hours-long tasks without losing the thread, and Mythos is the first model that understands itself well enough to spawn sub-models, split up work, and verify it.
- Getting orchestration behavior out of Mythos requires no custom harness or 'software factory' — you just prompt it to go further, which he thinks most people underestimate.
- He publicly retracts his earlier claim that model progress had hit a wall, and argues that since models are improving faster than engineers can, the only viable response is to attempt bigger projects rather than to try to get personally better.
- Developers are in a 'skeuomorphic phase,' clinging to terminals, Vim, language identity, and Git conventions like uncommittable env files out of familiarity rather than because those choices are correct.
- The tiers of project ambition have each dropped one level: what was a startup is now a side project, what was too big is now a startup, and a new bottom tier exists where an entire product is a markdown file piped to Codex or Claude on a cron.
- He replaced a PR-triage service with a markdown file that runs at 9:00 a.m. daily, reviews open PRs across four repos, prioritizes his work, and publishes a static HTML report to S3.
- The old startup playbook of winning on depth because you could never match AWS's breadth is obsolete — you can now build, for example, a database platform into your product in a day or two of prompting, even if it won't match RDS's reliability.
- Products should be architected so users can build the missing vertical features themselves; Slack accidentally became the platform people run agents in despite being, in his view, a bad product, because its bot APIs are the right shape.

## Notable Quotes

> "Mythos is another jump to orchestration. It feels to me like it's the first model that doesn't just understand your code base, but it understands itself."
>
> — [2:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=148s) &middot; *The talk's central capability claim and the definition of the current model era.*

> "And it knows how to spawn additional models and break up work in a way where it could be completed more reliably and then verified afterwards. And if you tell the model to do that, it will just do it. You don't need some custom tooling, some custom system, some fancy software factory."
>
> — [2:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=148s) &middot; *Directly contradicts the prevailing build-an-orchestration-framework advice at agent conferences.*

> "You're not going to see the benefits going forward if you're not pushing the model further, you're not pushing yourself further with what you're building."
>
> — [2:57](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=177s) &middot; *States the thesis that the bottleneck has moved from model to user ambition.*

> "Most of the Jira tickets I closed in my previous job could be trivially solved with a model like Opus 4.5. My previous work would not benefit from a model like Mythos."
>
> — [2:57](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=177s) &middot; *A concrete, falsifiable claim that frontier models are wasted on typical enterprise ticket work.*

> "I was wrong when I claimed that we were hitting a wall before."
>
> — [2:57](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=177s) &middot; *An explicit public retraction from a commentator known for the scaling-wall position.*

> "The models are getting better faster than we are. So, we can't necessarily get better. So, instead we have to go bigger."
>
> — [3:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=208s) &middot; *The compressed argument of the entire talk.*

> "We're currently in our skeuomorphic phase as software developers. Skeuomorphism is this design aesthetic trying to represent the way things used to look, the physical goods that we relied on, and try to make them digital."
>
> — [5:49](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=349s) &middot; *Introduces the organizing metaphor the middle third of the talk runs on.*

> "We're pretending our terminals are the ultimate interface when they're not even good interfaces. And I'm saying this as someone who loves their terminal deeply."
>
> — [5:49](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=349s) &middot; *A direct swipe at the terminal-first agent tooling consensus, hedged by self-implication.*

> "Natural language has no place in a terminal, but we pretend it does because the terminal's familiar."
>
> — [6:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=388s) &middot; *The sharpest interface-design position in the talk and the most contestable.*

> "When I have a team of engineers that are working on a project, why do I have to build another system to share this specific file, but all the other files can go and get just fine?"
>
> — [7:00](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=420s) &middot; *Grounds the abstract 'inherited habits' argument in a concrete daily annoyance.*

> "is this how we do things cuz it's right, or is this how we do things cuz it's just how we've always done it?"
>
> — [7:00](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=420s) &middot; *The reusable test he offers the audience for auditing their own practices.*

> "why are we so scared of deleting code? I cannot tell you how many times I've been in a conversation with someone where the solution is to just delete it and reset, but we have such a bad sunk cost mindset in this industry."
>
> — [8:30](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=510s) &middot; *Names sunk cost as a specific cultural obstacle to working at agent speed.*

> "Now that the models are bigger, the tiers have shifted. Everything is now one tier lower. And this is a crazy thing for me to process. The fact that what used to be a startup is now a side project."
>
> — [10:49](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=649s) &middot; *The tier-shift framing is the most portable idea in the talk.*

> "the fact that you can now execute markdown by just piping it to Codex or Claude is unbelievable and I think most of us haven't fully appreciated how insane that is"
>
> — [11:24](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=684s) &middot; *Compresses the new bottom tier into one mechanism anyone can try.*

> "I had a service that would triage all of my PRs, have them all get reviewed with AI and then help me prioritize. That service is a markdown file now."
>
> — [11:24](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=684s) &middot; *First-person evidence for the claim that whole products collapse into prompts.*

> "There's breadth and depth to any piece of software. The breadth is the range of things that your software covers. And the depth is the number of features in a given area."
>
> — [13:06](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=786s) &middot; *Sets up the strategy argument that closes the talk.*

> "I'm not saying you can build something as reliable as RDS. I'm saying that you can build a database platform into your product in a day or two of work with enough prompting and enough effort."
>
> — [14:15](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=855s) &middot; *A specific, bounded effort estimate with an explicit reliability caveat.*

> "Slack sucks. It's not a good product, but it's the right shape for people to build the features they want into it through the somewhat functional Slack bot APIs."
>
> — [14:55](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=895s) &middot; *Argues architecture shape beats product quality when users can build their own features.*

> "It's time to build your own AWS. It's time to challenge Salesforce directly. It sounds stupid, but I'm going to be real. If your idea doesn't feel stupid, it's cuz your idea's not big enough."
>
> — [15:27](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=927s) &middot; *The closing heuristic the whole talk builds toward.*

## Positions

- Sonnet 3.5, Opus 4.5, and Mythos represent three distinct capability eras — reliable tool calling, long-running multi-hour tasks, and self-orchestration — rather than incremental coding improvements. ([1:55](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=115s), confidence: stated)
- Mythos will spawn additional models, split up work, and verify it if you simply prompt it to, with no custom orchestration tooling or 'software factory' required. ([2:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=148s), confidence: stated)
- His earlier claim that model progress was hitting a wall was wrong; models are now improving faster than developers can improve. ([2:57](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=177s), confidence: stated)
- Most Jira-ticket-scale enterprise work is already trivially solvable by Opus 4.5 and gains nothing from a more capable model like Mythos. ([2:57](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=177s), confidence: stated)
- Because you cannot outpace the models, the correct response is to increase project ambition rather than to try to improve your own skills. ([3:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=208s), confidence: stated)
- iOS 7's move away from skeuomorphism produced a genuinely more useful interface, not a design downgrade. ([4:33](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=273s), confidence: stated)
- Terminals are not good interfaces, and natural language does not belong in one — developers use them out of familiarity and identity. ([6:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=388s), confidence: stated)
- Conventions like not committing env files are arbitrary artifacts of Git's original narrow purpose, not defensible engineering practice. ([7:00](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=420s), confidence: stated)
- Identifying professionally with specific programming languages was always near-meaningless and matters even less now. ([7:59](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=479s), confidence: stated)
- Every tier of project ambition has shifted down one level: former startups are now side projects, and a new bottom tier exists where the whole product is a markdown file. ([10:49](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=649s), confidence: stated)
- Many companies presenting at this event have products whose entire functionality could be replaced by a markdown file. ([11:24](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=684s), confidence: stated)
- Agents themselves show a preference for Vercel over AWS for front-end-leaning full-stack work. ([13:42](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=822s), confidence: stated)
- The startup rule that you must compete on depth because breadth is unreachable no longer holds — broad feature range is now viable for small teams. ([14:15](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=855s), confidence: stated)
- A production-usable database platform can be built into a product in one to two days of prompting, though not at RDS-level reliability. ([14:15](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=855s), confidence: stated)
- If you architect for extensibility, missing vertical features stop being your problem because users can build them themselves. ([14:15](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=855s), confidence: stated)
- Slack succeeded as an agent platform because of its extensible shape, not product quality — it is a bad product that is the right shape. ([14:55](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=895s), confidence: stated)
- An idea that doesn't feel stupid is not ambitious enough for current model capabilities. ([15:27](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=927s), confidence: stated)
- Nobody currently knows what counts as 'too big' anymore, and finding that boundary requires deliberately attempting projects that seem unreasonable. ([12:33](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=753s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [background agents](../concepts/background-agents.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

