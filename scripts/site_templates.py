"""HTML, CSS and JS templates for the MathVet static site (docs/)."""

KATEX_HEAD = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
"""

FONTS_HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=STIX+Two+Text:ital,wght@0,400..700;1,400..700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
"""

CSS = r"""
:root{color-scheme:light;
 --paper:#FBFBFA;--ink:#1A1F2B;--ink-2:#454C5A;--margin:#6B7280;--rule:#D9DBDF;--rule-strong:#1A1F2B;--field:#F1F2F4;--tip-bg:#1A1F2B;--tip-fg:#FBFBFA;
 --v-full:#275B9E;--v-partial:#6A9BD8;--v-weaker:#DE9430;--v-supporting:#B5491F;--v-none:#C7CAD0;
 --tier-vm:#275B9E;--tier-laptop:#6A9BD8;--link:#275B9E;--focus:#DE9430;
 --serif:"STIX Two Text",Georgia,"Times New Roman",serif;--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){color-scheme:dark;
 --paper:#14161B;--ink:#E6E7EA;--ink-2:#B9BEC7;--margin:#9AA1AB;--rule:#2B2F37;--rule-strong:#E6E7EA;--field:#1D2027;--tip-bg:#E6E7EA;--tip-fg:#14161B;
 --v-full:#2F6FC2;--v-partial:#1F9E9A;--v-weaker:#B8862A;--v-supporting:#B44238;--v-none:#3A3F48;
 --tier-vm:#2F6FC2;--tier-laptop:#1F9E9A;--link:#8FB3DF;--focus:#B8862A}}
:root[data-theme="dark"]{color-scheme:dark;
 --paper:#14161B;--ink:#E6E7EA;--ink-2:#B9BEC7;--margin:#9AA1AB;--rule:#2B2F37;--rule-strong:#E6E7EA;--field:#1D2027;--tip-bg:#E6E7EA;--tip-fg:#14161B;
 --v-full:#2F6FC2;--v-partial:#1F9E9A;--v-weaker:#B8862A;--v-supporting:#B44238;--v-none:#3A3F48;
 --tier-vm:#2F6FC2;--tier-laptop:#1F9E9A;--link:#8FB3DF;--focus:#B8862A}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:17px;line-height:1.6;font-feature-settings:"onum" 0}
a{color:var(--link);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.14em}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
code,pre{font-family:var(--mono);font-size:.88em}
pre{overflow:auto;padding:.75rem 1rem;border:1px solid var(--rule);background:var(--field)}
h1,h2,h3{font-family:var(--serif);font-weight:500;line-height:1.15;letter-spacing:-.01em;margin:0 0 .6rem}
h1{font-size:clamp(2rem,4.2vw,3.1rem);line-height:1.08;letter-spacing:-.015em;max-width:24ch;margin:0 0 1.2rem}
h2{font-size:1.65rem;margin-top:.2rem}h3{font-size:1.25rem;margin-top:2rem}
p{margin:0 0 1rem}
blockquote{margin:1.2rem 0;padding:0 0 0 1.1rem;border-left:2px solid var(--rule-strong);color:var(--ink-2)}
blockquote p{margin-bottom:.4rem}
ul,ol{padding-left:1.3rem}li{margin:.25rem 0}
header.top{border-bottom:1px solid var(--rule-strong)}
header.top .in{max-width:62rem;margin:0 auto;padding:1rem 1rem .8rem;display:flex;flex-wrap:wrap;gap:.4rem 2rem;align-items:baseline}
header.top .brand{font-family:var(--serif);font-weight:600;font-size:1.35rem;text-decoration:none;color:var(--ink);letter-spacing:-.01em}
header.top .brand span{display:block;font-family:var(--sans);font-weight:400;font-size:.8rem;color:var(--margin);letter-spacing:0}
header.top nav{margin-left:auto;display:flex;flex-wrap:wrap;gap:.2rem 1.2rem;font-family:var(--sans);font-size:.9rem}
header.top nav a{text-decoration:none;color:var(--ink-2);padding-bottom:.15rem;border-bottom:2px solid transparent}
header.top nav a.active{color:var(--ink);border-bottom-color:var(--ink)}header.top nav a:hover{color:var(--ink)}
main{max-width:62rem;margin:0 auto;padding:0 1rem 3rem;overflow-x:clip}
.main img,.main svg,.main table{max-width:100%}
footer{border-top:1px solid var(--rule);color:var(--margin);font-family:var(--sans);font-size:.82rem;line-height:1.5}
footer .in{max-width:62rem;margin:0 auto;padding:1.1rem 1rem 2rem}
/* annotated rows: text beside its evidence */
.row{display:grid;grid-template-columns:minmax(0,40rem) 15rem;column-gap:3rem;padding:2.4rem 0 .6rem}
.row.hero{padding-top:3.2rem}
.row .main{min-width:0}
.row .main>p,.row .main>ul,.row .main>ol,.row .main>blockquote,.row .main>h2+p{max-width:40rem}
.note{border-left:1px solid var(--rule);padding-left:1.25rem;font-family:var(--sans);font-size:.83rem;line-height:1.5;color:var(--margin);align-self:start;position:sticky;top:1.2rem}
.note p{margin:0 0 .75rem}.note .k{color:var(--ink);font-weight:500;margin-bottom:.1rem}
.note a{color:var(--link)}.note code{font-size:.9em}
@media (max-width:64rem){.row{grid-template-columns:minmax(0,1fr);row-gap:0}.note{position:static;border-left:0;border-top:1px solid var(--rule);padding:.8rem 0 0;margin:.6rem 0 1rem;max-width:40rem;display:grid;grid-template-columns:repeat(auto-fill,minmax(16rem,1fr));column-gap:2rem}.note:empty{display:none}}
.fig-note{font-family:var(--sans);font-size:.9rem;color:var(--ink-2);max-width:40rem}
.drift{border-left:3px solid var(--v-weaker);padding:.1rem 0 .1rem 1rem;color:var(--ink-2);font-size:.95rem}
/* the fidelity bar */
.fbar{margin:0 0 1.2rem}
.fbar-track{display:flex;gap:2px;height:3.4rem;margin:.4rem 0 .5rem}
.seg{display:block;min-width:2px;position:relative;outline-offset:1px}
.seg i{display:block;height:100%;background:var(--c);border-radius:2px}
.v-full{--c:var(--v-full)}.v-partial{--c:var(--v-partial)}.v-weaker-statement{--c:var(--v-weaker)}.v-supporting-only{--c:var(--v-supporting)}.v-none{--c:var(--v-none)}
.v-none i,.sw.v-none{background:repeating-linear-gradient(135deg,var(--v-none) 0 2px,transparent 2px 6px);border:1px solid var(--v-none)}
.seg:hover i{filter:brightness(.92)}
.fbar-groups{display:flex;gap:2px;font-family:var(--sans);font-size:.8rem;color:var(--margin);line-height:1.3}
.fbar-groups span{border-top:1px solid var(--rule-strong);padding:.35rem .4rem 0 0;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.fbar-groups b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.fbar-key{list-style:none;margin:1.1rem 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:.5rem 1.6rem;font-family:var(--sans);font-size:.85rem;line-height:1.4}
.fbar-key li{display:grid;grid-template-columns:.85rem minmax(0,1fr);column-gap:.55rem;align-items:start;margin:0}.fbar-key li .sw{margin-top:.2rem}
.fbar-key b{font-weight:600;font-variant-numeric:tabular-nums}.fbar-key .vk{margin-left:.35rem;color:var(--ink)}.fbar-key .vd{display:block;color:var(--margin)}
.sw{display:inline-block;width:.8rem;height:.8rem;border-radius:2px;background:var(--c);vertical-align:-1px}
/* verdicts by subject */
.sbars{margin:0 0 .8rem}
.sbars-rows{display:grid;row-gap:.42rem;margin:.9rem 0 .6rem}
.srow{display:grid;grid-template-columns:15rem minmax(0,1fr) 3.6rem;align-items:center;column-gap:.8rem;font-family:var(--sans);font-size:.84rem}
.slab{text-align:right;color:var(--ink-2);line-height:1.2}
.strack{display:flex;gap:2px;height:.95rem}
.sn{font-variant-numeric:tabular-nums}.sn b{font-weight:600}.sn .of{color:var(--margin)}
.sbars-foot,.cones-foot,.jm-foot{font-family:var(--sans);font-size:.8rem;color:var(--margin);max-width:40rem;margin:.4rem 0 0}
@media (max-width:40rem){.srow{grid-template-columns:8.5rem minmax(0,1fr) 3rem;font-size:.76rem}}
/* the 416 cones */
.cones-fig{margin:0 0 .8rem}
.cones{width:100%;height:auto;display:block;margin:.8rem 0 .4rem;font-family:var(--sans)}
.cones .grid{stroke:var(--rule);stroke-width:1}
.cones .ylab,.cones .xlab,.cones .ann{fill:var(--margin);font-size:11px}
.cones .ann{fill:var(--ink)}
.cones .bar.t-vm{fill:var(--tier-vm)}.cones .bar.t-laptop{fill:var(--tier-laptop)}.cones .bar.t-none{fill:var(--v-none)}
.cones .bar:hover{opacity:.75}
.cones .lead{stroke:var(--ink-2);stroke-width:1}
.cones-key{list-style:none;margin:.3rem 0 0;padding:0;display:flex;flex-wrap:wrap;gap:.3rem 1.6rem;font-family:var(--sans);font-size:.83rem}
.cones-key li{margin:0}.cones-key .sw{margin-right:.45rem}.t-vm.sw{background:var(--tier-vm)}.t-laptop.sw{background:var(--tier-laptop)}
/* judge vs review */
.jm{margin:0 0 .8rem;overflow-x:auto}
.jmt{border-collapse:separate;border-spacing:2px;font-family:var(--sans);font-size:.84rem;margin:.8rem 0 .2rem}
.jmt th{font-weight:500;color:var(--margin);text-align:left;padding:.25rem .5rem;line-height:1.25}
.jmt th[scope=col]{vertical-align:bottom;max-width:6.5rem}
.jmt th[scope=row]{color:var(--ink);white-space:nowrap}
.jmt td{text-align:right;padding:.5rem .65rem;font-variant-numeric:tabular-nums;border-radius:2px;min-width:3.6rem}
.jmt td.cell{background:color-mix(in oklab,var(--v-full) calc(var(--a)*100%),var(--paper));color:var(--ink)}
.jmt td.cell[data-hi]{color:var(--paper)}
.jmt td.cell .z{color:var(--margin)}
.jmt td.diag{box-shadow:inset 0 0 0 2px var(--rule-strong)}
.jmt td.tot{color:var(--margin)}
/* tooltip */
.tip{position:fixed;z-index:20;pointer-events:none;background:var(--tip-bg);color:var(--tip-fg);font-family:var(--sans);font-size:.8rem;line-height:1.35;padding:.35rem .55rem;border-radius:3px;max-width:22rem}
/* prose pages (protocol) */
.prose{max-width:40rem;padding:2.4rem 0 0}
.prose h1{font-size:2.1rem}.prose h2{font-size:1.5rem;margin-top:2.2rem}.prose h3{font-size:1.15rem}
.prose table{border-collapse:collapse;margin:1rem 0;width:100%;font-family:var(--sans);font-size:.9rem}
.prose th,.prose td{border-bottom:1px solid var(--rule);padding:.4rem .6rem;text-align:left;vertical-align:top}
.prose th{font-weight:500;color:var(--margin)}
.prose img{max-width:100%}
/* data pages */
.page-head{padding:2.2rem 0 .4rem}
.page-head h1{font-size:2rem;max-width:none;margin-bottom:.4rem}
.notice{border-left:3px solid var(--v-weaker);padding:.1rem 0 .1rem 1rem;margin:.4rem 0 1.2rem;color:var(--ink-2);font-size:.95rem;max-width:52rem}
.badge{display:inline-block;font-family:var(--sans);font-size:.8rem;font-weight:500;white-space:nowrap;color:var(--ink)}
.badge::before{content:"";display:inline-block;width:.62rem;height:.62rem;border-radius:1px;background:var(--c);margin-right:.38rem;vertical-align:-1px}
.badge.full{--c:var(--v-full)}.badge.partial{--c:var(--v-partial)}.badge.weaker-statement{--c:var(--v-weaker)}.badge.supporting-only{--c:var(--v-supporting)}.badge.none{--c:var(--v-none)}
.chip{display:inline-block;background:var(--field);border-radius:2px;padding:.05rem .4rem;font-family:var(--sans);font-size:.78rem;margin:.1rem .25rem .1rem 0}
.mc{font-family:var(--sans);font-size:.8rem;white-space:nowrap}
.mc.comparator-pass,.mc.comparator-sandboxed-pass,.mc.closure-pass{color:var(--v-full);font-weight:500}
.mc.built{color:var(--ink-2)}.mc.build-in-progress,.mc.none{color:var(--margin)}.mc.build-failed{color:var(--v-supporting)}
.filters{display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:center;margin:.8rem 0;padding:.6rem 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);font-family:var(--sans)}
.filters input[type=search],.filters select{font:inherit;font-size:.9rem;padding:.35rem .5rem;border:1px solid var(--rule);border-radius:2px;background:var(--field);color:var(--ink)}
.filters label{font-size:.88rem;color:var(--ink-2)}.filters .count{margin-left:auto;color:var(--margin);font-size:.85rem;font-variant-numeric:tabular-nums}
table.data{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:.88rem}
table.data th,table.data td{padding:.5rem .5rem;border-bottom:1px solid var(--rule);vertical-align:top;text-align:left}
table.data th{position:sticky;top:0;background:var(--paper);cursor:pointer;user-select:none;font-weight:500;font-size:.82rem;color:var(--margin);border-bottom:1px solid var(--rule-strong)}
table.data tr.row{display:table-row;padding:0;cursor:pointer}table.data tr.row:hover td{background:var(--field)}
table.data tr.details td{background:var(--field);padding:1rem 1.2rem 1.2rem;font-family:var(--serif);font-size:1rem}
.details .k{color:var(--margin);font-family:var(--sans);font-size:.78rem;font-weight:500;margin-top:.8rem}
.details .k:first-child{margin-top:0}.details p{margin:.2rem 0 .4rem;max-width:60rem}
.details ul{margin:.2rem 0 .4rem 1.1rem;padding:0}
.wrap{overflow-x:auto}
.dl{color:var(--margin);font-family:var(--sans);font-size:.82rem;margin-top:1rem}
@media (max-width:640px){table.data{font-size:.82rem}}
@media (prefers-reduced-motion: reduce){*{transition:none!important}}
"""

