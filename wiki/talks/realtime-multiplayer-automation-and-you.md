---
title: "Realtime multiplayer, automation, and you!"
type: "talk"
slug: "realtime-multiplayer-automation-and-you"
track: "Agentic Engineering"
org: "GitHub"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "iQ5xldZ9StU"
duration_sec: 1300
word_count: 4111
speakers: ["Idan Gazit"]
---

# Realtime multiplayer, automation, and you!

**Speakers:** [Idan Gazit](../speakers/idan-gazit.md)

**Org:** GitHub

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 21m 40s

[Watch on YouTube](https://www.youtube.com/watch?v=iQ5xldZ9StU)

## Summary

Idan Gazit, who leads GitHub Next (GitHub's labs team), argues that the next phase of AI-assisted software development is not multiplying individual productivity but automating routine judgment work and making team collaboration real-time. He demos two prototypes: Agentic Workflows, markdown-defined background automations that compile into GitHub Actions with deterministic YAML guardrails (permissions, network allowlists, "safe outputs"), and Ace, a Slack-like multiplayer interface where sessions are cloud micro-VMs branched from your repo and agents act on the team's chat backscroll and co-edited plan documents. His central claim is that background automation will become a bigger category than interactive AI, and that since typing is only ~5% of a developer's time, tools must now attack the other 95%. Worth watching for the concrete security model around unsupervised agents and for a credible sketch of what post-Slack, post-IDE team surfaces look like. Light on evaluation or failure modes — it's a vision-plus-demo talk, and one demo visibly stalls on conference Wi-Fi.

## Key Points

- The durable theme of this moment is shifting AI value from personal productivity (more parallel copies of me) to group productivity, because a team's shared understanding, not an individual's, is what gates shipping.
- Agentic Workflows are authored as plain markdown — roughly a Slack message you'd send a junior developer — and compiled into GitHub Actions YAML that you never read, making the English the source code and easy to iterate on.
- Guardrails must be deterministic configuration (read-only permissions, tool allowlists, network domain allowlists, and single-PR "safe outputs"), not prompt instructions, because a prompt-injected agent will ignore prompted rules.
- Explicitly permitting an agent to do nothing matters: at automation scale the real failure mode is agents denial-of-servicing their owners with noise.
- Four security principles: defense in depth, never let an agent see a secret (treat any secret it can read as already compromised — Agentic Workflows keeps secrets outside the agent's jail and brokers calls), stage and vet all writes, and log everything for auditability.
- Automation now covers tasks that need basic judgment rather than heuristics — the Home Assistant project's first workflow walks Python stack traces on incoming issues to decide whether the bug is first-party or third-party and auto-closes if not.
- Ace runs every session as a cloud micro-VM on a repo branch and lets agents read the whole team conversation, so "yo, Ace, do it" resolves a long back-and-forth into the final agreed state without re-specifying it.
- Plans and specs become co-edited markdown documents in a docs folder, pointing toward a workflow where you change software by editing a document and telling the AI to make the document true.
- A longitudinal study of ~100 developers over thousands of hours found hands-on-keyboard typing is only about 5% of the job, which is exactly the slice existing AI tools have optimized.

## Notable Quotes

> "the greatest value doesn't come from multiplying me into more me. It comes from enabling groups of people to do more. That's always been true."
>
> — [2:42](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=162s) &middot; *The thesis of the talk in one line.*

> "This is an all of us problem now. We're all labs teams now."
>
> — [2:01](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=121s) &middot; *Frames the audience, not just GitHub Next, as responsible for scouting what to build.*

> "the more we automate, the more time we have to spend on craft or on our product or on making it really good or on features"
>
> — [3:26](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=206s) &middot; *States the payoff he thinks automation buys — time, not headcount.*

> "going faster means that a small misalignment, uh, can snowball into a ton of wasted work, uh, and that work costs tokens, and tokens cost real money now"
>
> — [4:00](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=240s) &middot; *Names the concrete cost of team misalignment in an agentic workflow.*

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s) &middot; *Sharp, quotable statement of the prompt-injection threat model.*

> "in a world where I have lots of automations, the last thing I want is noise. I don't want the agents denial of servicing me."
>
> — [8:21](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=501s) &middot; *Identifies a non-obvious failure mode of background automation at scale.*

> "the markdown is the source code. The YAML is like a compiled artifact. You never look at it."
>
> — [9:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=599s) &middot; *Crisp statement of the authoring model behind Agentic Workflows.*

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s) &middot; *A hard security rule stated without hedging.*

> "walks the Python stack trace to figure out if the bug is in first-party code or third-party code, closes the issue if it's not their issue, right? That's something that was not possible before AI, not possible with heuristics"
>
> — [12:33](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=753s) &middot; *Concrete real-world deployment showing the judgment-vs-heuristic line.*

> "we actually believe that this is going to be a bigger category than interactive AI because automations that run in the background while you sleep, that's the ballgame."
>
> — [12:33](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=753s) &middot; *The talk's most contestable prediction, stated as a bet.*

> "Planning isn't before, and review isn't after. We iterate on the direction together, and AI takes a step, and then we iterate more in the direction."
>
> — [13:13](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=793s) &middot; *Compresses his argument about how the shape of the development process changes.*

> "It was never designed for making software or the needs of everyone involved in that."
>
> — [13:48](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=828s) &middot; *His critique of Slack as the default collaboration surface for engineering.*

> "Anything that's in code, any fact that's in code, the agents can figure out by reading the code. What's left are the things that are not in code, like political considerations."
>
> — [13:48](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=828s) &middot; *Defines what human collaboration surfaces are actually for once agents can read the repo.*

> "I don't email Word documents around anymore. I create and collaborate in the same surface, in the same place. This is coming for code, a trillion percent"
>
> — [14:22](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=862s) &middot; *The analogy driving the entire Ace prototype.*

> "none of this is running on my machine. It's all micro VMs in the cloud. So, every session is just a branch of my repo checked out to a spot in the cloud."
>
> — [14:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=899s) &middot; *The key architectural detail distinguishing Ace from local multi-agent conductors.*

> "in order to change something about my application, I'm going to edit a document, and I'm going to tell AI, "Hey, make the document true.""
>
> — [18:05](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1085s) &middot; *The clearest formulation of document-driven development in the talk.*

> "the better that we get at articulating, uh, our goals to the agents, the less they need us."
>
> — [19:18](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1158s) &middot; *States the inversion of the human-agent relationship he sees coming.*

> "for the past few years, AI has helped me to type. But, if you look at the science of the matter, it's only about 5% of the job."
>
> — [19:56](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1196s) &middot; *The empirical claim that justifies the whole product direction.*

> "the hands-on keyboard typing part is 5% of the time. Now, AI has to help me with the other 95%."
>
> — [19:56](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1196s) &middot; *The closing call to action for tool builders.*

## Positions

- The largest value of AI comes from enabling groups to do more, not from parallelizing a single developer into many agents. ([2:42](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=162s), confidence: stated)
- Background automation will be a bigger category than interactive AI. ([12:33](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=753s), confidence: stated)
- Guardrails expressed as prompts to the agent are not real guardrails, because a third party can prompt-inject the agent past them; guardrails must be deterministic configuration outside the agent. ([7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s), confidence: stated)
- Any secret an agent can see must be treated as already compromised, so secrets should be held outside the agent's sandbox and accessed only through a broker. ([11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s), confidence: stated)
- Automations must be permitted to produce no output at all, and bounded in output count (e.g. a single PR), or they become a denial-of-service on their owner. ([8:21](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=501s), confidence: stated)
- Hands-on-keyboard typing is about 5% of a developer's time, per a longitudinal study of roughly 100 developers over thousands of hours. ([19:56](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1196s), confidence: stated)
- Slack is the wrong surface for building software because it was designed for the average office worker rather than for software teams. ([13:48](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=828s), confidence: stated)
- Collaboration surfaces should carry the facts that are not in code (political, commercial, aesthetic constraints), since agents can derive everything already in code by reading it. ([13:48](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=828s), confidence: stated)
- Creation and collaboration will converge into a single surface for code, as they already did for documents. ([14:22](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=862s), confidence: stated)
- Automation authoring should be in natural-language markdown, with generated CI YAML treated as a compiled artifact nobody reads or edits. ([9:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=599s), confidence: stated)
- Automation should extend beyond engineers to roles like product managers in order to reach industrial scale. ([11:18](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=678s), confidence: stated)
- Agents should listen to team conversations continuously and invoke humans only when they need clarification or a pair of hands. ([19:18](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1158s), confidence: stated)
- The future unit of software change is an editable specification document that the AI is instructed to make true. ([18:05](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1085s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [background agents](../concepts/background-agents.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [spec-driven development](../concepts/spec-driven-development.md)

