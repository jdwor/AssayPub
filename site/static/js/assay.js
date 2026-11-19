/* Assay. Three small behaviors: the labels for the cover's wells, the list of editions and the topic chart.
   No dependencies. */

// ---- the cover: a label for each well ------------------------------------------
// A pointer over a well, or keyboard focus on it, shows the label beside the well. A finger gets the label as a
// bar along the bottom of the window: the first touch of a well shows it, and the bar (or a second touch of the
// same well) opens the work. Touching anything else, or scrolling, puts it away.
const tip = document.getElementById("tip");
if (tip) {
  const [kind, title, meta, open] = tip.children;
  let shown = null, touch = false, held = [];
  const place = (dot) => {
    const r = dot.getBoundingClientRect(), w = tip.offsetWidth, h = tip.offsetHeight, gap = 10, edge = 8;
    const x = Math.min(Math.max(r.left + r.width / 2 - w / 2, edge), innerWidth - w - edge);
    const above = r.top - h - gap;
    const y = above >= edge ? above : Math.min(r.bottom + gap, innerHeight - h - edge);
    tip.style.transform = `translate(${Math.round(x)}px, ${Math.round(y)}px)`;
  };
  const release = () => { held.forEach((e) => e.classList.remove("hot")); held = []; };
  const entry = (dot) => dot.dataset.w && document.querySelector(`.item[data-w="${dot.dataset.w}"]`);
  const show = (dot, bar = false) => {
    release();
    kind.textContent = dot.dataset.k; title.textContent = dot.dataset.t; meta.textContent = dot.dataset.m;
    tip.classList.toggle("bar", bar);
    tip.hidden = false; shown = dot;
    if (bar) {
      tip.style.transform = ""; tip.removeAttribute("role");
      open.href = dot.href; open.setAttribute("aria-label", `Open ${dot.getAttribute("aria-label")}`);
      held = [dot, entry(dot)].filter(Boolean);
      held.forEach((e) => e.classList.add("hot"));
    } else {
      tip.setAttribute("role", "tooltip"); open.removeAttribute("href");
      place(dot);
    }
  };
  const hide = () => { tip.hidden = true; shown = null; release(); };
  const pair = (a, b) => {
    const on = () => b.classList.add("hot"), off = () => { if (!held.includes(b)) b.classList.remove("hot"); };
    a.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") on(); });
    a.addEventListener("pointerleave", (e) => { if (e.pointerType === "mouse") off(); });
    a.addEventListener("focus", () => { if (!touch) on(); }); a.addEventListener("blur", off);
  };
  addEventListener("pointerdown", (e) => {
    touch = e.pointerType !== "mouse";
    if (shown && tip.classList.contains("bar") && !e.target.closest("a.d, .tip")) hide();
  }, true);
  addEventListener("keydown", () => { touch = false; }, true);
  for (const dot of document.querySelectorAll("a.d")) {
    dot.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") show(dot); });
    dot.addEventListener("pointerleave", (e) => { if (e.pointerType === "mouse") hide(); });
    dot.addEventListener("focus", () => { if (!touch) show(dot); });
    dot.addEventListener("blur", () => { if (!tip.classList.contains("bar")) hide(); });
    dot.addEventListener("click", (e) => { if (touch && shown !== dot) { e.preventDefault(); show(dot, true); } });
    const item = entry(dot);
    if (item) { pair(dot, item); pair(item, dot); }
  }
  addEventListener("scroll", hide, { passive: true });
  addEventListener("resize", hide);
  addEventListener("pageshow", hide);
}

// ---- the cover: the list of editions under the number --------------------------
// The list opens and closes without this. This puts it away on Escape, on a click or touch anywhere else, when
// the focus leaves it, and when the page is returned to.
const menu = document.querySelector(".edmenu");
if (menu) {
  const close = () => { menu.open = false; };
  addEventListener("pointerdown", (e) => { if (menu.open && !menu.contains(e.target)) close(); }, true);
  addEventListener("keydown", (e) => { if (e.key === "Escape" && menu.open) { close(); menu.firstElementChild.focus(); } });
  menu.addEventListener("focusout", (e) => { if (e.relatedTarget && !menu.contains(e.relatedTarget)) close(); });
  addEventListener("pageshow", close);
}

// ---- the topic chart: one series, monthly counts ------------------------------
const SVG = "http://www.w3.org/2000/svg";
const el = (name, attrs = {}, text) => {
  const node = document.createElementNS(SVG, name);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
  if (text != null) node.textContent = text;
  return node;
};
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const monthName = (ym) => `${MONTHS[+ym.slice(5) - 1]} ${ym.slice(0, 4)}`;

