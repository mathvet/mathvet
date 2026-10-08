"""HTML, CSS and JS templates for the MathVet static site (docs/)."""

KATEX_HEAD = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
"""

CSS = r"""
:root{--bg:#fbfbf9;--fg:#1d1d1b;--muted:#5f5f5a;--line:#e3e2dc;--card:#ffffff;--accent:#1f5f8b;--full:#2f7a4a;--partial:#b7791f;--weaker:#b4532a;--supporting:#7a5fa3;--none:#8a8a84;--chip:#eef1f4}
@media (prefers-color-scheme: dark){:root{--bg:#141513;--fg:#ececea;--muted:#a9a9a3;--line:#2e2f2c;--card:#1c1d1b;--accent:#7fb3dc;--full:#6cc08b;--partial:#e0a94a;--weaker:#e3865f;--supporting:#b59ad8;--none:#8f8f89;--chip:#24262a}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
a{color:var(--accent)}code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.92em}
pre{overflow:auto;padding:.75rem 1rem;border:1px solid var(--line);border-radius:6px;background:var(--card)}
header.top{border-bottom:1px solid var(--line);background:var(--card)}
header.top .in{max-width:76rem;margin:0 auto;padding:.7rem 1rem;display:flex;flex-wrap:wrap;gap:.5rem 1.2rem;align-items:baseline}
header.top .brand{font-weight:700;font-size:1.15rem;text-decoration:none;color:var(--fg)}
header.top .brand span{color:var(--muted);font-weight:400;font-size:.95rem;margin-left:.5rem}
header.top nav a{margin-right:1rem;text-decoration:none;color:var(--muted)}header.top nav a.active,header.top nav a:hover{color:var(--accent)}
main{max-width:76rem;margin:0 auto;padding:1rem 1rem 3rem}
.prose{max-width:46rem;margin:0 auto}.prose h1{font-size:1.9rem;line-height:1.2;margin:1.2rem 0 .6rem}.prose h2{font-size:1.35rem;margin-top:2rem}
.prose table{border-collapse:collapse;margin:1rem 0;width:100%}.prose th,.prose td{border:1px solid var(--line);padding:.4rem .6rem;text-align:left;vertical-align:top}
.prose blockquote{margin:1rem 0;padding:.2rem 1rem;border-left:3px solid var(--line);color:var(--muted)}
.prose img{max-width:100%}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.7rem;margin:1rem 0 .4rem}
.tile{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:.8rem .9rem}
.tile .n{font-size:2rem;font-weight:700;line-height:1.1}.tile .n .of{font-size:1rem;color:var(--muted);font-weight:400}.tile .l{color:var(--muted);font-size:.9rem;margin-top:.2rem}
.tile.full .n{color:var(--full)}.tile.narrower .n{color:var(--weaker)}.tile.none .n{color:var(--none)}
.status-line{color:var(--muted);font-size:.92rem;margin:.2rem 0 1.6rem}
.badge{display:inline-block;padding:.08rem .5rem;border-radius:999px;font-size:.8rem;font-weight:600;color:#fff;white-space:nowrap}
.badge.full{background:var(--full)}.badge.partial{background:var(--partial)}.badge.weaker-statement{background:var(--weaker)}.badge.supporting-only{background:var(--supporting)}.badge.none{background:var(--none)}
.chip{display:inline-block;background:var(--chip);border-radius:4px;padding:.05rem .4rem;font-size:.8rem;margin:.1rem .2rem .1rem 0}
.mc{font-size:.8rem;white-space:nowrap}.mc.comparator-pass{color:var(--full);font-weight:600}.mc.comparator-sandboxed-pass{color:var(--full);font-weight:700}.mc.closure-pass{color:var(--full)}.mc.built{color:var(--partial)}.mc.build-in-progress{color:var(--muted)}.mc.none{color:var(--muted)}.mc.build-failed{color:var(--weaker)}
.filters{display:flex;flex-wrap:wrap;gap:.5rem .9rem;align-items:center;margin:.8rem 0;padding:.7rem .9rem;background:var(--card);border:1px solid var(--line);border-radius:8px}
.filters input[type=search],.filters select{font:inherit;padding:.35rem .5rem;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg)}
.filters label{font-size:.9rem;color:var(--muted)}.filters .count{margin-left:auto;color:var(--muted);font-size:.9rem}
table.data{border-collapse:collapse;width:100%;font-size:.92rem}
table.data th,table.data td{padding:.45rem .5rem;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}
table.data th{position:sticky;top:0;background:var(--card);cursor:pointer;user-select:none;font-weight:600;font-size:.85rem;color:var(--muted)}
table.data tr.row{cursor:pointer}table.data tr.row:hover{background:var(--card)}
table.data tr.details td{background:var(--card);padding:.8rem 1rem 1rem}
.details .k{color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.04em;margin-top:.7rem}
.details .k:first-child{margin-top:0}.details p{margin:.25rem 0 .4rem}
.details ul{margin:.2rem 0 .4rem 1.1rem;padding:0}
.wrap{overflow-x:auto}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}footer .in{max-width:76rem;margin:0 auto;padding:1rem}
.notice{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--partial);border-radius:6px;padding:.6rem .9rem;margin:.6rem 0 1rem;font-size:.92rem}
@media (max-width:640px){table.data{font-size:.85rem}.tile .n{font-size:1.6rem}}
"""

LAYOUT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="MathVet: independent, pre-referee fidelity reviews of AI-generated Lean formalizations. Does the Lean statement say what the paper claims?">
<link rel="stylesheet" href="{root}style.css">
{extra_head}
</head>
<body>
<header class="top"><div class="in">
  <a class="brand" href="{root}">MathVet<span>does the Lean statement say what the paper claims?</span></a>
  <nav>
    <a href="{root}" class="{home}">Review: openai/math</a>
    <a href="{root}openai-math/" class="{table}">Fidelity table</a>
    <a href="{root}openai-math/challenges.html" class="{challenges}">Challenges</a>
    <a href="{root}protocol.html" class="{protocol}">Referee protocol</a>
    <a href="https://github.com/ceshanon/mathvet">GitHub</a>
  </nav>
</div></header>
<main>
{body}
</main>
<footer><div class="in">MathVet reviews are independent of every lab whose work they cover and are published under Apache-2.0; the reviewed artefacts are their authors'. Every verdict is pre-referee until the error rate in the <a href="{root}protocol.html">protocol</a> has been published. Upstream commit <code>{commit}</code>; generated {generated}. Corrections: <a href="https://github.com/ceshanon/mathvet/issues">open an issue</a>.</div></footer>
{extra_js}
</body>
</html>
"""


