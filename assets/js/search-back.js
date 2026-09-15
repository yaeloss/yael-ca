(function () {
    const container = document.getElementById('back-to-search');
    if (!container) return;
    let query;
    try { query = sessionStorage.getItem('lastSearchQuery'); } catch (_) { return; }
    if (!query) return;
    const link = document.createElement('a');
    link.className = 'back-to-search-link';
    link.href = '/?q=' + encodeURIComponent(query);
    link.textContent = `← Back to results for “${query}”`;
    container.append(link);
    container.style.display = '';
})();
