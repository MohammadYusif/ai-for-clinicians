/* Contrast audit for the rendered site (a developer tool, not part of the published pages).
 *
 * Why it exists: the palette was checked pair by pair on paper, and the first real audit of the
 * rendered page still found Bootstrap's gray-600 (#6c757d) on the dark breadcrumb bar at 2.85:1.
 * Paper ratios are not enough; measure the rendered result, in both colour schemes.
 *
 * Use, with the site served (for example `quarto preview`) and the page open:
 *   1. Paste this file into the browser console (or load it with a <script> tag).
 *   2. window.__auditIn(window)             audit the current page
 *      await window.__auditSite(urls)       audit many same-origin pages in hidden iframes
 * Flip the colour scheme (DevTools > Rendering > prefers-color-scheme) and run it again.
 *
 * A failure is any visible text below WCAG AA: 4.5:1, or 3:1 for large text (24px, or 18.66px bold).
 * Backgrounds are resolved by compositing every translucent ancestor onto the page colour.
 */
(function () {
  const parse = (c) => {
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map((s) => parseFloat(s));
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const lum = ({ r, g, b }) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const blend = (fg, bg) => ({
    r: fg.r * fg.a + bg.r * (1 - fg.a),
    g: fg.g * fg.a + bg.g * (1 - fg.a),
    b: fg.b * fg.a + bg.b * (1 - fg.a),
    a: 1,
  });

  window.__auditIn = function (win) {
    const doc = win.document;
    const bgOf = (el) => {
      const stack = [];
      for (let e = el; e; e = e.parentElement) {
        const c = parse(win.getComputedStyle(e).backgroundColor);
        if (c && c.a > 0) { stack.push(c); if (c.a >= 1) break; }
      }
      let base = { r: 255, g: 255, b: 255, a: 1 };
      const root = parse(win.getComputedStyle(doc.body).backgroundColor);
      if (root && root.a > 0) base = root;
      for (let i = stack.length - 1; i >= 0; i--) base = blend(stack[i], base);
      return base;
    };
    const seen = new Map();
    const walker = doc.createTreeWalker(doc.body, NodeFilter.SHOW_TEXT);
    let node, total = 0;
    while ((node = walker.nextNode())) {
      const text = node.textContent.trim();
      if (!text) continue;
      const el = node.parentElement;
      if (!el || ['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(el.tagName)) continue;
      // Text inside an SVG sits on the shape's fill, which is not a CSS background, so this audit
      // would misread it against the page. Mermaid nodes carry explicit fills and text colours
      // (checked by hand in both schemes); only their arrow lines are themed per scheme.
      if (el.closest('svg')) continue;
      const cs = win.getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none') continue;
      const box = el.getBoundingClientRect();
      if (box.width === 0 || box.height === 0) continue;
      let fg = parse(cs.color);
      if (!fg) continue;
      const bg = bgOf(el);
      fg = blend({ ...fg, a: fg.a * parseFloat(cs.opacity || 1) }, bg);
      total++;
      const l1 = lum(fg), l2 = lum(bg);
      const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
      const size = parseFloat(cs.fontSize);
      const bold = parseInt(cs.fontWeight, 10) >= 700;
      const need = size >= 24 || (size >= 18.66 && bold) ? 3 : 4.5;
      if (ratio < need) {
        const key = cs.color + '|' + el.tagName + '.' + String(el.className).split(' ')[0];
        if (!seen.has(key)) {
          seen.set(key, {
            ratio: +ratio.toFixed(2), need, fg: cs.color,
            bg: `rgb(${Math.round(bg.r)},${Math.round(bg.g)},${Math.round(bg.b)})`,
            el: el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).trim().split(/\s+/).join('.') : ''),
            sample: text.slice(0, 40),
          });
        }
      }
    }
    return {
      page: win.location.pathname,
      scheme: win.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light',
      textNodes: total,
      overflowX: doc.documentElement.scrollWidth > doc.documentElement.clientWidth,
      failures: [...seen.values()],
    };
  };

  // Audit many same-origin pages in hidden, laid-out iframes (one call per colour scheme).
  window.__auditSite = async function (urls, width = 1280, height = 900, settleMs = 900) {
    const results = [];
    for (const url of urls) {
      const frame = document.createElement('iframe');
      frame.style.cssText = `position:fixed;left:-30000px;top:0;width:${width}px;height:${height}px;border:0`;
      document.body.appendChild(frame);
      await new Promise((resolve) => { frame.onload = resolve; frame.src = url; });
      await new Promise((r) => setTimeout(r, settleMs));
      try { results.push(window.__auditIn(frame.contentWindow)); }
      catch (e) { results.push({ page: url, error: String(e) }); }
      frame.remove();
    }
    return results;
  };
})();
