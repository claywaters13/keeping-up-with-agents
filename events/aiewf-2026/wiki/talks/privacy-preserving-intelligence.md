---
title: "Privacy-Preserving Intelligence"
type: "talk"
slug: "privacy-preserving-intelligence"
org: "Bee (acq. Amazon)"
video_id: "IvE8n-ylFYY"
duration_sec: 953
word_count: 2063
speakers: ["Steve Korshakov"]
---

# Privacy-Preserving Intelligence

**Speakers:** [Steve Korshakov](../speakers/steve-korshakov.md)

**Org:** Bee (acq. Amazon)

**Duration:** 15m 53s

[Watch on YouTube](https://www.youtube.com/watch?v=IvE8n-ylFYY)

## Summary

Steve Korshakov describes how Bee (acquired by Amazon ~8 months prior) built an always-on AI wearable that records everything a user says while making it technically impossible for the company — including Amazon insiders — to read that data. He argues that personal agents are moving from request/response to long-running stateful execution, which forces a design where an encrypted, persistent runtime operates on the user's behalf in the cloud without the user's phone being online. The bulk of the talk is the concrete mechanism: keys generated and held only on the customer device, a remote attestation pipeline verified against a public Sigstore transparency log, confidential-compute nodes running their own inference, forced seven-day key expiry in memory, and a two-tier deployment split where a separate Amazon team's hardcoded signing keys gate what can ship. He closes on agent safety, arguing that sandboxing is the only thing that actually works and that the useful-but-unrestricted agent is still out of reach. Worth watching if you're building a system where the operator must be structurally unable to see user data, rather than merely promising not to.

## Key Points

- An always-on audio wearable captures roughly 10 million tokens per person per year, and within a single week of recording it is possible to learn virtually everything about that person.
- Being inside Amazon made privacy harder, not easier: the standard cloud guarantee that Amazon cannot see a customer's data does not apply when you are Amazon, so the team had to defend against internal threats.
- Personal agents are following the trajectory of coding agents like Claude Code — from request/response to running continuously for hours or days — which requires a stateful runtime with persistent memory rather than a stateless backend.
- The encryption design rests on four commitments: keys live only on the customer's phone, encryption has no opt-out or bypass, all workloads are publicly auditable via a transparency log, and trusted dependencies are minimized.
- The phone runs an attestation pipeline verifying both workload integrity and the workload's presence in a Sigstore public transparency log before releasing the key to backend nodes running in confidential compute.
- Keys held in memory are force-expired after seven days — chosen because 24 hours is too short if a user does not open their phone, while seven days bounds what an agent can usefully do.
- Deployment is split into a base image and a per-deploy manifest, with signing keys owned by a separate privacy team hardcoded into clients and backends, so the product team can influence but not control what ships.
- The team kept the security-critical surface to roughly 20,000 lines of memory-safe code — most of it attestation verification — and deliberately avoided rolling their own crypto, a lesson Korshakov attributes to his time at Telegram.
- On agent safety, Korshakov's position is that nothing works except sandboxing and denying agents the means to cause harm; he found that tightening OpenClaw's permissions made it markedly less useful.

## Notable Quotes

> "a single person usually like captures about 10 million tokens per year"
>
> — [0:01](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=1s) &middot; *quantifies the scale of personal data the device accumulates*

> "you can learn virtually everything about the person within the just like one week of wearing the B device which is extremely sensitive"
>
> — [1:10](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=70s) &middot; *states the threat model in one line*

> "our mission was to not have access to any of this data and not being able to look at it anyone at Amazon"
>
> — [1:10](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=70s) &middot; *the core design constraint the rest of the talk answers*

> "before like you run on Amazon and Amazon gives you pre like guarantees as a customer that they can see your data. But once you inside this changes a lot"
>
> — [10:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=606s) &middot; *the counterintuitive point that being the cloud provider removes a guarantee rather than granting one*

> "just few months ago it was like more like request response stuff like change this, change that and now it can works for like hours for us."
>
> — [2:51](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=171s) &middot; *uses coding agents as the leading indicator for personal agent architecture*

> "we don't require the user device to be online. So it's fully autonomous but at the same time it's fully controlled by the user."
>
> — [3:30](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=210s) &middot; *names the tension the whole key-management scheme exists to resolve*

> "First of all the key leaves and manage it only on customer device."
>
> — [3:30](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=210s) &middot; *first of the four stated encryption principles*

> "Everything is encrypted. We don't have any opt out there. No way to disable it. There no way to bypass it."
>
> — [4:18](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=258s) &middot; *a hard product position against configurable privacy*

> "We use six store for our transparency log and anyone can go there and try to look and verify that this workload is genuine."
>
> — [5:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=306s) &middot; *names the specific transparency mechanism (Sigstore) enabling third-party verification*

> "we can't leave the unencrypted data out of our perimeter uh all our we run our own inference too"
>
> — [5:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=306s) &middot; *explains why they self-host inference rather than call an API*

> "24 hours will be too low because you can like not open your phone for like 24 hours something will be missed and like so we pick like about seven days."
>
> — [6:53](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=413s) &middot; *shows the explicit usability/exposure tradeoff behind key expiry*

> "Our goal was to uh build a system that no one inside of uh Amazon will be able to ship anything unnoticed."
>
> — [6:53](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=413s) &middot; *frames insider deployment as the residual attack surface*

> "we hardcode their in their signing keys inside of our client apps and our back ends"
>
> — [7:39](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=459s) &middot; *the concrete mechanism separating the product team from release authority*

> "we are using private CA because you can't do this in public certificates because it will populate the public uh transparency log"
>
> — [8:47](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=527s) &middot; *a real constraint that forced a non-standard PKI choice*

> "I calculated before this talk it's just like about 20k lines on memory safe language"
>
> — [11:40](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=700s) &middot; *puts a number on the auditable trusted computing base*

> "when I was a telegram like we reintroduced like build our own crypto and that was like questionable way of doing stuff."
>
> — [12:34](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=754s) &middot; *rare on-record self-criticism informing a current design rule*

> "I think nothing works except like sandboxing and just not giving them a way to hurt themselves."
>
> — [13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s) &middot; *his blunt conclusion on agent safety after running experiments*

> "It's like you know our brains they can't stop the heart at will right"
>
> — [13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s) &middot; *the analogy for why capability denial beats behavioral alignment*

> "I tried open claw. It's like it was once they started to try to tighten this down it became much less use useful."
>
> — [14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s) &middot; *a direct critique of a competing approach to agent restriction*

## Positions

- A single person wearing an always-on audio device generates about 10 million tokens per year, and one week of recording is enough to learn virtually everything about them. ([0:01](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=1s), confidence: stated)
- Operating inside Amazon requires stronger privacy engineering than operating as an Amazon customer, because the customer-facing guarantee that Amazon cannot see your data no longer protects you. ([10:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=606s), confidence: stated)
- Personal agents will follow coding agents in shifting from request/response to running continuously for hours or days, so they must be built on stateful runtimes with persistent memory. ([2:51](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=171s), confidence: stated)
- An agent should be able to operate fully autonomously in the cloud without the user's device being online, while remaining fully controlled by the user. ([3:30](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=210s), confidence: stated)
- Encryption should have no opt-out, no way to disable it, and no bypass. ([4:18](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=258s), confidence: stated)
- Seven days is the right forced expiration for in-memory keys, because 24 hours risks missing work when a user does not open their phone and seven days covers the realistic horizon for useful agent work. ([6:53](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=413s), confidence: stated)
- Splitting deployment authority into a separate privacy team whose signing keys are hardcoded into clients and backends makes unnoticed shipping virtually impossible at a company the size of Amazon. ([7:39](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=459s), confidence: stated)
- Keeping the security-critical codebase small — around 20k lines in a memory-safe language, mostly attestation verification — is what makes full audit and verification feasible. ([11:40](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=700s), confidence: stated)
- Building your own crypto is the wrong approach; reuse trustworthy existing software instead. ([12:34](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=754s), confidence: stated)
- Behavioral techniques for taming agents do not work; only sandboxing and removing the means to cause harm do. ([13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s), confidence: stated)
- OpenClaw's approach of tightening down a general-purpose agent is not good, because restriction destroyed its usefulness — a narrowly sandboxed special-purpose agent is the better tradeoff today. ([14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s), confidence: stated)
- Agents should not be given direct access to personal computers. ([13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [audit trails](../concepts/audit-trails.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [durable execution](../concepts/durable-execution.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [local inference](../concepts/local-inference.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

