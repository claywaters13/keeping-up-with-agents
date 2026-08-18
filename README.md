# Keeping up with Agents

**AI moves fast. Keep up.**

A Claude Code plugin that gives your coding agent verified wikis of major AI events'
talks: what the field actually agrees on, every real disagreement with both sides
cited, and every quote deep-linked to the second it was said in the source video.
Install once; each new event indexed here reaches you as a plugin update, no
reinstall. By [Clay Waters](https://www.linkedin.com/in/claywaters).

```
claude plugin marketplace add claywaters13/keeping-up-with-agents
claude plugin install keeping-up-with-agents@keeping-up-with-agents
```

Then ask, in a session or headless:

```
/keeping-up-with-agents:ask what do practitioners disagree about on agent memory?
claude -p "which AIEWF 2026 concepts are contested?"
claude -p "what do the indexed events say about reward hacking?"
```

Answers cite talks with source-video timestamps, name which event each claim comes
from, and say plainly when a question falls outside the indexed corpora.

## Events

Each event gets a linked, graph-style wiki under `events/`. No vector database and no
server: the link graph plus grep is the index.

### [AI Engineer World's Fair 2026](events/aiewf-2026/)

231 talks, 134 concepts, 248 speakers, almost a million words. Headline finding: of
134 concepts synthesized across those talks, zero came back settled practice (87
consolidating, 43 contested, 4 frontier). Browse the
[wiki](events/aiewf-2026/wiki/README.md), open it as an Obsidian vault, or poke at the
[interactive concept explorer](https://claywaters13.github.io/keeping-up-with-agents/events/aiewf-2026/viz/explorer/).

More events are planned; each lands as `events/<slug>/` and ships automatically to
plugin users.

## How it's built

Talks are transcribed from the event's own published videos, distilled by an LLM
pipeline, and then verified: 4,633 quotes checked character for character against the
raw captions before publication, cross-talk syntheses that only quote from that
verified set, and a 10-case eval suite (`evals/`) that gates plugin releases,
including graders for quote fidelity and refusal outside the corpus. The published
layer is derived only: summaries, verified excerpts, and links back to the source
videos, never full transcripts. Full methodology per event lives in that event's
README.

## The podcast

Each season of the material also ships as an AI-narrated podcast, "Keeping up with
Agents." If you want the show, use a podcast app, not this repo:

- **RSS feed:** https://claywaters13.github.io/keeping-up-with-agents/feed.xml
- Spotify and Apple Podcasts links coming after directory approval.

Hosts are AI-generated (Google NotebookLM) and every episode discloses this. Episode
audio is hosted as GitHub Release assets, so cloning this repo (or installing the
plugin) never downloads audio. New episodes: `scripts/add_episode.py`, then upload the
asset and push.

## Layout

```
.claude-plugin/          plugin + marketplace manifests
skills/event-wiki/       event-agnostic Claude Code skill (corpus map, answer rules)
commands/ask.md          /keeping-up-with-agents:ask
evals/                   10-case eval suite, run against the AIEWF 2026 corpus
events/aiewf-2026/       the AIEWF 2026 wiki: wiki/, data/, scripts/, viz/
feed.xml, cover.png      the podcast feed (audio lives in Release assets)
scripts/add_episode.py   idempotent episode publisher
```