TIP_JS = """<script>(function(){var t=document.createElement('div');t.className='tip';t.hidden=true;document.body.appendChild(t);var cur=null;
function place(x,y){t.style.left=Math.max(4,Math.min(x+14,window.innerWidth-t.offsetWidth-8))+'px';t.style.top=(y+16)+'px'}
document.addEventListener('mouseover',function(e){var el=e.target.closest?e.target.closest('[data-tip]'):null;if(!el)return;cur=el;t.textContent=el.getAttribute('data-tip');t.hidden=false;place(e.clientX,e.clientY)});
document.addEventListener('mousemove',function(e){if(!t.hidden)place(e.clientX,e.clientY)});
document.addEventListener('mouseout',function(e){if(cur&&!(e.relatedTarget&&cur.contains(e.relatedTarget))){t.hidden=true;cur=null}});
document.addEventListener('focusin',function(e){var el=e.target.closest?e.target.closest('[data-tip]'):null;if(!el)return;var r=el.getBoundingClientRect();t.textContent=el.getAttribute('data-tip');t.hidden=false;t.style.left=r.left+'px';t.style.top=(r.bottom+6)+'px'});
document.addEventListener('focusout',function(){t.hidden=true});})();</script>"""

LAYOUT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="MathVet: independent, pre-referee fidelity reviews of AI-generated Lean formalizations. Does the Lean statement say what the paper claims?">
{fonts}
<link rel="stylesheet" href="{root}style.css">
{extra_head}
</head>
<body>
<header class="top"><div class="in">
  <a class="brand" href="{root}">MathVet<span>independent reviews of AI-generated formal mathematics</span></a>
  <nav>
    <a href="{root}" class="{home}">Review of openai/math</a>
    <a href="{root}openai-math/" class="{table}">Fidelity table</a>
    <a href="{root}openai-math/challenges.html" class="{challenges}">Challenges</a>
    <a href="{root}protocol.html" class="{protocol}">Referee protocol</a>
    <a href="https://github.com/mathvet/mathvet">GitHub</a>
  </nav>
