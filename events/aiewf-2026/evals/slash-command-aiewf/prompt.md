---
name: slash-command-aiewf
description: /aiewf slash command - must expand and answer from the corpus (not "Unknown command"). NOTE - headless sessions require the fully-qualified aiewf-wiki:aiewf form; the bare /aiewf short name only resolves interactively.
tags: [slash-command, groundedness]
runs: 1
max_turns: 25
allowed_tools: [Read, Glob, Grep, Skill]
---

/aiewf-wiki:aiewf which concepts are contested?
