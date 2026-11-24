# Design System — Pitch Deck PDF

Full reference for colors, pptxgenjs helpers, typography, layout patterns, and QA rules.
Paste the entire helper library at the top of `build.js` before writing any slides.

---

## Color Palette

```js
const C = {
  NAVY_DARK:   "0A1628",   // darkest background, cover, statement slides
  NAVY_MID:    "0D2045",   // standard dark slide background
  NAVY_LIGHT:  "1A3A6B",   // card backgrounds, table headers, borders
  GOLD:        "C9A84C",   // primary accent — stat values, highlights, CTAs
  GOLD_LIGHT:  "E8C97A",   // secondary gold — subheadings, tags
  WHITE:       "FFFFFF",   // body text on dark slides
  OFF_WHITE:   "F0F4FA",   // body text on dark slides (softer)
  LIGHT_BG:    "F4F6FA",   // light slide background
  CARD_LIGHT:  "EBF0F9",   // light card fill
  GRAY_TEXT:   "4B5563",   // body text on light slides
  GRAY_LIGHT:  "9CA3AF",   // captions, footnotes
  TABLE_HEAD:  "1A3A6B",   // table header fill
  TABLE_ALT:   "EBF0F9",   // alternating table row fill
  TABLE_LINE:  "C9A84C",   // table border / divider color
  DANGER:      "DC2626",   // loss/problem callouts
  GREEN:       "16A34A",   // gain/growth callouts
};
```

---

## Full Helper Library (paste this at the top of build.js)