</div></header>
<main>
{body}
</main>
<footer><div class="in">MathVet reviews are independent of every lab whose work they cover and are published under Apache-2.0; the reviewed artefacts are their authors'. Every verdict is pre-referee until the error rate in the <a href="{root}protocol.html">protocol</a> has been published. Upstream commit <code>{commit}</code>; generated {generated}. Corrections: <a href="https://github.com/mathvet/mathvet/issues">open an issue</a>.</div></footer>
{tip_js}
{extra_js}
</body>
</html>
"""


def layout(title, body, active, extra_head='', extra_js='', generated='', commit=''):
    root = '../' if active in ('table', 'challenges') else ''
    cls = {k: ('active' if k == active else '') for k in ('home', 'table', 'challenges', 'protocol')}
    return LAYOUT.format(title=title, body=body, root=root, extra_head=extra_head, extra_js=extra_js, fonts=FONTS_HEAD,
                         tip_js=TIP_JS, generated=generated, commit=commit, **cls)


TABLE_PAGE = r"""
<div class="page-head"><h1>Fidelity table for openai/math at <code>__COMMIT8__</code></h1>
<div class="notice">Every verdict on this page is <strong>pre-referee</strong>: one model-assisted reading per family, validated mechanically, not yet re-read by a named human referee. The repository's own scope note is shown next to each verdict so you can judge for yourself. Verdict scale: <span class="badge full">full</span> Lean states the headline claim; <span class="badge partial">partial</span> only one of several claims, or a special case; <span class="badge weaker-statement">weaker-statement</span> a nontrivially weaker statement; <span class="badge supporting-only">supporting-only</span> a lemma or auxiliary statement. Open a row for the evidence.</div></div>
<div class="filters">
  <input type="search" id="q" placeholder="search family, title, challenge, note" size="34" aria-label="search">
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
<p class="dl">Download: <a href="https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/fidelity-table.csv">fidelity-table.csv</a>, <a href="https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/fidelity-table.json">fidelity-table.json</a>, <a href="https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/formalization-review.yaml">formalization-review.yaml</a>, <a href="data.json">data.json</a>. Generated __GENERATED__.</p>
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
 const papers=d.papers.map(p=>`<a href="${p.url}">${esc(p.title)}</a>`).join('; ');
 return `<div class="details"><div class="k">Headline claim (overview summary)</div><p>${esc(d.headline)}</p>
 <div class="k">MathVet reading (pre-referee): ${esc(d.verdict)}</div><p>${esc(d.review_note)}</p>
 <div class="k">The repository's own scope note (<a href="${d.lab_docs_url}">lean/docs/${d.family}.md</a>, verbatim)</div><p style="white-space:pre-wrap">${esc(d.lab_scope_note)}</p>
 <div class="k">Definitions to check</div>${defs}
 <div class="k">Challenge statements</div><p>${cs}</p>
 <div class="k">Papers</div><p>${papers||'—'}</p>
 <div class="k">Machine check on our machine</div><p>${esc(MC[d.machine_check])}; see <a href="challenges.html#fam-${d.family}">challenge status</a></p>
 ${d.upstream_changed?'<div class="k">Changed upstream since the reviewed commit (not yet re-read)</div><p>'+esc(d.upstream_changed)+'</p>':''}</div>`}
