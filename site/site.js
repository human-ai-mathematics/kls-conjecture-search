/*
  site/site.js — the reader, the router, and the two maps.

  This file knows how to *display* a claim graph and a search portfolio. It does not know
  any mathematics, any status, any route, or any repository rule: all of that arrives in
  data.json, derived by scripts/site.py from the same validated report scripts/check.py
  prints. Everything user-visible below is chrome — headings, legends, empty states — with
  one deliberate exception noted where it occurs: the relation glosses travel *with* the
  data, so the legend cannot drift from research/program/ledger-schema.md.

  The distinction the interface exists to preserve, and the reason there are two maps
  rather than one:

      Ledger = what is mathematically claimed.
      Portfolio = what the search is doing.
      Checkpoints = why the portfolio changed.

  An approach is not a theorem. `completed` means an approach's objective ended, never that the
  target was settled; `saturated` is a synthesis judgment about effort, not a fact about
  mathematics. The two maps never share a canvas.
*/

'use strict';

/* ------------------------------------------------------------------ DOM helpers ---- */

const SVG_NS = 'http://www.w3.org/2000/svg';

/** Build an element. Children may be nodes, strings, arrays, or null. */
function el(tag, props, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(props || {})) {
    if (value === null || value === undefined || value === false) continue;
    if (key === 'class') node.className = value;
    else if (key === 'text') node.textContent = value;
    else if (key === 'html') node.appendChild(value);
    else if (key.startsWith('on')) node.addEventListener(key.slice(2), value);
    else if (key === 'dataset') Object.assign(node.dataset, value);
    else node.setAttribute(key, value === true ? '' : String(value));
  }
  append(node, children);
  return node;
}

function svg(tag, props, ...children) {
  const node = document.createElementNS(SVG_NS, tag);
  for (const [key, value] of Object.entries(props || {})) {
    if (value === null || value === undefined || value === false) continue;
    if (key.startsWith('on')) node.addEventListener(key.slice(2), value);
    else node.setAttribute(key, String(value));
  }
  append(node, children);
  return node;
}

function append(parent, children) {
  for (const child of children.flat(4)) {
    if (child === null || child === undefined || child === false) continue;
    parent.appendChild(typeof child === 'string' ? document.createTextNode(child) : child);
  }
}

function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }

/**
 * Place text containing LaTeX `$...$` into the DOM as text, never as markup.
 *
 * The dollar spans are wrapped so MathJax can typeset them if it loaded. When it did
 * not, the source stays on screen and stays readable — which is why the raw text goes in
 * first and typesetting happens afterwards.
 */
function math(text) {
  const fragment = document.createDocumentFragment();
  if (!text) return fragment;
  const parts = String(text).split(/(\$[^$]*\$)/g);
  for (const part of parts) {
    if (!part) continue;
    if (part.startsWith('$') && part.endsWith('$') && part.length > 1) {
      fragment.appendChild(el('span', { class: 'math', text: part }));
    } else {
      fragment.appendChild(document.createTextNode(part));
    }
  }
  return fragment;
}

/* Scopes and rows waiting to be handed to MathJax, and the frame that will hand them
 * over. Batching matters: MathJax walks and lays out everything it is given in one
 * synchronous burst, so one call per row is one long task per row, while one call for
 * the rows that just came into view is one short task for all of them.
 *
 * Nothing in this queue is needed for legibility. The LaTeX source is already on screen
 * — see math() — so a scope that is never flushed, because MathJax never loaded or the
 * reader never scrolled to it, reads as source rather than as a gap.
 */
const PENDING_TYPESET = new Set();
let typesetFrame = 0;

function mathjaxReady() {
  return !!(window.MathJax && typeof window.MathJax.typesetPromise === 'function');
}

function flushTypeset() {
  typesetFrame = 0;
  /* What the reader has navigated away from is never going to be typeset. Drop it here
     rather than in the MathJax branch, so a reader whose MathJax never arrives does not
     accumulate detached rows for the length of the session. */
  for (const node of PENDING_TYPESET) if (!node.isConnected) PENDING_TYPESET.delete(node);
  if (!mathjaxReady() || !PENDING_TYPESET.size) return; /* the ready event comes back */
  const batch = [...PENDING_TYPESET];
  PENDING_TYPESET.clear();
  window.MathJax.typesetPromise(batch).catch(() => { /* source stays visible */ });
}

function typeset(scope) {
  PENDING_TYPESET.add(scope);
  if (!typesetFrame) typesetFrame = requestAnimationFrame(flushTypeset);
}

/* MathJax is loaded with `defer`, so on a cold load it is not there when the first view
 * renders and every typeset() call before it arrives would otherwise be dropped. The
 * shell fires this once startup finishes; if the CDN is blocked it never fires, and the
 * source stays on screen, which is the arrangement index.html is built around. */
document.addEventListener('mathjax-ready', flushTypeset);

/* How far outside the viewport a row is typeset. Roughly a screenful, so scrolling at a
 * normal speed never overtakes MathJax and reaches a row still showing its source. */
const TYPESET_MARGIN = '800px';

const ROW_WATCHERS = new WeakMap();

/**
 * Hand a long list to MathJax a row at a time, as the rows are scrolled to.
 *
 * `mathjax_ignore` is MathJax's own opt-out class: it stops the whole-page pass dead at
 * the `<ul>`, so the 138 claims cost nothing at render time, and each `<li>` is then
 * passed in on its own — which still typesets, because the ignore class is only
 * consulted on the way down from whatever element MathJax was handed.
 *
 * Returns false when the browser has no IntersectionObserver, in which case the list is
 * left for the caller's ordinary whole-scope typeset, exactly as before.
 */
function deferRows(list) {
  if (typeof IntersectionObserver !== 'function') return false;
  list.classList.add('mathjax_ignore');
  let watcher = ROW_WATCHERS.get(list);
  if (watcher) {
    /* A redraw replaced the rows; the old ones are detached and must not be held. */
    watcher.disconnect();
  } else {
    watcher = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        watcher.unobserve(entry.target);
        typeset(entry.target);
      }
    }, { rootMargin: TYPESET_MARGIN });
    ROW_WATCHERS.set(list, watcher);
  }
  for (const row of list.children) watcher.observe(row);
  return true;
}

/* ------------------------------------------------------------------- vocabulary ---- */

/* Presentation only: a glyph and a word for each state, so colour is never the sole
   carrier of meaning. What the states *mean* is the repository's business, not this
   file's — the words below are the repository's own vocabulary, unaltered. */
const STATUS_GLYPH = { proved: '✓', open: '○', refuted: '✗', defined: '≡' };
const APPROACH_GLYPH = {
  queued: '·', active: '▸', blocked: '■', completed: '✓', duplicate: '⧉',
};
const FAMILY_GLYPH = { active: '▸', saturated: '◼', parked: '❙❙' };

const OUTCOME_WORD = {
  'dead-end': 'dead end', directional: 'directional',
  candidate: 'candidate', proposed: 'proposed',
};

let DATA = null;

function statusBadge(status) {
  const known = Object.prototype.hasOwnProperty.call(STATUS_GLYPH, status);
  return el('span', { class: `badge ${known ? status : 'neutral'}` },
    el('span', { class: 'glyph', 'aria-hidden': 'true', text: STATUS_GLYPH[status] || '?' }),
    status || 'unknown');
}

/* The tone glyphs. Same discipline as STATUS_GLYPH above: a shape so the badge survives
   monochrome and colour-blindness, and the words themselves carry the meaning. The tone
   names are the repository's, exported in data.json beside every claim; this file only
   decides what each one looks like. */
const STANDING_GLYPH = {
  published: '◆', preprint: '◇', certified: '✓', attested: '✓',
  'proved-elsewhere': '✓', open: '○', premise: '◻', barrier: '⚠',
  refuted: '✗', definition: '≡',
};

/* One reading order over the same tones: what is settled, then what rests on evidence
   of decreasing weight, then what is open, then what is closed the other way. It orders
   a list and nothing else — no claim is made that a `published` result outranks a
   `certified` one as mathematics, only that this is a sensible order to read them in. */
const STANDING_ORDER = [
  'published', 'certified', 'attested', 'proved-elsewhere', 'preprint',
  'definition', 'premise', 'open', 'barrier', 'refuted',
];

function standingRank(claim) {
  const index = STANDING_ORDER.indexOf(claim.standing_tone);
  return index === -1 ? STANDING_ORDER.length : index;
}

/**
 * The reader-facing standing of a claim.
 *
 * The text is `claim.standing` verbatim — the same string scripts/checks/editorial.py
 * writes into status.tex — so a badge here and a badge in the PDF can never say
 * different things. `standing_tone` chooses the drawing; `standing_conditional` adds a
 * modifier rather than a replacement, because a proved implication resting on an open
 * antecedent is still proved (repository contract, constraint 8) and still not progress
 * on the target (P2). The label already says both; the class only has to draw both.
 */
function standingBadge(claim) {
  const tone = claim.standing_tone || 'neutral';
  const conditional = claim.standing_conditional ? ' conditional' : '';
  return el('span', {
    class: `badge standing ${tone}${conditional}`,
    title: `schema status: ${claim.status}`,
  },
  el('span', { class: 'glyph', 'aria-hidden': 'true', text: STANDING_GLYPH[tone] || '?' }),
  claim.standing || claim.status || 'unknown');
}

/**
 * What to call a claim in a heading, a list or a graph box.
 *
 * The manuscript titles its own theorems, and that title is the name a mathematician
 * already uses for the result. The stable id stays exported, stays visible beside it and
 * stays copyable — it is what cross-references, issues and this site's own URLs are
 * written in — but it stops being the headline. A claim with no title keeps the id as
 * its name, which is the honest fallback rather than an invented one.
 */
function claimName(claim) {
  return (claim && claim.title) || (claim && claim.id) || 'unknown';
}

/* SVG text neither wraps nor clips, and a node box is a fixed 212px. Titles are prose
   and run to a hundred characters, so the box gets a shortened form and the full name
   goes to the tooltip and the accessible name, where there is room for it. */
function ellipsis(text, limit) {
  const value = String(text || '');
  return value.length <= limit ? value : `${value.slice(0, limit - 1).trimEnd()}…`;
}

function approachBadge(state) {
  return el('span', { class: 'badge neutral' },
    el('span', { class: 'glyph', 'aria-hidden': 'true', text: APPROACH_GLYPH[state] || '·' }),
    state || 'unknown');
}

function familyBadge(state) {
  return el('span', { class: 'badge neutral' },
    el('span', { class: 'glyph', 'aria-hidden': 'true', text: FAMILY_GLYPH[state] || '·' }),
    state || 'unknown');
}

/* ------------------------------------------------------------------------- links ---- */

function repoBase() {
  const slug = DATA.generated.repository;
  return slug ? `https://github.com/${slug}` : null;
}

/**
 * A permalink into the exact revision on screen, so a link cannot silently move.
 *
 * `source_prefix` turns a path relative to the *published tree* into one relative to the
 * *checkout*. They differ whenever a subtree is published, and without it every source
 * link on such a build is a 404 that looks like a missing file rather than a mis-built
 * site.
 */
function sourceLink(path, line) {
  const base = repoBase();
  if (!base || !path) return null;
  const revision = DATA.generated.commit || DATA.generated.branch || 'HEAD';
  const prefix = DATA.generated.source_prefix || '';
  return `${base}/blob/${revision}/${prefix}${path}${line ? `#L${line}` : ''}`;
}

function idLink(id) {
  if (!id) return null;
  if (DATA.claims[id]) return el('a', { class: 'id', href: `#/node/${id}`, text: id });
  if (DATA.search && DATA.search.routes[id]) {
    return el('a', { class: 'id', href: `#/approach/${id}`, text: id });
  }
  if (DATA.memory.candidates.some((entry) => entry.id === id)) {
    return el('a', { class: 'id', href: '#/audit/evidence', text: id });
  }
  return el('code', { class: 'id', text: id });
}

/**
 * The rendered manuscript, at the anchor of one claim.
 *
 * The anchor invariant is what makes this possible without inventing a web-specific id:
 * a ledger node id *is* its manuscript \label, and site/tex4ht.cfg is what carries that
 * through the HTML conversion. When no conversion was attached the answer is null, and
 * the reader is offered the LaTeX source and the PDF instead — never a broken link.
 */
function statementLink(id) {
  const html = DATA.documents && DATA.documents.html;
  return html && html.manuscript ? `${html.manuscript}#${id}` : null;
}

function dossierLinks(artifact) {
  const documents = DATA.documents || {};
  return {
    html: (documents.html && documents.html.dossiers[artifact]) || null,
    pdf: (documents.pdf && documents.pdf.dossiers[artifact]) || null,
  };
}

function fileLink(path, line, label) {
  const href = sourceLink(path, line);
  const text = label || (line ? `${path}:${line}` : path);
  return href ? el('a', { href, class: 'id', text }) : el('code', { class: 'id', text });
}

/**
 * A contribution link into GitHub, carrying the stable id of whatever is on screen.
 *
 * The boundary this respects, and it is the whole point: nothing that arrives through
 * one of these becomes a candidate, a route, a ledger node, a proof record, or a status.
 * It lands in a public inbox and is triaged by the repository's own roles. Popularity is
 * not truth, and a form is not a promotion.
 */
