(() => {
  const catalog = document.querySelector('[data-evaluation-catalog]');
  if (!catalog) return;

  const rows = Array.from(catalog.querySelectorAll('[data-evaluation-row]'));
  const search = document.getElementById('evaluation-search');
  const pageSize = document.getElementById('evaluation-page-size');
  const status = document.getElementById('evaluation-results');
  const previous = document.getElementById('evaluation-previous');
  const next = document.getElementById('evaluation-next');
  const indicator = document.getElementById('evaluation-page-indicator');
  const noResults = document.getElementById('evaluation-no-results');
  const controls = document.getElementById('evaluation-controls');
  let page = 1;

  const pageSizeValue = () => pageSize.value === 'all' ? Infinity : Number(pageSize.value);
  const matchingRows = () => {
    const query = search.value.trim().toLocaleLowerCase();
    return rows.filter((row) => row.dataset.search.includes(query));
  };

  const render = () => {
    const matching = matchingRows();
    const size = pageSizeValue();
    const pages = Math.max(1, Math.ceil(matching.length / size));
    const first = size === Infinity ? 0 : (page - 1) * size;
    const visible = new Set(matching.slice(first, first + size));

    rows.forEach((row) => { row.hidden = !visible.has(row); });
    previous.disabled = page === 1;
    next.disabled = page === pages;
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
  pageSize.addEventListener('change', () => { page = 1; render(); });
  previous.addEventListener('click', () => { page -= 1; render(); });
  next.addEventListener('click', () => { page += 1; render(); });

  controls.hidden = false;
  render();
})();