function render(){const r=rows();const tb=document.getElementById('tb');tb.innerHTML='';
 for(const d of r){const tr=document.createElement('tr');tr.className='row';tr.id='fam-'+d.family;
  tr.innerHTML=`<td><code>${d.family}</code>${d.upstream_changed?'<br><span class="chip" title="'+esc(d.upstream_changed)+'">changed upstream</span>':''}</td><td>${esc(d.title)}</td><td>${esc(d.subject)}</td><td><span class="badge ${d.verdict}">${d.verdict}</span></td><td>${d.challenges.map(c=>'<span class="chip">'+c+'</span>').join('')}</td><td>${d.cone_lines_max.toLocaleString()}</td><td><span class="mc ${d.machine_check}">${MC[d.machine_check]}</span></td>`;
  tr.onclick=()=>{if(open.has(d.family))open.delete(d.family);else open.add(d.family);render()};tb.appendChild(tr);
  if(open.has(d.family)){const td=document.createElement('tr');td.className='details';td.innerHTML=`<td colspan="7">${detail(d)}</td>`;tb.appendChild(td);if(window.renderMathInElement)renderMathInElement(td,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});}}
 const c={};for(const d of r)c[d.verdict]=(c[d.verdict]||0)+1;
 document.getElementById('count').textContent=`${r.length} families: ${c['full']||0} full, ${c['partial']||0} partial, ${c['weaker-statement']||0} weaker, ${c['supporting-only']||0} supporting-only`;
 if(window.renderMathInElement)renderMathInElement(tb,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});}