function contribute(template, label, anchor, extra) {
  const base = repoBase();
  if (!base) return null;
  const params = new URLSearchParams({ template, anchor: anchor || '' });
  if (extra) for (const [key, value] of Object.entries(extra)) params.set(key, value);
  return el('a', {
    class: 'action', href: `${base}/issues/new?${params.toString()}`,
    rel: 'noopener', target: '_blank',
  }, label);
}

function discussLink(label) {
  const base = repoBase();
  return base ? el('a', {
    class: 'action', href: `${base}/discussions`, rel: 'noopener', target: '_blank',
  }, label) : null;
}

/* ------------------------------------------------------------------- small parts ---- */

function idList(ids, emptyText) {
  if (!ids || !ids.length) return el('span', { class: 'note', text: emptyText || 'none' });
  return el('ul', { class: 'inline-list' }, ids.map((id) => el('li', {}, idLink(id))));
}

function glossBlock(claim) {
  const source = claim.source || {};
  const rendered = statementLink(claim.id);
  const documents = DATA.documents || {};
  const pdf = documents.pdf && documents.pdf.manuscript;
  const missing = [];
  if (!rendered) missing.push('the HTML conversion');
  if (!pdf) missing.push('the PDF');
  return el('div', {},
    el('span', { class: 'gloss-tag', text: 'One-line gloss — not the statement' }),
    el('p', { class: 'gloss' }, math(claim.gloss)),
    el('p', { class: 'note' },
      'The canonical statement is the ',
      el('code', { class: 'id', text: `\\label{${claim.id}}` }),
      source.file ? [' in ', fileLink(source.file, source.line)] : [],
      '. If the two disagree, the manuscript is right and this line is the defect.'),
    el('div', { class: 'actions' },
      rendered
        ? el('a', { class: 'action', href: rendered }, 'Read the statement')
        : null,
      pdf ? el('a', { class: 'action', href: pdf, target: '_blank' },
        'Manuscript (PDF)') : null,
      (() => {
        const href = source.file ? sourceLink(source.file, source.line) : null;
        return href ? el('a', { class: 'action', href, rel: 'noopener', target: '_blank' },
          'LaTeX source') : null;
      })()),
    /* A control that is simply absent tells a reader nothing; they conclude the
       statement is unavailable rather than that one rendering of it is. Say which. */
    rendered && pdf ? null : el('p', { class: 'note' },
      `${sentence(missing.join(' and '))} of the manuscript `
      + `${missing.length > 1 ? 'are' : 'is'} not attached to this build`,
      rendered || pdf || source.file
        ? '. The links above reach the statement by the routes that are.'
        : '. Nothing here can reach the statement, which is a build defect.'));
}

/* How long the search box waits for the typing to stop before redrawing, in ms. */
const SEARCH_DELAY = 140;

/**
 * A filter bar over a list, and the list it filters.
 *
 * 138 claims and 92 checkpoints in one alphabetical column is preservation, not
 * navigation: everything is there and nothing can be found. Each facet is derived from
 * the rows themselves, so a filter can never offer a value that matches nothing, and the
 * whole thing is inert with a single row.
 *
 * `facets` is [{ label, of(row) }]; `search` is a row -> haystack string; `render` is a
 * row -> element. Filtering is presentation only — it hides rows, never reinterprets
 * them, and the count line says exactly what is being withheld.
 */
/**
 * A list with facet filters, a search box and, optionally, a choice of order.
 *
 * `orders` is a list of `{ label, compare }`; the first is the default. It exists
 * because a long list is always in *some* order and a reader who cannot see which is
 * reading an arbitrary one: 138 claims sorted by title open on "A balanced posterior
 * event…", which tells nobody that the alphabet is what put it there. Naming the order
 * in a control fixes that and makes the alternative one click away, which is worth more
 * than picking a cleverer default would be — sorting by standing without saying so
 * would just be a different arbitrary order.
 */
function filteredList(rows, { facets, search, render, noun, orders }) {
  const chosen = new Map();
  let query = '';
  let order = (orders && orders[0]) || null;
  const list = el('ul', { class: 'rows' });
  const count = el('p', { class: 'note' });

  const matches = () => {
    const kept = rows.filter((row) => {
      for (const [label, value] of chosen) {
        const facet = facets.find((entry) => entry.label === label);
        const of = facet.of(row);
        const values = Array.isArray(of) ? of : [of];
        if (!values.includes(value)) return false;
      }
      return !query || (search(row) || '').toLowerCase().includes(query);
    });
    return order ? kept.sort(order.compare) : kept;
  };

  const draw = () => {
    const shown = matches();
    clear(list);
    append(list, shown.map(render));
    count.textContent = shown.length === rows.length
      ? `All ${rows.length} ${noun}.`
      : `${shown.length} of ${rows.length} ${noun}; the rest are filtered out, not gone.`;
    if (!shown.length) list.appendChild(el('li', { class: 'tight' },
      el('span', { class: 'note', text: 'Nothing matches every filter at once.' })));
    if (!deferRows(list)) typeset(list);
  };

  /* A keystroke is a full redraw of the list, so a fast typist would otherwise pay for
   * one redraw per character and see none of them. Waiting for a pause in the typing
   * costs a reader nothing they can perceive and turns eight redraws into one. */
  let pending = 0;
  const redrawSoon = () => {
    clearTimeout(pending);
    pending = setTimeout(draw, SEARCH_DELAY);
  };

  const controls = el('div', { class: 'filters' });
  if (orders && orders.length > 1) {
    controls.appendChild(el('label', {},
      el('span', { class: 'note', text: 'order' }),
      el('select', {
        'aria-label': `Order ${noun} by`,
        onchange: (event) => {
          order = orders[Number(event.target.value)] || orders[0];
          draw();
        },
      }, orders.map((entry, index) =>
        el('option', { value: index, text: entry.label })))));
  }
  for (const facet of facets) {
    const values = [...new Set(rows.flatMap((row) => {
      const of = facet.of(row);
      return (Array.isArray(of) ? of : [of]).filter((value) => value != null && value !== '');
    }))].sort();
    if (values.length < 2) continue;
    controls.appendChild(el('label', {},
      el('span', { class: 'note', text: facet.label }),
      el('select', {
        'aria-label': `Filter by ${facet.label}`,
        onchange: (event) => {
          if (event.target.value) chosen.set(facet.label, event.target.value);
          else chosen.delete(facet.label);
          draw();
        },
      },
      el('option', { value: '', text: `any ${facet.label}` }),
      values.map((value) => el('option', { value, text: String(value) })))));
  }
  controls.appendChild(el('label', { class: 'grow' },
    el('span', { class: 'note', text: 'search' }),
    el('input', {
      type: 'search', placeholder: 'name, id or text…',
      'aria-label': `Search ${noun}`,
      oninput: (event) => { query = event.target.value.trim().toLowerCase(); redrawSoon(); },
    })));

  draw();
  return el('div', {}, controls, count, list);
}

function statCard(value, label) {
  return el('div', { class: 'card stat' },
    el('span', { class: 'value', text: String(value) }),
    el('span', { class: 'label', text: label }));
}

/* Names of missing renderings read as sentence fragments ("the PDF"), and a fragment
   pasted at the head of a sentence starts it in lower case. Capitalise the join, once,
   here rather than duplicating a capitalised variant of every name. */
function sentence(text) { return text.charAt(0).toUpperCase() + text.slice(1); }

function emptyState(text) { return el('p', { class: 'empty', text }); }

/* How many of a claim's checkpoints a node page opens with, newest first. */
const RECENT_CHECKPOINTS = 5;

/* -------------------------------------------------------------------------- maps ---- */

const NODE_W = 212;
const NODE_H = 56;

/* Breathing room around the drawn subgraph, in layout units. Small on purpose: the fit
   scales the content box to the stage, so padding here is paid for in legibility. */
const PAD_X = 56;
const PAD_Y = 40;

/* The closest the initial fit will ever get — roughly five boxes across, four down.
 *
 * The vertical floor used to be 7.5 boxes, sized for an opening view of two or three
 * nodes that had to be stopped from filling the stage. openingView() no longer produces
 * one, so a floor that tall now does the opposite job: the layout is one column per
 * depth layer, a small star is two layers, and forcing that into a box seven boxes deep
 * is what left a band of drawing in the middle of an empty stage. The stage follows the
 * drawn shape instead — see the aspect ratio set at the end of draw(). */
const MIN_VIEW_W = NODE_W * 5;
const MIN_VIEW_H = NODE_H * 4;

/* Above this many nodes, "Whole map" stops being a map.
 *
 * The layout is one column per proof-depth layer, which is the right convention — a
 * dependency sits below what rests on it — and it is what makes the whole graph 15,000
 * pixels wide once a program has a hundred claims. Wrapping a wide layer into several
 * rows would fix the width and break the convention: several rows of one depth read as
 * several depths. So the honest answer is to withhold the view rather than degrade the
 * meaning of the one that remains. The neighbourhood graph is unaffected, and the list
 * above it, with its filters, is where a reader browses all of them. */
const WHOLE_MAP_LIMIT = 60;

/* How many boxes the opening view has to reach before it counts as showing something.
 *
 * Roughly a small star: enough that a reader sees a shape rather than a pair. */
const OPENING_MIN_NODES = 6;

/** The set reachable from `focus` within `depth` undirected steps. */
function neighbourhood(adjacency, focus, depth) {
  let frontier = new Set([focus]);
  const seen = new Set(frontier);
  for (let step = 0; step < depth; step += 1) {
    const next = new Set();
    for (const id of frontier) {
      for (const other of adjacency.get(id) || []) {
        if (!seen.has(other)) { seen.add(other); next.add(other); }
      }
    }
    frontier = next;
  }
  return seen;
}

/**
 * Where the map opens: a focus, and how far out from it.
 *
 * `preferred` is what the page *means* to centre on — the program's target on the claim
 * map, the first family on the portfolio map. That is the right anchor when the node
 * sits among its neighbours, and the wrong one when it does not. A target can easily
 * have degree one: a conjecture nothing has yet been proved *from* has an edge to
 * whatever bridges to it and nothing else. A map that opens there draws two boxes in a
 * full-width stage, and a reader's first impression of a graph of a hundred-odd claims
 * is that it is empty. The ledger is not wrong about that node, so the fix belongs
 * here, in what the view opens on.
 *
 * So the preference is honoured when it can be seen and dropped when it cannot, in
 * favour of the best-connected node, which is where the structure actually is. Either
 * way the depth grows until the view stops being degenerate. Nothing is hidden by this:
 * the focus and depth controls sit above the stage, the target keeps its `target` chip
 * wherever it is drawn, and the complete list is beneath.
 */
function openingView(nodes, adjacency, preferred) {
  const depths = [1, 2, 3];
  const reach = (id) => depths.map((depth) => neighbourhood(adjacency, id, depth));

  const candidates = [];
  if (preferred && adjacency.has(preferred)) candidates.push(preferred);
  const best = nodes.slice()
    .sort((a, b) => (adjacency.get(b.id)?.size || 0) - (adjacency.get(a.id)?.size || 0))[0];
  if (best && best.id !== preferred) candidates.push(best.id);

  for (const id of candidates) {
    const reached = reach(id);
    const index = reached.findIndex((set) => set.size >= OPENING_MIN_NODES);
    if (index !== -1) return { focus: id, depth: depths[index] };
  }
  /* Nothing reaches the floor — a sparse graph, or one small enough that `scope: all`
     is about to show everything anyway. Open widest on the best candidate there is. */
  const id = candidates[0] || (nodes[0] && nodes[0].id) || null;
  return { focus: id, depth: id ? depths[depths.length - 1] : 1 };
}

/**
 * Draw one graph. Layout arrives precomputed and deterministic from the exporter —
 * geometry here is navigation only. Proximity, centrality and column position carry no
 * mathematical meaning whatever, and no interaction in this function creates any.
 */