function niceMax(v) {
  const step = Math.pow(10, Math.floor(Math.log10(v)));
  for (const m of [1, 2, 2.5, 5, 10]) if (v <= m * step) return m * step;
  return 10 * step;
}

function drawChart(fig) {
  const all = JSON.parse(fig.dataset.chart).filter((d) => d.count != null);
  const full = all.filter((d) => !d.partial);
  const partial = all.find((d) => d.partial);
  const plot = fig.querySelector("[data-chart-plot]");
  plot.replaceChildren();
  const W = plot.clientWidth, H = Math.max(260, Math.min(380, W * 0.42));
  const m = { t: 16, r: 64, b: 30, l: 44 };
  const max = niceMax(Math.max(...all.map((d) => d.count), 1));
  const x = (i) => m.l + (i / (all.length - 1)) * (W - m.l - m.r);
  const y = (v) => H - m.b - (v / max) * (H - m.t - m.b);

  const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, width: W, height: H, role: "img",
    "aria-label": `${fig.dataset.label}: arXiv preprints per month, ${monthName(all[0].month)} to ${monthName(all.at(-1).month)}. The figures are in the table below.` });
  for (let t = 0; t <= 4; t++) {
    const v = (max / 4) * t;
    svg.append(el("line", { class: "grid", x1: m.l, x2: W - m.r, y1: y(v), y2: y(v) }));
    svg.append(el("text", { class: "axis-text", x: m.l - 8, y: y(v) + 4, "text-anchor": "end" }, v.toLocaleString()));
  }
  all.forEach((d, i) => {
    if (d.month.endsWith("-01")) svg.append(el("text", { class: "axis-text", x: x(i), y: H - 8, "text-anchor": "middle" }, d.month.slice(0, 4)));
  });
  const path = full.map((d, i) => `${i ? "L" : "M"}${x(i).toFixed(1)},${y(d.count).toFixed(1)}`).join("");
  svg.append(el("path", { class: "series-under", d: path }), el("path", { class: "series", d: path }));
  const last = full.at(-1), li = full.length - 1;
  svg.append(el("circle", { class: "end-dot", cx: x(li), cy: y(last.count), r: 4.5 }));
  svg.append(el("text", { class: "end-label", x: x(li) + 10, y: y(last.count) - 8 }, last.count.toLocaleString()));
  if (partial) svg.append(el("circle", { class: "partial-dot", cx: x(all.length - 1), cy: y(partial.count), r: 4.5 }));

  const cross = el("line", { class: "cross", y1: m.t, y2: H - m.b });
  const dot = el("circle", { class: "cross-dot", r: 5 });
  svg.append(cross, dot);
  const tip = document.createElement("div");
  tip.className = "chart-tip";
  const strong = document.createElement("b"), span = document.createElement("span");
  tip.append(strong, span);
  plot.append(svg, tip);

  const point = (i) => {
    const d = all[i];
    cross.setAttribute("x1", x(i)); cross.setAttribute("x2", x(i));
    dot.setAttribute("cx", x(i)); dot.setAttribute("cy", y(d.count));
    strong.textContent = d.count.toLocaleString();
    span.textContent = `${monthName(d.month)}${d.partial ? ", part month" : ""}`;
    const left = Math.min(Math.max(x(i) - tip.offsetWidth / 2, 0), W - tip.offsetWidth);
    tip.style.transform = `translate(${left}px, ${Math.max(y(d.count) - tip.offsetHeight - 14, 0)}px)`;
    fig.classList.add("is-active");
  };
  let at = all.length - 1;
  svg.addEventListener("pointermove", (e) => {
    const px = e.clientX - svg.getBoundingClientRect().left;
    at = Math.round(((px - m.l) / (W - m.l - m.r)) * (all.length - 1));
    at = Math.min(all.length - 1, Math.max(0, at));
    point(at);
  });
  svg.addEventListener("pointerleave", () => fig.classList.remove("is-active"));
  svg.setAttribute("tabindex", "0");
  svg.addEventListener("keydown", (e) => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault();
    at = Math.min(all.length - 1, Math.max(0, at + (e.key === "ArrowRight" ? 1 : -1)));
    point(at);
  });
  svg.addEventListener("blur", () => fig.classList.remove("is-active"));
}

const figures = [...document.querySelectorAll("figure[data-chart]")];
if (figures.length) {
  const redraw = () => figures.forEach(drawChart);
  redraw();
  let timer;
  addEventListener("resize", () => { clearTimeout(timer); timer = setTimeout(redraw, 150); });
}
