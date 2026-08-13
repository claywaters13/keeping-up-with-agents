#!/usr/bin/env python3
"""
Build the tripartite (talk / concept / speaker) graph explorer data files
for viz/explorer/ — the interactive Sigma.js graph linked from the LinkedIn
announcement post.

Reads:
  data/index.json                     231 talks
  data/concepts/canonical.json        134 canonical concepts (def, tier)
  data/concepts/concept_talks.json    concept -> [talk_slug, ...] (1,784 edges)
  data/passA/<slug>.json              per-talk summary + notable_quotes (for
                                       the talk detail panel)
  data/passC/<concept-slug>.json      per-concept state_of_practice/maturity,
                                       read defensively (owned by a
                                       concurrently-running agent; the
                                       extraction JSON lives in a `passC` key
                                       or, failing that, inside a `result`
                                       string that may be markdown-fenced —
                                       any file that doesn't parse is skipped,
                                       not fatal)
  data/speakers/index.json + <id>.json  OPTIONAL. If absent (another agent
                                       may still be building this), the
                                       script builds the talk+concept graph
                                       only and leaves speakers out cleanly —
                                       re-running later picks them up with no
                                       code changes.

Writes:
  viz/explorer/data/graph.json    topology + baked x/y coords (ForceAtlas2,
                                   precomputed here — no live sim on load)
  viz/explorer/data/details.json  panel content (summaries, quotes, defs)

Idempotent / re-runnable: always regenerates fully from current source data,
so it's safe to re-run as Pass C output and the speaker index land.

Does NOT write to data/passC/ or data/speakers/ — those are owned by other
build steps running concurrently.

Usage: python3 scripts/build_graph_explorer.py [--root ~/aiewf-2026]
"""
import argparse
import json
import math
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from forceatlas2 import layout as fa2_layout


def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def load_json(path):
    with open(path) as f:
        return json.load(f)