function graph({ nodes, edges, legend, focusId, selectHandler, stageNote }) {
  const stage = el('div', { class: 'map-stage' });
  const controls = el('div', { class: 'map-controls' });
  const legendBar = el('div', { class: 'legend' });
  const wrapper = el('div', { class: 'map' }, controls, stage, legendBar);
  const detail = el('div', {});
  const container = el('div', {}, wrapper, detail);

  const byId = new Map(nodes.map((node) => [node.id, node]));
  const adjacency = new Map(nodes.map((node) => [node.id, new Set()]));
  for (const edge of edges) {
    if (adjacency.has(edge.from)) adjacency.get(edge.from).add(edge.to);
    if (adjacency.has(edge.to)) adjacency.get(edge.to).add(edge.from);
  }

  const opening = openingView(nodes, adjacency, focusId);
  const state = {
    focus: opening.focus,
    depth: opening.depth,
    scope: nodes.length > 14 ? 'neighbourhood' : 'all',
    tooLarge: nodes.length > WHOLE_MAP_LIMIT,
    off: new Set(),
    selected: null,
  };

  function visible() {
    if (state.scope === 'all' || !state.focus || !byId.has(state.focus)) {
      return new Set(byId.keys());
    }
    return neighbourhood(adjacency, state.focus, state.depth);
  }

  /* --- controls ------------------------------------------------------------------ */

  /* A control with one choice is not a control. Above WHOLE_MAP_LIMIT the whole map is
     withheld, which leaves "Neighbourhood of…" alone in a dropdown that looks live,
     opens, and offers the reader the option they already have. So it becomes the label
     it always was, and stays a real select wherever both scopes exist. */
  const scopeSelect = state.tooLarge
    ? el('span', { class: 'control-label', text: 'Neighbourhood of' })
    : el('select', {
      'aria-label': 'How much of the map to show',
      onchange: (event) => { state.scope = event.target.value; refit(); },
    },
      el('option', { value: 'neighbourhood', text: 'Neighbourhood of…' }),
      el('option', { value: 'all', text: 'Whole map' }));
  if (!state.tooLarge) scopeSelect.value = state.scope;

  const focusSelect = el('select', {
    'aria-label': 'Centre of the neighbourhood',
    onchange: (event) => { state.focus = event.target.value; refit(); },
  }, nodes.slice()
    .sort((a, b) => (a.name || a.id).localeCompare(b.name || b.id))
    .map((node) => el('option', { value: node.id, text: node.name || node.id })));
  if (state.focus) focusSelect.value = state.focus;

  const depthSelect = el('select', {
    'aria-label': 'How many steps out',
    onchange: (event) => { state.depth = Number(event.target.value); refit(); },
  }, [1, 2, 3].map((n) => el('option', { value: n, text: `${n} step${n > 1 ? 's' : ''}` })));
  depthSelect.value = String(state.depth);

  const search = el('input', {
    type: 'search', placeholder: 'find by name, id or gloss…',
    'aria-label': 'Find a node by name, identifier or gloss',
    oninput: (event) => {
      const query = event.target.value.trim().toLowerCase();
      if (!query) { state.selected = null; draw(); return; }
      /* Prefer a hit in the name over one buried in a gloss: someone typing "carleson"
         means the theorem called that, not every claim whose gloss mentions it. */
      const matches = nodes.filter((node) => (node.haystack || node.id.toLowerCase()).includes(query));
      const hit = matches.find((node) => (node.name || node.id).toLowerCase().includes(query))
        || matches[0];
      if (hit) { state.focus = hit.id; focusSelect.value = hit.id; select(hit.id); }
    },
  });

  const toggles = el('div', { class: 'group' },
    legend.map((entry) => el('label', { title: entry.gloss || '' },
      el('input', {
        type: 'checkbox', checked: true,
        onchange: (event) => {
          if (event.target.checked) state.off.delete(entry.key); else state.off.add(entry.key);
          draw();
        },
      }),
      entry.label)));

  const zoomButtons = el('div', { class: 'group' },
    el('button', { type: 'button', class: 'action', 'aria-label': 'Zoom in',
      onclick: () => zoom(1 / 1.25) }, '+'),
    el('button', { type: 'button', class: 'action', 'aria-label': 'Zoom out',
      onclick: () => zoom(1.25) }, '−'),
    el('button', { type: 'button', class: 'action',
      onclick: () => refit() }, 'Fit'));

  append(controls, [
    el('div', { class: 'group' }, scopeSelect, focusSelect, depthSelect),
    el('div', { class: 'group' }, search),
    toggles,
    zoomButtons,
  ]);

  append(legendBar, [
    legend.map((entry) => el('span', { class: 'key', title: entry.gloss || '' },
      el('span', { class: `swatch ${entry.key}`, 'aria-hidden': 'true' }), entry.label)),
    el('span', { class: 'key', text: 'arrow reads: source → target, in the direction the relation is stored' }),
  ]);

  /* --- selection ------------------------------------------------------------------ */

  function select(id) {
    state.selected = id;
    draw();
    clear(detail);
    if (id && selectHandler) detail.appendChild(selectHandler(id));
    typeset(detail);
  }

  /* --- drawing -------------------------------------------------------------------- */

  let view = null;
  let canvas = null;

  /** Forget the viewport, so the next draw frames whatever is now shown. */
  function refit() { view = null; draw(); }

  function zoom(factor) {
    if (!view || !canvas) return;
    const cx = view.x + view.w / 2;
    const cy = view.y + view.h / 2;
    view.w *= factor;
    view.h *= factor;
    view.x = cx - view.w / 2;
    view.y = cy - view.h / 2;
    canvas.setAttribute('viewBox', `${view.x} ${view.y} ${view.w} ${view.h}`);
  }

  function boxEdge(from, to) {
    const dx = to.x - from.x;
    const dy = to.y - from.y;
    if (dx === 0 && dy === 0) return from;
    const scale = Math.min(
      Math.abs(dx) < 1e-6 ? Infinity : (NODE_W / 2) / Math.abs(dx),
      Math.abs(dy) < 1e-6 ? Infinity : (NODE_H / 2) / Math.abs(dy));
    return { x: from.x + dx * scale, y: from.y + dy * scale };
  }

  /**
   * Where the nodes that are actually drawn go.
   *
   * The exporter's layout is global: every node is placed once, against all of them, so
   * a layer a hundred nodes wide is fifteen thousand units wide. A neighbourhood is a
   * handful of those, and at their global coordinates two neighbours in the same layer
   * can sit nine thousand units apart with nothing drawn in between — the fit then
   * scales the whole picture down until no label is legible, which is the state this
   * view was in.
   *
   * So the drawn subgraph is compacted. The layer an exporter assigned is kept exactly
   * — a dependency still sits below what rests on it, which is the only thing this
   * geometry is allowed to mean — and inside a layer the gaps left by nodes that are
   * not shown are closed, in the exporter's own left-to-right order. Position within a
   * layer carries no meaning, so closing those gaps takes none away.
   */
  function place(shown) {
    const rows = new Map();
    for (const node of nodes) {
      if (!shown.has(node.id)) continue;
      if (!rows.has(node.y)) rows.set(node.y, []);
      rows.get(node.y).push(node);
    }
    const pitch = NODE_W + 48;
    const at = new Map();
    for (const row of rows.values()) {
      row.sort((a, b) => a.x - b.x || a.id.localeCompare(b.id));
      const start = -((row.length - 1) * pitch) / 2;
      row.forEach((node, index) => at.set(node.id, { x: start + index * pitch, y: node.y }));
    }
    return at;
  }

  function draw() {
    const shown = visible();
    clear(stage);

    const placed = nodes.filter((node) => shown.has(node.id));
    if (!placed.length) {
      stage.appendChild(emptyState('Nothing to draw here yet.'));
      return;
    }
    const at = place(shown);
    const spots = placed.map((node) => at.get(node.id));
    const minX = Math.min(...spots.map((p) => p.x)) - NODE_W / 2 - PAD_X;
    const maxX = Math.max(...spots.map((p) => p.x)) + NODE_W / 2 + PAD_X;
    const minY = Math.min(...spots.map((p) => p.y)) - NODE_H / 2 - PAD_Y;
    const maxY = Math.max(...spots.map((p) => p.y)) + NODE_H / 2 + PAD_Y;
    if (!view) {
      /* Fit what is drawn — but never closer than a floor. Most neighbourhoods here are
         two or three nodes, and a two-node picture stretched to fill a 600-pixel stage
         is a diagram of nothing, drawn enormous. The floor is stated in layout units
         rather than as a scale because the stage has no measurable width on the first
         draw: the graph is built before it is put on the page. */
      const w = Math.max(maxX - minX, MIN_VIEW_W);
      const h = Math.max(maxY - minY, MIN_VIEW_H);
      view = { x: (minX + maxX) / 2 - w / 2, y: (minY + maxY) / 2 - h / 2, w, h };
    }

    canvas = svg('svg', {
      viewBox: `${view.x} ${view.y} ${view.w} ${view.h}`,
      role: 'group', 'aria-label': 'Graph. Use the list below the map for a linear reading.',
    });

    const defs = svg('defs', {});
    for (const entry of legend) {
      defs.appendChild(svg('marker', {
        id: `arrow-${entry.key}`, viewBox: '0 0 10 10', refX: 9, refY: 5,
        markerWidth: 6, markerHeight: 6, orient: 'auto-start-reverse',
      }, svg('path', { d: 'M 0 0 L 10 5 L 0 10 z', class: `marker ${entry.key}`,
        fill: 'context-stroke' })));
    }
    canvas.appendChild(defs);

    const edgeLayer = svg('g', {});
    const nodeLayer = svg('g', {});
    canvas.appendChild(edgeLayer);
    canvas.appendChild(nodeLayer);

    for (const edge of edges) {
      if (state.off.has(edge.kind)) continue;
      if (!shown.has(edge.from) || !shown.has(edge.to)) continue;
      const a = at.get(edge.from);
      const b = at.get(edge.to);
      if (!a || !b) continue;
      const start = boxEdge(a, b);
      const end = boxEdge(b, a);
      const dim = state.selected
        && edge.from !== state.selected && edge.to !== state.selected;
      edgeLayer.appendChild(svg('line', {
        x1: start.x, y1: start.y, x2: end.x, y2: end.y,
        class: `gedge ${edge.kind}${dim ? ' dimmed' : ''}`,
        'marker-end': `url(#arrow-${edge.kind})`,
      }, svg('title', {}, `${edge.from} — ${edge.label} → ${edge.to}`)));
    }

    for (const node of placed) {
      const dim = state.selected && state.selected !== node.id
        && !(adjacency.get(state.selected) || new Set()).has(node.id);
      const classes = ['gnode', node.tone || 'neutral'];
      if (node.isTarget) classes.push('is-target');
      if (state.selected === node.id) classes.push('selected');
      if (dim) classes.push('dimmed');
      const group = svg('g', {
        class: classes.join(' '), tabindex: '0', role: 'button',
        'aria-label': `${node.name || node.label || node.id}, ${node.meta}`,
        transform: `translate(${at.get(node.id).x - NODE_W / 2} `
          + `${at.get(node.id).y - NODE_H / 2})`,
        onclick: () => select(node.id),
        onkeydown: (event) => {
          if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); select(node.id); }
        },
      },
        svg('rect', { class: 'box', width: NODE_W, height: NODE_H, rx: 8 }),
        svg('title', {}, `${node.name || node.id}\n${node.id}`),
        svg('text', { class: 'glabel', x: 12, y: 22 }, node.label || node.id),
        svg('text', { class: 'gmeta', x: 12, y: 40 }, node.meta),
        node.isTarget ? svg('text', { class: 'gkind', x: NODE_W - 12, y: 22,
          'text-anchor': 'end' }, 'target') : null);
      nodeLayer.appendChild(group);
    }

    stage.appendChild(canvas);

    /* Let the stage take the shape of what is in it.
     *
     * An SVG viewBox is letterboxed into its element, so a wide, shallow graph in a
     * stage fixed at 620px tall is drawn as a band across the middle of a large empty
     * rectangle — the emptiness is the element, not the drawing. Handing the ratio to
     * CSS lets the height follow the width, between the floor and ceiling the
     * stylesheet sets, and needs no measurement: the graph is built before it is on the
     * page and has no width to read at this point. Panning and zooming afterwards only
     * change `view`, so the stage keeps the shape it opened with. */
    stage.style.aspectRatio = `${Math.round(view.w)} / ${Math.round(view.h)}`;

    stage.appendChild(el('span', { class: 'map-hint',
      text: state.tooLarge
        ? `${stageNote || 'drag to pan · scroll to zoom · click a box'} · `
          + `${nodes.length} nodes is too many to draw at once, so this shows a `
          + 'neighbourhood; the list below holds all of them'
        : (stageNote || 'drag to pan · scroll to zoom · click a box') }));
    wirePanZoom();
  }

  function wirePanZoom() {
    let dragging = null;
    canvas.addEventListener('pointerdown', (event) => {
      if (event.target.closest('.gnode')) return;
      dragging = { x: event.clientX, y: event.clientY };
      canvas.classList.add('dragging');
      canvas.setPointerCapture(event.pointerId);
    });
    canvas.addEventListener('pointermove', (event) => {
      if (!dragging) return;
      const rect = canvas.getBoundingClientRect();
      view.x -= (event.clientX - dragging.x) * (view.w / rect.width);
      view.y -= (event.clientY - dragging.y) * (view.h / rect.height);
      dragging = { x: event.clientX, y: event.clientY };
      canvas.setAttribute('viewBox', `${view.x} ${view.y} ${view.w} ${view.h}`);
    });
    const stop = () => { dragging = null; canvas.classList.remove('dragging'); };
    canvas.addEventListener('pointerup', stop);
    canvas.addEventListener('pointercancel', stop);
    canvas.addEventListener('wheel', (event) => {
      event.preventDefault();
      const rect = canvas.getBoundingClientRect();
      const factor = event.deltaY > 0 ? 1.12 : 1 / 1.12;
      const px = view.x + ((event.clientX - rect.left) / rect.width) * view.w;
      const py = view.y + ((event.clientY - rect.top) / rect.height) * view.h;
      view.x = px - (px - view.x) * factor;
      view.y = py - (py - view.y) * factor;
      view.w *= factor;
      view.h *= factor;
      canvas.setAttribute('viewBox', `${view.x} ${view.y} ${view.w} ${view.h}`);
    }, { passive: false });
  }

  draw();
  /* The card below the stage describes what the stage is centred on, which after
     openingView() is not always what the caller asked for. */
  if (state.focus) select(state.focus);
  return container;
}

