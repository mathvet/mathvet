"""Composition of the MathVet home page: hero, charts and the explainer, each section beside its evidence."""
import re
from collections import OrderedDict

from site_charts import fidelity_bar, subject_bars, cone_strip, judge_matrix, fmt

GH = 'https://github.com/mathvet/mathvet/blob/main/'
UP = 'https://github.com/openai/math/tree/'


def row(main, aside='', cls=''):
    a = f'<aside class="note">{aside}</aside>' if aside else '<aside class="note"></aside>'
    return f'<section class="row {cls}"><div class="main">{main}</div>{a}</section>'


def split_sections(html_text):
    """Split rendered Markdown at <h2> boundaries: [(heading_text or None, html)]."""
    parts = re.split(r'(?=<h2[^>]*>)', html_text)
    out = []
    for p in parts:
        if not p.strip():
            continue
        m = re.match(r'<h2[^>]*>(.*?)</h2>', p, re.S)
        out.append((re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else None, p))
    return out


def home_body(status, counts, families, challenges, explainer_md, md, baseline_md, drift_sentence, commit, release):
    d = status.get('upstream_drift') or {}
    drift_changed = bool(d) and any(d.get(k) for k in ('families_new_with_lean', 'families_gained_lean', 'families_to_reread', 'challenges_new', 'challenges_modified'))
    n_total = status['families_total']
    n_lean = status['families_with_lean']
    n_none = status['families_without_lean']
    n_ch = status['challenges']
    sandboxed = sum(1 for c in challenges if c.get('cloud_comparator') == 'pass')
    laptop_only = sum(1 for c in challenges if c.get('cloud_comparator') != 'pass' and c.get('comparator') == 'pass')
    any_pass = sandboxed + laptop_only
    ext = sum(1 for c in challenges if c.get('cone_external'))
    c8 = commit[:8]
    gen_date = status['generated'][:10]

    # --- explainer: drop the H1 + byline (the hero carries them) and the counts table (the bar replaces it)
    body_md = explainer_md.split('\n', 1)[1] if explainer_md.startswith('# ') else explainer_md
    body_md = re.sub(r'^\s*\*A pre-referee fidelity review.*?\*\s*$', '', body_md, count=1, flags=re.S | re.M)
    intro_md, _, rest_md = body_md.partition('## The counts')
    _, _, rest_md = rest_md.partition('## How the verdicts were produced')
    rest_md = '## How the verdicts were produced' + rest_md
    counts_para = re.search(r'\n(Of \d+ families, .*?)\n', body_md, re.S)
    counts_text = md(counts_para.group(1)) if counts_para else ''

    sections = split_sections(md(rest_md))

    asides = {
        'How the verdicts were produced': (
            f'<p>Rubric: <a href="protocol.html#the-rubric-identical-to-the-one-used-for-the-original-pass">protocol</a>.</p>'
            f'<p>Audit source, one row per family: <a href="{GH}reviews/openai-math/source/">source/</a>.</p>'
            f'<p>Reading dates: 6 to 7 October 2026; the twelve families changed upstream were re-read on 10 October.</p>'),
        'What was checked by machine': (
            f'<p>{fmt(n_ch)} challenge statements, {fmt(any_pass)} accepted by the Comparator, {fmt(sandboxed)} of them on isolated Linux VMs with the Landlock sandbox; 0 rejected.</p>'
            f'<p>Only the three standard axioms in every configuration; no <code>sorry</code>, no custom <code>axiom</code> in the library.</p>'
            f'<p>{ext} challenges depend on external packages pinned by the lab.</p>'
            f'<p>Logs: <a href="{GH}reviews/openai-math/evidence/cloud/">evidence/cloud/</a> and <a href="{GH}reviews/openai-math/evidence/lean_checks/">evidence/lean_checks/</a>; the scripts: <a href="{GH}checker/">checker/</a>.</p>'),
        'The repository already says much of this': (
            f'<p>Scope notes are quoted verbatim from <a href="{UP}{commit}/lean/docs">lean/docs</a> at the reviewed commit; the table shows each family\'s note next to our reading.</p>'),
        'What this review is not': '',
        'The error rate': (
            f'<p>Sample of 40 families frozen 8 October 2026 at <code>adc7f124</code>: <a href="{GH}reviews/openai-math/sample.txt">sample.txt</a>, '
            f'SHA-256 in <a href="{GH}reviews/openai-math/sample.sha256">sample.sha256</a>; draw reproduced by <a href="{GH}reviews/openai-math/draw_sample.py">draw_sample.py</a>.</p>'
            f'<p>Decision lines fixed in advance: pass at or below 0.10, kill at or above 0.20.</p>'
            f'<p>Referee packet: <a href="{GH}reviews/openai-math/referee/">referee/</a>.</p>'),
        'In the standard\'s own fields': (
            f'<p>The review in formalization.yaml v0.4: <a href="{GH}reviews/openai-math/formalization-review.yaml">formalization-review.yaml</a>, '
            f'validated against the published schema.</p>'),
        'Using and correcting it': (
            f'<p>Data: <a href="{GH}reviews/openai-math/fidelity-table.csv">fidelity-table.csv</a>, <a href="{GH}reviews/openai-math/challenge-status.csv">challenge-status.csv</a>, '
            f'<a href="{GH}dataset/">dataset/</a>.</p><p>Changes: <a href="{GH}CHANGELOG.md">CHANGELOG.md</a>. Corrections: <a href="https://github.com/mathvet/mathvet/issues">issues</a>.</p>'),
    }

    # --- hero
    hero_aside = (
        f'<p class="k">Review of</p><p><a href="https://github.com/openai/math">openai/math</a> at commit <a href="{UP}{commit}"><code>{c8}</code></a>, the release of 6 October 2026 as updated on 8 October.</p>'
        f'<p class="k">Status</p><p>Pre-referee. The referee round is <a href="protocol.html">pre-registered</a>; its error rate will be published whatever it shows.</p>'
        f'<p class="k">Reviewer</p><p>Tejpal Virk, Berkeley, CA. MathVet takes no funding from, and has no affiliation with, any lab whose work it reviews.</p>'
        f'<p class="k">Regenerated</p><p>{gen_date}, from the committed sources and logs by <a href="{GH}scripts/build_review.py">build_review.py</a>.</p>')
    hero = (
        '<h1>Which of OpenAI\'s 372 mathematical results are machine-checked as stated?</h1>'
        + md(intro_md.strip())
    )
    out = [row(hero, hero_aside, 'hero')]

    # --- the finding: one bar
    bar_aside = (f'<p>One segment per family, {fmt(n_total)} in all. Counts from <a href="{GH}reviews/openai-math/fidelity-table.csv">fidelity-table.csv</a>; '
                 f'every verdict opens to its evidence in the <a href="{release}/">fidelity table</a>.</p>'
                 f'<p>"Machine-checked" means the Lean kernel accepted a proof of the challenge statement under the lab\'s own Comparator configuration; the verdict is about whether that statement is the headline.</p>')
    out.append(row(fidelity_bar(counts, n_none, n_total) + counts_text, bar_aside, 'finding'))
    if drift_sentence and drift_changed:
        out.append(row(f'<div class="drift">{md(drift_sentence)}</div>', '<p>Upstream is watched nightly; a changed family is rebuilt and re-read before its verdict moves.</p>'))

    # --- explainer sections with charts interleaved
    for heading, html_sec in sections:
        extra = ''
        aside = asides.get(heading, '')
        if heading == 'How the verdicts were produced':
            extra = ('<h3>Where the narrower statements are</h3>' + subject_bars(families)
                     + '<p class="fig-note">Over-statement is not evenly spread: mathematical physics and probability carry most of the weaker and supporting-only readings; number theory and functional analysis are almost all stated in full.</p>')
        if heading == 'What was checked by machine':
            extra = ('<h3>Every one of the 416 statements, by how much Lean it depends on</h3>' + cone_strip(challenges))
            jm = judge_matrix(baseline_md)
            if jm:
                extra += ('<h3>How a single-shot model judge compares with the review</h3>'
                          '<p>As a baseline for the public dataset, a general-purpose model (Claude Sonnet 5.5) classified each challenge statement on its own, three samples per statement, seeing the headline, the scope note, the Lean text and the paper\'s main theorem but nothing from this review. '
                          'The judge agrees with the review on most families and is more lenient on the <em>partial</em> stratum, which is where the referee round concentrates. Both are automated readings, so this measures consistency, not correctness.</p>'
                          + jm)
                aside += (f'<p>Benchmark at <code>adc7f124</code> (235 families): <a href="{GH}dataset/baseline.md">dataset/baseline.md</a>; aggregates only until the verdicts are refereed.</p>')
        out.append(row(html_sec + extra, aside))
    return '\n'.join(out)
