#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const models = JSON.parse(fs.readFileSync(path.join(root, 'data/generated/labs-models.json'))).models;

// The static catalog renders each Evaluation page's front matter verbatim, so this
// harness parses those pages instead of assuming what the template exposes.
const evaluationsDir = path.join(root, 'content/evaluations');
const frontMatter = (file) => {
  const block = fs.readFileSync(file, 'utf8').match(/^\+\+\+\n([\s\S]*?)\n\+\+\+/);
  assert(block, `${file}: missing +++ front matter block`);
  const fields = {};
  for (const line of block[1].split('\n')) {
    const pair = line.match(/^([A-Za-z0-9_]+) = (.*)$/);
    if (pair) {
      const value = pair[2].trim();
      fields[pair[1]] = /^".*"$/s.test(value) ? value.slice(1, -1) : value;
    }
  }
  return fields;
};
const catalogPages = fs.readdirSync(evaluationsDir)
  .filter((file) => file.endsWith('.md') && file !== '_index.md')
  .map((file) => frontMatter(path.join(evaluationsDir, file)))
  .filter((page) => page.model_id && page.redirect_page !== 'true');
const pageById = new Map(catalogPages.map((page) => [page.model_id, page]));

assert.equal(catalogPages.length, models.length, 'catalog pages must map 1:1 onto generated models');
assert.deepEqual(
  [...catalogPages]
    .sort((left, right) => Number(left.weight) - Number(right.weight))
    .map((page) => page.model_id),
  models.map((model) => model.model_id),
  'Zola weight order (static row order) must stay newest evidence first');

for (const model of models) {
  const page = pageById.get(model.model_id);
  assert.equal(page.latest_evidence_date || '', model.latest_evidence_date || '',
    `${model.model_id}: front matter latest_evidence_date must match the generated dataset`);
}

// Mirrors the template's data-search corpus: model, identifier, producer,
// recommended profile (artifact), practical context. Classification, status
// text and placeholder advertisement are deliberately absent so catalog rows
// expose no status discovery metadata.
const searchable = (page) =>
  `${page.title} ${page.model_id} ${page.vendor} `
  + `${page.recommended_profile_name || 'No recommended profile recorded'} `
  + `${page.practical_context || 'Not recorded'}`;

class Control {
  constructor(value = '') {
    this.value = value;
    this.hidden = false;
    this.disabled = false;
    this.textContent = '';
    this.listeners = new Map();
  }

  addEventListener(type, listener) {
    this.listeners.set(type, listener);
  }

  dispatch(type) {
    this.listeners.get(type)();
  }

  focus() {
    document.activeElement = this;
  }
}

class Body {
  constructor(children) {
    this.children = children;
  }

  append(...rows) {
    for (const row of rows) {
      this.children.splice(this.children.indexOf(row), 1);
      this.children.push(row);
    }
  }
}

const rows = models.map((model) => {
  const page = pageById.get(model.model_id);
  return {
    dataset: {
      model: page.title.toLowerCase(),
      producer: page.vendor.toLowerCase(),
      latestEvidence: page.latest_evidence_date || '',
      search: searchable(page).toLowerCase(),
    },
    hidden: false,
  };
});
const body = new Body(rows);
for (const row of rows) row.parentElement = body;
const controls = {
  'evaluation-search': new Control(),
  'evaluation-sort': new Control('newest'),
  'evaluation-page-size': new Control('10'),
  'evaluation-results': new Control(),
  'evaluation-previous': new Control(),
  'evaluation-next': new Control(),
  'evaluation-page-indicator': new Control(),
  'evaluation-no-results': new Control(),
  'evaluation-controls': new Control(),
};
controls['evaluation-controls'].hidden = true;
const catalog = { querySelectorAll: () => rows };
global.document = {
  activeElement: null,
  querySelector: (selector) => selector === '[data-evaluation-catalog]' ? catalog : null,
  getElementById: (id) => controls[id],
};

const newest = [...models].sort((left, right) =>
  right.latest_evidence_date.localeCompare(left.latest_evidence_date)
  || left.display_name.toLowerCase().localeCompare(right.display_name.toLowerCase()));
const oldest = [...models].sort((left, right) =>
  left.latest_evidence_date.localeCompare(right.latest_evidence_date)
  || left.display_name.toLowerCase().localeCompare(right.display_name.toLowerCase()));
const newestOrder = newest.map((model) => model.display_name.toLowerCase());
const visible = () => body.children.filter((row) => !row.hidden);
const visibleModels = () => visible().map((row) => row.dataset.model);
const change = (id, value) => {
  controls[id].value = value;
  controls[id].dispatch('change');
};
const search = (value) => {
  controls['evaluation-search'].value = value;
  controls['evaluation-search'].dispatch('input');
};