/* --------------------------------------------------------------- the claim map ----- */

function claimGraphModel() {
  const layout = DATA.layout.claims;
  const target = DATA.program.target;
  const nodes = Object.values(DATA.claims).map((claim) => ({
    id: claim.id,
    label: ellipsis(claimName(claim), 26),
    name: claimName(claim),
    /* What the find box matches. A mathematician looking for a theorem types a word
       from its name, not its stable identifier — and may well type one from the gloss. */
    haystack: `${claim.id} ${claim.title || ''} ${claim.gloss || ''}`.toLowerCase(),
    x: (layout[claim.id] || { x: 0 }).x,
    y: -(layout[claim.id] || { y: 0 }).y,
    tone: claim.standing_tone || claim.status,
    meta: `${claim.kind || '?'} · ${claim.standing || claim.status || '?'}`,
    isTarget: claim.id === target,
  }));
  const edges = [];
  for (const claim of Object.values(DATA.claims)) {
    for (const relation of DATA.vocabulary.relations) {
      for (const other of claim.edges[relation.field] || []) {
        if (!DATA.claims[other]) continue;
        edges.push({
          from: claim.id, to: other, kind: relation.class, label: relation.label,
        });
      }
    }
  }
  const used = new Set(edges.map((edge) => edge.kind));
  const legend = DATA.vocabulary.relations
    .filter((relation) => used.has(relation.class))
    .filter((relation, index, all) =>
      all.findIndex((other) => other.class === relation.class) === index)
    .map((relation) => ({ key: relation.class, label: relation.label, gloss: relation.gloss }));
  return { nodes, edges, legend };
}

/* -------------------------------------------------------------- the search map ----- */

function searchGraphModel() {
  const search = DATA.search;
  if (!search) return null;
  const layout = DATA.layout.search;
  const nodes = [];
  for (const family of Object.values(search.families)) {
    nodes.push({
      id: family.id,
      x: (layout[family.id] || { x: 0 }).x,
      y: -(layout[family.id] || { y: 0 }).y,
      tone: 'neutral',
      meta: `family · ${family.state || '?'}`,
    });
  }
  for (const route of Object.values(search.routes)) {
    nodes.push({
      id: route.id,
      x: (layout[route.id] || { x: 0 }).x,
      y: -(layout[route.id] || { y: 0 }).y,
      tone: 'neutral',
      meta: `approach · ${route.state || '?'}`,
    });
  }
  const edges = [];
  for (const route of Object.values(search.routes)) {
    if (route.family && search.families[route.family] && !route.parent) {
      edges.push({ from: route.family, to: route.id, kind: 'family', label: 'contains' });
    }
    if (route.parent && search.routes[route.parent]) {
      edges.push({ from: route.parent, to: route.id, kind: 'family', label: 'grew into' });
    }
    for (const relation of route.related) {
      if (!search.routes[relation.to]) continue;
      edges.push({
        from: route.id, to: relation.to, kind: relation.relation, label: relation.relation,
      });
    }
  }
  const used = new Set(edges.map((edge) => edge.kind));
  const legend = [
    { key: 'family', label: 'family / parent', gloss: 'Which family an approach belongs to, and which approach it grew out of.' },
    { key: 'overlaps', label: 'overlaps', gloss: 'Two approaches cover some of the same ground.' },
    { key: 'duplicates', label: 'duplicates', gloss: 'The same idea as another approach. Both may not be active.' },
    { key: 'refines', label: 'refines', gloss: 'A sharper version of another approach.' },
  ].filter((entry) => used.has(entry.key));
  return { nodes, edges, legend };
}

/* ------------------------------------------------------------------------- views ---- */

function viewOverview() {
  const page = el('div', {});
  const program = DATA.program;

  // Two different "not ready" states, and telling a reader they are the same would be
  // the first thing on the page that is false. A tree with no claims is a fresh clone;
  // a tree with claims and no brief is a repository that has not opened a search yet.
  if (!Object.keys(DATA.claims).length) {
    page.appendChild(el('div', { class: 'banner' },
      el('strong', { text: 'This repository is still an uninstantiated template. ' }),
      'It is structurally valid and states nothing yet, which is the correct state for a '
      + 'fresh clone rather than a defect. Nothing below describes a live search.'));
  } else if (!program.target) {
    page.appendChild(el('div', { class: 'banner' },
      el('strong', { text: 'No target is named. ' }),
      'This repository states claims but has no problem brief, so nothing here says '
      + 'what the search is aimed at or what would finish it. The mathematics below is '
      + 'real; the search around it has not been opened.'));
  }

  const target = program.target ? DATA.claims[program.target] : null;

  const g = guide();
  page.appendChild(el('h1', {},
    (g && g.site && g.site.name) || (target ? 'The target' : 'This repository')));
  if (g && g.site && g.site.tagline) {
    page.appendChild(el('p', { class: 'lede' }, math(g.site.tagline)));
  } else if (program.scope) {
    page.appendChild(el('p', { class: 'lede' }, math(program.scope)));
  }

  if (target) {
    const proofCount = target.proofs.length;
    page.appendChild(el('div', { class: 'card' },
      el('div', { class: 'badges' },
        el('a', { class: 'id', href: `#/node/${target.id}`, text: target.id }),
        el('span', { class: 'badge kind', text: target.kind || 'unknown kind' }),
        statusBadge(target.status),
        target.provenance ? el('span', { class: 'badge kind', text: target.provenance }) : null),
      el('div', { style: 'margin-top:.8rem' }, glossBlock(target)),
      el('div', { class: 'actions' },
        el('a', { class: 'action', href: `#/node/${target.id}` }, 'Open the claim'),
        program.brief ? (() => {
          const link = sourceLink(program.brief);
          return link ? el('a', { class: 'action', href: link, rel: 'noopener', target: '_blank' },
            'Problem brief — what would finish this') : null;
        })() : null,
        proofCount ? null : discussLink('Discuss'))));
  }

  /* --- the frontier, the routes, the way in ---------------------------------------- */

  if (g) {
    const frontier = (g.frontier || []).map((id) => DATA.claims[id]).filter(Boolean);
    if (frontier.length) {
      page.appendChild(el('h2', { text: 'Where the problem stands in the literature' }));
      page.appendChild(el('ul', { class: 'rows' },
        frontier.map((claim) => featuredRow({ id: claim.id, claim }))));
    }

    if ((g.routes || []).length) {
      page.appendChild(el('div', { class: 'section-head' },
        el('h2', { text: 'Four routes are studied here' }),
        el('a', { href: '#/routes', text: 'All four, in full →' })));
      page.appendChild(el('ul', { class: 'rows' }, g.routes.map(routeRow)));
    }

    if ((g.reading || []).length) {
      page.appendChild(el('h2', { text: 'Read the manuscript' }));
      page.appendChild(el('div', { class: 'actions' },
        g.reading.slice(0, 3).map((entry) =>
          manuscriptAction(entry.anchor, entry.label)).filter(Boolean),
        el('a', { class: 'action', href: '#/manuscript' }, 'All entry points')));
    }
  }

  /* --- state of the search ------------------------------------------------------- */

  const claims = Object.values(DATA.claims);
  const approaches = DATA.search ? Object.values(DATA.search.routes) : [];
  const live = approaches.filter((approach) => ['active', 'queued'].includes(approach.state));
  const blocked = approaches.filter((approach) => approach.state === 'blocked');
  const heads = DATA.memory.checkpoints.filter((record) => !record.superseded_by.length);

  /* Counted by standing, not by schema status.
   *
   * `proved` is 86 nodes here and means four different things: a theorem published in a
   * journal, an unreviewed preprint imported as a premise, a result certified in this
   * repository against a dossier, and an implication proved here whose antecedent is
   * still open. One number over all of them, captioned with the strongest of the four,
   * is a claim about evidence that the ledger does not support. Each row below is
   * separately true, which is the only kind of total worth printing. */
  const byStanding = new Map();
  for (const claim of claims) {
    const label = claim.standing || claim.status || 'unknown';
    const entry = byStanding.get(label)
      || { count: 0, tone: claim.standing_tone || 'neutral' };
    entry.count += 1;
    byStanding.set(label, entry);
  }
  const standings = [...byStanding.entries()].sort((a, b) => b[1].count - a[1].count);

  page.appendChild(el('h2', { text: 'Where the search stands' }));
  page.appendChild(el('div', { class: 'grid three' },
    statCard(claims.length, `claim${claims.length === 1 ? '' : 's'} in the ledger`),
    statCard(live.length, `approach${live.length === 1 ? '' : 'es'} live`),
    statCard(blocked.length, `approach${blocked.length === 1 ? '' : 'es'} blocked`)));

  const largest = standings.length ? standings[0][1].count : 0;
  page.appendChild(el('h3', { text: 'What those claims are, one category at a time' }));
  page.appendChild(el('ul', { class: 'standing-tally' }, standings.map(([label, entry]) =>
    el('li', {},
      el('span', { class: `badge standing ${entry.tone}` },
        el('span', { class: 'glyph', 'aria-hidden': 'true',
          text: STANDING_GLYPH[entry.tone] || '?' }),
        label),
      /* Length beside the number, never instead of it. Eleven rows of right-aligned
         digits is an inventory a reader has to add up; the bar answers "which of these
         dominate" at a glance and the count stays printed for the answer that matters.
         It is scaled against the largest row rather than the total because that is the
         question it is being asked, and it is hidden from assistive technology, which
         is already reading the number it duplicates. */
      el('span', { class: 'tally-bar', 'aria-hidden': 'true' },
        el('span', { class: `fill ${entry.tone}`,
          style: `width:${largest ? (entry.count / largest) * 100 : 0}%` })),
      el('span', { class: 'tally', text: String(entry.count) })))));
  page.appendChild(el('p', { class: 'note' },
    'Derived from each node\u2019s status, provenance, import class, proof records and '
    + 'open antecedents \u2014 the same projection that prints the standing beside every '
    + 'statement in the manuscript. "Certified here" means a dossier and an independent '
    + 'review exist in this repository; it does not mean the proof is right, which is '
    + 'settled by that review and not by this page.'));

  /* --- recent durable advances --------------------------------------------------- */

  page.appendChild(el('div', { class: 'section-head' },
    el('h2', { text: 'Recent durable records' }),
    el('a', { href: '#/audit/evidence', text: 'All evidence →' })));
  if (!heads.length) {
    page.appendChild(emptyState('No checkpoints recorded yet.'));
  } else {
    page.appendChild(el('ul', { class: 'rows' },
      heads.slice(0, 5).map((record) => checkpointRow(record, { excerpt: false }))));
    page.appendChild(el('p', { class: 'note' },
      'What the search has been working on, and which claims it touched. Each record '
      + 'opens in the repository; the excerpts are under ',
      el('a', { href: '#/audit/evidence' }, 'Evidence'), '.'));
  }

  /* --- into the audit layer -------------------------------------------------------- */

  page.appendChild(el('p', { class: 'note' },
    'The two maps are drawn separately and never merged: what is claimed has a truth '
    + 'status and a provenance, and what the search is doing has neither. Both are under ',
    el('a', { href: '#/audit' }, 'Audit'), ', in full.'));

  /* --- contribute ----------------------------------------------------------------- */

  if (repoBase()) {
    page.appendChild(el('h2', { text: 'Where another mathematician could help' }));
    page.appendChild(el('p', { class: 'note' },
      'Everything below opens a public inbox. Nothing that arrives through it becomes a '
      + 'candidate, an approach, a claim, a proof record, or a status by itself — it is '
      + 'triaged by the repository’s own roles, and proofs still pass through a '
      + 'standalone dossier and independent certification.'));
    page.appendChild(el('div', { class: 'actions' },
      contribute('proof-gap.yml', 'Report a proof gap', program.target),
      contribute('counterexample.yml', 'Propose a counterexample', program.target),
      contribute('literature-lead.yml', 'Point at existing work', program.target),
      contribute('route-proposal.yml', 'Propose an approach', program.target),
      discussLink('Ask a question')));
  }

  return page;
}

