(() => {
  const existing = document.getElementById('codex-issue-pdf');
  if (existing) throw new Error('Export view already exists; use a fresh task-owned tab.');
  const title = document.querySelector('h1 bdi') || document.querySelector('h1 .markdown-title');
  const body = document.querySelector('[data-testid="issue-body-viewer"]');
  const timeline = document.querySelector('[data-testid="issue-timeline-container"]');
  if (!title || !body) throw new Error('GitHub markup differs; inspect current content selectors before exporting.');
  const comments = timeline ? Array.from(timeline.querySelectorAll('[data-testid^="comment-viewer-outer-box-"]')) : [];
  const sourceImages = [body, ...comments].flatMap(el => Array.from(el.querySelectorAll('img')))
    .filter(img => !img.closest('[data-testid="comment-header"]'));
  const issueTitle = title.textContent.trim();
  const root = document.createElement('main');
  root.id = 'codex-issue-pdf';
  const h1 = document.createElement('h1');
  h1.textContent = issueTitle;
  root.append(h1);
  const source = document.createElement('p');
  const sourceLink = document.createElement('a');
  sourceLink.href = location.origin + location.pathname;
  sourceLink.textContent = sourceLink.href;
  source.append(sourceLink);
  root.append(source);
  root.append(body.cloneNode(true));
  if (comments.length) {
    const heading = document.createElement('h2');
    heading.textContent = 'Activity';
    root.append(heading);
    for (const comment of comments) root.append(comment.cloneNode(true));
  }
  // Controls and account/navigation chrome have no role in the exported issue.
  root.querySelectorAll('button,[role="toolbar"],form').forEach(el => el.remove());
  // Open details containing distinct proof so hidden state cannot drop images.
  root.querySelectorAll('details').forEach(el => { if (el.querySelector('img')) el.open = true; });
  root.querySelectorAll('img').forEach(img => { img.loading = 'eager'; });
  const repeated = [];
  const seen = new Set();
  for (const img of root.querySelectorAll('img')) {
    if (img.closest('[data-testid="comment-header"]')) continue;
    const key = img.getAttribute('data-canonical-src') || img.getAttribute('src');
    if (!key) continue;
    if (seen.has(key)) {
      repeated.push(img.alt || '(unlabelled duplicate)');
      const link = document.createElement('a');
      link.href = img.closest('a')?.href || img.src;
      link.textContent = img.alt || 'Previously shown proof';
      img.replaceWith(link);
    } else seen.add(key);
  }
  // Images are embedded by the PDF renderer. Do not distribute expiring
  // private-image access tokens as clickable PDF annotation targets.
  root.querySelectorAll('a[href]').forEach(link => {
    const url = new URL(link.href, location.href);
    if (url.hostname === 'private-user-images.githubusercontent.com' && url.search) link.removeAttribute('href');
  });
  const style = document.createElement('style');
  style.id = 'codex-issue-pdf-style';
  style.textContent = `
    html { width:210mm!important; min-width:0!important; background:#fff!important; color-scheme:light!important; }
    body { width:210mm!important; min-width:0!important; margin:0!important; padding:0!important; background:#fff!important; }
    body > :not(#codex-issue-pdf) { display:none!important; }
    #codex-issue-pdf { display:block!important; box-sizing:border-box!important; width:210mm!important; max-width:210mm!important; padding:8mm!important; margin:0!important; background:#fff!important; color:#1f2328!important; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }
    #codex-issue-pdf *, #codex-issue-pdf *::before, #codex-issue-pdf *::after { box-sizing:border-box!important; min-width:0!important; break-before:auto!important; break-after:auto!important; page-break-before:auto!important; page-break-after:auto!important; }
    #codex-issue-pdf h1 { font-size:26px!important; line-height:1.25!important; margin:0 0 16px!important; overflow-wrap:anywhere!important; }
    #codex-issue-pdf .markdown-body, #codex-issue-pdf [data-testid="issue-body-viewer"] { width:100%!important; max-width:100%!important; margin-left:0!important; margin-right:0!important; background:transparent!important; }
    #codex-issue-pdf [data-testid^="comment-viewer-outer-box-"] { width:100%!important; max-width:100%!important; margin:16px 0!important; }
    #codex-issue-pdf img { max-width:100%!important; height:auto!important; object-fit:contain!important; }
    #codex-issue-pdf p, #codex-issue-pdf li, #codex-issue-pdf a { overflow-wrap:anywhere!important; }
    #codex-issue-pdf pre { white-space:pre-wrap!important; overflow-wrap:anywhere!important; overflow:visible!important; }
    #codex-issue-pdf table { max-width:100%!important; width:auto!important; table-layout:auto!important; }
    #codex-issue-pdf svg { max-width:100%!important; }
    @page { margin:0; }
  `;
  document.documentElement.setAttribute('data-color-mode', 'light');
  document.documentElement.setAttribute('data-light-theme', 'light');
  document.head.append(style);
  document.body.append(root);
  return {
    title: issueTitle,
    comments: comments.length,
    sourceProofImages: sourceImages.length,
    uniqueProofImages: seen.size,
    duplicateOccurrences: repeated.length,
    widthCssPx: root.getBoundingClientRect().width,
    heightCssPx: root.getBoundingClientRect().height,
    pendingImages: Array.from(root.querySelectorAll('img')).filter(img => !img.complete || !img.naturalWidth).map(img => img.alt),
  };
})()