// Expected search results derive from the real front-matter corpus: a probe
// matches every page whose data-search corpus contains it, never a pinned
// registry count. Assertions follow the active page size and sort instead of
// assuming them.
let pageSize = '10';
const changeSize = (value) => {
  change('evaluation-page-size', value);
  pageSize = value;
};
const corpus = (page) => searchable(page).toLowerCase();
const matchPages = (probe) => catalogPages.filter((page) => corpus(page).includes(probe));
const titles = (pages) => pages.map((page) => page.title.toLowerCase());
const singular = (count) => (count === 1 ? 'evaluation' : 'evaluations');
const shownLine = (total) => {
  if (pageSize === 'all') return `Showing all ${total} ${singular(total)}.`;
  const shown = Math.min(Number(pageSize), total);
  return `Showing 1–${shown} of ${total} ${singular(total)}.`;
};

const expectSearch = (probe, message) => {
  const expected = matchPages(probe);
  assert(expected.length > 0,
    `corpus probe ${JSON.stringify(probe)} must match at least one catalog page (${message})`);
  search(probe);
  const ordered = newestOrder.filter((title) => titles(expected).includes(title));
  const shown = pageSize === 'all' ? ordered : ordered.slice(0, Number(pageSize));
  assert.deepEqual(visibleModels(), shown, message);
  assert.equal(visible().length, shown.length, message);
  assert.equal(controls['evaluation-results'].textContent, shownLine(expected.length),
    `search results must report the matched subset (${message})`);
  return expected;
};

// Guard: catalog rows must not expose classification/status discovery metadata,
// even though the underlying generated classification data is retained.
const classifications = models
  .map((model) => model.classification)
  .filter((classification) => typeof classification === 'string');
assert(classifications.length > 0, 'generated classification data must exist for the status guard to be meaningful');
const statusTexts = [...classifications.map((c) => c.toLowerCase()), 'evidence in progress'];
for (const row of rows) {
  assert.deepEqual(Object.keys(row.dataset).sort(), ['latestEvidence', 'model', 'producer', 'search'],
    'catalog rows must carry no classification/status discovery metadata');
  for (const statusText of statusTexts) {
    assert(!row.dataset.search.includes(statusText),
      `status discovery leak: ${statusText} is searchable from catalog rows`);
  }
}

assert(rows.every((row) => !row.hidden), 'static rows must be visible before enhancement');
assert.deepEqual(rows.map((row) => row.dataset.model), newestOrder,
  'static rows must begin newest-first');
require(path.join(root, 'static/js/evaluations-catalog.js'));

assert.equal(controls['evaluation-controls'].hidden, false);

// Status discovery must stay impossible through search after enhancement too.
for (const statusText of statusTexts) {
  search(statusText);
  assert.equal(visible().length, 0,
    `status classification text must not be discoverable through search: ${statusText}`);
}
assert.equal(controls['evaluation-results'].textContent, 'No evaluations match this search.');
search('');

// Static pagination derives every boundary from the corpus size.
const perPage = 10;
const pageCount = Math.max(1, Math.ceil(models.length / perPage));
assert.equal(visible().length, Math.min(perPage, models.length));
assert.equal(visibleModels()[0], newest[0].display_name.toLowerCase());
assert.equal(controls['evaluation-results'].textContent,
  `Showing 1–${Math.min(perPage, models.length)} of ${models.length} ${singular(models.length)}.`);
assert.equal(controls['evaluation-previous'].disabled, true);
assert.equal(controls['evaluation-next'].disabled, pageCount === 1);
for (let target = 2; target <= pageCount; target += 1) {
  controls['evaluation-next'].dispatch('click');
  assert.equal(controls['evaluation-page-indicator'].textContent, `Page ${target} of ${pageCount}`);
  const expectedCount = Math.min(perPage, models.length - (target - 1) * perPage);
  assert.equal(visible().length, expectedCount, 'each page must show its remaining rows');
  assert.deepEqual(visibleModels(), newestOrder.slice((target - 1) * perPage, target * perPage),
    'pagination must continue the newest-first order without omissions or duplicates');
}
assert.equal(controls['evaluation-next'].disabled, true, 'last page must disable Next');
for (let target = pageCount - 1; target >= 1; target -= 1) {
  controls['evaluation-previous'].dispatch('click');
  assert.equal(controls['evaluation-page-indicator'].textContent, `Page ${target} of ${pageCount}`);
}
assert.equal(controls['evaluation-previous'].disabled, true, 'first page must disable Previous');

// Search probes picked from the corpus itself.
const vendorCounts = new Map();
for (const page of catalogPages) {
  vendorCounts.set(page.vendor, (vendorCounts.get(page.vendor) || 0) + 1);
}
const [producerName, producerCount] = [...vendorCounts.entries()]
  .sort((left, right) => right[1] - left[1] || left[0].localeCompare(right[0]))[0];
assert(producerCount >= 2, 'the corpus must contain a producer with two or more models');
expectSearch(producerName.toLowerCase(),
  'producer search must match every model of that producer');

const probeModel = [...catalogPages].sort((left, right) => left.model_id.localeCompare(right.model_id))[0];
const modelExpected = expectSearch(probeModel.model_id.toLowerCase(),
  'model identifier search must find its own model page');