function viewClaims() {
  const page = el('div', {});
  page.appendChild(auditNav('#/audit/claims'));
  page.appendChild(el('h1', { text: 'The mathematical map' }));
  page.appendChild(el('p', { class: 'lede' },
    'Every statement this program has committed to, and how they rest on each other. '
    + 'Truth and applicability are separate: a proved implication whose antecedent is '
    + 'open is still proved, and its antecedent is drawn as an assumption, never as a '
    + 'proof dependency.'));

  const claims = Object.values(DATA.claims);
  if (!claims.length) {
    page.appendChild(emptyState('This ledger has no nodes yet.'));
    return page;
  }

  const model = claimGraphModel();
  page.appendChild(graph({
    ...model,
    focusId: DATA.program.target || model.nodes[0].id,
    selectHandler: (id) => claimSummaryCard(DATA.claims[id]),
    stageNote: 'dependencies sit below what rests on them',
  }));

  const routeOf = {};
  const g = guide();
  if (g) {
    for (const entry of g.featured || []) if (entry.route) routeOf[entry.id] = `Route ${entry.route}`;
  }

  page.appendChild(el('h2', { text: 'Every claim, as a list' }));
  page.appendChild(filteredList(claims.slice(), {
    noun: 'claims',
    orders: [
      { label: 'by name',
        compare: (a, b) => claimName(a).localeCompare(claimName(b)) },
      /* Strongest evidence first, then by name inside each band. STANDING_ORDER is a
         presentation decision over the tone names the repository exports, on the same
         footing as the glyph each tone is drawn with. */
      { label: 'by standing',
        compare: (a, b) => (standingRank(a) - standingRank(b))
          || claimName(a).localeCompare(claimName(b)) },
      { label: 'by identifier', compare: (a, b) => a.id.localeCompare(b.id) },
    ],
    facets: [
      { label: 'kind', of: (claim) => claim.kind },
      { label: 'standing', of: (claim) => claim.standing },
      { label: 'provenance', of: (claim) => claim.provenance },
      { label: 'route', of: (claim) => routeOf[claim.id] },
    ],
    search: (claim) => `${claim.id} ${claim.title || ''} ${claim.gloss || ''}`,
    render: (claim) => el('li', {},
      el('div', { class: 'row-head' },
        el('a', { class: 'row-name', href: `#/node/${claim.id}` }, math(claimName(claim))),
        el('span', { class: 'badge kind', text: claim.kind || '?' }),
        standingBadge(claim),
        claim.applicability_blocked_by.length
          ? el('span', { class: 'badge warn' }, 'applicability-blocked') : null,
        claim.id === DATA.program.target ? el('span', { class: 'badge neutral', text: 'target' }) : null),
      el('p', { class: 'row-note' }, el('code', { class: 'id', text: claim.id })),
      el('p', { class: 'row-body' }, math(claim.gloss))),
  }));
  return page;
}

function claimSummaryCard(claim) {
  if (!claim) return el('div', {});
  return el('div', { class: 'card', style: 'margin-top:1rem' },
    el('h3', { class: 'card-name' },
      el('a', { href: `#/node/${claim.id}` }, math(claimName(claim)))),
    el('div', { class: 'badges' },
      el('code', { class: 'id', text: claim.id }),
      el('span', { class: 'badge kind', text: claim.kind || '?' }),
      standingBadge(claim)),
    el('p', { class: 'row-body gloss' }, math(claim.gloss)),
    el('div', { class: 'actions' },
      el('a', { class: 'action', href: `#/node/${claim.id}` }, 'Full record')));
}

function viewSearch() {
  const page = el('div', {});
  page.appendChild(auditNav('#/audit/portfolio'));
  page.appendChild(el('h1', { text: 'The portfolio' }));
  page.appendChild(el('p', { class: 'lede' },
    'What the search is doing, which is not what is true. A family is a mechanism; an '
    + 'approach is one attempt within it. "Completed" means an approach’s objective '
    + 'ended, not that anything was settled, and "saturated" is a judgment about effort '
    + 'that carries a reopening condition.'));
  page.appendChild(el('p', { class: 'note' },
    'These are not the four routes. Route E, S, C and F are the mathematical '
    + 'organization of the manuscript; the approaches below are the search state '
    + 'underneath them, and there are far more of them.'));

  if (!DATA.search) {
    page.appendChild(emptyState(
      'This repository has no search portfolio. That is a normal state: a portfolio is '
      + 'created when several approaches, agents or sessions are in flight at once, and '
      + 'one describing a search nobody is running is overhead.'));
    return page;
  }

  const model = searchGraphModel();
  if (model.nodes.length) {
    page.appendChild(graph({
      ...model,
      focusId: model.nodes[0].id,
      selectHandler: (id) => (DATA.search.routes[id]
        ? approachSummaryCard(DATA.search.routes[id])
        : familySummaryCard(DATA.search.families[id])),
      stageNote: 'families on top, approaches beneath them',
    }));
  }

  page.appendChild(el('h2', { text: 'Families and their approaches' }));
  for (const family of Object.values(DATA.search.families)) {
    page.appendChild(el('div', { class: 'card', style: 'margin-bottom:1rem' },
      el('div', { class: 'badges' },
        el('code', { class: 'id', text: family.id }),
        familyBadge(family.state)),
      family.mechanism ? el('p', { class: 'row-body' }, math(family.mechanism)) : null,
      family.reopen_if
        ? el('p', { class: 'row-note' }, 'Reopens if: ', math(family.reopen_if)) : null,
      family.closure_checkpoint
        ? el('p', { class: 'row-note' }, 'Closed at ', fileLink(family.closure_checkpoint)) : null,
      el('ul', { class: 'rows', style: 'margin-top:.8rem' },
        family.routes.map((id) => approachRow(DATA.search.routes[id])))));
  }
  return page;
}

/* The id is drawn as this row's name, not as metadata beside one.
 *
 * A claim row leads with a title and carries its id alongside; an approach has no title
 * to lead with — the portfolio schema gives it an `id` and an `objective` and nothing
 * else, deliberately, because an approach is coordination state rather than a statement
 * with a name. So the two lists were reading differently for a reason, but drawing the
 * id as a small chip made it look like a footnote to a row with no heading at all. It
 * stays monospace, because it is an id and is quoted as one. Inventing a display name
 * here is what this directory does not do. */
function approachRow(route) {
  if (!route) return null;
  return el('li', { class: 'tight' },
    el('div', { class: 'row-head' },
      el('a', { class: 'id row-name', href: `#/approach/${route.id}`, text: route.id }),
      approachBadge(route.state),
      route.parent ? el('span', { class: 'note' }, 'from ', idLink(route.parent)) : null,
      route.blocker ? el('span', { class: 'note' }, 'blocked on ', idLink(route.blocker)) : null),
    route.objective ? el('p', { class: 'row-body' }, math(route.objective)) : null);
}

function approachSummaryCard(route) {
  return el('div', { class: 'card', style: 'margin-top:1rem' },
    el('div', { class: 'badges' },
      el('a', { class: 'id', href: `#/approach/${route.id}`, text: route.id }),
      approachBadge(route.state)),
    route.objective ? el('p', { class: 'row-body' }, math(route.objective)) : null,
    el('div', { class: 'actions' },
      el('a', { class: 'action', href: `#/approach/${route.id}` }, 'Full record')));
}

function familySummaryCard(family) {
  if (!family) return el('div', {});
  return el('div', { class: 'card', style: 'margin-top:1rem' },
    el('div', { class: 'badges' },
      el('code', { class: 'id', text: family.id }),
      familyBadge(family.state)),
    family.mechanism ? el('p', { class: 'row-body' }, math(family.mechanism)) : null);
}

/* ---------------------------------------------------------------- node detail ------ */

function proofCard(proof) {
  const detail = proof.review_detail;
  const agent = proof.mode === 'agent';
  const links = dossierLinks(proof.artifact);
  return el('li', {},
    el('div', { class: 'row-head' },
      el('span', { class: 'badge neutral', text: `mode: ${proof.mode || '?'}` }),
      fileLink(proof.artifact, null, proof.artifact),
      links.html ? el('a', { class: 'action', href: links.html }, 'Read it') : null,
      links.pdf ? el('a', { class: 'action', href: links.pdf, target: '_blank' }, 'PDF') : null),
    agent
      ? el('div', {},
        el('p', { class: 'row-body' },
          'Certified by an independent review on disk: ',
          fileLink(proof.review, null, proof.review), '.'),
        detail ? el('dl', { class: 'kv' },
          el('dt', { text: 'verdict' }), el('dd', { text: detail.verdict || '—' }),
          el('dt', { text: 'reviewer' }), el('dd', { text: detail.reviewer || '—' }),
          el('dt', { text: 'author(s)' }), el('dd', { text: detail.authors.join(', ') || '—' }),
          el('dt', { text: 'dated' }), el('dd', { text: detail.date || '—' })) : null)
      : el('p', { class: 'row-body' },
        'Accepted by ',
        el('strong', { text: proof.accepted_by || 'an unnamed person' }),
        '. A human acceptance is an attestation: unlike an agent certification it '
        + 'carries no persisted review report in the repository, and this page does not '
        + 'present the two as equal evidence.'));
}

function viewNode(id) {
  const claim = DATA.claims[id];
  const page = el('div', {});
  if (!claim) {
    page.appendChild(el('h1', { text: 'No such claim' }));
    page.appendChild(el('p', { class: 'lede' },
      'Nothing in this ledger has the id ', el('code', { class: 'id', text: id }), '. It '
      + 'may have been a candidate that was never promoted, or a route — those live '
      + 'on the search map.'));
    page.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'action', href: '#/audit/claims' }, 'The claim graph'),
      el('a', { class: 'action', href: '#/audit/portfolio' }, 'The search map')));
    return page;
  }

  page.appendChild(el('div', { class: 'detail-head' },
    el('p', { class: 'crumb' }, el('a', { href: '#/audit/claims', text: 'Claims' }), ' / ', claim.id),
    el('h1', {}, math(claimName(claim))),
    claim.title ? el('p', { class: 'subhead' },
      el('code', { class: 'id', text: claim.id }),
      el('span', { class: 'note', text: ' — the stable identifier: quote this one.' })) : null,
    el('div', { class: 'badges' },
      el('span', { class: 'badge kind', text: claim.kind || '?' }),
      standingBadge(claim),
      el('span', { class: 'badge kind', text: claim.provenance || 'unknown provenance' }),
      claim.import_class ? el('span', { class: 'badge kind', text: claim.import_class }) : null,
      claim.id === DATA.program.target ? el('span', { class: 'badge neutral', text: 'target' }) : null,
      claim.applicability_blocked_by.length
        ? el('span', { class: 'badge warn' }, 'applicability-blocked') : null)));

  page.appendChild(el('div', { class: 'card' }, glossBlock(claim)));

  /* --- what fences it ------------------------------------------------------------- */

  const hard = claim.edges.bounded_by || [];
  const soft = claim.edges.heuristic_barriers || [];
  if (hard.length || soft.length) {
    page.appendChild(el('h2', { text: 'Obstructions' }));
    const cards = [];
    if (hard.length) {
      cards.push(el('div', { class: 'card fence hard' },
        el('span', { class: 'fence-label', text: 'Hard fence — proved' }),
        el('p', { class: 'row-body' },
          'A statement violating one of these is wrong by construction.'),
        idList(hard)));
    }
    if (soft.length) {
      cards.push(el('div', { class: 'card fence soft' },
        el('span', { class: 'fence-label', text: 'Heuristic barrier — advisory' }),
        el('p', { class: 'row-body' },
          'These guide work and fence nothing logically. An open obstruction is a '
          + 'method barrier somebody expects to bite, not a proved impossibility.'),
        idList(soft)));
    }
    page.appendChild(el('div', { class: 'grid two' }, cards));
  }

  /* --- truth vs applicability ------------------------------------------------------ */

  page.appendChild(el('h2', { text: 'How it sits in the graph' }));
  const relationRows = [];
  for (const relation of DATA.vocabulary.relations) {
    if (relation.field === 'bounded_by' || relation.field === 'heuristic_barriers') continue;
    const forward = claim.edges[relation.field] || [];
    const reverseSpec = DATA.vocabulary.reverse[relation.field];
    const backward = reverseSpec ? claim.reverse[reverseSpec.field] || [] : [];
    if (!forward.length && !backward.length) continue;
    relationRows.push(el('div', { class: 'card' },
      el('h3', { text: relation.label }),
      el('p', { class: 'note', text: relation.gloss }),
      el('dl', { class: 'kv' },
        el('dt', { text: relation.label }), el('dd', {}, idList(forward)),
        reverseSpec ? el('dt', { text: reverseSpec.label }) : null,
        reverseSpec ? el('dd', {}, idList(backward)) : null)));
  }
  page.appendChild(relationRows.length
    ? el('div', { class: 'grid two' }, relationRows)
    : emptyState('This claim stands on its own: no recorded relation to another node.'));

  if (claim.applicability_blocked_by.length) {
    page.appendChild(el('div', { class: 'card', style: 'margin-top:1rem' },
      el('h3', { text: 'Applicability' }),
      el('p', { class: 'row-body' },
        'This is proved, and its antecedents are not. That does not weaken the proof: '
        + 'the implication holds; what it can be applied to is what is blocked.'),
      idList(claim.applicability_blocked_by)));
  }

  /* --- certification --------------------------------------------------------------- */

  page.appendChild(el('h2', { text: 'Certification' }));
  if (claim.proofs.length) {
    page.appendChild(el('ul', { class: 'rows' }, claim.proofs.map(proofCard)));
  } else if (claim.status === 'refuted') {
    page.appendChild(el('div', { class: 'card' },
      el('p', { class: 'row-body' },
        'This statement is refuted. A refuted node has no proof: it names its proved '
        + 'refuters, each of which is an ordinary node carrying an ordinary certified '
        + 'dossier of its own.'),
      idList(claim.edges.refuted_by)));
  } else {
    page.appendChild(emptyState(
      claim.status === 'open'
        ? 'Open. No proof is recorded — this is the work that remains.'
        : 'No proof record.'));
  }

  if (claim.references.length) {
    page.appendChild(el('h2', { text: 'References' }));
    page.appendChild(el('ul', { class: 'inline-list' },
      claim.references.map((key) => el('li', {}, el('code', { class: 'id', text: key })))));
  }

  /* --- the search around it -------------------------------------------------------- */

  page.appendChild(el('h2', { text: 'The search around it' }));
  const around = [];
  if (claim.blocks_routes.length) {
    around.push(el('div', { class: 'card' },
      el('h3', { text: 'Routes blocked on this' }),
      el('ul', { class: 'rows' },
        claim.blocks_routes.map((id) => approachRow(DATA.search.routes[id])))));
  }
  if (claim.checkpoints.length) {
    /* Newest first, and only the newest few unfolded.
     *
     * A claim near the centre of a search collects dozens of these. In the order the
     * ledger stores them the reader meets the oldest first and scrolls past a year of
     * work to reach what happened last week, on a page whose question is what this claim
     * is doing now. Nothing is dropped: constraint 6 makes this record append-only, and a
     * page that quietly truncated it would be misreporting the memory. The rest are
     * behind a disclosure that says how many. */
    const records = claim.checkpoints
      .map((path) => DATA.memory.checkpoints.find((record) => record.path === path))
      .filter(Boolean)
      .sort((a, b) => String(b.date || '').localeCompare(String(a.date || '')));
    const card = el('div', { class: 'card' },
      el('h3', { text: 'Checkpoints that engaged it' }),
      el('ul', { class: 'rows' }, records.slice(0, RECENT_CHECKPOINTS).map(checkpointRow)));
    if (records.length > RECENT_CHECKPOINTS) {
      const rest = records.length - RECENT_CHECKPOINTS;
      card.appendChild(el('details', { class: 'more' },
        el('summary', { text: `${rest} earlier record${rest === 1 ? '' : 's'}` }),
        el('ul', { class: 'rows' }, records.slice(RECENT_CHECKPOINTS).map(checkpointRow))));
    }
    around.push(card);
  }
  page.appendChild(around.length
    ? el('div', { class: 'grid two' }, around)
    : emptyState('No route is blocked on this and no checkpoint has engaged it.'));

  /* --- contribute ------------------------------------------------------------------ */

  if (repoBase()) {
    page.appendChild(el('h2', { text: 'Contribute to this claim' }));
    page.appendChild(el('div', { class: 'actions' },
      claim.proofs.length ? contribute('proof-gap.yml', 'Report a gap in this proof', claim.id) : null,
      claim.status !== 'refuted' ? contribute('counterexample.yml', 'Propose a counterexample', claim.id) : null,
      contribute('literature-lead.yml', 'Point at existing work', claim.id),
      contribute('correction.yml', 'Report an error on this page', claim.id),
      discussLink('Discuss this claim')));
    page.appendChild(el('p', { class: 'note', style: 'margin-top:.6rem' },
      'A proof or refutation enters the same way here as anywhere else in this '
      + 'repository: a standalone dossier and an independent certification. Nothing '
      + 'reaches this page’s status field by acclamation.'));
  }

  return page;
}

