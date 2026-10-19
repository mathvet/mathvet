"""Build-time charts for the MathVet site: plain HTML/SVG strings computed from the review data.

Every chart is generated from the same records the tables use, so a reader who distrusts the
picture can check it against fidelity-table.csv and challenge-status.csv. Colors are CSS
variables (see site_templates.CSS) so light and dark modes share one markup.
"""
import html
import math
import re
from collections import Counter, OrderedDict

VERDICTS = OrderedDict([
    ('full', 'Lean states the headline claim'),
    ('partial', 'one of several claims, or a special case'),
    ('weaker-statement', 'a nontrivially weaker statement'),
    ('supporting-only', 'a supporting lemma only'),
])
NONE_LABEL = 'no Lean'


def esc(s):
    return html.escape(str(s), quote=True)


def fmt(n):
    return f'{n:,}'


# ----------------------------------------------------------------------------- fidelity bar
def fidelity_bar(counts, n_none, n_total):
    """One proportional bar of every family in the release, five segments, labelled below."""
    segs = [(k, counts.get(k, 0)) for k in VERDICTS] + [('none', n_none)]
    out = ['<figure class="fbar" aria-label="All families in the release by verdict">']
    out.append('<div class="fbar-track" role="img" aria-label="' + esc('; '.join(f'{v} {k}' for k, v in segs)) + '">')
    for k, v in segs:
        w = 100.0 * v / n_total
        tip = f'{fmt(v)} families ({w:.0f}%): {VERDICTS.get(k, NONE_LABEL)}'
        out.append(f'<span class="seg v-{k}" style="flex-basis:{w:.3f}%" data-tip="{esc(tip)}" tabindex="0"><i></i></span>')
    out.append('</div>')
    # bracket line: three groups
    full = counts.get('full', 0)
    narrower = sum(counts.get(k, 0) for k in VERDICTS if k != 'full')
    groups = [('machine-checked as stated', full), ('machine-checked in a narrower form', narrower), ('manuscript only', n_none)]
    out.append('<div class="fbar-groups">')
    for label, v in groups:
        w = 100.0 * v / n_total
        out.append(f'<span style="flex-basis:{w:.3f}%"><b>{w:.0f}%</b> {esc(label)}</span>')
    out.append('</div>')
    out.append('<ul class="fbar-key">')
    for k, v in segs:
        out.append(f'<li><i class="sw v-{k}"></i><div><b>{fmt(v)}</b> <span class="vk">{esc(k if k != "none" else NONE_LABEL)}</span>'
                   f'<span class="vd">{esc(VERDICTS.get(k, "no formalization in the release"))}</span></div></li>')
    out.append('</ul></figure>')
    return '\n'.join(out)


# ----------------------------------------------------------------------------- verdicts by subject
def subject_bars(families):
    by = {}
    for f in families:
        if f['verdict'] == 'none':
            continue
        by.setdefault(f['subject'], Counter())[f['verdict']] += 1
    rows = sorted(by.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))
    mx = max(sum(c.values()) for _, c in rows)
    out = ['<figure class="sbars" aria-label="Verdicts by subject">', '<div class="sbars-rows">']
    for subj, c in rows:
        n = sum(c.values())
        full = c.get('full', 0)
        out.append('<div class="srow">')
        out.append(f'<span class="slab">{esc(subj)}</span>')
        out.append(f'<span class="strack" style="width:{100.0 * n / mx:.2f}%">')
        for k in VERDICTS:
            v = c.get(k, 0)
            if not v:
                continue
            tip = f'{esc(subj)}: {v} of {n} {k}'
            out.append(f'<span class="seg v-{k}" style="flex-basis:{100.0 * v / n:.3f}%" data-tip="{tip}" tabindex="0"><i></i></span>')
        out.append('</span>')
        out.append(f'<span class="sn"><b>{full}</b><span class="of">/{n}</span></span>')
        out.append('</div>')
    out.append('</div>')
    out.append('<p class="sbars-foot">Bar length is the number of families with Lean in the subject; the number is how many of them are stated in full. '
               'Colors as in the bar above.</p>')
    out.append('</figure>')
    return '\n'.join(out)


