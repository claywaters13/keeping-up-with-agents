#!/usr/bin/env python3
"""
Minimal vectorized ForceAtlas2-style layout (numpy only, no JS/Node dependency).

Implements the core ForceAtlas2 forces (Jacomy et al. 2014) on a dense
adjacency matrix: mass-scaled repulsion between every node pair, weighted
attraction along edges, and gravity pulling everything toward the origin,
with a linear cooling schedule for stable convergence. Deterministic given a
fixed random seed for the initial layout.

Not Barnes-Hut accelerated — repulsion is O(n^2) per iteration, which is
fine up to a few thousand nodes (this project has ~600) and keeps the
implementation dependency-free and auditable.
"""
import numpy as np


def layout(
    node_ids,
    edges,  # list of (source_id, target_id, weight)
    seed=42,
    iterations=800,
    gravity=1.0,
    scaling=8.0,
    init_radius=500.0,
):
    """Return {node_id: (x, y)}.

    node_ids: ordered list of unique node id strings.
    edges: iterable of (source_id, target_id, weight).
    """
    n = len(node_ids)
    index = {nid: i for i, nid in enumerate(node_ids)}

    # degree (mass) from edge endpoints, +1 per FA2 convention so isolated
    # nodes still repel.
    degree = np.zeros(n, dtype=np.float64)
    src = np.zeros(len(edges), dtype=np.int64)
    dst = np.zeros(len(edges), dtype=np.int64)
    w = np.zeros(len(edges), dtype=np.float64)
    for k, (s, t, weight) in enumerate(edges):
        si, ti = index[s], index[t]
        src[k], dst[k], w[k] = si, ti, weight
        degree[si] += weight
        degree[ti] += weight
    mass = degree + 1.0

    # deterministic seeded initial positions on a circle + jitter, grouped
    # loosely so the sim doesn't have to untangle a fully random start.
    rng = np.random.default_rng(seed)
    angles = rng.uniform(0, 2 * np.pi, n)
    radii = init_radius * np.sqrt(rng.uniform(0.15, 1.0, n))
    pos = np.stack([radii * np.cos(angles), radii * np.sin(angles)], axis=1)

    for it in range(iterations):
        cooling = 1.0 - (it / iterations) * 0.92  # decays to 0.08x speed

        # --- repulsion (all pairs) ---
        delta = pos[:, None, :] - pos[None, :, :]  # (n, n, 2)
        dist2 = np.sum(delta ** 2, axis=2)
        np.fill_diagonal(dist2, 1.0)
        dist = np.sqrt(dist2)
        np.fill_diagonal(dist, 1.0)
        rep_factor = scaling * np.outer(mass, mass) / dist2
        np.fill_diagonal(rep_factor, 0.0)
        rep = np.sum(rep_factor[:, :, None] * (delta / dist[:, :, None]), axis=1)

        # --- attraction (edges, weighted, linear FA2 model) ---
        att = np.zeros_like(pos)
        if len(edges):
            ed = pos[src] - pos[dst]
            edist = np.sqrt(np.sum(ed ** 2, axis=1))
            edist_safe = np.where(edist < 1e-6, 1e-6, edist)
            mag = w  # linear attraction, proportional to edge weight
            fx = -ed[:, 0] / edist_safe * mag * edist_safe / 1.0
            fy = -ed[:, 1] / edist_safe * mag * edist_safe / 1.0
            # simplifies to: force along edge proportional to weight (Hooke-ish)
            fvec = -ed * mag[:, None]
            np.add.at(att, src, fvec)
            np.add.at(att, dst, -fvec)

        # --- gravity (toward origin, mass-scaled) ---
        dist_origin = np.sqrt(np.sum(pos ** 2, axis=1))
        dist_origin_safe = np.where(dist_origin < 1e-6, 1e-6, dist_origin)
        grav = -gravity * mass[:, None] * pos / dist_origin_safe[:, None]

        force = (rep + att * 0.02 + grav) * cooling
        # clamp per-step displacement to avoid blow-ups early on
        step_norm = np.sqrt(np.sum(force ** 2, axis=1))
        max_step = 50.0 * cooling + 1.0
        scale = np.where(step_norm > max_step, max_step / np.where(step_norm == 0, 1, step_norm), 1.0)
        pos = pos + force * scale[:, None] * 0.02

    return {nid: (float(pos[i, 0]), float(pos[i, 1])) for i, nid in enumerate(node_ids)}