/* --------------------------------------------------------------- route detail ------ */

function viewApproach(id) {
  const page = el('div', {});
  const route = DATA.search && DATA.search.routes[id];
  if (!route) {
    page.appendChild(el('h1', { text: 'No such approach' }));
    page.appendChild(el('p', { class: 'lede' },
      'The portfolio has no approach ', el('code', { class: 'id', text: id }),
      '. Approaches are transient by design and this one may never have existed; the '
      + 'portfolio records what the search is doing now, not everything it ever did.'));
    page.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'action', href: '#/audit/portfolio' }, 'The portfolio')));
    return page;
  }
  const family = DATA.search.families[route.family];
  /* Which of the four mathematical routes contains this approach, if any. Shown above
     everything else: the objective and the blocker below are far easier to place once a
     reader knows which route they belong to. */
  const g = guide();
  const within = g && [...(g.routes || []),
    ...(g.probes ? [{ code: null, name: g.probes.name, families: g.probes.families }] : [])]
    .find((entry) => (entry.families || []).includes(route.family));

  page.appendChild(el('div', { class: 'detail-head' },
    el('p', { class: 'crumb' }, el('a', { href: '#/audit/portfolio', text: 'Portfolio' }), ' / ', route.id),
    el('h1', { text: route.id }),
    el('div', { class: 'badges' },
      approachBadge(route.state),
      family ? el('span', { class: 'badge kind', text: family.id }) : null,
      within ? el('a', { class: 'badge kind',
        href: within.code ? `#/routes/${within.code}` : '#/routes',
        text: within.code ? `Route ${within.code}` : within.name }) : null)));

  page.appendChild(el('div', { class: 'banner' },
    el('strong', { text: 'This page describes search activity, not mathematical truth. ' }),
    'An approach records what is being tried and why it stopped. Nothing on it is a '
    + 'claim; the claims it names are, and each of those links to its own page.',
    within && within.code
      ? [' It sits under ', el('a', { href: `#/routes/${within.code}` },
        `Route ${within.code} — ${within.name}`), '.']
      : []));

  page.appendChild(el('div', { class: 'card' },
    el('span', { class: 'gloss-tag', text: 'Objective — an intention, never a claim' }),
    el('p', { class: 'gloss' }, math(route.objective || '—')),
    el('p', { class: 'note' },
      'An approach has no truth value. "Completed" would mean this approach’s objective '
      + 'is finished and there is nothing left to try along it — it says nothing about '
      + 'whether the target is settled.')));

  if (family) {
    page.appendChild(el('h2', { text: 'Its family' }));
    page.appendChild(el('div', { class: 'card' },
      el('div', { class: 'badges' },
        el('code', { class: 'id', text: family.id }), familyBadge(family.state)),
      family.mechanism ? el('p', { class: 'row-body' }, math(family.mechanism)) : null,
      family.reopen_if ? el('p', { class: 'row-note' }, 'Family reopens if: ', math(family.reopen_if)) : null,
      family.closure_checkpoint
        ? el('p', { class: 'row-note' }, 'Closed at ', fileLink(family.closure_checkpoint)) : null));
  }

  if (route.state === 'blocked') {
    page.appendChild(el('h2', { text: 'What it is stuck on' }));
    page.appendChild(el('div', { class: 'card fence hard' },
      el('p', { class: 'row-head' }, 'Blocked on ', idLink(route.blocker)),
      route.reopen_if ? el('p', { class: 'row-body' }, 'Reopens if: ', math(route.reopen_if)) : null,
      el('p', { class: 'note' },
        'The blocker is named, never restated here. If it is a candidate it is a '
        + 'tentative statement with no status; if it is a node it is a claim with one.')));
  }

  page.appendChild(el('h2', { text: 'How it relates to other routes' }));
  const relations = [];
  if (route.parent) relations.push(el('dt', { text: 'grew out of' }), el('dd', {}, idLink(route.parent)));
  if (route.children.length) relations.push(el('dt', { text: 'grew into' }), el('dd', {}, idList(route.children)));
  for (const relation of route.related) {
    relations.push(el('dt', { text: relation.relation }), el('dd', {}, idLink(relation.to)));
  }
  page.appendChild(relations.length
    ? el('div', { class: 'card' }, el('dl', { class: 'kv' }, relations))
    : emptyState('No recorded relation to another route.'));

  page.appendChild(el('h2', { text: 'Why its state changed' }));
  if (route.checkpoints.length) {
    page.appendChild(el('ul', { class: 'rows' }, route.checkpoints.map((path) =>
      checkpointRow(DATA.memory.checkpoints.find((record) => record.path === path)
        || { path, date: null, outcome: null, nodes: [], superseded_by: [] }))));
  } else {
    page.appendChild(emptyState(
      'No checkpoint is attached. A route that stops owes one; a live route need not.'));
  }

  if (repoBase()) {
    page.appendChild(el('h2', { text: 'Contribute to this route' }));
    page.appendChild(el('div', { class: 'actions' },
      contribute('route-proposal.yml', 'Propose a way past this', route.id),
      contribute('literature-lead.yml', 'Point at existing work', route.id),
      discussLink('Discuss this route')));
  }
  return page;
}

/* -------------------------------------------------------------------- evidence ----- */

/**
 * One dated record.
 *
 * `excerpt: false` drops the prose and keeps the structure — date, outcome, the record
 * itself, the approach, the nodes it engaged. A checkpoint is written by and for the
 * roles running the search, so its opening paragraph is frequently operational rather
 * than mathematical: which role wrote it, under which run and identity, holding which
 * concurrency key. That is the right content for the record, and it is right under
 * Audit, where a reader has come to see what the search did. On the front page it is
 * the last thing before the contribution links, and it reads as machine exhaust to the
 * mathematician the front page exists to reach. The dates, the outcomes and the engaged
 * claims still say what a front page needs to say — that the search is live, and what it
 * has been touching.
 */
function checkpointRow(record, { excerpt = true } = {}) {
  if (!record) return null;
  const superseded = record.superseded_by && record.superseded_by.length;
  return el('li', {},
    el('div', { class: 'row-head' },
      el('span', { class: 'note', text: record.date || '—' }),
      record.outcome
        ? el('span', { class: 'badge neutral', text: OUTCOME_WORD[record.outcome] || record.outcome })
        : null,
      superseded ? el('span', { class: 'badge warn' }, 'superseded') : null,
      fileLink(record.path, null, record.path.split('/').pop()),
      record.approach ? idLink(record.approach) : null),
    excerpt && record.excerpt ? el('p', { class: 'row-body' }, math(record.excerpt)) : null,
    record.nodes && record.nodes.length
      ? el('p', { class: 'row-note' }, 'engaged ', idList(record.nodes)) : null,
    superseded
      ? el('p', { class: 'row-note' }, 'Read instead: ',
        el('ul', { class: 'inline-list' }, record.superseded_by.map((path) =>
          el('li', {}, fileLink(path, null, path.split('/').pop())))))
      : null);
}

