#!/usr/bin/env python3
"""
Build a speaker index from data/index.json talks (via data/passA/<slug>.json
extractions).

Adapted from events/aiewf-2026/scripts/build_speaker_index.py. AIEWF had an
official speaker roster (raw/speakers.json) and an official schedule
(raw/sessions.json) to join against. Y Combinator publishes neither for Startup
School 2026, so speakers here are derived entirely from the parsed video titles
(see scripts/normalize.py) plus Pass A's `speaker_org`, and every speaker is
`profile_source: "talk-only"`. Both raw files are now optional: if they ever
appear the original join path runs unchanged.

The name-normalization and conservative fuzzy-match machinery is kept as-is, so
title variants of the same person still collapse to one page.

Deterministic, name-matching only. No model calls. Idempotent / re-runnable —
always writes a fresh, fully-derived output tree.

Usage: python3 scripts/build_speaker_index.py [--root <project_root>]
"""
import argparse
import glob
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher

# ---------------------------------------------------------------------------
# Name normalization / resolution helpers
# ---------------------------------------------------------------------------

TITLE_RE = re.compile(r'^(dr|prof|mr|ms|mrs)\.?\s+', re.IGNORECASE)
AKA_RE = re.compile(r'\s+aka\s+@?\S+.*$', re.IGNORECASE)
PAREN_RE = re.compile(r'\([^)]*\)')
SPLIT_RE = re.compile(r'\s*&\s*|\s*,\s*|\s+and\s+|\s+ft\.?\s+', re.IGNORECASE)
NONWORD_RE = re.compile(r'[^a-z0-9\s]')
WS_RE = re.compile(r'\s+')

# conservative non-person detector: applied to a *candidate* string after
# splitting on combinators, before name normalization.
NON_PERSON_KEYWORDS = re.compile(
    r'\b(results?|recap|highlights?|playlist|tbd|panel discussion|roundtable|'
    r'keynotes?|state of ai)\b',
    re.IGNORECASE,
)
YEAR_RE = re.compile(r'\b(19|20)\d{2}\b')

# Hand-reviewed identity merges: normalized talk-credit name -> profile name.
# Only for cases the automatic matcher correctly refuses (it will not merge on a
# partial surname) but where external evidence settles it.
MANUAL_ALIASES = {
    # Talk credits "Elizabeth Fuentes" with org AWS; profile is "Elizabeth Fuentes
    # Leone", Developer Advocate at Amazon Web Services (linkedin.com/in/lizfue).
    # Compound surname shortened to the paternal one in the video title.
    'elizabeth fuentes': 'Elizabeth Fuentes Leone',
}


def normalize_name(s: str) -> str:
    """Strip accents, lowercase, drop parentheticals/punctuation, collapse ws."""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = PAREN_RE.sub('', s)
    s = s.lower()
    s = NONWORD_RE.sub(' ', s)
    s = WS_RE.sub(' ', s).strip()
    return s


def clean_candidate(raw: str) -> str:
    """Clean a single split-out candidate name string (title/aka stripped)."""
    s = raw.strip()
    s = AKA_RE.sub('', s)
    s = TITLE_RE.sub('', s)
    s = s.strip(' -—–')
    return s


def split_speaker_string(raw: str):
    """Split a raw speaker field entry into individual candidate name strings."""
    parts = SPLIT_RE.split(raw)
    return [p.strip() for p in parts if p.strip()]


def is_non_person(candidate: str) -> bool:
    if NON_PERSON_KEYWORDS.search(candidate):
        return True
    if YEAR_RE.search(candidate):
        return True
    return False


def slugify(name: str) -> str:
    n = normalize_name(name)
    n = n.replace(' ', '-')
    n = re.sub(r'-+', '-', n).strip('-')
    return n or 'unknown'


def surname_initial_key(norm_name: str):
    toks = norm_name.split()
    if not toks:
        return None
    surname = toks[-1]
    initial = toks[0][0] if toks[0] else ''
    return (surname, initial)


def name_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def strip_fences(s: str) -> str:
    s = s.strip()
    if s.startswith('```'):
        s = re.sub(r'^```[a-zA-Z]*\n', '', s)
        s = re.sub(r'\n```\s*$', '', s)
    return s


