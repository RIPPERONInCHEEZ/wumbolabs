(() => {
  const catalog = document.querySelector('[data-evaluation-catalog]');
  if (!catalog) return;

  const rows = Array.from(catalog.querySelectorAll('[data-evaluation-row]'));
  const tbody = rows[0]?.parentElement;
  const search = document.getElementById('evaluation-search');
  const sort = document.getElementById('evaluation-sort');
  const pageSize = document.getElementById('evaluation-page-size');
  const status = document.getElementById('evaluation-results');
  const previous = document.getElementById('evaluation-previous');
  const next = document.getElementById('evaluation-next');
  const indicator = document.getElementById('evaluation-page-indicator');
  const noResults = document.getElementById('evaluation-no-results');
  const controls = document.getElementById('evaluation-controls');
  let page = 1;

  const compareText = (left, right) => {
    if (left < right) return -1;
    if (left > right) return 1;
    return 0;
  };
  const compareModel = (left, right) => compareText(left.dataset.model, right.dataset.model);
  const pageSizeValue = () => pageSize.value === 'all' ? Infinity : Number(pageSize.value);
  const matchingRows = () => {
    const query = search.value.trim().toLowerCase();
    return rows.filter((row) => row.dataset.search.includes(query));
  };
  const sortedRows = (matching) => matching.sort((left, right) => {
    if (sort.value === 'model') return compareModel(left, right);
    if (sort.value === 'producer') {
      return compareText(left.dataset.producer, right.dataset.producer) || compareModel(left, right);
    }

    const leftDate = left.dataset.latestEvidence;
    const rightDate = right.dataset.latestEvidence;
    if (!leftDate || !rightDate) {
      if (leftDate) return -1;
      if (rightDate) return 1;
      return compareModel(left, right);
    }
    const dateOrder = compareText(leftDate, rightDate);
    return (sort.value === 'oldest' ? dateOrder : -dateOrder) || compareModel(left, right);
  });

  const render = () => {
    const matching = sortedRows(matchingRows());
    const size = pageSizeValue();
    const pages = Math.max(1, Math.ceil(matching.length / size));
    const first = size === Infinity ? 0 : (page - 1) * size;
    const visible = new Set(matching.slice(first, first + size));

    if (tbody) tbody.append(...matching);
    rows.forEach((row) => { row.hidden = !visible.has(row); });
    const activeControl = document.activeElement;
    previous.disabled = page === 1;
    next.disabled = page === pages;
    if (next.disabled && activeControl === next && !previous.disabled) previous.focus();
    if (previous.disabled && activeControl === previous && !next.disabled) next.focus();
    indicator.textContent = `Page ${page} of ${pages}`;

    if (!matching.length) {
      status.textContent = 'No evaluations match this search.';
      noResults.hidden = false;
    } else if (size === Infinity) {
      noResults.hidden = true;
      status.textContent = `Showing all ${matching.length} evaluation${matching.length === 1 ? '' : 's'}.`;
    } else {
      noResults.hidden = true;
      const last = Math.min(first + size, matching.length);
      status.textContent = `Showing ${first + 1}–${last} of ${matching.length} evaluation${matching.length === 1 ? '' : 's'}.`;
    }
  };

  search.addEventListener('input', () => { page = 1; render(); });
  sort.addEventListener('change', () => { page = 1; render(); });
  pageSize.addEventListener('change', () => { page = 1; render(); });
  previous.addEventListener('click', () => { page -= 1; render(); });
  next.addEventListener('click', () => { page += 1; render(); });

  controls.hidden = false;
  render();
})();