document.querySelectorAll('#q,.v,#subj,#mc,#ext').forEach(e=>e.addEventListener('input',render));
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{const k=th.dataset.k;if(sortK===k)sortD=-sortD;else{sortK=k;sortD=1}render()});
render();
if(location.hash){const el=document.getElementById(location.hash.slice(1));if(el){const f=location.hash.replace('#fam-','');open.add(f);render();document.getElementById(location.hash.slice(1))?.scrollIntoView()}}
</script>
"""

CHALLENGES_PAGE = r"""
<div class="page-head"><h1>Challenge status for openai/math at <code>__COMMIT8__</code></h1>
<div class="notice">One row per Comparator challenge. <strong>Build</strong>: the solution module compiled on the reviewer's machine. <strong>Closure</strong>: every constant in the challenge statement's transitive closure found alpha-equivalent to the solution's, no instance shadowing, only the three standard axioms (<code>checker/</code>). <strong>Comparator (laptop)</strong>: the real <code>leanprover/comparator</code> accepted the solution on the reviewer's laptop, run with its development landrun shim (no sandbox). <strong>Comparator (Linux VM)</strong>: the same check on an isolated Ubuntu VM with the real landrun (Landlock) sandbox, the citable configuration. Logs are in <code>reviews/openai-math/evidence/</code>.</div></div>
<div class="filters">
  <input type="search" id="q" placeholder="search challenge, family, module" size="30" aria-label="search">
  <label><input type="checkbox" id="only"> checked here only</label>
  <span class="count" id="count"></span>
