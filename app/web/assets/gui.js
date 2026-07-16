/* Shared helpers for ARC's browser GUIs (feature + settings consoles).
   Loaded at /assets/gui.js.  Framework-free, no build step.  Keep this the
   single source of truth for DOM/AJAX/theme/modal utilities both pages use. */

/* ---- DOM + escaping ---- */
function esc(s){return String(s==null?"":s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}
function escA(s){return esc(s).replace(/"/g,"&quot;");}
function el(tag,cls,html){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e;}
function matchTxt(t,q){if(!q)return true;const n=String(t).toLowerCase().replace(/[-_]/g," ");
  try{return new RegExp("(?<![a-z])"+q.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"(?![a-z])","i").test(n);}catch(e){return n.includes(q.toLowerCase());}}

/* ---- AJAX ---- */
async function api(p){const r=await fetch(p);return r.json();}
async function post(p,b){const r=await fetch(p,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(b||{})});
  const j=await r.json();if(!r.ok||j.error)throw new Error(j.error||"failed");return j;}

/* ---- feedback ---- */
let _tt;function toast(m,e){const t=document.getElementById("toast");if(!t)return;t.textContent=m;t.className="toast show"+(e?" err":"");
  clearTimeout(_tt);_tt=setTimeout(()=>t.className="toast"+(e?" err":""),2500);}
function flash(node){node.classList.add("saved");setTimeout(()=>node.classList.remove("saved"),1000);}

/* ---- help modal ---- */
function qmark(qs){const b=document.createElement("button");b.className="qmark";b.textContent="?";b.title="Help";
  b.onclick=(e)=>{e.stopPropagation();showHelp(qs);};return b;}
async function showHelp(qs){const body=document.getElementById("mbody");if(!body)return;body.innerHTML="<p>Loading…</p>";
  document.getElementById("modal").classList.add("show");
  try{const r=await api("/api/help?"+qs);body.innerHTML=r.html||"<p>No help.</p>";}catch(e){body.innerHTML="<p>Could not load help.</p>";}}
function wireModal(){const mc=document.getElementById("mclose");if(mc)mc.onclick=()=>document.getElementById("modal").classList.remove("show");}

/* ---- theme (shared GUI theme system) ---- */
function applyThemeColors(colors){const r=document.documentElement;
  Object.entries(colors||{}).forEach(([k,v])=>{if(v)r.style.setProperty(k,v);});}
function toggleLightDark(){const r=document.documentElement;
  r.setAttribute("data-theme",r.getAttribute("data-theme")==="dark"?"light":"dark");}

/* ---- Save & Exit ---- : tells the server to shut down, then shows the
   "you can close this tab" overlay.  Browsers won't let a page close a tab it
   didn't open, so the user closes the tab/window themselves. */
async function saveExit(){try{await fetch("/api/close",{method:"POST"});}catch(e){}
  stopHeartbeat();
  const cv=document.getElementById("closedv");if(cv)cv.classList.add("show");}

/* ---- tab-lifecycle heartbeat ----
   The server BLOCKS the CLI while a console is open and only unblocks on an
   explicit close.  If the user closes the tab without Save & Exit, no fetch
   fires and the CLI would hang forever.  Two safeguards:
     1. `pagehide` beacon — fires on tab/window close (not tab switch) and
        reliably delivers even as the page is torn down, so the server closes
        instantly in the common case.
     2. periodic `/api/ping` — a liveness heartbeat; if the beacon is missed
        (crash, forced kill, sleep) the server's watchdog reaps it after a
        timeout.  Backgrounded (not closed) tabs keep pinging, so they survive.
*/
let _hb=null;
function startHeartbeat(){if(_hb)return;
  const ping=()=>{try{fetch("/api/ping",{method:"POST",keepalive:true});}catch(e){}};
  ping();_hb=setInterval(ping,10000);
  window.addEventListener("pagehide",()=>{
    try{navigator.sendBeacon("/api/close");}catch(e){
      try{fetch("/api/close",{method:"POST",keepalive:true});}catch(_){}}
  });}
function stopHeartbeat(){if(_hb){clearInterval(_hb);_hb=null;}}
document.addEventListener("DOMContentLoaded",startHeartbeat);

/* =====================================================================
   Reusable widget library (shared by all ARC browser consoles).
   Build new GUIs from these so every console looks/behaves the same.
   ===================================================================== */

/* ---- form inputs ---- */
function numInput(id,val,min){return `<input id="${id}" type="number" min="${min==null?0:min}" value="${val}" class="w-num"/>`;}
function txtInput(id,val,ph){return `<input id="${id}" type="text" value="${escA(val==null?"":val)}" placeholder="${escA(ph||"")}" class="w-txt"/>`;}
function secInput(id,ph){return `<input id="${id}" type="password" placeholder="${escA(ph||"")}" autocomplete="new-password" class="w-txt"/>`;}
function txtArea(id,val,rows){return `<textarea id="${id}" spellcheck="false" class="w-area" style="min-height:${(rows||8)*1.4}em">${esc(val==null?"":val)}</textarea>`;}
function selInput(id,options,selected){return `<select id="${id}" class="w-txt">${options.map(o=>{const v=o.v!=null?o.v:o,l=o.label!=null?o.label:o;return `<option value="${escA(v)}" ${v===selected?"selected":""}>${esc(l)}</option>`;}).join("")}</select>`;}

/* ---- toggle ---- */
function toggleHtml(id,on){return `<button id="${id}" class="toggle ${on?"on":""}" data-on="${on?1:0}" type="button"><span class="knob"></span></button>`;}
function wireToggle(id,cb){const t=document.getElementById(id);if(!t)return;t.onclick=()=>{const on=t.dataset.on==="1";t.dataset.on=on?"0":"1";t.classList.toggle("on",!on);if(cb)cb(!on);};}
function toggleVal(id){const t=document.getElementById(id);return !!(t&&t.dataset.on==="1");}

/* ---- segmented control ---- : options=[{v,label}], onChange(v) */
function segmented(id,options,selected,onChange){
  const wrap=el("div","seg segmented");wrap.id=id;
  options.forEach(o=>{const b=el("button",o.v===selected?"sel":"",esc(o.label));b.type="button";b.dataset.v=o.v;
    b.onclick=()=>{wrap.querySelectorAll("button").forEach(x=>x.classList.toggle("sel",x.dataset.v===o.v));if(onChange)onChange(o.v);};
    wrap.appendChild(b);});
  return wrap;
}

/* ---- layout ---- */
function pageHead(title,topic){const ph=el("div","phead");ph.appendChild(el("h1",null,esc(title)));
  if(topic)ph.appendChild(qmark("topic="+topic));return ph;}
function panel(title,topic){const p=el("div","section-block");const h=el("div","panel-head");
  h.appendChild(el("h2",null,esc(title)));if(topic)h.appendChild(qmark("topic="+topic));p.appendChild(h);return p;}
function fieldRow(label,inputHtml,opts){opts=opts||{};const r=el("div","field-row");
  const lab=el("div","field-label");lab.innerHTML=`${esc(label)}${opts.hint?`<span class="field-hint">${esc(opts.hint)}</span>`:""}`;
  if(opts.help){lab.appendChild(qmark("topic="+opts.help));}
  r.appendChild(lab);const wrap=el("div","field-input");
  if(typeof inputHtml==="string")wrap.innerHTML=inputHtml;else wrap.appendChild(inputHtml);
  r.appendChild(wrap);return r;}
function saveBar(onSave,label){const bar=el("div","save-bar");const b=el("button","btn primary",label||"Save");
  b.type="button";b.onclick=onSave;bar.appendChild(b);return bar;}

/* ---- stat cards (dashboard) ---- : status = ok|warn|bad|"" */
function statCard(label,valueHtml,opts){opts=opts||{};const c=el("div","stat"+(opts.wide?" wide":"")+(opts.big?" big":""));
  const dot=opts.status?`<span class="d ${opts.status}"></span>`:"";
  c.innerHTML=`<div class="k">${esc(label)}${opts.help?"":""}</div><div class="v">${dot}${valueHtml}</div>${opts.sub?`<div class="sub">${opts.sub}</div>`:""}`;
  if(opts.help)c.querySelector(".k").appendChild(qmark("topic="+opts.help));
  return c;}
function statGrid(cards){const g=el("div","cards");cards.forEach(c=>g.appendChild(c));return g;}

/* ---- line-list editor ---- : add/remove single-line rows (like aliases)
   opts={items:[str], placeholder, addLabel, onChange(items)} → element */
function lineListEditor(opts){opts=opts||{};let items=(opts.items||[]).slice();
  const box=el("div","line-list");
  function emit(){if(opts.onChange)opts.onChange(items.slice());}
  function render(){box.innerHTML="";
    items.forEach((val,i)=>{const row=el("div","ll-row");
      const inp=el("input","w-txt");inp.value=val;inp.placeholder=opts.placeholder||"";
      inp.oninput=()=>{items[i]=inp.value;emit();};
      const del=el("button","btn sm ll-del","✕");del.type="button";del.title="Remove";
      del.onclick=()=>{items.splice(i,1);render();emit();};
      row.appendChild(inp);row.appendChild(del);box.appendChild(row);});
    const add=el("button","btn sm ll-add","+ "+(opts.addLabel||"Add line"));add.type="button";
    add.onclick=()=>{items.push("");render();emit();
      const inputs=box.querySelectorAll(".ll-row input");if(inputs.length)inputs[inputs.length-1].focus();};
    box.appendChild(add);}
  render();box.getItems=()=>items.slice();return box;}

/* ---- key/value editor ---- : rows of key→value; some may be read-only labels
   opts={entries:[{key,value,readonly,label,help}], addable, onChange(entries), addLabel} */
function kvListEditor(opts){opts=opts||{};let entries=(opts.entries||[]).map(e=>Object.assign({},e));
  const box=el("div","kv-list");
  function emit(){if(opts.onChange)opts.onChange(entries.map(e=>Object.assign({},e)));}
  function render(){box.innerHTML="";
    entries.forEach((e,i)=>{
      if(e.readonly&&e.label){const hdr=el("div","kv-label",esc(e.label));box.appendChild(hdr);return;}
      const row=el("div","kv-row");
      const k=el("input","w-txt kv-k");k.value=e.key||"";k.placeholder="key";k.disabled=!!e.lockKey;
      k.oninput=()=>{e.key=k.value;emit();};
      const arrow=el("span","kv-arrow","→");
      const v=el("input","w-txt kv-v");v.value=e.value==null?"":e.value;v.placeholder="value";
      v.oninput=()=>{e.value=v.value;emit();};
      row.appendChild(k);row.appendChild(arrow);row.appendChild(v);
      if(e.help)row.appendChild(qmark("topic="+e.help));
      if(!e.locked){const del=el("button","btn sm ll-del","✕");del.type="button";del.title="Remove";
        del.onclick=()=>{entries.splice(i,1);render();emit();};row.appendChild(del);}
      box.appendChild(row);});
    if(opts.addable){const add=el("button","btn sm ll-add","+ "+(opts.addLabel||"Add"));add.type="button";
      add.onclick=()=>{entries.push({key:"",value:""});render();emit();};box.appendChild(add);}}
  render();box.getEntries=()=>entries.map(e=>Object.assign({},e));return box;}