def load_passA(passA_dir: str):
    """Return dict slug -> parsed passA extraction dict.

    Prefers the pre-parsed 'passA' key (post quote-verification cleanup) over
    re-parsing the raw 'result' string, because the 'passA' key already
    reflects data/passA/_dropped_quotes.json removals (quotes that failed
    deterministic verification against raw captions). See build report for
    the exact discrepancy this causes vs. a naive 'result' re-parse.
    """
    out = {}
    for fp in sorted(glob.glob(os.path.join(passA_dir, '*.json'))):
        slug = os.path.splitext(os.path.basename(fp))[0]
        if slug == '_dropped_quotes':
            continue
        with open(fp) as f:
            envelope = json.load(f)
        p = envelope.get('passA')
        if p is None:
            # fallback: parse result string
            try:
                p = json.loads(strip_fences(envelope['result']))
            except Exception as e:
                print(f'WARN: could not parse passA for {slug}: {e}', file=sys.stderr)
                continue
        out[slug] = p
    return out


def build(root: str):
    raw_dir = os.path.join(root, 'raw')
    data_dir = os.path.join(root, 'data')
    out_dir = os.path.join(data_dir, 'speakers')
    os.makedirs(out_dir, exist_ok=True)
    # idempotent: clear previously generated output before regenerating, so a
    # speaker who no longer resolves on a re-run doesn't leave a stale file.
    for stale in glob.glob(os.path.join(out_dir, '*.json')):
        os.remove(stale)

    # Optional: this event has no official speaker roster or schedule feed.
    speakers_path = os.path.join(raw_dir, 'speakers.json')
    sessions_path = os.path.join(raw_dir, 'sessions.json')
    if os.path.exists(speakers_path):
        with open(speakers_path) as f:
            profiles_raw = json.load(f)['speakers']
    else:
        profiles_raw = []
    if os.path.exists(sessions_path):
        with open(sessions_path) as f:
            sessions_raw = json.load(f)['sessions']
    else:
        sessions_raw = []
    with open(os.path.join(data_dir, 'index.json')) as f:
        talks = json.load(f)
    with open(os.path.join(data_dir, 'concepts', 'concept_talks.json')) as f:
        concept_talks = json.load(f)  # canonical concept -> [slug, ...]

    passA_dir = os.path.join(data_dir, 'passA')
    passA = load_passA(passA_dir)

    # --- profile index -----------------------------------------------------
    profile_by_norm = {}
    for p in profiles_raw:
        n = normalize_name(p['name'])
        if n in profile_by_norm:
            print(f'WARN: duplicate profile norm name {n!r} — keeping first', file=sys.stderr)
            continue
        profile_by_norm[n] = p

    surname_index = defaultdict(list)
    for n in profile_by_norm:
        key = surname_initial_key(n)
        if key:
            surname_index[key].append(n)

    # --- sessions grouped by normalized speaker name ------------------------
    sessions_by_norm = defaultdict(list)
    for s in sessions_raw:
        for sp_name in s.get('speakers', []):
            n = normalize_name(sp_name)
            sessions_by_norm[n].append({
                'scheduled_title': s.get('title'),
                'track': s.get('track'),
                'day': s.get('day'),
                'time': s.get('time'),
                'room': s.get('room'),
            })

    # --- talk -> canonical concepts (reverse concept_talks.json) -----------
    concepts_by_slug = defaultdict(list)  # slug -> [concept, ...]
    for concept, slugs in concept_talks.items():
        for slug in slugs:
            concepts_by_slug[slug].append(concept)

    # --- speaker registry ----------------------------------------------------
    # speaker_id -> record accumulator
    speakers = {}          # speaker_id -> dict
    norm_to_id = {}         # normalized name -> speaker_id (covers both profile and talk-only)

    fuzzy_matches_log = []
    manual_alias_log = []
    dropped_strings_log = []
    no_speaker_talks = []

    def get_or_create_speaker(display_name: str, norm: str, profile: dict | None):
        if norm in norm_to_id:
            return norm_to_id[norm]
        # canonical identity: for a profile match this is the profile's own
        # normalized name (stable across exact AND fuzzy matches to the same
        # profile); for a talk-only person it's the candidate's own norm.
        canonical_norm = normalize_name(profile['name']) if profile is not None else norm
        if canonical_norm in norm_to_id:
            # already created via a different raw variant (e.g. exact match
            # earlier, this call is a fuzzy match to the same profile)
            sid = norm_to_id[canonical_norm]
            norm_to_id[norm] = sid
            return sid
        sid = slugify(profile['name']) if profile is not None else slugify(display_name)
        # avoid id collisions across distinct identities that happen to slugify
        # the same (defensive; shouldn't occur since slugify is derived 1:1
        # from normalize_name)
        base_sid = sid
        i = 2
        while sid in speakers and speakers[sid]['_norm'] != canonical_norm:
            sid = f'{base_sid}-{i}'
            i += 1
        norm_to_id[norm] = sid
        norm_to_id[canonical_norm] = sid
        if sid not in speakers:
            if profile is not None:
                speakers[sid] = {
                    'speaker_id': sid,
                    'name': profile['name'],
                    'role': profile.get('role') or None,
                    'company': profile.get('company') or None,
                    'bio': profile.get('bio') or None,
                    'linkedin': profile.get('linkedin') or None,
                    'photo_url': profile.get('photoUrl') or None,
                    'profile_source': 'ai.engineer',
                    'talks': [],
                    'sessions': sessions_by_norm.get(canonical_norm, []),
                    'quotes': [],
                    'positions': [],
                    'concepts_raw': defaultdict(set),  # concept -> set(slug)
                    'orgs': set(),
                    '_norm': canonical_norm,
                }
                if profile.get('company'):
                    speakers[sid]['orgs'].add(profile['company'])
            else:
                speakers[sid] = {
                    'speaker_id': sid,
                    'name': display_name,
                    'role': None,
                    'company': None,
                    'bio': None,
                    'linkedin': None,
                    'photo_url': None,
                    'profile_source': 'talk-only',
                    'talks': [],
                    'sessions': sessions_by_norm.get(canonical_norm, []),
                    'quotes': [],
                    'positions': [],
                    'concepts_raw': defaultdict(set),
                    'orgs': set(),
                    '_norm': canonical_norm,
                }
        return sid

    def resolve_candidate(raw_candidate: str, talk_slug: str):
        """Resolve one cleaned candidate name string to a speaker_id, or None if dropped."""
        cleaned = clean_candidate(raw_candidate)
        if is_non_person(cleaned):
            dropped_strings_log.append({'talk_slug': talk_slug, 'raw': raw_candidate})
            return None
        norm = normalize_name(cleaned)
        if not norm:
            dropped_strings_log.append({'talk_slug': talk_slug, 'raw': raw_candidate})
            return None

        # hand-reviewed merge, applied before the automatic paths
        if norm in MANUAL_ALIASES:
            alias_norm = normalize_name(MANUAL_ALIASES[norm])
            if alias_norm in profile_by_norm:
                manual_alias_log.append({
                    'talk_slug': talk_slug,
                    'raw': raw_candidate,
                    'merged_into': profile_by_norm[alias_norm]['name'],
                })
                return get_or_create_speaker(
                    profile_by_norm[alias_norm]['name'], alias_norm,
                    profile_by_norm[alias_norm])

        if norm in norm_to_id:
            return norm_to_id[norm]

        # exact match to a known profile
        if norm in profile_by_norm:
            return get_or_create_speaker(cleaned, norm, profile_by_norm[norm])

        # conservative fuzzy fallback: surname + given-name initial
        key = surname_initial_key(norm)
        if key:
            candidates = surname_index.get(key, [])
            # only accept if exactly one profile shares (surname, initial) AND
            # the full-name similarity is high (guards against unrelated
            # people who happen to share a surname+initial)
            accept = None
            for cand_norm in candidates:
                if cand_norm == norm:
                    continue
                sim = name_similarity(norm, cand_norm)
                if sim >= 0.82:
                    if accept is not None:
                        accept = None  # ambiguous -> bail
                        break
                    accept = cand_norm
            if accept is not None:
                fuzzy_matches_log.append({
                    'talk_slug': talk_slug,
                    'raw': raw_candidate,
                    'matched_to': profile_by_norm[accept]['name'],
                    'similarity': round(name_similarity(norm, accept), 3),
                })
                return get_or_create_speaker(cleaned, norm, profile_by_norm[accept])

        # no match at all: talk-only speaker
        return get_or_create_speaker(cleaned, norm, None)

    # --- process talks -------------------------------------------------------
    total_attributed_quotes = 0
    total_talk_level_quotes = 0
    total_attributed_positions = 0
    total_talk_level_positions = 0
    multi_speaker_talk_slugs = set()
    talk_level_quote_count_by_slug = {}
    talk_level_position_count_by_slug = {}

    for talk in talks:
        slug = talk['slug']
        raw_speakers = talk.get('speakers', [])
        p = passA.get(slug)
        video_id = talk.get('video_id')

        # split combined strings, resolve each candidate
        resolved_ids = []
        for raw_sp in raw_speakers:
            for cand in split_speaker_string(raw_sp):
                sid = resolve_candidate(cand, slug)
                if sid is not None and sid not in resolved_ids:
                    resolved_ids.append(sid)

        if not resolved_ids:
            # no person could be resolved for this talk (0 raw speakers, or
            # every raw speaker string was dropped as a non-person). Any
            # extracted quotes/positions are orphaned — no individual to
            # attribute to — but they still belong in the talk-level
            # conservation total.
            no_speaker_talks.append(slug)
            if p:
                oq = len(p.get('notable_quotes', []))
                opos = len(p.get('positions', []))
                total_talk_level_quotes += oq
                total_talk_level_positions += opos
            continue

        is_sole = len(resolved_ids) == 1
        if not is_sole:
            multi_speaker_talk_slugs.add(slug)

        for sid in resolved_ids:
            rec = speakers[sid]
            rec['talks'].append({
                'slug': slug,
                'title': talk.get('title'),
                'url': talk.get('url'),
                'track': talk.get('track'),
                'day': talk.get('day'),
                'room': talk.get('room'),
                'is_sole_speaker': is_sole,
            })
            org = talk.get('org') or (p.get('speaker_org') if p else None)
            if org:
                rec['orgs'].add(org)
            for c in concepts_by_slug.get(slug, []):
                rec['concepts_raw'][c].add(slug)

        # quotes / positions
        if p:
            quotes = p.get('notable_quotes', [])
            positions = p.get('positions', [])
            if is_sole:
                sid = resolved_ids[0]
                rec = speakers[sid]
                for q in quotes:
                    ts = q.get('timestamp_sec')
                    rec['quotes'].append({
                        'quote': q.get('text'),
                        'timestamp_sec': ts,
                        'talk_slug': slug,
                        'deep_link': f'https://www.youtube.com/watch?v={video_id}&t={ts}s' if video_id and ts is not None else None,
                        'speaker_attributed': True,
                    })
                total_attributed_quotes += len(quotes)
                for pos in positions:
                    ts = pos.get('timestamp_sec')
                    rec['positions'].append({
                        'claim': pos.get('claim'),
                        'confidence': pos.get('confidence'),
                        'timestamp_sec': ts,
                        'talk_slug': slug,
                        'deep_link': f'https://www.youtube.com/watch?v={video_id}&t={ts}s' if video_id and ts is not None else None,
                        'speaker_attributed': True,
                    })
                total_attributed_positions += len(positions)
            else:
                # talk-level: do NOT attach to any individual speaker's
                # quotes/positions list. Just count them, keyed by talk so
                # each co-speaker's stats block can show their share of the
                # talk-level pool without claiming individual attribution.
                total_talk_level_quotes += len(quotes)
                total_talk_level_positions += len(positions)
                talk_level_quote_count_by_slug[slug] = len(quotes)
                talk_level_position_count_by_slug[slug] = len(positions)

    # --- finalize per-speaker records ----------------------------------------
    final_speakers = {}
    for sid, rec in speakers.items():
        concepts_list = []
        for c, slugs in rec['concepts_raw'].items():
            concepts_list.append({
                'concept': c,
                'talk_count': len(slugs),
                'talk_slugs': sorted(slugs),
            })
        concepts_list.sort(key=lambda x: (-x['talk_count'], x['concept']))

        attributed_quote_count = sum(1 for q in rec['quotes'])
        attributed_position_count = sum(1 for p_ in rec['positions'])
        talk_level_quote_count = sum(
            talk_level_quote_count_by_slug.get(t['slug'], 0)
            for t in rec['talks'] if not t['is_sole_speaker']
        )
        talk_level_position_count = sum(
            talk_level_position_count_by_slug.get(t['slug'], 0)
            for t in rec['talks'] if not t['is_sole_speaker']
        )

        # No official profile for this event, so a talk-only speaker's company is
        # whatever the title parser or Pass A's speaker_org resolved. Single
        # unambiguous org only — never guess when a speaker's talks disagree.
        company = rec['company']
        if not company and len(rec['orgs']) == 1:
            company = next(iter(rec['orgs']))

        final_speakers[sid] = {
            'speaker_id': sid,
            'name': rec['name'],
            'role': rec['role'],
            'company': company,
            'bio': rec['bio'],
            'linkedin': rec['linkedin'],
            'photo_url': rec['photo_url'],
            'profile_source': rec['profile_source'],
            'talks': rec['talks'],
            'sessions': rec['sessions'],
            'quotes': rec['quotes'],
            'positions': rec['positions'],
            'concepts': concepts_list,
            'orgs': sorted(rec['orgs']),
            'stats': {
                'talk_count': len(rec['talks']),
                'attributed_quote_count': attributed_quote_count,
                'talk_level_quote_count': talk_level_quote_count,
                'attributed_position_count': attributed_position_count,
                'talk_level_position_count': talk_level_position_count,
                'concept_count': len(concepts_list),
            },
        }

    # --- write per-speaker files ----------------------------------------------
    for sid, rec in final_speakers.items():
        with open(os.path.join(out_dir, f'{sid}.json'), 'w') as f:
            json.dump(rec, f, indent=2, ensure_ascii=False)

    # --- roster index.json -----------------------------------------------------
    roster = []
    for sid, rec in sorted(final_speakers.items(), key=lambda kv: kv[1]['name'].lower()):
        top_concepts = [c['concept'] for c in rec['concepts'][:5]]
        roster.append({
            'speaker_id': sid,
            'name': rec['name'],
            'company': rec['company'],
            'talk_count': rec['stats']['talk_count'],
            'concept_count': rec['stats']['concept_count'],
            'attributed_quote_count': rec['stats']['attributed_quote_count'],
            'top_concepts': top_concepts,
        })
    with open(os.path.join(out_dir, 'index.json'), 'w') as f:
        json.dump(roster, f, indent=2, ensure_ascii=False)

    # --- concept_speakers.json (reverse edge) -----------------------------------
    concept_speakers = defaultdict(list)
    for sid, rec in final_speakers.items():
        for c in rec['concepts']:
            concept_speakers[c['concept']].append({
                'speaker_id': sid,
                'name': rec['name'],
                'talk_count': c['talk_count'],
            })
    for c in concept_speakers:
        concept_speakers[c].sort(key=lambda x: (-x['talk_count'], x['name'].lower()))
    with open(os.path.join(out_dir, 'concept_speakers.json'), 'w') as f:
        json.dump(dict(sorted(concept_speakers.items())), f, indent=2, ensure_ascii=False)

    # --- verification / report ---------------------------------------------
    used_profile_norms = {rec['_norm'] for rec in speakers.values() if rec['profile_source'] == 'ai.engineer'}
    unused_profiles = [p['name'] for n, p in profile_by_norm.items() if n not in used_profile_norms]

    profile_sourced = sum(1 for r in final_speakers.values() if r['profile_source'] == 'ai.engineer')
    talk_only = sum(1 for r in final_speakers.values() if r['profile_source'] == 'talk-only')

    # zero-attribution check on multi-speaker talks
    bad_attrib = []
    for sid, rec in final_speakers.items():
        for q in rec['quotes']:
            if q['talk_slug'] in multi_speaker_talk_slugs and q['speaker_attributed']:
                bad_attrib.append((sid, q['talk_slug']))

    report = {
        'speakers_total': len(final_speakers),
        'profile_sourced': profile_sourced,
        'talk_only': talk_only,
        'profiles_total': len(profile_by_norm),
        'profiles_unused': len(unused_profiles),
        'unused_profiles_sample': unused_profiles[:15],
        'fuzzy_matches_accepted': fuzzy_matches_log,
        'manual_aliases_applied': manual_alias_log,
        'dropped_non_person_strings': dropped_strings_log,
        'no_speaker_talks': no_speaker_talks,
        'multi_speaker_talk_count': len(multi_speaker_talk_slugs),
        'total_attributed_quotes': total_attributed_quotes,
        'total_talk_level_quotes': total_talk_level_quotes,
        'quote_conservation_sum': total_attributed_quotes + total_talk_level_quotes,
        'total_attributed_positions': total_attributed_positions,
        'total_talk_level_positions': total_talk_level_positions,
        'bad_multi_speaker_attribution': bad_attrib,
    }
    with open(os.path.join(out_dir, '_build_report.json'), 'w') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report, final_speakers


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    report, speakers = build(args.root)
    print(json.dumps(report, indent=2, ensure_ascii=False)[:4000])


if __name__ == '__main__':
    main()