</div>
<div class="wrap"><table class="data" id="t">
<thead><tr><th data-k="challenge">Challenge</th><th data-k="family">Family</th><th data-k="family_verdict">Family verdict</th><th>Lab's result label</th><th data-k="cone_oai_lines">Cone (lines)</th><th data-k="build">Build</th><th data-k="closure">Closure</th><th data-k="comparator">Comparator (laptop, shim)</th><th data-k="cloud_comparator">Comparator (Linux VM, landrun)</th><th>Evidence</th></tr></thead>
<tbody id="tb"></tbody>
</table></div>
<p class="dl">Download: <a href="https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/challenge-status.csv">challenge-status.csv</a>, <a href="https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/challenge-status.json">challenge-status.json</a>, <a href="data.json">data.json</a>. Generated __GENERATED__.</p>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let sortK='challenge',sortD=1;
const REVIEW8='__COMMIT8__';const EV='https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/evidence/lean_checks/';const EVC='https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/evidence/cloud/';
function rows(){const q=document.getElementById('q').value.trim().toLowerCase();const only=document.getElementById('only').checked;
 let r=DATA.filter(d=>(!only||d.machine_check!=='none')&&(!q||[d.challenge,d.family,d.solution_module,d.result_label,d.theorem_names.join(' ')].join(' ').toLowerCase().includes(q)));
 r.sort((a,b)=>{let x=a[sortK],y=b[sortK];if(typeof x==='number')return (x-y)*sortD;return String(x).localeCompare(String(y))*sortD});return r}
