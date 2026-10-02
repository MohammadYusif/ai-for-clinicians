/* Layout and contrast audit for one rendered deck. Run it in the browser console (or through the
   Browser pane's javascript tool) on a deck page such as _site/slides/m1-rule-and-mechanics.html:

     paste this file, then:  await deckAudit()

   It steps through every slide with all fragments shown, and reports:
     - overflow:  content that runs past the slide's 1050 x 700 box (it would be cut off or scroll);
     - nested:    a <section> inside a slide, which reveal.js turns into a vertical stack. This is what
                  happens when a heading is written inside a ::: div (use a .t paragraph instead);
     - contrast:  text under 4.5:1 (3:1 for large text) against the ground it sits on;
     - notes:     speaker notes over 900 characters (1,600 on a topic slide), or none at all.

   Like tools/contrast_audit.js, this measures what rendered, not what the source says. The result is
   [] when the deck is clean. A dark slide's gradient is judged by its first colour stop. */
async function deckAudit() {
  const R = window.Reveal;
  if (!R) return ["not a reveal.js deck"];
  const out = [];
  const cfg = R.getConfig();
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const lum = (r, g, b) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const parse = (s) => {
    const m = /rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/.exec(s || "");
    return m ? [+m[1], +m[2], +m[3], m[4] === undefined ? 1 : +m[4]] : null;
  };
  const hex = (s) => {
    const m = /#([0-9a-f]{6})/i.exec(s || "");
    return m ? [parseInt(m[1].slice(0, 2), 16), parseInt(m[1].slice(2, 4), 16), parseInt(m[1].slice(4, 6), 16), 1] : null;
  };
  const ratio = (a, b) => {
    const x = lum(a[0], a[1], a[2]), y = lum(b[0], b[1], b[2]);
    return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
  };
  const groundOf = (el, slide) => {
    for (let e = el; e && e !== document.body; e = e.parentElement) {
      const c = parse(getComputedStyle(e).backgroundColor);
      if (c && c[3] > 0.5) return c;
      if (e === slide) break;
    }
    const attr = slide.getAttribute("data-background-gradient") || slide.getAttribute("data-background-color");
    return hex(attr) || parse(attr) || [255, 255, 255, 1];
  };

  const leaves = [...document.querySelectorAll(".reveal .slides section")].filter((s) => !s.querySelector("section") && !s.closest("aside"));
  // A slide that holds a <section> that is not a topic stack is a heading written inside a div.
  [...document.querySelectorAll(".reveal .slides section")].forEach((s) => {
    if (s.closest("aside")) return;
    const inner = [...s.children].filter((c) => c.tagName === "SECTION");
    if (inner.length && !s.classList.contains("stack") && !s.matches(".slides > section")) out.push(`nested: <section id="${inner[0].id}"> inside a slide`);
  });

  for (const slide of leaves) {
    const ix = R.getIndices(slide);
    R.slide(ix.h, ix.v || 0, 99);
    await sleep(60);
    const scale = R.getScale() || 1;
    const box = slide.getBoundingClientRect();
    const name = slide.id || slide.querySelector("h1,h2")?.textContent?.trim() || "(untitled)";
    let bottom = 0, right = 0, lowest = null, widest = null;
    for (const el of slide.querySelectorAll("*")) {
      if (el.closest("aside")) continue;
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      if ((r.bottom - box.top) / scale > bottom) { bottom = (r.bottom - box.top) / scale; lowest = el; }
      if ((r.right - box.left) / scale > right) { right = (r.right - box.left) / scale; widest = el; }
    }
    const isTopic = slide.classList.contains("level1");
    const isCover = slide.classList.contains("quarto-title-block");
    const who = (el) => el ? `<${el.tagName.toLowerCase()}${el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).join(".") : ""}> "${(el.textContent || "").trim().slice(0, 30)}"` : "";
    if (bottom > cfg.height + 2) out.push(`overflow: ${name} runs ${Math.round(bottom - cfg.height)}px below the slide, at ${who(lowest)}`);
    if (right > cfg.width + 2) out.push(`overflow: ${name} runs ${Math.round(right - cfg.width)}px past the right edge, at ${who(widest)}`);

    const notes = slide.querySelector("aside.notes");
    // Quarto puts a <style> for assistive math inside each notes block; it is not the trainer's text.
    const copy = notes ? notes.cloneNode(true) : null;
    if (copy) copy.querySelectorAll("style, script").forEach((e) => e.remove());
    const text = copy ? copy.textContent.replace(/\s+/g, " ").trim() : "";
    if (!text && !isCover) out.push(`notes: ${name} has no speaker notes`);
    if (text.length > (isTopic || isCover ? 1600 : 900)) out.push(`notes: ${name} has ${text.length} characters of notes`);

    const walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
    const seen = new Set();
    for (let node = walker.nextNode(); node; node = walker.nextNode()) {
      const el = node.parentElement;
      if (!node.textContent.trim() || el.closest("aside") || seen.has(el)) continue;
      seen.add(el);
      const cs = getComputedStyle(el);
      if (cs.visibility === "hidden" || cs.display === "none" || parseFloat(cs.opacity) < 0.05) continue;
      const fg = parse(cs.color);
      if (!fg) continue;
      const bg = groundOf(el, slide);
      const px = parseFloat(cs.fontSize) / scale;
      const large = px >= 24 || (px >= 18.66 && parseInt(cs.fontWeight, 10) >= 700);
      const need = large ? 3 : 4.5;
      const got = ratio(fg, bg);
      if (got < need) out.push(`contrast: ${name}: "${node.textContent.trim().slice(0, 40)}" is ${got.toFixed(2)}:1 (needs ${need}:1)`);
    }
  }
  R.slide(0, 0);
  return out;
}