function viewEvidence() {
  const page = el('div', {});
  page.appendChild(auditNav('#/audit/evidence'));
  page.appendChild(el('h1', { text: 'Durable evidence' }));
  page.appendChild(el('p', { class: 'lede' },
    'Why the search is where it is. These records are append-only: nothing here is '
    + 'rewritten or deleted, and a later record may declare an earlier one superseded — '
    + 'which changes what to read first and nothing else.'));

  /* --- candidates ----------------------------------------------------------------- */

  page.appendChild(el('h2', { text: 'Live candidate statements' }));
  page.appendChild(el('p', { class: 'note' },
    'A candidate is a statement somebody thought worth writing down and nothing more. '
    + 'It has no manuscript anchor, no status and no certification, and it is not a '
    + 'claim. Unlike a ledger node’s one-line gloss, a candidate’s text below '
    + 'is canonical — nothing else in the repository holds it.'));
  const candidates = DATA.memory.candidates;
  page.appendChild(candidates.length
    ? el('ul', { class: 'rows' }, candidates.map((candidate) => el('li', {},
      el('div', { class: 'row-head' },
        el('code', { class: 'id', text: candidate.id }),
        el('span', { class: 'badge neutral', text: 'candidate — not a claim' }),
        el('span', { class: 'note', text: candidate.date || '' })),
      el('p', { class: 'row-body gloss' }, math(candidate.statement)),
      el('p', { class: 'row-note' }, 'proposed in ', fileLink(candidate.source)),
      candidate.blocks_routes && candidate.blocks_routes.length
        ? el('p', { class: 'row-note' }, 'blocks ', idList(candidate.blocks_routes)) : null)))
    : emptyState('No live candidates.'));

  const promoted = Object.entries(DATA.memory.promoted);
  if (promoted.length) {
    page.appendChild(el('h3', { text: 'Promoted — no longer candidates' }));
    page.appendChild(el('ul', { class: 'rows' }, promoted.map(([id, promotion]) =>
      el('li', { class: 'tight' }, el('div', { class: 'row-head' },
        el('code', { class: 'id', text: id }), '→', idLink(promotion.node),
        el('span', { class: 'note', text: promotion.date || '' }))))));
  }

  /* --- checkpoints ----------------------------------------------------------------- */

  const heads = DATA.memory.checkpoints.filter((record) => !record.superseded_by.length);
  const stale = DATA.memory.checkpoints.filter((record) => record.superseded_by.length);
  page.appendChild(el('h2', {},
    `Checkpoints — ${heads.length} current`,
    stale.length ? `, ${stale.length} superseded` : ''));
  page.appendChild(heads.length
    ? filteredList(heads, {
      noun: 'current checkpoints',
      facets: [
        { label: 'approach', of: (record) => record.approach },
        { label: 'outcome', of: (record) => record.outcome },
        { label: 'year', of: (record) => (record.date || '').slice(0, 4) },
      ],
      search: (record) => `${record.path} ${record.excerpt || ''} ${record.nodes.join(' ')}`,
      render: checkpointRow,
    })
    : emptyState('No checkpoints recorded.'));
  if (stale.length) {
    page.appendChild(el('h3', { text: 'Superseded' }));
    page.appendChild(el('p', { class: 'note' },
      'Kept, never rewritten: research/explorations/ is append-only, and a superseded '
      + 'record still says truthfully what was believed when it was written. The heir '
      + 'named on each one is which to read first.'));
    page.appendChild(filteredList(stale, {
      noun: 'superseded checkpoints',
      facets: [
        { label: 'approach', of: (record) => record.approach },
        { label: 'outcome', of: (record) => record.outcome },
        { label: 'year', of: (record) => (record.date || '').slice(0, 4) },
      ],
      search: (record) => `${record.path} ${record.excerpt || ''}`,
      render: checkpointRow,
    }));
  }

  /* --- reviews --------------------------------------------------------------------- */

  const reviews = Object.values(DATA.memory.reviews);
  page.appendChild(el('h2', { text: 'Independent certifications' }));
  page.appendChild(el('p', { class: 'note' },
    'An author never certifies their own proof. Each report below names distinct '
    + 'author(s) and reviewer, and the ledger record that cites it is what makes the '
    + 'node proved.'));
  page.appendChild(reviews.length
    ? el('ul', { class: 'rows' }, reviews.map((review) => el('li', {},
      el('div', { class: 'row-head' },
        el('span', { class: 'note', text: review.date || '—' }),
        el('span', { class: 'badge proved' },
          el('span', { class: 'glyph', 'aria-hidden': 'true', text: '✓' }), review.verdict || '—'),
        fileLink(review.path, null, review.path.split('/').pop())),
      el('dl', { class: 'kv' },
        el('dt', { text: 'reviewer' }), el('dd', { text: review.reviewer || '—' }),
        el('dt', { text: 'author(s)' }), el('dd', { text: review.authors.join(', ') || '—' }),
        el('dt', { text: 'nodes' }), el('dd', {}, idList(review.nodes)),
        el('dt', { text: 'dossiers' }), el('dd', {}, review.solutions.map((path) =>
          el('span', {}, fileLink(path), ' ')))))))
    : emptyState('No certifications recorded.'));

  /* --- audits ---------------------------------------------------------------------- */

  const audits = Object.values(DATA.memory.audits);
  if (audits.length) {
    page.appendChild(el('h2', { text: 'Audits' }));
    page.appendChild(el('p', { class: 'note' },
      'An audit certifies nothing. It reports on the repository itself, and a later '
      + 'audit may supersede it.'));
    page.appendChild(el('ul', { class: 'rows' }, audits.map((audit) => el('li', {},
      el('div', { class: 'row-head' },
        el('span', { class: 'note', text: audit.date || '—' }),
        audit.superseded ? el('span', { class: 'badge warn' }, 'superseded') : null,
        fileLink(audit.path, null, audit.path.split('/').pop())),
      audit.excerpt ? el('p', { class: 'row-body' }, math(audit.excerpt)) : null))));
  }

  /* --- runs ------------------------------------------------------------------------ */

  const runs = DATA.memory.runs;
  page.appendChild(el('h2', { text: 'Numerical run artifacts' }));
  page.appendChild(el('p', { class: 'note' },
    'Provenance-stamped and immutable, and they certify nothing: no run changes a '
    + 'claim, a proof step, or a status. An exact witness a run emits is a candidate '
    + 'until it is checked independently.'));
  page.appendChild(runs.length
    ? el('ul', { class: 'rows' }, runs.map((run) => el('li', { class: 'tight' },
      el('div', { class: 'row-head' },
        fileLink(run.path, null, run.path.split('/').pop()),
        el('span', { class: 'badge neutral', text: `target: ${run.target}` }),
        el('span', { class: 'note', text: `${run.observations} observation(s)` })))))
    : emptyState('No run artifacts.'));

  return page;
}

/* ------------------------------------------------------------------------ router ---- */

/* -------------------------------------------------------------- explore views ------ */

/**
 * The editorial guide, or a null object.
 *
 * Everything below degrades to the audit views when no guide is published: a repository
 * that keeps none is complete, and the site must not be the reason someone writes one.
 */
function guide() {
  return DATA.guide || null;
}

function routeByCode(code) {
  const g = guide();
  return g && (g.routes || []).find((route) => route.code === code);
}

/** Every portfolio approach belonging to one route's families, in portfolio order. */
function approachesOf(entry) {
  if (!DATA.search || !entry) return [];
  const families = new Set(entry.families || []);
  return Object.values(DATA.search.routes)
    .filter((approach) => families.has(approach.family))
    .sort((a, b) => a.id.localeCompare(b.id));
}

/**
 * What a route is made of, as a composition rather than a single state.
 *
 * A route holding four active approaches, one blocked and two queued is not "active",
 * and a badge saying so would flatten the one thing a reader wants from this line. The
 * portfolio has five approach states and this prints whichever are present, in the order
 * a reader cares about them.
 */
const APPROACH_ORDER = ['active', 'blocked', 'queued', 'completed', 'duplicate'];

function composition(approaches) {
  const counts = {};
  for (const approach of approaches) counts[approach.state] = (counts[approach.state] || 0) + 1;
  return APPROACH_ORDER.filter((state) => counts[state])
    .map((state) => `${counts[state]} ${state}`)
    .join(' · ');
}

function featuredFor(code, role) {
  const g = guide();
  if (!g) return [];
  return (g.featured || [])
    .filter((entry) => (code === null || entry.route === code)
      && (role === null || entry.role === role))
    .map((entry) => ({ ...entry, claim: DATA.claims[entry.id] }))
    .filter((entry) => entry.claim);
}

/** A link into the rendered manuscript at one \label, or null when none is attached. */
function anchorLink(anchor) {
  const html = DATA.documents && DATA.documents.html;
  return html && html.manuscript ? `${html.manuscript}#${anchor}` : null;
}

function manuscriptAction(anchor, label) {
  const href = anchorLink(anchor);
  return href ? el('a', { class: 'action', href }, label) : null;
}

/** One claim, named and standing-badged, as a row in a curated list. */
function featuredRow(entry) {
  const claim = entry.claim;
  return el('li', {},
    el('div', { class: 'row-head' },
      el('a', { class: 'row-name', href: `#/node/${claim.id}` }, math(claimName(claim))),
      el('span', { class: 'badge kind', text: claim.kind || '?' }),
      standingBadge(claim),
      entry.route ? el('span', { class: 'badge kind', text: `Route ${entry.route}` }) : null),
    el('p', { class: 'row-note' }, el('code', { class: 'id', text: claim.id })),
    el('p', { class: 'row-body' }, math(claim.gloss)));
}

function routeCard(route) {
  const approaches = approachesOf(route);
  const bridges = featuredFor(route.code, 'bridge');
  const blockers = featuredFor(route.code, 'bottleneck');
  return el('div', { class: 'card route-card' },
    el('h3', {},
      el('a', { href: `#/routes/${route.code}`, text: `Route ${route.code} — ${route.name}` })),
    el('p', { class: 'note' },
      approaches.length
        ? `${approaches.length} approach${approaches.length === 1 ? '' : 'es'} in the `
          + `portfolio: ${composition(approaches)}`
        : 'No approach in the portfolio is filed under this route.'),
    bridges.length ? el('p', { class: 'row-note' },
      el('span', { class: 'gloss-tag', text: 'Bridge to KLS' }), ' ',
      el('a', { href: `#/node/${bridges[0].claim.id}` }, math(claimName(bridges[0].claim)))) : null,
    blockers.length ? el('p', { class: 'row-note' },
      el('span', { class: 'gloss-tag', text: 'Exact bottleneck' }), ' ',
      el('a', { href: `#/node/${blockers[0].claim.id}` }, math(claimName(blockers[0].claim)))) : null,
    el('div', { class: 'actions' },
      el('a', { class: 'action', href: `#/routes/${route.code}` }, 'Open the route'),
      manuscriptAction(route.anchor, 'Route gateway in the manuscript')));
}

/**
 * The same four routes, named and counted, as one row apiece.
 *
 * The front page and the Routes page were drawing the identical `routeCard`, which made
 * Routes a copy of a section the reader had already scrolled past and gave the tab
 * nothing to add but "Other probes". The nav's own split says the Overview should
 * orient in one screen; four rows do that, and the full cards — bridge, bottleneck, and
 * the way into the manuscript gateway — are what the reader finds on arriving at Routes.
 */
function routeRow(route) {
  const approaches = approachesOf(route);
  const blockers = featuredFor(route.code, 'bottleneck');
  return el('li', {},
    el('div', { class: 'row-head' },
      el('a', { class: 'row-name', href: `#/routes/${route.code}`,
        text: `Route ${route.code} — ${route.name}` })),
    el('p', { class: 'row-note' },
      approaches.length
        ? `${approaches.length} approach${approaches.length === 1 ? '' : 'es'}: `
          + `${composition(approaches)}`
        : 'No approach in the portfolio is filed under this route.'),
    blockers.length ? el('p', { class: 'row-note' },
      el('span', { class: 'gloss-tag', text: 'Exact bottleneck' }), ' ',
      el('a', { href: `#/node/${blockers[0].claim.id}` },
        math(claimName(blockers[0].claim)))) : null);
}

function viewRoutes() {
  const page = el('div', {});
  const g = guide();
  page.appendChild(el('h1', { text: 'Four routes' }));
  if (!g) {
    page.appendChild(el('p', { class: 'lede' },
      'This repository publishes no editorial guide, so there is no curated route '
      + 'grouping. The portfolio itself is under Audit.'));
    page.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'action', href: '#/audit/portfolio' }, 'The portfolio')));
    return page;
  }
  page.appendChild(el('p', { class: 'lede' },
    'The manuscript organizes this work into four mathematical routes. They are the '
    + 'organization to read by. Beneath each sit the portfolio approaches actually in '
    + 'flight — search state, which changes with the week and carries no truth value.'));
  page.appendChild(el('div', { class: 'grid two' },
    (g.routes || []).map((route) => routeCard(route))));

  if (g.probes && (g.probes.families || []).length) {
    const probes = approachesOf(g.probes);
    page.appendChild(el('h2', { text: g.probes.name || 'Other probes' }));
    page.appendChild(el('p', { class: 'note' },
      'Registered probes that have not become a route. They are listed apart from E, S, '
      + 'C and F on purpose: drawing them level would claim a standing the portfolio '
      + 'does not give them.'));
    page.appendChild(probes.length
      ? el('ul', { class: 'rows' }, probes.map(approachRow))
      : emptyState('No probe is registered.'));
  }
  return page;
}

function viewRouteDetail(code) {
  const page = el('div', {});
  const route = routeByCode(code);
  if (!route) {
    page.appendChild(el('h1', { text: 'No such route' }));
    page.appendChild(el('p', { class: 'lede' },
      'This site names four routes, E, S, C and F. ',
      el('code', { class: 'id', text: code }), ' is not one of them.'));
    page.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'action', href: '#/routes' }, 'The four routes')));
    return page;
  }
  const approaches = approachesOf(route);

  page.appendChild(el('div', { class: 'detail-head' },
    el('p', { class: 'crumb' }, el('a', { href: '#/routes', text: 'Routes' }), ' / ', code),
    el('h1', { text: `Route ${code} — ${route.name}` }),
    el('div', { class: 'badges' },
      el('span', { class: 'badge kind', text: composition(approaches) || 'no approaches' }))));

  page.appendChild(el('p', { class: 'lede' },
    'The mechanism, the bridge to KLS, the main advance, the exact bottleneck and the '
    + 'failed variants are stated once, in the manuscript’s route gateway. This page '
    + 'names the claims and the live approaches and sends you there rather than '
    + 'paraphrasing it into a second version that nothing keeps in step.'));
  page.appendChild(el('div', { class: 'actions' },
    manuscriptAction(route.anchor, 'Route gateway in the manuscript')
      || el('p', { class: 'note' },
        'The HTML manuscript is not attached to this build, so the gateway cannot be '
        + 'linked here.')));

  for (const [role, heading] of [
    ['bridge', 'Bridge to KLS'],
    ['advance', 'Main advance so far'],
    ['bottleneck', 'Exact bottleneck'],
    ['obstruction', 'Proved obstruction'],
    ['refuted', 'Refuted variant'],
    ['model', 'Decisive model computation'],
  ]) {
    const entries = featuredFor(code, role);
    if (!entries.length) continue;
    page.appendChild(el('h2', { text: heading }));
    page.appendChild(el('ul', { class: 'rows' }, entries.map(featuredRow)));
  }

  page.appendChild(el('h2', { text: 'Approaches in flight' }));
  page.appendChild(el('p', { class: 'note' },
    'Search state, not mathematics. An approach records what is being tried; '
    + '"completed" means its objective ended, never that anything was settled.'));
  page.appendChild(approaches.length
    ? el('ul', { class: 'rows' }, approaches.map(approachRow))
    : emptyState('No approach in the portfolio is filed under this route.'));
  return page;
}

