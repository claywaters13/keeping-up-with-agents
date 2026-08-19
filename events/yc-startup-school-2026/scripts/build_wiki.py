#!/usr/bin/env python3
"""
Deterministic markdown wiki generator for the YC Startup School 2026 corpus.

Adapted from events/aiewf-2026/scripts/build_wiki.py. Differences: the event
name/labels and README template, no livestream-duplication offset (this event
has no compilation videos, so words and hours are plain sums over index.json),
and no schedule fields (single-track event: no track, day, or room).

Reads the derived JSON layer (data/index.json, data/passA/*.json,
data/passC/*.json, data/concepts/*.json, data/speakers/*.json) and renders
a linked markdown wiki at wiki/{talks,concepts,speakers}/*.md plus a
wiki/README.md entry point.

NO MODEL CALLS. Pure rendering from already-extracted, already-verified JSON.

Publishing posture (binding, see BUILD.md): derived layer only — summaries,
extracted quotes with timestamps, concepts, positions, speakers, links back
to YouTube. NEVER full verbatim transcripts. data/transcripts/*.md is build
substrate and is never read into a rendered page by this script.

Links are relative markdown links ([Name](../speakers/x.md)), not
[[wikilinks]] — GitHub only renders the former, and both Obsidian and Quartz
build their graph from relative links too.

Idempotent: wipes and regenerates wiki/talks, wiki/concepts, wiki/speakers,
and wiki/README.md on every run. Safe to re-run any time the source JSON
changes.

Usage: python3 scripts/build_wiki.py [--root <project_root>] [--verify]
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
import unicodedata
from collections import defaultdict

# ---------------------------------------------------------------------------
# generic helpers
# ---------------------------------------------------------------------------

SLUG_RE = re.compile(r'[^a-z0-9]+')


def slugify(s: str) -> str:
    s = s.lower()
    s = SLUG_RE.sub('-', s)
    return s.strip('-')


def strip_fences(s: str) -> str:
    s = s.strip()
    if s.startswith('```'):
        s = re.sub(r'^```[a-zA-Z]*\n', '', s)
        s = re.sub(r'\n```\s*$', '', s)
    return s


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_envelope_key(path, key):
    """Load a passA/passC-style envelope, preferring the parsed `key` over
    a fresh re-parse of the raw `result` string. Returns None if neither
    works (e.g. missing file, unparseable result)."""
    if not os.path.exists(path):
        return None
    env = load_json(path)
    val = env.get(key)
    if val is not None:
        return val
    try:
        return json.loads(strip_fences(env['result']))
    except Exception as e:
        print(f'WARN: could not parse {key} from {path}: {e}', file=sys.stderr)
        return None


def yaml_str(s) -> str:
    """Render a python value as a double-quoted YAML scalar."""
    if s is None:
        return '""'
    s = str(s)
    s = s.replace('\\', '\\\\').replace('"', '\\"')
    s = s.replace('\n', ' ').replace('\r', ' ')
    return f'"{s}"'


def yaml_list(items) -> str:
    if not items:
        return '[]'
    return '[' + ', '.join(yaml_str(i) for i in items) + ']'


def fmt_duration(sec) -> str:
    if not sec:
        return 'unknown'
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f'{h}h {m}m'
    return f'{m}m {s:02d}s'


def deep_link(video_id, ts) -> str:
    ts = int(ts or 0)
    return f'https://www.youtube.com/watch?v={video_id}&t={ts}s'


def link_text(s: str) -> str:
    """Escape characters that break markdown link text."""
    return (s or '').replace('[', '(').replace(']', ')').replace('\n', ' ')


def md_link(text, target) -> str:
    return f'[{link_text(text)}]({target})'


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def norm_name(s: str) -> str:
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\([^)]*\)', '', s)
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


MATURITY_LABEL = {
    'settled': 'Settled — broad agreement, established practice',
    'consolidating': 'Consolidating — converging practice, some open edges',
    'contested': 'Contested — active, unresolved disagreement across talks',
    'frontier': 'Frontier — too new or sparse for consensus yet',
}
MATURITY_BADGE = {
    'settled': 'SETTLED',
    'consolidating': 'CONSOLIDATING',
    'contested': 'CONTESTED',
    'frontier': 'FRONTIER',
}

TIER_LABEL = {
    'core': 'Core concept',
    'supporting': 'Supporting concept',
}

# ---------------------------------------------------------------------------
# load everything
# ---------------------------------------------------------------------------


def load_all(root):
    data_dir = os.path.join(root, 'data')

    index = load_json(os.path.join(data_dir, 'index.json'))
    talks_by_slug = {t['slug']: t for t in index}

    canonical = load_json(os.path.join(data_dir, 'concepts', 'canonical.json'))['canonical']
    concept_by_slug = {}
    concept_slug_by_name = {}
    for c in canonical:
        cslug = slugify(c['concept'])
        concept_by_slug[cslug] = c
        concept_slug_by_name[c['concept']] = cslug

    concept_talks = load_json(os.path.join(data_dir, 'concepts', 'concept_talks.json'))
    # concept name -> [talk slug, ...]
    talk_to_concepts = defaultdict(list)  # talk slug -> [concept name, ...]
    for concept_name, slugs in concept_talks.items():
        if concept_name not in concept_slug_by_name:
            continue  # not in canonical (shouldn't happen, defensive)
        for slug in slugs:
            talk_to_concepts[slug].append(concept_name)

    concept_speakers = load_json(os.path.join(data_dir, 'speakers', 'concept_speakers.json'))

    # speakers: every *.json in data/speakers/ except the three aggregate files
    speakers_dir = os.path.join(data_dir, 'speakers')
    skip = {'index.json', 'concept_speakers.json', '_build_report.json'}
    speaker_by_id = {}
    for fn in sorted(os.listdir(speakers_dir)):
        if fn in skip or not fn.endswith('.json'):
            continue
        sid = fn[:-5]
        speaker_by_id[sid] = load_json(os.path.join(speakers_dir, fn))

    # talk slug -> [speaker_id, ...], authoritative (derived from each
    # speaker's own resolved `talks` list, avoids re-doing fuzzy name
    # matching here).
    talk_to_speakers = defaultdict(list)
    for sid, sp in speaker_by_id.items():
        for t in sp.get('talks', []):
            talk_to_speakers[t['slug']].append(sid)

    # passA: talk slug -> parsed extraction dict (or None)
    passA_dir = os.path.join(data_dir, 'passA')
    passA_by_slug = {}
    for slug in talks_by_slug:
        passA_by_slug[slug] = load_envelope_key(
            os.path.join(passA_dir, slug + '.json'), 'passA')

    # passC: concept slug -> parsed synthesis dict (or None)
    passC_dir = os.path.join(data_dir, 'passC')
    passC_by_slug = {}
    for cslug in concept_by_slug:
        passC_by_slug[cslug] = load_envelope_key(
            os.path.join(passC_dir, cslug + '.json'), 'passC')

    return dict(
        talks_by_slug=talks_by_slug,
        canonical=canonical,
        concept_by_slug=concept_by_slug,
        concept_slug_by_name=concept_slug_by_name,
        concept_talks=concept_talks,
        talk_to_concepts=talk_to_concepts,
        concept_speakers=concept_speakers,
        speaker_by_id=speaker_by_id,
        talk_to_speakers=talk_to_speakers,
        passA_by_slug=passA_by_slug,
        passC_by_slug=passC_by_slug,
    )


# ---------------------------------------------------------------------------
# talk pages
# ---------------------------------------------------------------------------


def render_talk(slug, ctx):
    t = ctx['talks_by_slug'][slug]
    passA = ctx['passA_by_slug'].get(slug)
    speaker_ids = sorted(ctx['talk_to_speakers'].get(slug, []),
                          key=lambda sid: ctx['speaker_by_id'][sid]['name'])
    concept_names = sorted(ctx['talk_to_concepts'].get(slug, []))
    video_id = t.get('video_id', '')

    org = t.get('org') or (passA or {}).get('speaker_org') or ''

    fm = ['---']
    fm.append(f'title: {yaml_str(t["title"])}')
    fm.append('type: "talk"')
    fm.append(f'slug: {yaml_str(slug)}')
    if t.get('track'):
        fm.append(f'track: {yaml_str(t["track"])}')
    if org:
        fm.append(f'org: {yaml_str(org)}')
    if t.get('day'):
        fm.append(f'day: {yaml_str(t["day"])}')
    if t.get('room'):
        fm.append(f'room: {yaml_str(t["room"])}')
    fm.append(f'video_id: {yaml_str(video_id)}')
    fm.append(f'duration_sec: {int(t.get("duration_sec") or 0)}')
    fm.append(f'word_count: {int(t.get("word_count") or 0)}')
    fm.append(f'speakers: {yaml_list([ctx["speaker_by_id"][sid]["name"] for sid in speaker_ids] or t.get("speakers") or [])}')
    fm.append('---')

    lines = fm + ['']
    lines.append(f'# {t["title"]}')
    lines.append('')

    if t.get('scheduled_title') and t['scheduled_title'] != t['title']:
        lines.append(f'*Program title: {t["scheduled_title"]}*')
        lines.append('')

    # speaker line
    if speaker_ids:
        sp_links = [md_link(ctx['speaker_by_id'][sid]['name'], f'../speakers/{sid}.md')
                    for sid in speaker_ids]
        lines.append('**Speakers:** ' + ', '.join(sp_links))
    elif t.get('speakers'):
        lines.append('**Speakers:** ' + ', '.join(t['speakers']) + ' *(not resolved to a speaker profile)*')
    else:
        lines.append('**Speakers:** unknown / not credited')
    if org:
        lines.append('')
        lines.append(f'**Org:** {org}')
    lines.append('')

    meta_bits = []
    if t.get('track'):
        meta_bits.append(f'**Track:** {t["track"]}')
    if t.get('day'):
        day_room = t['day']
        if t.get('room'):
            day_room += f' &middot; {t["room"]}'
        meta_bits.append(f'**Day/Room:** {day_room}')
    meta_bits.append(f'**Duration:** {fmt_duration(t.get("duration_sec"))}')
    lines.append(' &nbsp;|&nbsp; '.join(meta_bits))
    lines.append('')
    if video_id:
        lines.append(f'[Watch on YouTube]({t.get("url") or "https://www.youtube.com/watch?v=" + video_id})')
        lines.append('')

    if passA is None:
        lines.append('> **Extraction not yet available for this entry.** This talk is part of the '
                      'corpus (metadata above is real) but its Pass A summary/quotes/concepts have '
                      'not been generated yet.')
        lines.append('')
        return '\n'.join(lines) + '\n'

    if passA.get('summary'):
        lines.append('## Summary')
        lines.append('')
        lines.append(passA['summary'])
        lines.append('')

    if passA.get('key_points'):
        lines.append('## Key Points')
        lines.append('')
        for kp in passA['key_points']:
            lines.append(f'- {kp}')
        lines.append('')

    if passA.get('notable_quotes'):
        lines.append('## Notable Quotes')
        lines.append('')
        for q in passA['notable_quotes']:
            ts = q.get('timestamp_sec', 0)
            link = deep_link(video_id, ts) if video_id else None
            ts_str = md_link(fmt_ts(ts), link) if link else fmt_ts(ts)
            lines.append(f'> "{q["text"]}"')
            lines.append('>')
            lines.append(f'> — {ts_str}' + (f' &middot; *{q["why"]}*' if q.get('why') else ''))
            lines.append('')

    if passA.get('positions'):
        lines.append('## Positions')
        lines.append('')
        for p in passA['positions']:
            ts = p.get('timestamp_sec', 0)
            link = deep_link(video_id, ts) if video_id else None
            ts_str = md_link(fmt_ts(ts), link) if link else fmt_ts(ts)
            conf = p.get('confidence', '')
            lines.append(f'- {p["claim"]} ({ts_str}' + (f', confidence: {conf}' if conf else '') + ')')
        lines.append('')

    if concept_names:
        lines.append('## Concepts')
        lines.append('')
        for cn in concept_names:
            cslug = ctx['concept_slug_by_name'][cn]
            lines.append(f'- {md_link(cn, "../concepts/" + cslug + ".md")}')
        lines.append('')

    return '\n'.join(lines) + '\n'


def fmt_ts(sec):
    sec = int(sec or 0)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f'{h}:{m:02d}:{s:02d}'
    return f'{m}:{s:02d}'


# ---------------------------------------------------------------------------
# concept pages
# ---------------------------------------------------------------------------


def render_concept(cslug, ctx):
    c = ctx['concept_by_slug'][cslug]
    passC = ctx['passC_by_slug'].get(cslug)
    talk_slugs = sorted(ctx['concept_talks'].get(c['concept'], []))
    speakers = ctx['concept_speakers'].get(c['concept'], [])

    maturity = (passC or {}).get('maturity', '')

    fm = ['---']
    fm.append(f'title: {yaml_str(c["concept"])}')
    fm.append('type: "concept"')
    fm.append(f'slug: {yaml_str(cslug)}')
    fm.append(f'tier: {yaml_str(c.get("tier", ""))}')
    if maturity:
        fm.append(f'maturity: {yaml_str(maturity)}')
    fm.append(f'talk_count: {len(talk_slugs)}')
    fm.append(f'speaker_count: {len(speakers)}')
    fm.append('---')

    lines = fm + ['']
    lines.append(f'# {c["concept"]}')
    lines.append('')
    if maturity:
        lines.append(f'**Maturity: {MATURITY_BADGE.get(maturity, maturity.upper())}** — {MATURITY_LABEL.get(maturity, "")}')
        lines.append('')
    lines.append(f'*{TIER_LABEL.get(c.get("tier"), c.get("tier", ""))}* &middot; discussed across **{len(talk_slugs)}** talk(s) by **{len(speakers)}** speaker(s)')
    lines.append('')
    lines.append(f'**Definition:** {c["definition"]}')
    lines.append('')

    if c.get('aliases') and len(c['aliases']) > 1:
        others = [a for a in c['aliases'] if a != c['concept']]
        if others:
            lines.append(f'*Also referred to as: {", ".join(others)}*')
            lines.append('')

    if passC is None:
        # Expected, not an error: Pass C only synthesizes concepts tagged by 3+
        # talks (see BUILD.md). Thinner concepts still get a page — definition,
        # talk links, speakers — just no cross-talk synthesis.
        lines.append('> **No cross-talk synthesis for this concept.** Synthesis requires at '
                     'least 3 tagged talks; a "state of practice" drawn from fewer would be '
                     'an artifact of the sample rather than a finding. The talks that engage '
                     'this concept are listed below.')
        lines.append('')
    else:
        if passC.get('state_of_practice'):
            lines.append('## State of Practice')
            lines.append('')
            lines.append(passC['state_of_practice'])
            lines.append('')

        if passC.get('consensus'):
            lines.append('## Consensus')
            lines.append('')
            for item in passC['consensus']:
                lines.append(f'### {item["claim"]}')
                lines.append('')
                lines.append(f'Support: **{item.get("support_count", 0)}** talk(s)')
                lines.append('')
                if item.get('evidence_quote'):
                    ev_talk = item.get('evidence_talk')
                    ev_ts = item.get('evidence_timestamp_sec', 0)
                    vid = ctx['talks_by_slug'].get(ev_talk, {}).get('video_id', '')
                    link = deep_link(vid, ev_ts) if vid else None
                    ts_str = md_link(fmt_ts(ev_ts), link) if link else fmt_ts(ev_ts)
                    ev_title = ctx['talks_by_slug'].get(ev_talk, {}).get('title', ev_talk)
                    lines.append(f'> "{item["evidence_quote"]}"')
                    lines.append('>')
                    talk_link = md_link(ev_title, f'../talks/{ev_talk}.md') if ev_talk in ctx['talks_by_slug'] else ev_talk
                    lines.append(f'> — {talk_link}, {ts_str}')
                    lines.append('')
                if item.get('supporting_talks'):
                    st_links = [md_link(ctx['talks_by_slug'][s]['title'], f'../talks/{s}.md')
                                for s in item['supporting_talks'] if s in ctx['talks_by_slug']]
                    lines.append('Supporting talks: ' + ', '.join(st_links))
                    lines.append('')

        if passC.get('disagreements'):
            lines.append('## Disagreements')
            lines.append('')
            for d in passC['disagreements']:
                lines.append(f'### {d["question"]}')
                lines.append('')
                lines.append('| Position A | Position B |')
                lines.append('|---|---|')
                a_talks = ', '.join(md_link(ctx['talks_by_slug'][s]['title'], f'../talks/{s}.md')
                                     for s in d.get('position_a_talks', []) if s in ctx['talks_by_slug'])
                b_talks = ', '.join(md_link(ctx['talks_by_slug'][s]['title'], f'../talks/{s}.md')
                                     for s in d.get('position_b_talks', []) if s in ctx['talks_by_slug'])
                a_cell = d['position_a'].replace('|', '\\|').replace('\n', ' ')
                b_cell = d['position_b'].replace('|', '\\|').replace('\n', ' ')
                lines.append(f'| {a_cell}<br>*{a_talks}* | {b_cell}<br>*{b_talks}* |')
                lines.append('')
                if d.get('why_it_matters'):
                    lines.append(f'*Why it matters: {d["why_it_matters"]}*')
                    lines.append('')

        pg = passC.get('practical_guidance') or {}
        if pg.get('do') or pg.get('avoid'):
            lines.append('## Practical Guidance')
            lines.append('')
            if pg.get('do'):
                lines.append('**Do:**')
                lines.append('')
                for x in pg['do']:
                    lines.append(f'- {x}')
                lines.append('')
            if pg.get('avoid'):
                lines.append('**Avoid:**')
                lines.append('')
                for x in pg['avoid']:
                    lines.append(f'- {x}')
                lines.append('')

        if passC.get('notable_outliers'):
            lines.append('## Notable Outliers')
            lines.append('')
            for o in passC['notable_outliers']:
                talk = o.get('talk')
                ts = o.get('timestamp_sec', 0)
                vid = ctx['talks_by_slug'].get(talk, {}).get('video_id', '')
                link = deep_link(vid, ts) if vid else None
                ts_str = md_link(fmt_ts(ts), link) if link else fmt_ts(ts)
                talk_title = ctx['talks_by_slug'].get(talk, {}).get('title', talk)
                talk_link = md_link(talk_title, f'../talks/{talk}.md') if talk in ctx['talks_by_slug'] else talk
                lines.append(f'- {o["claim"]} ({talk_link}, {ts_str})')
            lines.append('')

    if talk_slugs:
        lines.append('## All Talks')
        lines.append('')
        for s in talk_slugs:
            if s not in ctx['talks_by_slug']:
                continue
            lines.append(f'- {md_link(ctx["talks_by_slug"][s]["title"], "../talks/" + s + ".md")}')
        lines.append('')

    if speakers:
        lines.append('## Speakers')
        lines.append('')
        for sp in sorted(speakers, key=lambda x: x['name']):
            sid = sp['speaker_id']
            if sid not in ctx['speaker_by_id']:
                continue
            lines.append(f'- {md_link(sp["name"], "../speakers/" + sid + ".md")}')
        lines.append('')

    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# speaker pages
# ---------------------------------------------------------------------------


def render_speaker(sid, ctx):
    sp = ctx['speaker_by_id'][sid]

    fm = ['---']
    fm.append(f'title: {yaml_str(sp["name"])}')
    fm.append('type: "speaker"')
    fm.append(f'slug: {yaml_str(sid)}')
    if sp.get('role'):
        fm.append(f'role: {yaml_str(sp["role"])}')
    if sp.get('company'):
        fm.append(f'company: {yaml_str(sp["company"])}')
    fm.append(f'talk_count: {len(sp.get("talks", []))}')
    fm.append('---')

    lines = fm + ['']
    lines.append(f'# {sp["name"]}')
    lines.append('')

    role_co = ' &middot; '.join(x for x in [sp.get('role'), sp.get('company')] if x)
    if role_co:
        lines.append(f'**{role_co}**')
        lines.append('')

    if sp.get('bio'):
        lines.append(sp['bio'])
        lines.append('')

    if sp.get('linkedin'):
        lines.append(f'[LinkedIn]({sp["linkedin"]})')
        lines.append('')

    talks = sp.get('talks', [])
    if talks:
        lines.append('## Talks')
        lines.append('')
        for t in talks:
            slug = t['slug']
            if slug not in ctx['talks_by_slug']:
                continue
            title = ctx['talks_by_slug'][slug]['title']
            bits = []
            if t.get('track'):
                bits.append(t['track'])
            if not t.get('is_sole_speaker'):
                bits.append('co-presented')
            suffix = f' ({", ".join(bits)})' if bits else ''
            lines.append(f'- {md_link(title, "../talks/" + slug + ".md")}{suffix}')
        lines.append('')

    sessions = sp.get('sessions', [])
    if sessions:
        lines.append('## Scheduled Sessions')
        lines.append('')
        for s in sessions:
            bits = [b for b in [s.get('day'), s.get('time'), s.get('room')] if b]
            lines.append(f'- **{s.get("scheduled_title", "")}** &middot; ' + ' &middot; '.join(bits))
        lines.append('')

    concepts = sp.get('concepts', [])
    if concepts:
        lines.append('## Concepts')
        lines.append('')
        for c in sorted(concepts, key=lambda x: x['concept']):
            cslug = ctx['concept_slug_by_name'].get(c['concept'])
            if not cslug or cslug not in ctx['concept_by_slug']:
                continue
            lines.append(f'- {md_link(c["concept"], "../concepts/" + cslug + ".md")}')
        lines.append('')

    # attributed quotes: only speaker_attributed == True quotes ever live in
    # sp['quotes'] (see scripts/build_speaker_index.py) — sole-speaker talks
    # only. This is the ONLY place this script renders a quote as this
    # person's own words.
    quotes = [q for q in sp.get('quotes', []) if q.get('speaker_attributed')]
    if quotes:
        lines.append('## Quotes')
        lines.append('')
        for q in quotes:
            talk_slug = q.get('talk_slug')
            talk_title = ctx['talks_by_slug'].get(talk_slug, {}).get('title', talk_slug)
            talk_link = md_link(talk_title, f'../talks/{talk_slug}.md') if talk_slug in ctx['talks_by_slug'] else talk_slug
            ts_str = md_link(fmt_ts(q.get('timestamp_sec', 0)), q.get('deep_link')) if q.get('deep_link') else fmt_ts(q.get('timestamp_sec', 0))
            lines.append(f'> "{q["quote"]}"')
            lines.append('>')
            lines.append(f'> — {talk_link}, {ts_str}')
            lines.append('')

    # co-presented (talk-level, NOT individually attributed) quotes: pulled
    # from Pass A for multi-speaker talks this person was on. Never labeled
    # as this person's own words — see HANDOFF quote-attribution rule.
    co_slugs = [t['slug'] for t in talks if not t.get('is_sole_speaker') and t['slug'] in ctx['talks_by_slug']]
    co_quotes = []
    for slug in co_slugs:
        passA = ctx['passA_by_slug'].get(slug)
        if not passA:
            continue
        for q in passA.get('notable_quotes', []):
            co_quotes.append((slug, q))
    if co_quotes:
        lines.append('## From Talks This Speaker Co-Presented')
        lines.append('')
        lines.append('*These quotes come from talks with multiple speakers. The extraction is '
                      'talk-level only and does not identify which co-presenter said which line — '
                      'do not read these as this person\'s individual words.*')
        lines.append('')
        for slug, q in co_quotes:
            talk_title = ctx['talks_by_slug'][slug]['title']
            talk_link = md_link(talk_title, f'../talks/{slug}.md')
            video_id = ctx['talks_by_slug'][slug].get('video_id', '')
            ts = q.get('timestamp_sec', 0)
            link = deep_link(video_id, ts) if video_id else None
            ts_str = md_link(fmt_ts(ts), link) if link else fmt_ts(ts)
            lines.append(f'> "{q["text"]}"')
            lines.append('>')
            lines.append(f'> — {talk_link}, {ts_str}')
            lines.append('')

    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------

README_TEMPLATE = """# Y Combinator Startup School 2026 Wiki