# ----------------------------------------------------------------------------- the 416 cones
def cone_strip(challenges):
    """Every Comparator challenge as one thin bar: the lines of Lean the kernel re-checked, log scale, sorted."""
    rows = []
    for c in challenges:
        tier = 'vm' if c.get('cloud_comparator') == 'pass' else ('laptop' if c.get('comparator') == 'pass' else 'none')
        rows.append((c['cone_oai_lines'], c['challenge'], tier, bool(c.get('cone_external'))))
    rows.sort(key=lambda r: -r[0])
    n = len(rows)
    W, H = 880, 230
    L, R, T, B = 64, 12, 28, 30
    pw = W - L - R
    ph = H - T - B
    lo, hi = math.log10(100), math.log10(4_000_000)

    def y(v):
        return T + ph * (1 - (math.log10(max(v, 100)) - lo) / (hi - lo))

    out = [f'<svg class="cones" viewBox="0 0 {W} {H}" role="img" aria-label="Lines of Lean in the import cone of each of the {n} challenge statements, all accepted by the Comparator">']
    out.append('<title>Each bar is one challenge statement; height is the size of the Lean it depends on (log scale)</title>')
    # grid
    for v, lab in ((1_000, '1,000 lines'), (10_000, '10,000'), (100_000, '100,000'), (1_000_000, '1,000,000')):
        yy = y(v)
        out.append(f'<line class="grid" x1="{L}" x2="{W - R}" y1="{yy:.1f}" y2="{yy:.1f}"/>')
        out.append(f'<text class="ylab" x="{L - 6}" y="{yy + 4:.1f}" text-anchor="end">{lab}</text>')
    bw = pw / n
    gap = 0.35 if bw > 1.2 else 0.0
    for i, (lines, name, tier, ext) in enumerate(rows):
        x = L + i * bw
        top = y(lines)
        h = T + ph - top
        tip = f'{name}: {fmt(lines)} lines' + (' (external packages)' if ext else '') + \
              ('; accepted on a sandboxed Linux VM' if tier == 'vm' else '; accepted on the reviewer\'s laptop' if tier == 'laptop' else '')
        out.append(f'<rect class="bar t-{tier}" x="{x:.2f}" y="{top:.1f}" width="{max(bw - gap, 0.6):.2f}" height="{h:.1f}" rx="0.6" data-tip="{esc(tip)}"><title>{esc(tip)}</title></rect>')
    # annotate the three largest
    lines0, name0, _, _ = rows[0]
    x0 = L + bw / 2
    out.append(f'<line class="lead" x1="{x0:.1f}" y1="{y(lines0) - 3:.1f}" x2="{x0 + 30:.1f}" y2="{T - 10:.1f}"/>')
    out.append(f'<text class="ann" x="{x0 + 34:.1f}" y="{T - 7:.1f}">{esc(name0)}, {fmt(lines0)} lines</text>')
    # the next names are listed in the caption instead of overlapping labels
    out.append(f'<text class="xlab" x="{L}" y="{H - 8}">largest cone</text>')
    out.append(f'<text class="xlab" x="{W - R}" y="{H - 8}" text-anchor="end">smallest</text>')
    out.append('</svg>')
    top3 = ', '.join(f'{r[1]} ({fmt(r[0])} lines)' for r in rows[:3])
    tiers = Counter(r[2] for r in rows)
    key = (f'<ul class="cones-key"><li><i class="sw t-vm"></i>{tiers.get("vm", 0)} accepted on an isolated Linux VM with the Landlock sandbox</li>'
           f'<li><i class="sw t-laptop"></i>{tiers.get("laptop", 0)} accepted on the reviewer\'s laptop (development sandbox shim)</li></ul>')
    cap = f'<p class="cones-foot">Largest three: {esc(top3)}. Median {fmt(int(sorted(r[0] for r in rows)[n // 2]))} lines.</p>'
    return f'<figure class="cones-fig" aria-label="Challenge cones">{"".join(out)}{key}{cap}</figure>'


# ----------------------------------------------------------------------------- judge vs review matrix
def parse_baseline_matrix(md_text):
    """First 'MathVet \\ baseline' table in dataset/baseline.md -> (cols, rows[(label, counts, total)])."""
    m = re.search(r'\| MathVet \\ baseline \|(.*?)\n\|[-| ]+\|\n((?:\|.*\n)+)', md_text)
    if not m:
        return None
    cols = [c.strip() for c in m.group(1).strip('| \n').split('|')]
    cols = [c for c in cols if c and c != 'total']
    rows = []
    for line in m.group(2).strip().splitlines():
        cells = [c.strip() for c in line.strip('|').split('|')]
        label = cells[0].strip('* ')
        nums = [int(x) for x in cells[1:1 + len(cols)]]
        total = int(cells[1 + len(cols)])
        rows.append((label, nums, total))
    return cols, rows


def judge_matrix(md_text):
    parsed = parse_baseline_matrix(md_text)
    if not parsed:
        return ''
    cols, rows = parsed
    agree = sum(nums[cols.index(label)] for label, nums, _ in rows if label in cols)
    n = sum(t for _, _, t in rows)
    out = ['<figure class="jm" aria-label="Single-shot model judge against the MathVet verdict">',
           '<table class="jmt"><thead><tr><th scope="col">MathVet verdict</th>']
    for c in cols:
        out.append(f'<th scope="col">judge: {esc(c)}</th>')
    out.append('<th scope="col">families</th></tr></thead><tbody>')
    for label, nums, total in rows:
        out.append(f'<tr><th scope="row">{esc(label)}</th>')
        for c, v in zip(cols, nums):
            a = (v / total) if total else 0
            diag = ' diag' if c == label else ''
            tip = f'{v} of {total} {label} families judged {c}'
            shown = str(v) if v else '<span class="z">0</span>'
            hi = ' data-hi="1"' if a > 0.55 else ''
            out.append(f'<td class="cell{diag}"{hi} style="--a:{a:.3f}" data-tip="{esc(tip)}" tabindex="0">{shown}</td>')
        out.append(f'<td class="tot">{total}</td></tr>')
    out.append('</tbody></table>')
    out.append(f'<p class="jm-foot">Rows sum to the review\'s families at the benchmark commit; the outlined diagonal is agreement: {agree} of {n} families ({100.0 * agree / n:.1f}%). '
               'Shading is the share of the row.</p></figure>')
    return '\n'.join(out)