function b(d){if(d.build==='built')return `<span class="mc closure-pass">built${d.build_seconds?' ('+d.build_seconds+' s)':''}</span>`;if(d.build==='incomplete')return '<span class="mc build-in-progress">in progress</span>';if(d.build==='timeout')return '<span class="mc build-failed" title="stopped by the time cap on the reviewer\'s 16 GB machine; see the log">not completed (time cap)</span>';if(d.build==='failed')return '<span class="mc build-failed">failed</span>';return '<span class="mc none">—</span>'}
function c(d){if(d.closure==='ok')return `<span class="mc closure-pass">ok (${d.closure_constants} constants, ${d.shadowing}, ${(d.axioms||[]).join(', ')})</span>`;if(d.closure==='problems')return `<span class="mc build-failed">problems (${d.closure_problems})</span>`;if(d.closure==='error')return '<span class="mc build-failed">error (see log)</span>';if(d.closure==='n/a')return '<span class="mc none" title="the challenge file imports the solution\'s own modules, so the re-elaboration check does not apply; the Comparator\'s structural comparison is the check">n/a (imports the solution library)</span>';return '<span class="mc none">—</span>'}
function at(d,k){const c=d[k+'_evidence_commit'];if(!c||c===REVIEW8)return '';const same=d[k+'_statement_unchanged'];return ` <span class="chip" title="${same?'checked at upstream commit '+c+'; the challenge statement is byte-identical at the reviewed commit; the solution checked is the one at '+c:'checked at upstream commit '+c+'; the statement has changed since, so this check does not transfer'}">at ${c.slice(0,7)}${same?'':', statement changed'}</span>`}
function k(d){if(d.comparator==='pass')return `<span class="mc comparator-pass">PASS ${d.comparator_finished?'('+d.comparator_finished.slice(0,10)+')':''}</span>`+at(d,'mac');if(d.comparator==='running')return '<span class="mc build-in-progress">running</span>';if(d.comparator==='timeout')return '<span class="mc build-in-progress" title="the export did not finish within the time cap on the reviewer\'s 16 GB machine; see the log">not completed (time cap)</span>';if(d.comparator==='fail')return '<span class="mc build-failed">not accepted (see log)</span>';return '<span class="mc none">—</span>'}
function kc(d){if(d.cloud_comparator==='pass')return `<span class="mc comparator-sandboxed-pass" title="${esc(d.cloud_sandbox||'')}">PASS ${d.cloud_finished?'('+d.cloud_finished.slice(0,10)+')':''}</span>`+at(d,'cloud');if(d.cloud_comparator==='running')return '<span class="mc build-in-progress">running</span>';if(d.cloud_comparator==='incomplete')return '<span class="mc build-in-progress" title="the challenge config enables the external nanoda kernel, which is not installed on the VM; Lean\'s kernel and the structural comparison accepted the solution">incomplete (nanoda kernel unavailable)</span>';if(d.cloud_comparator==='fail')return '<span class="mc build-failed">not accepted (see log)</span>';return '<span class="mc none">—</span>'}
function render(){const r=rows();const tb=document.getElementById('tb');tb.innerHTML='';
 for(const d of r){const tr=document.createElement('tr');tr.id='fam-'+d.family;
  tr.innerHTML=`<td><a href="${d.lean_url}"><code>${d.challenge}</code></a></td><td><a href="index.html#fam-${d.family}"><code>${d.family}</code></a></td><td><span class="badge ${d.family_verdict}">${d.family_verdict}</span></td><td>${esc(d.result_label)}</td><td>${d.cone_oai_lines.toLocaleString()}${d.cone_external.length?'<br><small>'+d.cone_external.join(', ')+'</small>':''}</td><td>${b(d)}</td><td>${c(d)}</td><td>${k(d)}</td><td>${kc(d)}</td><td>${[...d.evidence_files.map(f=>`<a href="${EV}${f}">${f.split('.').slice(1).join('.')}</a>`),...(d.cloud_files||[]).map(f=>`<a href="${EVC}${f}">cloud ${f.split('.').slice(1).join('.')}</a>`)].join(' ')||'—'}</td>`;
  tb.appendChild(tr)}
 const n=DATA.filter(d=>d.machine_check!=='none').length;document.getElementById('count').textContent=`${r.length} challenges shown, ${n} with a local check`}
document.querySelectorAll('#q,#only').forEach(e=>e.addEventListener('input',render));
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{const k=th.dataset.k;if(sortK===k)sortD=-sortD;else{sortK=k;sortD=1}render()});
render();
</script>
"""