A linked, graph-style wiki built from {talk_count} talks and firesides at Y Combinator's
Startup School 2026 (Chase Center, San Francisco, July 25-26, 2026), transcribed from
YC's own YouTube channel and distilled into summaries, extracted quotes, concepts, and
cross-talk syntheses. Every claim links back to the source video at the exact timestamp.

## Scope, and the snapshot caveat

**This is a snapshot of a corpus that is still growing.** Y Combinator was still
publishing Startup School 2026 talks the day before this wiki was built. The {talk_count}
videos in this corpus were uploaded between {first_upload} and {last_upload}, and the
corpus was frozen on {snapshot_date}. Membership is taken from YC's official
[Startup School 2026 playlist](https://www.youtube.com/playlist?list=PLEb7ftOB0yf0),
which held {talk_count} videos on that date. More talks from the same event will almost
certainly appear on that playlist later and are not here. A recurring refresh has not
been built yet.

So every count on this page describes the {talk_count} published talks, not the event's
full program. Anything said in a session YC has not published, or has not published yet,
is invisible here.

**Exclusions:** none. All {talk_count} playlist members were vetted individually against
their video metadata — description, chapters, duration, upload date — and all {talk_count}
are talks or on-stage firesides recorded at this event, with English captions available.
No video was dropped as repackaged podcast content, channel evergreen, or caption-less.

## What this is

- **{talk_count} talks**, **{word_count:,} words**, **{hours:.1f} hours** of source material
- **{speaker_count} speakers**
- **{concept_count} concepts**, of which **{synthesized_count}** carry a cross-talk
  synthesis: state of practice, consensus, open disagreements, and do/avoid guidance
- **{quote_count:,} verified quotes**, every one checked verbatim against the raw YouTube
  captions before publication (see Quote verification below)

Synthesis is gated at **3 or more tagged talks**. With only {talk_count} talks in the
corpus, a "state of practice" distilled from one or two of them would describe the sample,
not the field. The {unsynthesized_count} thinner concepts still have pages — definition,
talk list, speakers — they just carry no synthesis.

### Concept maturity

Across the {synthesized_count} synthesized concepts:

| Maturity | Count | Meaning |
|---|---|---|
| Settled | {m_settled} | Broad agreement, established practice |
| Consolidating | {m_consolidating} | Converging practice, some open edges |
| Contested | {m_contested} | Active, unresolved disagreement across talks |
| Frontier | {m_frontier} | Too new or sparse for consensus yet |

These labels come from a deliberately adversarial synthesis prompt that is told to hunt
for disagreement, which biases the distribution. Read them as a reading order, not a
measurement.

## Shared concept vocabulary

Concept names here are shared with the other event wikis in this repository rather than
minted fresh. Where a concept the AI Engineer World's Fair 2026 corpus already named
covers the same idea, this wiki reuses that concept's name and definition exactly, so the
same concept page title means the same thing across events. New concepts were minted only
for ideas the sibling vocabulary does not cover — which, for a founder-facing event, is
most of the company-building material. Syntheses are always per-event: a concept page here
describes what *this* event concluded.

## Publishing posture

This repo ships the derived layer only: summaries, extracted quotes with timestamps,
concepts, positions, speakers, and links back to YouTube. It does not contain full
verbatim transcripts of any talk. Those stay local as build substrate. Every notable quote
and consensus claim deep-links to `youtube.com/watch?v=<id>&t=<sec>s` on Y Combinator's own
channel, so reading this wiki drives traffic back to the original talks rather than
replacing them.

**Speaker attribution:** {multi_speaker_count} talks have multiple credited speakers. Where
the extraction cannot tell which co-presenter said which line, quotes and positions are kept
at talk level and rendered on speaker pages under a clearly labeled "From Talks This Speaker
Co-Presented" heading. They are never attributed to one individual as their own words. Note
that most talks here are firesides with a YC host; the corpus credits the guest, and the
extraction is instructed to capture the guest's positions rather than the interviewer's
questions.

## Layout

```
wiki/
  README.md            this file
  talks/<slug>.md       {talk_count} talk pages: summary, key points, quotes, positions, concepts
  concepts/<slug>.md    {concept_count} concept pages: definition, state of practice, consensus,
                        disagreements, do/avoid guidance, full talk list, speakers
  speakers/<slug>.md    {speaker_count} speaker pages: company, talks, concepts, quotes
```

Every page carries YAML frontmatter (`title`, `type`, plus type-appropriate fields like
`org`, `maturity`, `company`) so Obsidian and Quartz can filter and query on it.

## Three ways to use this repo

1. **Obsidian vault.** Clone the repo, open `wiki/` as a vault. The relative markdown links
   between talks, concepts, and speakers build Obsidian's graph view for free, with no
   plugin configuration needed.
2. **Quartz static site.** Point a [Quartz](https://quartz.jzhao.xyz/) build at `wiki/` for a
   searchable site with backlinks and a graph view, deployable to GitHub Pages.
3. **Claude Code / agent access.** Point an agent at this repo and let it `Grep`, `Glob`,
   and `Read` the markdown directly. No RAG server, no vector DB, no hosted API. The link
   graph plus the YAML frontmatter is the retrieval structure.

## Quote verification

Every quote in this wiki passed a deterministic verification pass against the raw YouTube
caption files (`raw/caps/<video_id>.en.json3`) before publication, using normalized
word-sequence matching rather than a model judgment call. Quotes that failed verbatim
verification were dropped, not edited (see `data/passA/_dropped_quotes.json` for the list).
{quote_count:,} quotes passed and are rendered across the {talk_count} talk pages:
{attributed_quote_count:,} individually speaker-attributed, and {talk_level_quote_count:,}
talk-level from multi-speaker sessions.

## Source data

Generated deterministically (no model calls) by `scripts/build_wiki.py` from:

- `data/index.json`, the corpus index ({talk_count} entries)
- `data/passA/<slug>.json`, per-talk extraction (summary, quotes, concepts, positions)
- `data/passC/<concept-slug>.json`, per-concept cross-talk synthesis
- `data/concepts/canonical.json` and `data/concepts/concept_talks.json`, concept vocabulary
- `data/speakers/<slug>.json` and `data/speakers/concept_speakers.json`, speaker profiles

Re-run `python3 scripts/build_wiki.py` any time the source JSON changes. The generator wipes
and rebuilds `wiki/talks`, `wiki/concepts`, `wiki/speakers`, and this README from scratch.
See [`../BUILD.md`](../BUILD.md) for how the corpus was built.
"""

SNAPSHOT_DATE = '2026-08-19'


def render_readme(ctx, real_talk_count, multi_speaker_count):
    talks = ctx['talks_by_slug']
    talk_count = len(talks)

    # No livestream/compilation videos in this event, so no duplication offset:
    # words and hours are plain sums over index.json. (AIEWF carried a measured
    # DUP_WORDS/DUP_HOURS constant here for its two full-day livestreams.)
    word_count = sum(t.get('word_count', 0) for t in talks.values())
    hours = sum(t.get('duration_sec', 0) for t in talks.values()) / 3600.0

    uploads = sorted(t.get('upload_date') for t in talks.values() if t.get('upload_date'))
    def fmt_upload(d):
        return f'{d[:4]}-{d[4:6]}-{d[6:]}' if d and len(d) == 8 else (d or 'unknown')

    # Quote totals, derived from the same source data the pages render from:
    # every notable_quote in Pass A ships on a talk page; the ones that could be
    # pinned to an individual speaker also ship on that speaker's page.
    quote_count = sum(
        len((pa or {}).get('notable_quotes') or [])
        for pa in ctx['passA_by_slug'].values()
    )
    attributed_quote_count = sum(
        len([q for q in sp.get('quotes', []) if q.get('speaker_attributed')])
        for sp in ctx['speaker_by_id'].values()
    )
    talk_level_quote_count = quote_count - attributed_quote_count

    maturity_counts = defaultdict(int)
    synthesized_count = 0
    for cslug, passC in ctx['passC_by_slug'].items():
        if passC:
            synthesized_count += 1
            if passC.get('maturity'):
                maturity_counts[passC['maturity']] += 1

    return README_TEMPLATE.format(
        talk_count=talk_count,
        word_count=word_count,
        hours=hours,
        speaker_count=len(ctx['speaker_by_id']),
        concept_count=len(ctx['concept_by_slug']),
        synthesized_count=synthesized_count,
        unsynthesized_count=len(ctx['concept_by_slug']) - synthesized_count,
        quote_count=quote_count,
        attributed_quote_count=attributed_quote_count,
        talk_level_quote_count=talk_level_quote_count,
        m_settled=maturity_counts.get('settled', 0),
        m_consolidating=maturity_counts.get('consolidating', 0),
        m_contested=maturity_counts.get('contested', 0),
        m_frontier=maturity_counts.get('frontier', 0),
        multi_speaker_count=multi_speaker_count,
        first_upload=fmt_upload(uploads[0] if uploads else None),
        last_upload=fmt_upload(uploads[-1] if uploads else None),
        snapshot_date=SNAPSHOT_DATE,
    )


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------


def build(root):
    ctx = load_all(root)
    wiki_dir = os.path.join(root, 'wiki')

    for sub in ('talks', 'concepts', 'speakers'):
        d = os.path.join(wiki_dir, sub)
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)

    for slug in ctx['talks_by_slug']:
        content = render_talk(slug, ctx)
        write(os.path.join(wiki_dir, 'talks', slug + '.md'), content)

    for cslug in ctx['concept_by_slug']:
        content = render_concept(cslug, ctx)
        write(os.path.join(wiki_dir, 'concepts', cslug + '.md'), content)

    for sid in ctx['speaker_by_id']:
        content = render_speaker(sid, ctx)
        write(os.path.join(wiki_dir, 'speakers', sid + '.md'), content)

    real_talk_count = len(ctx['talks_by_slug'])  # no compilation videos in this event
    multi_speaker_count = sum(
        1 for slug, sids in ctx['talk_to_speakers'].items() if len(sids) > 1)

    readme = render_readme(ctx, real_talk_count, multi_speaker_count)
    write(os.path.join(wiki_dir, 'README.md'), readme)

    return ctx


# ---------------------------------------------------------------------------
# verification
# ---------------------------------------------------------------------------


def verify(root, ctx):
    wiki_dir = os.path.join(root, 'wiki')
    report = []

    counts = {}
    for sub in ('talks', 'concepts', 'speakers'):
        n = len(glob.glob(os.path.join(wiki_dir, sub, '*.md')))
        counts[sub] = n
    expected = (len(ctx['talks_by_slug']), len(ctx['concept_by_slug']), len(ctx['speaker_by_id']))
    report.append(f'Page counts: talks={counts["talks"]} concepts={counts["concepts"]} '
                   f'speakers={counts["speakers"]} '
                   f'(expected {expected[0]}/{expected[1]}/{expected[2]} from source data)')

    # link integrity
    link_re = re.compile(r'\]\((\.\./[a-z]+/[^)]+\.md)\)')
    checked = 0
    broken = []
    for sub in ('talks', 'concepts', 'speakers'):
        for fp in glob.glob(os.path.join(wiki_dir, sub, '*.md')):
            text = open(fp, encoding='utf-8').read()
            for m in link_re.finditer(text):
                checked += 1
                target = os.path.normpath(os.path.join(os.path.dirname(fp), m.group(1)))
                if not os.path.exists(target):
                    broken.append((fp, m.group(1)))
    report.append(f'Link integrity: {checked} relative links checked, {len(broken)} broken')
    for fp, target in broken[:30]:
        report.append(f'  BROKEN: {fp} -> {target}')

    # quote count reconciliation
    quote_total = 0
    for fp in glob.glob(os.path.join(wiki_dir, 'talks', '*.md')):
        text = open(fp, encoding='utf-8').read()
        if '## Notable Quotes' in text:
            section = text.split('## Notable Quotes', 1)[1].split('\n## ', 1)[0]
            quote_total += len(re.findall(r'^> "', section, re.M))
    expected_quotes = sum(
        len((pa or {}).get('notable_quotes') or [])
        for pa in ctx['passA_by_slug'].values()
    )
    report.append(
        f'Quote count across talk pages: {quote_total} '
        f'(expect {expected_quotes} from Pass A){"" if quote_total == expected_quotes else "  MISMATCH"}'
    )

    # speaker_attributed false check: our own generator never writes
    # non-attributed quotes into the "## Quotes" section (only into the
    # separate co-presented section), so grep-verify the invariant on the
    # source data used, not just trust the code path.
    bad = 0
    for sid, sp in ctx['speaker_by_id'].items():
        for q in sp.get('quotes', []):
            if not q.get('speaker_attributed'):
                bad += 1
    report.append(f'speaker_attributed:false quotes present in any speaker "quotes" array (source data): {bad} (expect 0)')

    size_out = os.popen(f'du -sh "{wiki_dir}"').read().strip()
    report.append(f'Wiki size on disk: {size_out}')

    return '\n'.join(report)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument('--verify', action='store_true')
    args = ap.parse_args()

    ctx = build(args.root)
    print('Build complete.')

    if args.verify:
        print()
        print(verify(args.root, ctx))


if __name__ == '__main__':
    main()