```js
const PptxGenJS = require("pptxgenjs");
const pres = new PptxGenJS();
pres.layout = "LAYOUT_WIDE"; // 13.33" × 7.5"

// ─── COLORS ────────────────────────────────────────────────────────────────
const C = {
  NAVY_DARK:   "0A1628",
  NAVY_MID:    "0D2045",
  NAVY_LIGHT:  "1A3A6B",
  GOLD:        "C9A84C",
  GOLD_LIGHT:  "E8C97A",
  WHITE:       "FFFFFF",
  OFF_WHITE:   "F0F4FA",
  LIGHT_BG:    "F4F6FA",
  CARD_LIGHT:  "EBF0F9",
  GRAY_TEXT:   "4B5563",
  GRAY_LIGHT:  "9CA3AF",
  TABLE_HEAD:  "1A3A6B",
  TABLE_ALT:   "EBF0F9",
  TABLE_LINE:  "C9A84C",
  DANGER:      "DC2626",
  GREEN:       "16A34A",
};

// ─── SLIDE FACTORIES ────────────────────────────────────────────────────────

function darkSlide(bg = C.NAVY_MID) {
  const s = pres.addSlide();
  s.background = { color: bg };
  return s;
}

function lightSlide() {
  const s = pres.addSlide();
  s.background = { color: C.LIGHT_BG };
  return s;
}

// ─── SLIDE NUMBER ───────────────────────────────────────────────────────────

function slideNum(slide, num, darkBg = true) {
  slide.addText(String(num), {
    x: 12.6, y: 7.1, w: 0.5, h: 0.25,
    fontSize: 9, color: darkBg ? "4B6A99" : C.GRAY_LIGHT,
    align: "right", fontFace: "Calibri",
  });
}

// ─── SECTION TITLE (two-line heading) ───────────────────────────────────────
// IMPORTANT: Always call this as two separate addText() calls when the slide
// has content below — never combine lines into one box. This prevents overlap.

function sectionTitleDark(slide, topLine, bottomLine, y1 = 0.35) {
  const y2 = y1 + 0.42;
  slide.addText(topLine, {
    x: 0.5, y: y1, w: 12.3, h: 0.38,
    fontSize: 13, bold: false, color: C.GOLD_LIGHT,
    fontFace: "Calibri", charSpacing: 3,
  });
  slide.addText(bottomLine, {
    x: 0.5, y: y2, w: 12.3, h: 0.48,
    fontSize: 26, bold: true, color: C.WHITE,
    fontFace: "Calibri",
  });
  return y2 + 0.55; // returns y position for first content element
}

function sectionTitleLight(slide, topLine, bottomLine, y1 = 0.35) {
  const y2 = y1 + 0.42;
  slide.addText(topLine, {
    x: 0.5, y: y1, w: 12.3, h: 0.38,
    fontSize: 13, bold: false, color: C.NAVY_LIGHT,
    fontFace: "Calibri", charSpacing: 3,
  });
  slide.addText(bottomLine, {
    x: 0.5, y: y2, w: 12.3, h: 0.48,
    fontSize: 26, bold: true, color: C.NAVY_DARK,
    fontFace: "Calibri",
  });
  return y2 + 0.55;
}

// ─── GOLD DIVIDER LINE ──────────────────────────────────────────────────────

function goldDivider(slide, y, x = 0.5, w = 1.2) {
  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h: 0.04,
    fill: { color: C.GOLD },
    line: { color: C.GOLD, width: 0 },
  });
}

// ─── STAT CARD (dark navy, gold value) ──────────────────────────────────────

function makeCard(slide, x, y, w, h, label, value, sub = "") {
  // background
  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h,
    fill: { color: C.NAVY_LIGHT },
    line: { color: C.GOLD, width: 1.5 },
  });
  // label
  slide.addText(label.toUpperCase(), {
    x: x + 0.18, y: y + 0.14, w: w - 0.36, h: 0.28,
    fontSize: 9, bold: false, color: C.GOLD_LIGHT,
    fontFace: "Calibri", charSpacing: 1.5,
  });
  // value
  slide.addText(value, {
    x: x + 0.18, y: y + 0.38, w: w - 0.36, h: 0.55,
    fontSize: 28, bold: true, color: C.GOLD,
    fontFace: "Calibri",
  });
  // sub
  if (sub) {
    slide.addText(sub, {
      x: x + 0.18, y: y + h - 0.32, w: w - 0.36, h: 0.25,
      fontSize: 9.5, color: C.OFF_WHITE,
      fontFace: "Calibri",
    });
  }
}

// ─── LIGHT STAT CARD ────────────────────────────────────────────────────────

function lightCard(slide, x, y, w, h, label, value, sub = "") {
  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h,
    fill: { color: C.CARD_LIGHT },
    line: { color: C.NAVY_LIGHT, width: 1 },
  });
  slide.addText(label.toUpperCase(), {
    x: x + 0.18, y: y + 0.14, w: w - 0.36, h: 0.28,
    fontSize: 9, color: C.NAVY_LIGHT,
    fontFace: "Calibri", charSpacing: 1.5,
  });
  slide.addText(value, {
    x: x + 0.18, y: y + 0.38, w: w - 0.36, h: 0.55,
    fontSize: 28, bold: true, color: C.NAVY_DARK,
    fontFace: "Calibri",
  });
  if (sub) {
    slide.addText(sub, {
      x: x + 0.18, y: y + h - 0.32, w: w - 0.36, h: 0.25,
      fontSize: 9.5, color: C.GRAY_TEXT,
      fontFace: "Calibri",
    });
  }
}

// ─── GOLD TAG LABEL ─────────────────────────────────────────────────────────

function goldTag(slide, x, y, text) {
  const w = Math.max(text.length * 0.095 + 0.3, 1.0);
  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h: 0.28,
    fill: { color: C.GOLD },
    line: { color: C.GOLD, width: 0 },
  });
  slide.addText(text.toUpperCase(), {
    x: x + 0.1, y: y + 0.03, w: w - 0.2, h: 0.22,
    fontSize: 8.5, bold: true, color: C.NAVY_DARK,
    fontFace: "Calibri", charSpacing: 1,
  });
}

// ─── TRACK / STRATEGY CARD ─────────────────────────────────────────────────
// Numbered pillar card for strategy slides. darkBg = true for dark slides.

function trackCard(slide, x, y, w, h, num, title, bullets, darkBg = true) {
  const bg   = darkBg ? C.NAVY_LIGHT : C.CARD_LIGHT;
  const bord = darkBg ? C.GOLD       : C.NAVY_LIGHT;
  const numC = C.GOLD;
  const titC = darkBg ? C.WHITE   : C.NAVY_DARK;
  const bulC = darkBg ? C.OFF_WHITE : C.GRAY_TEXT;

  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h,
    fill: { color: bg },
    line: { color: bord, width: 1.5 },
  });
  // number circle effect (just large text)
  slide.addText(String(num), {
    x: x + 0.15, y: y + 0.12, w: 0.4, h: 0.4,
    fontSize: 22, bold: true, color: numC,
    fontFace: "Calibri",
  });
  slide.addText(title, {
    x: x + 0.15, y: y + 0.5, w: w - 0.3, h: 0.35,
    fontSize: 13, bold: true, color: titC,
    fontFace: "Calibri",
  });
  bullets.forEach((b, i) => {
    slide.addText(`• ${b}`, {
      x: x + 0.2, y: y + 0.88 + i * 0.28, w: w - 0.4, h: 0.26,
      fontSize: 10, color: bulC,
      fontFace: "Calibri", wrap: true,
    });
  });
}

// ─── TABLE HELPER ───────────────────────────────────────────────────────────
// rows: array of arrays. First row = header. colW: array of column widths.

function addTable(slide, rows, colW, x, y, rowH = 0.38) {
  const header = rows[0].map(cell => ({
    text: cell,
    options: {
      bold: true, color: C.WHITE, fill: C.TABLE_HEAD,
      fontSize: 10, fontFace: "Calibri", align: "center",
      border: [
        { type: "solid", color: C.TABLE_LINE, pt: 1 },
        { type: "solid", color: C.TABLE_LINE, pt: 1 },
        { type: "solid", color: C.TABLE_LINE, pt: 1 },
        { type: "solid", color: C.TABLE_LINE, pt: 1 },
      ],
    },
  }));

  const dataRows = rows.slice(1).map((row, rowIdx) =>
    row.map(cell => ({
      text: cell,
      options: {
        color: C.GRAY_TEXT, fontSize: 10, fontFace: "Calibri", align: "center",
        fill: rowIdx % 2 === 0 ? "FFFFFF" : C.TABLE_ALT,
        border: [
          { type: "solid", color: "D1D5DB", pt: 0.5 },
          { type: "solid", color: "D1D5DB", pt: 0.5 },
          { type: "solid", color: "D1D5DB", pt: 0.5 },
          { type: "solid", color: "D1D5DB", pt: 0.5 },
        ],
      },
    }))
  );

  slide.addTable([header, ...dataRows], {
    x, y,
    colW,
    rowH,
    border: { type: "solid", color: C.TABLE_LINE, pt: 1 },
  });
}

// ─── FUNNEL STEP ────────────────────────────────────────────────────────────
// Use for conversion mechanics slides. Stack 4-5 of these vertically.

function funnelStep(slide, x, y, w, h, label, value, color = C.NAVY_LIGHT) {
  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h,
    fill: { color },
    line: { color: C.GOLD, width: 1 },
  });
  slide.addText(label, {
    x: x + 0.15, y, w: w * 0.65, h,
    fontSize: 11, bold: false, color: C.WHITE,
    fontFace: "Calibri", valign: "middle",
  });
  slide.addText(value, {
    x: x + w * 0.65, y, w: w * 0.3, h,
    fontSize: 13, bold: true, color: C.GOLD,
    fontFace: "Calibri", align: "right", valign: "middle",
  });
}

// ─── BULLET BLOCK ───────────────────────────────────────────────────────────

function bulletBlock(slide, bullets, x, y, w, darkBg = true) {
  const color = darkBg ? C.OFF_WHITE : C.GRAY_TEXT;
  bullets.forEach((b, i) => {
    slide.addText(`• ${b}`, {
      x, y: y + i * 0.32, w, h: 0.30,
      fontSize: 11, color,
      fontFace: "Calibri", wrap: true,
    });
  });
}
```

