/* AIEWF 2026 graph explorer — Sigma.js v3 + graphology.
 * All layout is precomputed at build time (scripts/build_graph_explorer.py);
 * this file only renders, filters, searches, and answers clicks/hover. No
 * live physics sim runs here.
 */
(function () {
  "use strict";

  var TYPE_LABEL = { talk: "Talk", concept: "Concept", speaker: "Speaker" };

  var state = {
    graph: null,
    sigma: null,
    details: {},
    typeFilters: new Set(["talk", "concept", "speaker"]),
    allTracks: [],
    trackFilters: new Set(),
    hoveredNode: null,
    hoveredNeighbors: null,
    selectedNode: null,
    searchIndex: [],
  };

  function css(varName) {
    return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
  }

  function nodeColor(type) {
    if (type === "talk") return css("--node-talk");
    if (type === "concept") return css("--node-concept");
    if (type === "speaker") return css("--node-speaker");
    return css("--text-muted");
  }

  function fmtDuration(sec) {
    if (!sec && sec !== 0) return null;
    var m = Math.floor(sec / 60), s = Math.round(sec % 60);
    return m + ":" + String(s).padStart(2, "0");
  }

  function fmtTimestamp(sec) {
    if (sec === null || sec === undefined) return null;
    var h = Math.floor(sec / 3600);
    var m = Math.floor((sec % 3600) / 60);
    var s = Math.floor(sec % 60);
    var mm = h > 0 ? String(m).padStart(2, "0") : String(m);
    var ss = String(s).padStart(2, "0");
    return h > 0 ? h + ":" + mm + ":" + ss : mm + ":" + ss;
  }

  function escapeHtml(s) {
    if (s === null || s === undefined) return "";
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // ---------------------------------------------------------------------
  // boot
  // ---------------------------------------------------------------------

  Promise.all([
    fetch("./data/graph.json").then(function (r) { return r.json(); }),
    fetch("./data/details.json").then(function (r) { return r.json(); }),
  ]).then(function (res) {
    boot(res[0], res[1]);
  }).catch(function (err) {
    document.getElementById("loading").textContent =
      "Failed to load graph data: " + err.message;
  });

  function boot(graphData, details) {
    state.details = details;

    var graph = new graphology.Graph({ multi: false, type: "mixed" });

    graphData.nodes.forEach(function (n) {
      graph.addNode(n.id, {
        label: n.label,
        kind: n.type, // NOT "type" — sigma reserves that attribute to pick the WebGL node program
        x: n.x,
        y: n.y,
        size: n.size,
        deg: n.deg,
        track: n.track || null,
        tier: n.tier || null,
        org: n.org || null,
        color: nodeColor(n.type),
      });
    });

    graphData.edges.forEach(function (e) {
      if (!graph.hasNode(e.source) || !graph.hasNode(e.target)) return;
      if (graph.hasEdge(e.source, e.target)) return;
      graph.addEdge(e.source, e.target, { w: e.w, etype: e.type, color: css("--edge-default") });
    });

    state.graph = graph;
    state.allTracks = graphData.meta.tracks || [];
    state.trackFilters = new Set(state.allTracks);

    buildSearchIndex(graphData.nodes);
    renderLegend(graphData.meta);
    renderTypeFilters();
    renderTrackFilters();

    var container = document.getElementById("graph-container");
    var sigma = new Sigma(graph, container, {
      minCameraRatio: 0.02,
      maxCameraRatio: 3,
      labelDensity: 0.8,
      labelGridCellSize: 90,
      labelRenderedSizeThreshold: 7,
      zIndex: true,
      nodeReducer: nodeReducer,
      edgeReducer: edgeReducer,
    });
    state.sigma = sigma;

    wireInteraction(sigma, graph);
    wireSearch();
    wireFilters(sigma);
    wireThemeToggle();

    document.getElementById("loading").classList.add("hidden");

    // deep link: #node=<id>
    handleHash();
    window.addEventListener("hashchange", handleHash);
  }

  // ---------------------------------------------------------------------
  // reducers (hover-dim, type/track filter, selection)
  // ---------------------------------------------------------------------

  function trackVisible(track) {
    if (!track) return true; // untracked talks always shown
    return state.trackFilters.has(track);
  }

  function nodeReducer(node, data) {
    var res = Object.assign({}, data);

    var typeOk = state.typeFilters.has(data.kind);
    var trackOk = data.kind !== "talk" || trackVisible(data.track);
    if (!typeOk || !trackOk) {
      res.hidden = true;
      return res;
    }

    if (state.hoveredNode) {
      var isFocus = node === state.hoveredNode || (state.hoveredNeighbors && state.hoveredNeighbors.has(node));
      if (!isFocus) {
        res.color = css("--node-dim");
        res.label = "";
        res.zIndex = 0;
      } else {
        res.zIndex = 2;
        res.label = data.label;
      }
    }

    if (node === state.selectedNode) {
      res.size = data.size * 1.7;
      res.zIndex = 3;
    }

    return res;
  }

  function edgeReducer(edge, data) {
    var res = Object.assign({}, data);
    var graph = state.graph;
    var src = graph.source(edge), tgt = graph.target(edge);
    var srcData = graph.getNodeAttributes(src), tgtData = graph.getNodeAttributes(tgt);

    var srcOk = state.typeFilters.has(srcData.kind) && (srcData.kind !== "talk" || trackVisible(srcData.track));
    var tgtOk = state.typeFilters.has(tgtData.kind) && (tgtData.kind !== "talk" || trackVisible(tgtData.track));
    if (!srcOk || !tgtOk) {
      res.hidden = true;
      return res;
    }

    if (state.hoveredNode) {
      if (src === state.hoveredNode || tgt === state.hoveredNode) {
        res.color = css("--text-muted");
        res.zIndex = 1;
      } else {
        res.color = css("--edge-dim");
        res.zIndex = 0;
        res.hidden = true; // fully hide non-neighbor edges while hovering; the hairball is the enemy
      }
    } else if (data.etype !== "concept-concept") {
      // At rest, only show the sparse concept-concept backbone (~300 edges).
      // The full talk/speaker fan-out (~2,050 edges) would alpha-composite
      // into a solid haze at this node density — it lights up on hover
      // instead, scoped to one node's neighborhood.
      res.hidden = true;
    }

    return res;
  }

  // ---------------------------------------------------------------------
  // interaction: hover, click, camera
  // ---------------------------------------------------------------------

  function wireInteraction(sigma, graph) {
    sigma.on("enterNode", function (e) {
      state.hoveredNode = e.node;
      state.hoveredNeighbors = new Set(graph.neighbors(e.node));
      sigma.refresh();
      container_style_pointer("pointer");
    });
    sigma.on("leaveNode", function () {
      state.hoveredNode = null;
      state.hoveredNeighbors = null;
      sigma.refresh();
      container_style_pointer("default");
    });
    sigma.on("clickNode", function (e) {
      selectNode(e.node, true);
    });
    sigma.on("clickStage", function () {
      closeDetail();
    });
  }

  function container_style_pointer(cursor) {
    document.getElementById("graph-container").style.cursor = cursor;
  }

  function selectNode(id, updateHash) {
    if (!state.graph.hasNode(id)) return;
    state.selectedNode = id;
    state.sigma.refresh();

    var display = state.sigma.getNodeDisplayData(id);
    if (display) {
      state.sigma.getCamera().animate(
        { x: display.x, y: display.y, ratio: Math.min(state.sigma.getCamera().ratio, 0.35) },
        { duration: 450 }
      );
    }

    openDetail(id);
    if (updateHash !== false) {
      history.replaceState(null, "", "#node=" + encodeURIComponent(id));
    }
  }

  function handleHash() {
    var m = /node=([^&]+)/.exec(location.hash);
    if (m) {
      var id = decodeURIComponent(m[1]);
      if (state.graph.hasNode(id)) selectNode(id, false);
    }
  }

  // ---------------------------------------------------------------------
  // search
  // ---------------------------------------------------------------------

  function buildSearchIndex(nodes) {
    state.searchIndex = nodes.map(function (n) {
      return { id: n.id, label: n.label, type: n.type, lower: n.label.toLowerCase() };
    });
  }

  function wireSearch() {
    var input = document.getElementById("search-input");
    var results = document.getElementById("search-results");
    var activeIdx = -1;
    var currentMatches = [];

    function render(matches) {
      currentMatches = matches;
      activeIdx = -1;
      if (!matches.length) {
        results.classList.remove("open");
        results.innerHTML = "";
        return;
      }
      results.innerHTML = matches.map(function (m, i) {
        return '<div class="result-row" data-idx="' + i + '" data-id="' + escapeHtml(m.id) + '">' +
          '<span class="result-dot" style="background:' + nodeColor(m.type) + '"></span>' +
          '<span class="result-label">' + escapeHtml(m.label) + "</span>" +
          '<span class="result-type">' + TYPE_LABEL[m.type] + "</span>" +
          "</div>";
      }).join("");
      results.classList.add("open");
      Array.prototype.forEach.call(results.querySelectorAll(".result-row"), function (row) {
        row.addEventListener("mousedown", function (ev) {
          ev.preventDefault();
          selectNode(row.getAttribute("data-id"));
          input.value = "";
          render([]);
        });
      });
    }

    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      if (!q) { render([]); return; }
      var starts = [], includes = [];
      for (var i = 0; i < state.searchIndex.length; i++) {
        var item = state.searchIndex[i];
        if (item.lower.indexOf(q) === 0) starts.push(item);
        else if (item.lower.indexOf(q) !== -1) includes.push(item);
        if (starts.length + includes.length > 60) break;
      }
      render(starts.concat(includes).slice(0, 8));
    });

    input.addEventListener("keydown", function (ev) {
      if (!currentMatches.length) return;
      if (ev.key === "ArrowDown") {
        ev.preventDefault();
        activeIdx = Math.min(activeIdx + 1, currentMatches.length - 1);
        highlightActive();
      } else if (ev.key === "ArrowUp") {
        ev.preventDefault();
        activeIdx = Math.max(activeIdx - 1, 0);
        highlightActive();
      } else if (ev.key === "Enter") {
        var pick = currentMatches[activeIdx >= 0 ? activeIdx : 0];
        if (pick) {
          selectNode(pick.id);
          input.value = "";
          render([]);
        }
      } else if (ev.key === "Escape") {
        input.value = "";
        render([]);
        input.blur();
      }
    });

    function highlightActive() {
      Array.prototype.forEach.call(results.querySelectorAll(".result-row"), function (row, i) {
        row.classList.toggle("active", i === activeIdx);
      });
    }

    document.addEventListener("click", function (ev) {
      if (!results.contains(ev.target) && ev.target !== input) render([]);
    });
  }

  // ---------------------------------------------------------------------
  // legend + filters
  // ---------------------------------------------------------------------

  function renderLegend(meta) {
    var el = document.getElementById("legend");
    var items = [
      ["talk", meta.node_counts.talk],
      ["concept", meta.node_counts.concept],
      ["speaker", meta.node_counts.speaker],
    ];
    el.innerHTML = items.filter(function (it) { return it[1] > 0; }).map(function (it) {
      return '<span class="legend-item"><span class="legend-dot" style="background:' + nodeColor(it[0]) + '"></span>' +
        TYPE_LABEL[it[0]] + ' <span class="legend-count">' + it[1] + "</span></span>";
    }).join("");
  }

  function renderTypeFilters() {
    var el = document.getElementById("type-filters");
    var types = ["talk", "concept", "speaker"];
    el.innerHTML = types.map(function (t) {
      return '<label class="filter-row type-' + t + '">' +
        '<input type="checkbox" checked data-type="' + t + '">' +
        '<span class="swatch"></span>' + TYPE_LABEL[t] + "</label>";
    }).join("");
  }

  function renderTrackFilters() {
    var wrap = document.getElementById("track-filters-wrap");
    if (!state.allTracks.length) { wrap.style.display = "none"; return; }
    var el = document.getElementById("track-filters");
    el.innerHTML = state.allTracks.map(function (tr) {
      return '<label class="filter-row"><input type="checkbox" checked data-track="' + escapeHtml(tr) + '">' + escapeHtml(tr) + "</label>";
    }).join("");
  }

  function wireFilters(sigma) {
    document.getElementById("type-filters").addEventListener("change", function (ev) {
      var t = ev.target.getAttribute("data-type");
      if (!t) return;
      if (ev.target.checked) state.typeFilters.add(t); else state.typeFilters.delete(t);
      sigma.refresh();
    });
    document.getElementById("track-filters").addEventListener("change", function (ev) {
      var t = ev.target.getAttribute("data-track");
      if (!t) return;
      if (ev.target.checked) state.trackFilters.add(t); else state.trackFilters.delete(t);
      sigma.refresh();
    });
    document.getElementById("tracks-all").addEventListener("click", function () {
      state.trackFilters = new Set(state.allTracks);
      Array.prototype.forEach.call(document.querySelectorAll("#track-filters input"), function (i) { i.checked = true; });
      sigma.refresh();
    });
    document.getElementById("tracks-none").addEventListener("click", function () {
      state.trackFilters = new Set();
      Array.prototype.forEach.call(document.querySelectorAll("#track-filters input"), function (i) { i.checked = false; });
      sigma.refresh();
    });
  }

  function wireThemeToggle() {
    var btn = document.getElementById("theme-toggle");
    function apply(mode) {
      if (mode) document.documentElement.setAttribute("data-theme", mode);
      else document.documentElement.removeAttribute("data-theme");
      btn.textContent = mode === "dark" ? "Dark" : mode === "light" ? "Light" : "Auto";
      if (state.sigma) {
        state.graph.forEachNode(function (n, attrs) {
          state.graph.setNodeAttribute(n, "color", nodeColor(attrs.kind));
        });
        state.graph.forEachEdge(function (e) {
          state.graph.setEdgeAttribute(e, "color", css("--edge-default"));
        });
        state.sigma.refresh();
      }
    }
    var cur = null;
    btn.addEventListener("click", function () {
      cur = cur === null ? "dark" : cur === "dark" ? "light" : null;
      apply(cur);
    });
  }

  // ---------------------------------------------------------------------
  // detail panel
  // ---------------------------------------------------------------------

  function openDetail(id) {
    var d = state.details[id];
    var panel = document.getElementById("detail-panel");
    if (!d) { panel.classList.remove("open"); return; }

    var html = '<button class="detail-close" id="detail-close-btn">Close</button>';
    html += '<div class="detail-type-badge ' + d.type + '">' + TYPE_LABEL[d.type] + "</div>";

    if (d.type === "talk") html += renderTalk(d);
    else if (d.type === "concept") html += renderConcept(d);
    else if (d.type === "speaker") html += renderSpeaker(d);

    panel.innerHTML = html;
    panel.classList.add("open");
    document.getElementById("detail-close-btn").addEventListener("click", closeDetail);
    Array.prototype.forEach.call(panel.querySelectorAll("[data-nodelink]"), function (el) {
      el.addEventListener("click", function () {
        selectNode(el.getAttribute("data-nodelink"));
      });
    });
  }

  function closeDetail() {
    document.getElementById("detail-panel").classList.remove("open");
    state.selectedNode = null;
    state.sigma.refresh();
    history.replaceState(null, "", location.pathname + location.search);
  }

  function renderTalk(d) {
    var html = '<h2 class="detail-title">' + escapeHtml(d.title) + "</h2>";
    html += '<div class="detail-meta">';
    if (d.speakers && d.speakers.length) html += "<strong>" + escapeHtml(d.speakers.join(", ")) + "</strong><br>";
    if (d.org) html += escapeHtml(d.org) + "<br>";
    if (d.track) html += '<span class="chip">' + escapeHtml(d.track) + "</span> ";
    if (d.duration_sec) html += '<span class="chip">' + fmtDuration(d.duration_sec) + "</span> ";
    if (d.url) html += '<br><a href="' + escapeHtml(d.url) + '" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>';
    html += "</div>";

    if (d.summary) {
      html += '<div class="detail-section"><h4>Summary</h4><p>' + escapeHtml(d.summary) + "</p></div>";
    }

    if (d.quotes && d.quotes.length) {
      html += '<div class="detail-section"><h4>Notable quotes</h4>';
      d.quotes.forEach(function (q) {
        html += '<div class="quote-card"><p class="quote-text">“' + escapeHtml(q.text) + '”</p>';
        if (q.youtube_url) {
          var ts = fmtTimestamp(q.timestamp_sec);
          html += '<a class="quote-link" href="' + escapeHtml(q.youtube_url) + '" target="_blank" rel="noopener">Watch at ' + (ts || "start") + " &rarr;</a>";
        }
        html += "</div>";
      });
      html += "</div>";
    }

    if (d.concepts && d.concepts.length) {
      html += '<div class="detail-section"><h4>Concepts (' + d.concepts.length + ')</h4>';
      d.concepts.forEach(function (c) {
        html += '<span class="chip chip-link" data-nodelink="' + escapeHtml(c.id) + '">' + escapeHtml(c.label) + "</span>";
      });
      html += "</div>";
    }
    return html;
  }

  function renderConcept(d) {
    var html = '<h2 class="detail-title">' + escapeHtml(d.name) + "</h2>";
    html += '<div class="detail-meta">';
    if (d.tier) html += '<span class="chip">' + escapeHtml(d.tier) + " tier</span> ";
    html += '<span class="chip">' + d.talk_count + " talk" + (d.talk_count === 1 ? "" : "s") + "</span>";
    html += "</div>";

    if (d.maturity) {
      html += '<div class="maturity-badge">Maturity: ' + escapeHtml(d.maturity) + "</div>";
    }

    if (d.definition) {
      html += '<div class="detail-section"><h4>Definition</h4><p>' + escapeHtml(d.definition) + "</p></div>";
    }

    if (d.state_of_practice) {
      html += '<div class="detail-section"><h4>State of practice</h4><p>' + escapeHtml(d.state_of_practice) + "</p></div>";
    }

    if (d.talks && d.talks.length) {
      html += '<div class="detail-section"><h4>Talks</h4>';
      d.talks.forEach(function (t) {
        html += '<a class="node-link-row" data-nodelink="' + escapeHtml(t.id) + '">' + escapeHtml(t.title) +
          (t.track ? '<span class="sub"> &middot; ' + escapeHtml(t.track) + "</span>" : "") + "</a>";
      });
      html += "</div>";
    }
    return html;
  }

  function renderSpeaker(d) {
    var html = '<h2 class="detail-title">' + escapeHtml(d.name) + "</h2>";
    html += '<div class="detail-meta">';
    var line = [d.role, d.company].filter(Boolean).join(" at ");
    if (line) html += escapeHtml(line);
    html += "</div>";

    if (d.bio) {
      html += '<div class="detail-section"><h4>Bio</h4><p>' + escapeHtml(d.bio) + "</p></div>";
    }

    if (d.talks && d.talks.length) {
      html += '<div class="detail-section"><h4>Talks (' + d.talks.length + ")</h4>";
      d.talks.forEach(function (t) {
        html += '<a class="node-link-row" data-nodelink="' + escapeHtml(t.id) + '">' + escapeHtml(t.title) +
          (t.track ? '<span class="sub"> &middot; ' + escapeHtml(t.track) + "</span>" : "") + "</a>";
      });
      html += "</div>";
    }

    if (d.concepts && d.concepts.length) {
      html += '<div class="detail-section"><h4>Concepts</h4>';
      d.concepts.forEach(function (c) {
        html += '<span class="chip chip-link" data-nodelink="' + escapeHtml(c.id) + '">' + escapeHtml(c.label) + "</span>";
      });
      html += "</div>";
    }
    return html;
  }
})();