assert(modelExpected.some((page) => page.model_id === probeModel.model_id),
  'identifier search result must include the probed model');

const withoutProfile = titles(catalogPages.filter((page) => !page.recommended_profile_name)).sort();
assert.deepEqual(titles(matchPages('no recommended profile')).sort(), withoutProfile,
  'profile fallback text must be searchable exactly for models without a recommended profile');
const withoutContext = titles(catalogPages.filter((page) => !page.practical_context)).sort();
assert.deepEqual(titles(matchPages('not recorded')).sort(), withoutContext,
  'context fallback text must be searchable exactly for models without recorded context');

search('does-not-exist');
assert.equal(visible().length, 0);
assert.equal(controls['evaluation-results'].textContent, 'No evaluations match this search.');
search('');
assert.equal(visible().length, Math.min(perPage, models.length));

change('evaluation-sort', 'oldest');
assert.equal(visibleModels()[0], oldest[0].display_name.toLowerCase());
change('evaluation-sort', 'model');
assert.deepEqual(visibleModels(), [...visibleModels()].sort());
change('evaluation-sort', 'producer');
assert.deepEqual(visibleModels(), [...visibleModels()].sort((left, right) => {
  const leftRow = rows.find((row) => row.dataset.model === left);
  const rightRow = rows.find((row) => row.dataset.model === right);
  return leftRow.dataset.producer.localeCompare(rightRow.dataset.producer)
    || left.localeCompare(right);
}));

// Sorting while filtered must reset pagination to the first page.
search(producerName.toLowerCase());
const producerPages = Math.max(1, Math.ceil(producerCount / perPage));
assert.equal(controls['evaluation-page-indicator'].textContent, `Page 1 of ${producerPages}`);
if (producerPages > 1) {
  controls['evaluation-next'].dispatch('click');
  assert.equal(controls['evaluation-page-indicator'].textContent, `Page 2 of ${producerPages}`);
}
change('evaluation-sort', 'model');
assert.equal(controls['evaluation-page-indicator'].textContent, `Page 1 of ${producerPages}`,
  'changing sort must reset filtered pagination to the first page');
const producerSorted = matchPages(producerName.toLowerCase())
  .map((page) => page.title)
  .sort((left, right) => left.toLowerCase().localeCompare(right.toLowerCase()))
  .map((title) => title.toLowerCase());
assert.deepEqual(visibleModels(), producerSorted.slice(0, perPage),
  'model sort must order the filtered subset by model name');
change('evaluation-sort', 'newest');
search('');

// Page-size sweeps run under Model A–Z so every slice is deterministic.
change('evaluation-sort', 'model');
changeSize('25');
const alphabetical = models.map((model) => model.display_name.toLowerCase()).sort();
for (let first = 0; first < models.length; first += 25) {
  assert.deepEqual(visibleModels(), alphabetical.slice(first, first + 25),
    'page-size 25 must preserve sorted model coverage without omissions or duplicates');
  assert.equal(controls['evaluation-previous'].disabled, first === 0);
  assert.equal(controls['evaluation-next'].disabled, first + 25 >= models.length);
  if (first + 25 < models.length) controls['evaluation-next'].dispatch('click');
}
changeSize('50');
assert.deepEqual(visibleModels(), alphabetical.slice(0, 50),
  'changing page size must reset pagination to the first page');
changeSize('all');
assert.equal(visible().length, models.length);
assert.equal(controls['evaluation-results'].textContent, `Showing all ${models.length} ${singular(models.length)}.`);

// Token probes run under the default newest sort.
change('evaluation-sort', 'newest');
search('');

// Artifact (recommended profile) and practical-context tokens picked from the
// corpus: whatever subset they match must stay searchable.
const frequentToken = (source, minimum) => {
  const counts = new Map();
  for (const page of catalogPages) {
    const value = source(page);
    if (!value) continue;
    for (const token of new Set(value.toLowerCase().split(/\s+/))) {
      if (token.length < 5 || /^\d+(?:[.,]\d+)*$/.test(token)) continue;
      counts.set(token, (counts.get(token) || 0) + 1);
    }
  }
  return [...counts.entries()]
    .map(([token]) => [token, matchPages(token).length])
    .filter(([, matched]) => matched >= minimum)
    .sort((left, right) => right[1] - left[1] || left[0].localeCompare(right[0]))[0];
};
const artifactToken = frequentToken((page) => page.recommended_profile_name, 2);
assert(artifactToken, 'the corpus must contain a repeated recommended-profile token');
expectSearch(artifactToken[0], 'recommended profile (artifact) search must stay available');
const contextToken = frequentToken((page) => page.practical_context, 1);
assert(contextToken, 'the corpus must contain a practical-context token');
expectSearch(contextToken[0], 'practical context search must stay available');
search('');

console.log(`PASS: evaluations catalog interaction matrix (${models.length} models)`);