---

## Typography Rules

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Slide eyebrow (top label) | Calibri | 13px | Normal | GOLD_LIGHT / NAVY_LIGHT |
| Slide title | Calibri | 26px | Bold | WHITE / NAVY_DARK |
| Card label | Calibri | 9px | Normal | GOLD_LIGHT / NAVY_LIGHT |
| Card value | Calibri | 28px | Bold | GOLD / NAVY_DARK |
| Card sub | Calibri | 9.5px | Normal | OFF_WHITE / GRAY_TEXT |
| Body copy | Calibri | 11px | Normal | OFF_WHITE / GRAY_TEXT |
| Table header | Calibri | 10px | Bold | WHITE |
| Table body | Calibri | 10px | Normal | GRAY_TEXT |
| Slide number | Calibri | 9px | Normal | 4B6A99 / GRAY_LIGHT |
| Gold tag | Calibri | 8.5px | Bold | NAVY_DARK |

---

## Layout Patterns

### Stat Card Row (3 or 4 cards)
- 3 cards: `w=3.9`, `x` values: `0.5, 4.72, 8.94`
- 4 cards: `w=2.9`, `x` values: `0.5, 3.65, 6.80, 9.95`
- Standard `h=1.3`, `y=1.5` (below section title)

### Track Cards Row (3 pillars)
- `w=3.9`, `h=2.8`
- `x` values: `0.5, 4.72, 8.94`
- `y=1.55`
- Each card: number + title + 3-4 bullet points

