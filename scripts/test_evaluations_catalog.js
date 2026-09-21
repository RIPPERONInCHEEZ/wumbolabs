#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const models = JSON.parse(fs.readFileSync(path.join(root, 'data/generated/labs-models.json'))).models;
const registry = JSON.parse(fs.readFileSync(path.join(root, 'data/labs-registry.json')));
const producers = new Map(registry.models.map((model) => [model.model_id, model.vendor.toLowerCase()]));

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

const rows = models.map((model) => ({
  dataset: {
    model: model.display_name.toLowerCase(),
    producer: producers.get(model.model_id),
    latestEvidence: model.latest_evidence_date || '',
    search: `${model.display_name} ${model.model_id} ${producers.get(model.model_id)}`.toLowerCase(),
  },
  hidden: false,
}));
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

assert(rows.every((row) => !row.hidden), 'static rows must be visible before enhancement');
assert.deepEqual(rows.map((row) => row.dataset.model), newest.map((model) => model.display_name.toLowerCase()),
  'static rows must begin newest-first');
require(path.join(root, 'static/js/evaluations-catalog.js'));

assert.equal(controls['evaluation-controls'].hidden, false);
assert.equal(visible().length, 10);
assert.equal(visibleModels()[0], newest[0].display_name.toLowerCase());
assert.equal(controls['evaluation-results'].textContent, `Showing 1–10 of ${models.length} evaluations.`);
assert.equal(controls['evaluation-previous'].disabled, true);
assert.equal(controls['evaluation-next'].disabled, false);

controls['evaluation-next'].dispatch('click');
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 2 of 3');
controls['evaluation-previous'].dispatch('click');
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 1 of 3');
controls['evaluation-next'].dispatch('click');
controls['evaluation-next'].dispatch('click');
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 3 of 3');
assert.equal(controls['evaluation-next'].disabled, true);
controls['evaluation-previous'].dispatch('click');
controls['evaluation-previous'].dispatch('click');
assert.equal(controls['evaluation-previous'].disabled, true);

search('mellum2');
assert.deepEqual(visibleModels(), ['mellum2 12b-a2.5b']);
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 1 of 1');
search('google');
assert.equal(visible().length, 2, 'producer search must match both Google models');
search('does-not-exist');
assert.equal(visible().length, 0);
assert.equal(controls['evaluation-results'].textContent, 'No evaluations match this search.');
search('');
assert.equal(visible().length, 10);

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

search('qwen');
change('evaluation-sort', 'oldest');
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 1 of 1');
change('evaluation-sort', 'model');
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 1 of 1');
search('');
change('evaluation-page-size', '25');
assert.equal(visible().length, models.length);
assert.equal(controls['evaluation-page-indicator'].textContent, 'Page 1 of 1');
change('evaluation-page-size', '50');
assert.equal(visible().length, models.length);
change('evaluation-page-size', 'all');
assert.equal(visible().length, models.length);
assert.equal(controls['evaluation-results'].textContent, `Showing all ${models.length} evaluations.`);

console.log(`PASS: evaluations catalog interaction matrix (${models.length} models)`);