def layout(title, body, active, extra_head='', extra_js='', generated='', commit=''):
    root = '../' if active in ('table', 'challenges') else ''
    cls = {k: ('active' if k == active else '') for k in ('home', 'table', 'challenges', 'protocol')}
    return LAYOUT.format(title=title, body=body, root=root, extra_head=extra_head, extra_js=extra_js,
                         generated=generated, commit=commit, **cls)


TABLE_PAGE = r"""
<h1 style="margin:.6rem 0 .3rem">Fidelity table — openai/math @ <code>__COMMIT8__</code></h1>
<div class="notice">Every verdict on this page is <strong>pre-referee</strong>: one model-assisted reading per family, validated mechanically, not yet re-read by a named human referee. The repository's own scope note is shown next to each verdict so you can judge for yourself. Verdict scale: <span class="badge full">full</span> Lean states the headline claim · <span class="badge partial">partial</span> only one of several claims, or a special case · <span class="badge weaker-statement">weaker-statement</span> a nontrivially weaker statement · <span class="badge supporting-only">supporting-only</span> a lemma or auxiliary statement. Click a row for the evidence.</div>
<div class="filters">
  <input type="search" id="q" placeholder="search family, title, challenge, note…" size="34" aria-label="search">
  <label><input type="checkbox" class="v" value="full" checked> full</label>
  <label><input type="checkbox" class="v" value="partial" checked> partial</label>
  <label><input type="checkbox" class="v" value="weaker-statement" checked> weaker</label>
  <label><input type="checkbox" class="v" value="supporting-only" checked> supporting-only</label>
  <select id="subj" aria-label="subject"><option value="">all subjects</option></select>
  <label><input type="checkbox" id="mc"> machine-checked here only</label>
  <label><input type="checkbox" id="ext"> external packages only</label>
  <span class="count" id="count"></span>
</div>
<div class="wrap"><table class="data" id="t">
<thead><tr><th data-k="family">Family</th><th data-k="title">Title</th><th data-k="subject">Subject</th><th data-k="verdict">Verdict</th><th>Challenges</th><th data-k="cone_lines_max">Cone (lines)</th><th data-k="machine_check">Checked here</th></tr></thead>
<tbody id="tb"></tbody>
</table></div>
<p style="color:var(--muted);font-size:.85rem">Download: <a href="https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/fidelity-table.csv">fidelity-table.csv</a> · <a href="https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/fidelity-table.json">fidelity-table.json</a> · <a href="https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/formalization-review.yaml">formalization-review.yaml</a> · <a href="data.json">data.json</a>. Generated __GENERATED__.</p>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA=JSON.parse(document.getElementById('data').textContent);
const MC={'comparator-sandboxed-pass':'Comparator PASS, sandboxed VM','comparator-pass':'Comparator PASS','closure-pass':'built + closure ok','built':'built','build-in-progress':'building…','build-failed':'build failed','none':'—'};
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let sortK='family',sortD=1,open=new Set();
const subj=document.getElementById('subj');[...new Set(DATA.map(d=>d.subject))].sort().forEach(s=>{const o=document.createElement('option');o.value=s;o.textContent=s;subj.appendChild(o)});
function rows(){const q=document.getElementById('q').value.trim().toLowerCase();const vs=new Set([...document.querySelectorAll('.v:checked')].map(c=>c.value));const sj=subj.value;const mc=document.getElementById('mc').checked;const ext=document.getElementById('ext').checked;
 let r=DATA.filter(d=>vs.has(d.verdict)&&(!sj||d.subject===sj)&&(!mc||d.machine_check!=='none')&&(!ext||d.external_packages.length)&&(!q||[d.family,d.title,d.subject,d.challenges.join(' '),d.review_note,d.headline].join(' ').toLowerCase().includes(q)));
 r.sort((a,b)=>{let x=a[sortK],y=b[sortK];if(typeof x==='number')return (x-y)*sortD;return String(x).localeCompare(String(y))*sortD});return r}
function detail(d){const cs=d.challenges.map(c=>`<a href="https://github.com/openai/math/blob/__COMMIT__/lean/ComparatorChallenges/${c}.lean">${c}.lean</a>`).join(', ');
 const defs=d.definitions_to_check.length?'<ul>'+d.definitions_to_check.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>':'<p>none noted</p>';
 const papers=d.papers.map(p=>`<a href="${p.url}">${esc(p.title)}</a>`).join(' · ');
 return `<div class="details"><div class="k">Headline claim (overview summary)</div><p>${esc(d.headline)}</p>
 <div class="k">MathVet reading (pre-referee) — ${esc(d.verdict)}</div><p>${esc(d.review_note)}</p>
 <div class="k">The repository's own scope note (<a href="${d.lab_docs_url}">lean/docs/${d.family}.md</a>, verbatim)</div><p style="white-space:pre-wrap">${esc(d.lab_scope_note)}</p>
 <div class="k">Definitions to check</div>${defs}
 <div class="k">Challenge statements</div><p>${cs}</p>
 <div class="k">Papers</div><p>${papers||'—'}</p>
 <div class="k">Machine check on our machine</div><p>${esc(MC[d.machine_check])} — see <a href="challenges.html#fam-${d.family}">challenge status</a></p></div>`}
function render(){const r=rows();const tb=document.getElementById('tb');tb.innerHTML='';
 for(const d of r){const tr=document.createElement('tr');tr.className='row';tr.id='fam-'+d.family;
  tr.innerHTML=`<td><code>${d.family}</code></td><td>${esc(d.title)}</td><td>${esc(d.subject)}</td><td><span class="badge ${d.verdict}">${d.verdict}</span></td><td>${d.challenges.map(c=>'<span class="chip">'+c+'</span>').join('')}</td><td>${d.cone_lines_max.toLocaleString()}</td><td><span class="mc ${d.machine_check}">${MC[d.machine_check]}</span></td>`;
  tr.onclick=()=>{if(open.has(d.family))open.delete(d.family);else open.add(d.family);render()};tb.appendChild(tr);
  if(open.has(d.family)){const td=document.createElement('tr');td.className='details';td.innerHTML=`<td colspan="7">${detail(d)}</td>`;tb.appendChild(td);if(window.renderMathInElement)renderMathInElement(td,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});}}
 const c={};for(const d of r)c[d.verdict]=(c[d.verdict]||0)+1;
 document.getElementById('count').textContent=`${r.length} families — full ${c['full']||0} · partial ${c['partial']||0} · weaker ${c['weaker-statement']||0} · supporting-only ${c['supporting-only']||0}`;
 if(window.renderMathInElement)renderMathInElement(tb,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});}
document.querySelectorAll('#q,.v,#subj,#mc,#ext').forEach(e=>e.addEventListener('input',render));
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{const k=th.dataset.k;if(sortK===k)sortD=-sortD;else{sortK=k;sortD=1}render()});
render();
if(location.hash){const el=document.getElementById(location.hash.slice(1));if(el){const f=location.hash.replace('#fam-','');open.add(f);render();document.getElementById(location.hash.slice(1))?.scrollIntoView()}}
</script>
"""

