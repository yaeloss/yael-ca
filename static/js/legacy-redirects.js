// Handle unenumerated WordPress pagination only when the destination exists.
// Known old URLs receive static redirect pages during the production build.
(async function () {
    const path = window.location.pathname;
    const archive = path.match(/^\/(tag|category|tags|categories)\/([^/]+)(?:\/page\/[1-9]\d*)?\/?$/);
    const post = path.match(/^\/(?:\d{4}\/\d{2}\/\d{2}\/)?([^/]+)\/?$/);
    const page = /^\/page\/[1-9]\d*\/?$/.test(path);
    if (!archive && !post && !page) return;
    try {
        const response = await fetch('/legacy-redirects.json');
        if (!response.ok) return;
        const manifest = await response.json();
        let target;
        if (archive) {
            const taxonomy = ['category', 'categories'].includes(archive[1]) ? 'categories' : 'tags';
            let slug = decodeURIComponent(archive[2]);
            if (taxonomy === 'tags' && Object.hasOwn(manifest.tagMerges, slug)) {
                slug = manifest.tagMerges[slug];
            }
            const old = `/${taxonomy}/${slug}/`;
            const candidate = Object.hasOwn(manifest.archiveMoves || {}, old) ? manifest.archiveMoves[old] : old;
            target = manifest.terms.find(term => decodeURI(term.url) === candidate)?.url;
        } else if (page) {
            target = '/posts/';
        } else if (post) {
            const candidate = `/posts/${decodeURIComponent(post[1])}/`;
            target = manifest.posts.find(entry => decodeURI(entry.url) === candidate)?.url;
        }
        if (target && target !== path) {
            window.location.replace(target + window.location.search + window.location.hash);
        }
    } catch (_) {
        // Keep the usable 404 and search interface if the manifest cannot load.
    }
})();