### Two-Column Layout
- Left col: `x=0.5, w=6.0`
- Right col: `x=6.8, w=6.0`

### Three-Column Layout
- `w=3.9` each, `x` values: `0.5, 4.72, 8.94`

### Full-Width Table
- `x=0.5, w=12.33`
- Calculate `colW` to sum to 12.33
- `rowH=0.38` standard, `0.42` for taller rows

### Chart Dimensions
- Full-width chart: `x=0.5, y=2.0, w=12.3, h=4.8`
- Half-width chart: `x=0.5, y=2.0, w=5.8, h=4.5`
- Chart alongside table: chart `w=6.5`, table `w=5.5`

---

## Dark vs. Light Slide Rhythm

Alternate to create visual pacing. Typical pattern for a 12-slide deck:

| Slide | Background |
|-------|-----------|
| Cover | NAVY_DARK |
| Opportunity | Light |
| Problem | NAVY_DARK (statement moment) |
| Asset Overview | Light |
| Why Act Now | NAVY_MID |
| Strategy | NAVY_MID |
| Projections | Light |
| Segments | Light |
| Roadmap | NAVY_MID |
| Conversion | Light |
| Investment & ROI | NAVY_MID |
| CTA | NAVY_DARK |

---

## QA Checklist

Run through these before delivering:

- [ ] Title lines not overlapping any content below (0.5" min gap)
- [ ] No text cut off at right edge (all `x + w ≤ 13.33`)
- [ ] No text cut off at bottom (all `y + h ≤ 7.5`)
- [ ] Stat cards aligned horizontally (same `y` value)
- [ ] Tables have correct number of columns matching header
- [ ] All `colW` arrays sum to the declared table width
- [ ] No placeholder text left in — all data pulled from brief
- [ ] Gold and white text readable against dark backgrounds
- [ ] Dark navy text readable against light backgrounds
- [ ] Slide numbers present on every slide
- [ ] CTA slide has specific numbers (not "contact us")

## Common Pitfalls

**Title overlap:** If a slide has both `sectionTitleDark()` and a table/chart, always use the returned `y` value as the start `y` for the content — never hardcode a `y` that's too close to the title.

**Table column mismatch:** Every row in `rows` must have the same number of cells as `colW.length`. A mismatch silently corrupts the table.

**colW sum:** `colW` values must sum exactly to the `w` you want. Off-by-0.01 causes right-edge bleed.

**Text overflow:** For bullet points and body text, always set `wrap: true` and give generous `h`. If you're unsure, use `h: 0.5` for single lines, `h: 1.0` for wrapping blocks.

**Chart data empty:** pptxgenjs will render a blank chart without errors if `chartData` has empty `values`. Always verify the data array is populated.