CHALLENGES_PAGE = r"""
<h1 style="margin:.6rem 0 .3rem">Challenge status — openai/math @ <code>__COMMIT8__</code></h1>
<div class="notice">One row per Comparator challenge (405). <strong>Build</strong>: the solution module compiled on the reviewer's machine. <strong>Closure</strong>: every constant in the challenge statement's transitive closure found alpha-equivalent to the solution's, no instance shadowing, only the three standard axioms (<code>checker/</code>). <strong>Comparator (laptop)</strong>: the real <code>leanprover/comparator</code> accepted the solution on the reviewer's laptop, run with its development landrun shim (no sandbox). <strong>Comparator (Linux VM)</strong>: the same check on an isolated Ubuntu VM with the real landrun (Landlock) sandbox, the citable configuration. Logs are in <code>reviews/openai-math/evidence/lean_checks/</code>.</div>
<div class="filters">
  <input type="search" id="q" placeholder="search challenge, family, module…" size="30" aria-label="search">
  <label><input type="checkbox" id="only"> checked here only</label>
  <span class="count" id="count"></span>
</div>
<div class="wrap"><table class="data" id="t">
<thead><tr><th data-k="challenge">Challenge</th><th data-k="family">Family</th><th data-k="family_verdict">Family verdict</th><th>Lab's result label</th><th data-k="cone_oai_lines">Cone (lines)</th><th data-k="build">Build</th><th data-k="closure">Closure</th><th data-k="comparator">Comparator (laptop, shim)</th><th data-k="cloud_comparator">Comparator (Linux VM, landrun)</th><th>Evidence</th></tr></thead>
<tbody id="tb"></tbody>
</table></div>
<p style="color:var(--muted);font-size:.85rem">Download: <a href="https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/challenge-status.csv">challenge-status.csv</a> · <a href="https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/challenge-status.json">challenge-status.json</a> · <a href="data.json">data.json</a>. Generated __GENERATED__.</p>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let sortK='challenge',sortD=1;
const EV='https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/evidence/lean_checks/';const EVC='https://github.com/ceshanon/mathvet/blob/main/reviews/openai-math/evidence/cloud/';
function rows(){const q=document.getElementById('q').value.trim().toLowerCase();const only=document.getElementById('only').checked;
 let r=DATA.filter(d=>(!only||d.machine_check!=='none')&&(!q||[d.challenge,d.family,d.solution_module,d.result_label,d.theorem_names.join(' ')].join(' ').toLowerCase().includes(q)));
 r.sort((a,b)=>{let x=a[sortK],y=b[sortK];if(typeof x==='number')return (x-y)*sortD;return String(x).localeCompare(String(y))*sortD});return r}
function b(d){if(d.build==='built')return `<span class="mc closure-pass">built${d.build_seconds?' ('+d.build_seconds+' s)':''}</span>`;if(d.build==='incomplete')return '<span class="mc build-in-progress">in progress</span>';if(d.build==='failed')return '<span class="mc build-failed">failed</span>';return '<span class="mc none">—</span>'}
function c(d){if(d.closure==='ok')return `<span class="mc closure-pass">ok (${d.closure_constants} constants, ${d.shadowing}, ${(d.axioms||[]).join(', ')})</span>`;if(d.closure==='problems')return `<span class="mc build-failed">problems (${d.closure_problems})</span>`;if(d.closure==='error')return '<span class="mc build-failed">error (see log)</span>';return '<span class="mc none">—</span>'}
function k(d){if(d.comparator==='pass')return `<span class="mc comparator-pass">PASS ${d.comparator_finished?'('+d.comparator_finished.slice(0,10)+')':''}</span>`;if(d.comparator==='running')return '<span class="mc build-in-progress">running</span>';if(d.comparator==='fail')return '<span class="mc build-failed">not accepted (see log)</span>';return '<span class="mc none">—</span>'}
function kc(d){if(d.cloud_comparator==='pass')return `<span class="mc comparator-sandboxed-pass" title="${esc(d.cloud_sandbox||'')}">PASS ${d.cloud_finished?'('+d.cloud_finished.slice(0,10)+')':''}</span>`;if(d.cloud_comparator==='running')return '<span class="mc build-in-progress">running</span>';if(d.cloud_comparator==='fail')return '<span class="mc build-failed">not accepted (see log)</span>';return '<span class="mc none">—</span>'}
function render(){const r=rows();const tb=document.getElementById('tb');tb.innerHTML='';
 for(const d of r){const tr=document.createElement('tr');tr.id='fam-'+d.family;
  tr.innerHTML=`<td><a href="${d.lean_url}"><code>${d.challenge}</code></a></td><td><a href="index.html#fam-${d.family}"><code>${d.family}</code></a></td><td><span class="badge ${d.family_verdict}">${d.family_verdict}</span></td><td>${esc(d.result_label)}</td><td>${d.cone_oai_lines.toLocaleString()}${d.cone_external.length?'<br><small>'+d.cone_external.join(', ')+'</small>':''}</td><td>${b(d)}</td><td>${c(d)}</td><td>${k(d)}</td><td>${kc(d)}</td><td>${[...d.evidence_files.map(f=>`<a href="${EV}${f}">${f.split('.').slice(1).join('.')}</a>`),...(d.cloud_files||[]).map(f=>`<a href="${EVC}${f}">cloud ${f.split('.').slice(1).join('.')}</a>`)].join(' ')||'—'}</td>`;
  tb.appendChild(tr)}
 const n=DATA.filter(d=>d.machine_check!=='none').length;document.getElementById('count').textContent=`${r.length} challenges shown · ${n} with a local check`}
document.querySelectorAll('#q,#only').forEach(e=>e.addEventListener('input',render));
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{const k=th.dataset.k;if(sortK===k)sortD=-sortD;else{sortK=k;sortD=1}render()});
render();
</script>
"""