def try_load_passc(path):
    """Load a Pass C envelope defensively. Returns the parsed passC dict, or
    None if the file is missing, mid-write, or fails to parse in any way."""
    try:
        with open(path) as f:
            d = json.load(f)
    except Exception:
        return None
    if isinstance(d, dict) and isinstance(d.get('passC'), dict):
        return d['passC']
    result = d.get('result') if isinstance(d, dict) else None
    if not isinstance(result, str):
        return None
    text = result.strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
    if m:
        text = m.group(1).strip()
    try:
        parsed = json.loads(text)
    except Exception:
        return None
    return parsed if isinstance(parsed, dict) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.expanduser('~/aiewf-2026'))
    ap.add_argument('--concept-cooc-threshold', type=int, default=4,
                     help='min shared talks for a concept-concept edge')
    ap.add_argument('--iterations', type=int, default=800)
    ap.add_argument('--seed', type=int, default=42)
    args = ap.parse_args()
    root = args.root
    t0 = time.time()

    # ---- load sources -------------------------------------------------
    talks = load_json(f'{root}/data/index.json')
    canon = load_json(f'{root}/data/concepts/canonical.json')['canonical']
    concept_talks = load_json(f'{root}/data/concepts/concept_talks.json')

    speakers_present = os.path.isfile(f'{root}/data/speakers/index.json')
    speaker_roster = []
    speaker_records = {}
    if speakers_present:
        try:
            speaker_roster = load_json(f'{root}/data/speakers/index.json')
        except Exception:
            speaker_roster = []
        for s in speaker_roster:
            sid = s.get('speaker_id')
            p = f'{root}/data/speakers/{sid}.json'
            if sid and os.path.isfile(p):
                try:
                    speaker_records[sid] = load_json(p)
                except Exception:
                    pass

    passa_by_slug = {}
    for t in talks:
        p = f"{root}/data/passA/{t['slug']}.json"
        if os.path.isfile(p):
            try:
                d = load_json(p)
                pa = d.get('passA')
                if isinstance(pa, dict):
                    passa_by_slug[t['slug']] = pa
            except Exception:
                pass

    # ---- concept slug map ----------------------------------------------
    concept_slug = {}   # concept name -> slug
    concept_meta = {}   # slug -> canonical record
    for c in canon:
        slug = slugify(c['concept'])
        concept_slug[c['concept']] = slug
        concept_meta[slug] = c

    passc_by_slug = {}
    passc_dir = f'{root}/data/passC'
    if os.path.isdir(passc_dir):
        for fn in sorted(os.listdir(passc_dir)):
            if not fn.endswith('.json'):
                continue
            slug = fn[:-5]
            if slug not in concept_meta:
                continue
            parsed = try_load_passc(f'{passc_dir}/{fn}')
            if parsed is not None:
                passc_by_slug[slug] = parsed

    # ---- nodes -----------------------------------------------------------
    nodes = {}
    talk_slug_set = {t['slug'] for t in talks}

    for t in talks:
        nid = f"talk:{t['slug']}"
        nodes[nid] = {
            'id': nid, 'type': 'talk', 'label': t['title'],
            'track': t.get('track') or None,
        }

    for slug, c in concept_meta.items():
        nid = f'concept:{slug}'
        nodes[nid] = {
            'id': nid, 'type': 'concept', 'label': c['concept'],
            'tier': c.get('tier'),
        }

    for s in speaker_roster:
        sid = s.get('speaker_id')
        if not sid:
            continue
        nid = f'speaker:{sid}'
        nodes[nid] = {
            'id': nid, 'type': 'speaker', 'label': s.get('name'),
            'org': s.get('company'),
        }

    # ---- edges -------------------------------------------------------------
    edges = []  # (source, target, weight, type)
    skipped_concept_talk_refs = 0
    for concept_name, talk_slugs in concept_talks.items():
        slug = concept_slug.get(concept_name)
        if slug is None:
            continue
        cid = f'concept:{slug}'
        for ts in talk_slugs:
            if ts not in talk_slug_set:
                skipped_concept_talk_refs += 1
                continue
            edges.append((cid, f'talk:{ts}', 1.0, 'talk-concept'))

    talk_sets = {c: set(v) for c, v in concept_talks.items()}
    names = [c['concept'] for c in canon]
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            shared = len(talk_sets.get(a, set()) & talk_sets.get(b, set()))
            if shared >= args.concept_cooc_threshold:
                edges.append((f'concept:{concept_slug[a]}', f'concept:{concept_slug[b]}',
                               float(shared), 'concept-concept'))

    talk_speaker_edges = 0
    for s in speaker_roster:
        sid = s.get('speaker_id')
        rec = speaker_records.get(sid)
        if not rec:
            continue
        for t in rec.get('talks', []):
            ts = t.get('slug')
            if ts in talk_slug_set:
                edges.append((f'speaker:{sid}', f'talk:{ts}', 1.0, 'talk-speaker'))
                talk_speaker_edges += 1

    # ---- degree (drives node size) -----------------------------------------
    degree = {nid: 0 for nid in nodes}
    for s, t, w, _ in edges:
        if s in degree:
            degree[s] += 1
        if t in degree:
            degree[t] += 1
    for nid, n in nodes.items():
        n['deg'] = degree.get(nid, 0)

    # ---- layout (baked at build time, no live sim on page load) ------------
    node_ids = list(nodes.keys())
    layout_edges = [(s, t, w) for s, t, w, _ in edges]
    coords = fa2_layout(node_ids, layout_edges, seed=args.seed, iterations=args.iterations)
    for nid, (x, y) in coords.items():
        nodes[nid]['x'] = round(x, 2)
        nodes[nid]['y'] = round(y, 2)

    max_deg = max((n['deg'] for n in nodes.values()), default=1) or 1
    for n in nodes.values():
        n['size'] = round(3.0 + 9.0 * math.sqrt(n['deg'] / max_deg), 2)

    # ---- assemble graph.json (topology, kept lean) --------------------------
    graph_nodes = []
    for n in nodes.values():
        rec = {'id': n['id'], 'type': n['type'], 'label': n['label'],
               'x': n['x'], 'y': n['y'], 'size': n['size'], 'deg': n['deg']}
        if n['type'] == 'talk':
            rec['track'] = n.get('track')
        elif n['type'] == 'concept':
            rec['tier'] = n.get('tier')
        elif n['type'] == 'speaker':
            rec['org'] = n.get('org')
        graph_nodes.append(rec)

    graph_edges = [{'source': s, 'target': t, 'w': w, 'type': ty} for s, t, w, ty in edges]
    tracks = sorted({n.get('track') for n in graph_nodes if n['type'] == 'talk' and n.get('track')})

    graph = {
        'meta': {
            'generated_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'node_counts': {
                'talk': sum(1 for n in graph_nodes if n['type'] == 'talk'),
                'concept': sum(1 for n in graph_nodes if n['type'] == 'concept'),
                'speaker': sum(1 for n in graph_nodes if n['type'] == 'speaker'),
            },
            'edge_counts': {
                'talk-concept': sum(1 for e in graph_edges if e['type'] == 'talk-concept'),
                'concept-concept': sum(1 for e in graph_edges if e['type'] == 'concept-concept'),
                'talk-speaker': sum(1 for e in graph_edges if e['type'] == 'talk-speaker'),
            },
            'speakers_present': speakers_present,
            'tracks': tracks,
        },
        'nodes': graph_nodes,
        'edges': graph_edges,
    }

    # ---- assemble details.json (panel content) -------------------------------
    details = {}
    for t in talks:
        slug = t['slug']
        nid = f'talk:{slug}'
        pa = passa_by_slug.get(slug, {})
        concepts_for_talk = [
            {'id': f'concept:{concept_slug[c]}', 'label': c}
            for c in concept_talks
            if c in concept_slug and slug in talk_sets.get(c, ())
        ]
        quotes = []
        for q in (pa.get('notable_quotes') or [])[:5]:
            sec = q.get('timestamp_sec')
            yt = (f"https://www.youtube.com/watch?v={t['video_id']}&t={int(sec)}s"
                  if sec is not None and t.get('video_id') else t.get('url'))
            quotes.append({'text': q.get('text'), 'timestamp_sec': sec,
                            'why': q.get('why'), 'youtube_url': yt})
        details[nid] = {
            'id': nid, 'type': 'talk', 'title': t['title'],
            'speakers': t.get('speakers') or [],
            'org': t.get('org') or None,
            'track': t.get('track') or None,
            'url': t.get('url'), 'video_id': t.get('video_id'),
            'duration_sec': t.get('duration_sec'), 'word_count': t.get('word_count'),
            'summary': pa.get('summary'),
            'quotes': quotes,
            'concepts': concepts_for_talk,
        }

    for slug, c in concept_meta.items():
        nid = f'concept:{slug}'
        talk_slugs = [s for s in concept_talks.get(c['concept'], []) if s in talk_slug_set]
        talk_index = {x['slug']: x for x in talks}
        talk_list = [{'id': f'talk:{ts}', 'title': talk_index[ts]['title'], 'track': talk_index[ts].get('track')}
                     for ts in talk_slugs if ts in talk_index]
        pc = passc_by_slug.get(slug)
        details[nid] = {
            'id': nid, 'type': 'concept', 'name': c['concept'],
            'definition': c.get('definition'), 'tier': c.get('tier'),
            'talk_count': len(talk_list), 'talks': talk_list,
            'state_of_practice': pc.get('state_of_practice') if pc else None,
            'maturity': pc.get('maturity') if pc else None,
        }

    for s in speaker_roster:
        sid = s.get('speaker_id')
        if not sid:
            continue
        nid = f'speaker:{sid}'
        rec = speaker_records.get(sid, {})
        talk_list = [{'id': f"talk:{t['slug']}", 'title': t.get('title'), 'track': t.get('track')}
                     for t in rec.get('talks', [])]
        concept_list = [{'id': f"concept:{concept_slug[c['concept']]}", 'label': c['concept']}
                         for c in rec.get('concepts', []) if c.get('concept') in concept_slug]
        details[nid] = {
            'id': nid, 'type': 'speaker', 'name': s.get('name'),
            'role': rec.get('role'), 'company': s.get('company'), 'bio': rec.get('bio'),
            'talks': talk_list, 'concepts': concept_list,
        }

    # ---- write ------------------------------------------------------------
    out_dir = f'{root}/viz/explorer/data'
    os.makedirs(out_dir, exist_ok=True)
    with open(f'{out_dir}/graph.json', 'w') as f:
        json.dump(graph, f, separators=(',', ':'), ensure_ascii=False)
    with open(f'{out_dir}/details.json', 'w') as f:
        json.dump(details, f, separators=(',', ':'), ensure_ascii=False)

    graph_size = os.path.getsize(f'{out_dir}/graph.json')
    details_size = os.path.getsize(f'{out_dir}/details.json')

    print(json.dumps({
        'elapsed_sec': round(time.time() - t0, 1),
        'nodes': graph['meta']['node_counts'],
        'edges': graph['meta']['edge_counts'],
        'total_nodes': len(graph_nodes),
        'total_edges': len(graph_edges),
        'speakers_present': speakers_present,
        'concepts_with_passC': len(passc_by_slug),
        'talks_with_passA': len(passa_by_slug),
        'skipped_concept_talk_refs': skipped_concept_talk_refs,
        'graph_json_bytes': graph_size,
        'details_json_bytes': details_size,
        'total_bytes': graph_size + details_size,
    }, indent=2))


if __name__ == '__main__':
    main()