function viewResults() {
  const page = el('div', {});
  const g = guide();
  page.appendChild(el('h1', { text: 'Key results' }));
  if (!g || !(g.featured || []).length) {
    page.appendChild(el('p', { class: 'lede' },
      'This repository publishes no curated selection. Every claim is under Audit.'));
    page.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'action', href: '#/audit/claims' }, 'Every claim')));
    return page;
  }
  const total = Object.keys(DATA.claims).length;
  page.appendChild(el('p', { class: 'lede' },
    `${g.featured.length} claims of ${total}, grouped by the job each one does in the `
    + 'argument. This is a reading order, not a ranking, and it is the only part of this '
    + 'site that is a matter of editorial judgment rather than derivation. The complete '
    + 'inventory is under Audit.'));

  for (const [role, heading, blurb] of [
    ['bridge', 'Bridges to KLS',
      'What would give the conjecture, if its antecedent were discharged.'],
    ['advance', 'Principal established advances',
      'What this repository has actually proved and certified.'],
    ['bottleneck', 'Exact open bottlenecks',
      'The precise statements whose absence stops each route.'],
    ['obstruction', 'Proved obstructions',
      'Fences. A statement violating one is wrong by construction.'],
    ['refuted', 'Refuted variants',
      'Attempts settled in the negative, kept because knowing what fails is a result.'],
    ['model', 'Decisive model computations',
      'Exact cases that fixed the shape of the general question.'],
  ]) {
    const entries = featuredFor(null, role);
    if (!entries.length) continue;
    page.appendChild(el('h2', { text: heading }));
    page.appendChild(el('p', { class: 'note' }, blurb));
    page.appendChild(el('ul', { class: 'rows' }, entries.map(featuredRow)));
  }
  return page;
}

function viewManuscript() {
  const page = el('div', {});
  const g = guide();
  const documents = DATA.documents || {};
  const html = documents.html && documents.html.manuscript;
  const pdf = documents.pdf && documents.pdf.manuscript;

  page.appendChild(el('h1', { text: 'The manuscript' }));
  page.appendChild(el('p', { class: 'lede' },
    'The mathematics lives here, not on this site. The manuscript states every claim, '
    + 'proves what is proved, and explains the frontier in an order meant to be read. '
    + 'Everything else on this site is an index into it.'));

  page.appendChild(el('div', { class: 'actions' },
    html ? el('a', { class: 'action', href: html }, 'Read it (HTML)') : null,
    pdf ? el('a', { class: 'action', href: pdf, target: '_blank' }, 'Download it (PDF)') : null,
    (() => {
      const source = sourceLink('main.tex');
      return source ? el('a', { class: 'action', href: source, rel: 'noopener', target: '_blank' },
        'LaTeX source') : null;
    })()));

  /* Missing renderings are named, not hidden. A control that is simply absent tells a
     reader the manuscript is unavailable rather than that one form of it is. */
  if (!html || !pdf) {
    const missing = [];
    if (!html) missing.push('the HTML conversion');
    if (!pdf) missing.push('the PDF');
    page.appendChild(el('p', { class: 'note' },
      `${sentence(missing.join(' and '))} `
      + `${missing.length > 1 ? 'were' : 'was'} not attached to this build. `
      + `${missing.length > 1 ? 'Both are' : 'It is'} produced by the publishing `
      + 'workflow, which compiles LaTeX; a build made without it reaches the manuscript '
      + 'through the source instead.'));
  }

  if (g && (g.reading || []).length) {
    page.appendChild(el('h2', { text: 'Where to start' }));
    page.appendChild(el('p', { class: 'note' },
      'Each of these is a section of the manuscript, linked at its own anchor.'));
    page.appendChild(el('ul', { class: 'rows reading-path' }, g.reading.map((entry) => {
      const href = anchorLink(entry.anchor);
      return el('li', {},
        el('div', { class: 'row-head' },
          href
            ? el('a', { class: 'row-name', href, text: entry.label })
            : el('span', { class: 'row-name', text: entry.label }),
          el('code', { class: 'id', text: entry.anchor })));
    })));
  }

  if (g && (g.routes || []).length) {
    page.appendChild(el('h2', { text: 'The four route gateways' }));
    page.appendChild(el('ul', { class: 'rows reading-path' }, g.routes.map((route) => {
      const href = anchorLink(route.anchor);
      return el('li', {},
        el('div', { class: 'row-head' },
          href
            ? el('a', { class: 'row-name', href, text: `Route ${route.code} — ${route.name}` })
            : el('span', { class: 'row-name', text: `Route ${route.code} — ${route.name}` }),
          el('a', { class: 'id', href: `#/routes/${route.code}`, text: `on this site` })));
    })));
  }
  return page;
}

/* The three audit views, and the order the Audit page lists them in. */
const AUDIT_SECTIONS = [
  { href: '#/audit/claims', label: 'Claims' },
  { href: '#/audit/portfolio', label: 'Portfolio' },
  { href: '#/audit/evidence', label: 'Evidence' },
];

/**
 * A breadcrumb back to Audit, and a link to each sibling view.
 *
 * Audit holds three views and the masthead reaches only their index, so moving from the
 * claim graph to the portfolio meant going back through a hub page whose whole content
 * is three cards — a toll booth on the one section a reader browses rather than lands
 * on. The hub keeps its place, because what it explains (claims, portfolio and evidence
 * are three separate domains and are never merged) is worth a page; it just stops being
 * the only road between them.
 */
function auditNav(current) {
  return el('nav', { class: 'subnav', 'aria-label': 'Audit sections' },
    el('a', { href: '#/audit', text: 'Audit' }),
    AUDIT_SECTIONS.map((section) => (section.href === current
      ? el('span', { 'aria-current': 'page', text: section.label })
      : el('a', { href: section.href, text: section.label }))));
}

function viewAudit() {
  const page = el('div', {});
  page.appendChild(el('h1', { text: 'Audit' }));
  page.appendChild(el('p', { class: 'lede' },
    'The complete research state, unreduced: every claim and every edge, the live search '
    + 'portfolio, and the durable evidence behind both. Nothing here is curated — that is '
    + 'the point of it.'));
  const counts = {
    claims: Object.keys(DATA.claims).length,
    approaches: DATA.search ? Object.keys(DATA.search.routes).length : 0,
    checkpoints: DATA.memory.checkpoints.length,
  };
  page.appendChild(el('div', { class: 'grid three' },
    el('div', { class: 'card' },
      el('h3', { text: 'Claims' }),
      el('p', { class: 'note' },
        `All ${counts.claims} ledger nodes, the dependency graph, statuses, provenance, `
        + 'proof dossiers and independent reviews.'),
      el('div', { class: 'actions' },
        el('a', { class: 'action', href: '#/audit/claims' }, 'Open'))),
    el('div', { class: 'card' },
      el('h3', { text: 'Portfolio' }),
      el('p', { class: 'note' },
        `All ${counts.approaches} approaches and their families: objectives, states, `
        + 'blockers and reopening conditions. Search state, never truth.'),
      el('div', { class: 'actions' },
        el('a', { class: 'action', href: '#/audit/portfolio' }, 'Open'))),
    el('div', { class: 'card' },
      el('h3', { text: 'Evidence' }),
      el('p', { class: 'note' },
        `All ${counts.checkpoints} checkpoints, plus candidates, reviews, audits, `
        + 'numerical artifacts and build provenance.'),
      el('div', { class: 'actions' },
        el('a', { class: 'action', href: '#/audit/evidence' }, 'Open')))));
  return page;
}

const PAGES = [
  [/^\/?$/, viewOverview, 'overview'],
  [/^\/routes\/?$/, viewRoutes, 'routes'],
  [/^\/routes\/(.+)$/, viewRouteDetail, 'routes'],
  [/^\/results\/?$/, viewResults, 'results'],
  [/^\/manuscript\/?$/, viewManuscript, 'manuscript'],
  [/^\/audit\/?$/, viewAudit, 'audit'],
  [/^\/audit\/claims\/?$/, viewClaims, 'audit'],
  [/^\/audit\/portfolio\/?$/, viewSearch, 'audit'],
  [/^\/audit\/evidence\/?$/, viewEvidence, 'audit'],
  [/^\/node\/(.+)$/, viewNode, 'audit'],
  [/^\/approach\/(.+)$/, viewApproach, 'audit'],
];

/* The hashes this site published before the Explore layer existed.
 *
 * A URL that was once correct stays correct: these are in citations, in issues, and in
 * whatever anyone bookmarked. Redirecting costs one line each and is cheaper than any
 * conversation about a link that used to work. */
const MOVED = [
  [/^\/claims\/?$/, () => '#/audit/claims'],
  [/^\/search\/?$/, () => '#/audit/portfolio'],
  [/^\/evidence\/?$/, () => '#/audit/evidence'],
  [/^\/route\/(.+)$/, (match) => `#/approach/${match[1]}`],
];

/**
 * Draw the view the hash names.
 *
 * `navigated` is true for every render but the first. On a hash change the whole of
 * <main> is replaced and nothing says so: a sighted reader watches it happen, a screen
 * reader carries on announcing the page that is no longer there, and the next Tab
 * continues from wherever focus happened to be rather than from the top of what is now
 * shown. Moving focus into <main> — which carries `tabindex="-1"` for exactly this —
 * fixes all three. It is deliberately not done on the first render: nothing changed
 * then, and taking focus away from a reader on load is its own defect.
 */
function render(navigated) {
  const main = document.getElementById('main');
  const path = decodeURIComponent(location.hash.replace(/^#/, '')) || '/';
  for (const [pattern, target] of MOVED) {
    const match = pattern.exec(path);
    if (match) { location.replace(target(match)); return; }
  }
  let page = null;
  let tab = 'overview';
  for (const [pattern, view, name] of PAGES) {
    const match = pattern.exec(path);
    if (match) { page = view(match[1]); tab = name; break; }
  }
  if (!page) {
    page = el('div', {},
      el('h1', { text: 'Not found' }),
      el('p', { class: 'lede' }, 'Nothing is published at ',
        el('code', { class: 'id', text: path }), '.'),
      el('div', { class: 'actions' }, el('a', { class: 'action', href: '#/' }, 'Start here')));
  }
  clear(main);
  main.appendChild(page);
  /* Name the tab after what is in it. A dozen bookmarks all reading "kls — conjecture
     search" are a dozen bookmarks nobody can tell apart, and a shared link should say
     what it opens before it opens. The heading the page just rendered is the best
     available answer, and there is always one. */
  const heading = page.querySelector('h1');
  const site = (DATA.guide && DATA.guide.site && DATA.guide.site.name)
    || DATA.program.id || 'Conjecture search';
  const named = heading ? heading.textContent.trim() : '';
  document.title = !named || named === site ? site : `${named} — ${site}`;
  for (const link of document.querySelectorAll('.tabs a')) {
    if (link.dataset.tab === tab) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  }
  window.scrollTo(0, 0);
  if (navigated) main.focus();
  /* Every list of rows is taken out of the whole-page pass first and typeset a row at a
     time as it is scrolled to. A view is not allowed to cost a MathJax run over every
     row it holds before it will paint — the claim list holds 138 of them. */
  for (const list of main.querySelectorAll('ul.rows')) deferRows(list);
  typeset(main);
}

function chrome() {
  const program = DATA.program;
  const generated = DATA.generated;
  /* The masthead names the problem, not the repository slug. `kls` is what the ledger
     and every cross-reference call this program and it stays exported; it is not what a
     mathematician arriving at the page is looking for. render() sets document.title per
     page, so nothing is set here. */
  const site = (DATA.guide && DATA.guide.site) || {};
  document.getElementById('brand-name').textContent =
    site.name || program.id || 'Conjecture search';
  document.getElementById('brand-sub').textContent = site.name
    ? (program.id || '')
    : (program.target ? `target: ${program.target}`
      : 'no target yet — uninstantiated template');

  const build = document.getElementById('build-provenance');
  const parts = [];
  parts.push(`built ${generated.built_at} `);
  if (generated.short_commit) {
    const link = repoBase()
      ? `${repoBase()}/commit/${generated.commit}` : null;
    parts.push('from ');
    build.appendChild(document.createTextNode(parts.join('')));
    build.appendChild(link
      ? el('a', { href: link, rel: 'noopener', target: '_blank', text: generated.short_commit })
      : document.createTextNode(generated.short_commit));
    if (generated.branch) build.appendChild(document.createTextNode(` on ${generated.branch}`));
  } else {
    build.appendChild(document.createTextNode(`${parts.join('')} from an unknown revision`));
  }
  if (generated.dirty) {
    build.appendChild(el('span', { class: 'dirty',
      text: ' · built from a dirty working tree, not a committed revision' }));
  }
}

fetch('data.json', { cache: 'no-cache' })
  .then((response) => {
    if (!response.ok) throw new Error(`data.json: ${response.status}`);
    return response.json();
  })
  .then((data) => {
    DATA = data;
    chrome();
    window.addEventListener('hashchange', () => render(true));
    render();
  })
  .catch((error) => {
    document.getElementById('main').appendChild(el('div', {},
      el('h1', { text: 'This site has no data' }),
      el('p', { class: 'lede' },
        'data.json could not be loaded, so nothing is being displayed. Showing an empty '
        + 'or stale page as though it were the current research state would be worse '
        + 'than showing this one.'),
      el('p', { class: 'note', text: String(error) })));
  });
