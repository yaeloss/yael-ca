// Search is optional: neither the index nor Fuse is downloaded on page load.
(function () {
    const config = document.currentScript.dataset;
    const input = document.getElementById('search-input');
    const button = document.getElementById('search-btn');
    const results = document.getElementById('search-results');
    const recent = document.getElementById('recent-posts');
    if (!input || !button || !results) return;
    let loading;
    let request = 0;

    function remember(query) {
        try {
            if (query) sessionStorage.setItem('lastSearchQuery', query);
            else sessionStorage.removeItem('lastSearchQuery');
        } catch (_) { /* Search still works when browser storage is unavailable. */ }
    }

    function loadFuse() {
        if (window.Fuse) return Promise.resolve();
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = config.fuseUrl;
            script.onload = resolve;
            script.onerror = () => {
                script.remove();
                reject(new Error('Search library unavailable'));
            };
            document.head.append(script);
        });
    }

    function loadSearch() {
        if (!loading) {
            loading = Promise.all([
                loadFuse(),
                fetch(config.indexUrl).then(response => {
                    if (!response.ok) throw new Error('Search index unavailable');
                    return response.json();
                })
            ]).then(([, index]) => new window.Fuse(index, {
                keys: [
                    { name: 'title', weight: 3 },
                    { name: 'tags', weight: 2 },
                    { name: 'categories', weight: 2 },
                    { name: 'summary', weight: 1.5 },
                    { name: 'content', weight: 1 }
                ],
                threshold: 0.4,
                ignoreLocation: true,
                minMatchCharLength: 2
            })).catch(error => {
                loading = null;
                throw error;
            });
        }
        return loading;
    }

    function element(tag, className, text) {
        const node = document.createElement(tag);
        node.className = className;
        if (text !== undefined) node.textContent = text;
        return node;
    }

    function clearButton() {
        const clear = element('button', 'search-clear-btn', '← Back to home');
        clear.id = 'clear-search-btn';
        clear.type = 'button';
        clear.addEventListener('click', () => {
            input.value = '';
            search();
            input.focus();
        });
        return clear;
    }

    async function search() {
        const current = ++request;
        const query = input.value.trim();
        const url = new URL(window.location.href);
        results.replaceChildren();
        remember('');
        if (!query) {
            results.removeAttribute('aria-busy');
            if (recent) recent.style.display = '';
            url.searchParams.delete('q');
            history.replaceState({}, '', url.pathname + url.search + url.hash);
            return;
        }
        url.searchParams.set('q', query);
        history.replaceState({}, '', url.pathname + url.search + url.hash);
        if (recent) recent.style.display = 'none';
        results.setAttribute('aria-busy', 'true');
        results.append(element('p', 'search-no-results', 'Loading search…'));
        try {
            const fuse = await loadSearch();
            // Ignore an older request if the user searched again or cleared it.
            if (current !== request) return;
            const matches = fuse.search(query);
            const header = element('div', 'search-results-header');
            header.append(element('h3', 'posts-item-note', `Results for “${query}” (${matches.length})`), clearButton());
            results.replaceChildren(header);
            if (!matches.length) results.append(element('p', 'search-no-results', 'No results found. Try a different search.'));
            for (const { item } of matches.slice(0, 30)) {
                const row = element('div', 'search-result-item');
                const link = element('a', 'search-result-link', item.title);
                link.href = item.url;
                link.addEventListener('click', () => remember(query));
                row.append(link, element('span', 'search-result-date', item.date));
                results.append(row);
            }
        } catch (_) {
            if (current !== request) return;
            results.replaceChildren(clearButton(), element('p', 'search-no-results', 'Search could not load. Please try again or browse the article archive.'));
            const archive = element('a', '', 'Browse all articles');
            archive.href = '/posts/';
            results.append(archive);
        } finally {
            if (current === request) results.removeAttribute('aria-busy');
        }
    }

    button.addEventListener('click', search);
    input.addEventListener('keydown', event => {
        if (event.key === 'Enter') {
            event.preventDefault();
            search();
        }
    });
    input.addEventListener('focus', () => { loadSearch().catch(() => {}); }, { once: true });
    const query = new URL(window.location.href).searchParams.get('q');
    if (query) {
        input.value = query;
        search();
    } else {
        remember('');
    }
})();
