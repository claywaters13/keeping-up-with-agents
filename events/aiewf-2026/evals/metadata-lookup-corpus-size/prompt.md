---
name: metadata-lookup-corpus-size
description: Metadata lookup - correct corpus counts from data/index.json or wiki/README.md, not guessed
tags: [metadata]
runs: 1
max_turns: 16
allowed_tools: [Read, Glob, Grep, Skill]
---

How many talks, concepts, and speakers are in the AIEWF 2026 wiki corpus?
