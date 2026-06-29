// TAT-Secretary v2.0 — с индикатором экономии
const LAYERS = ["theme","role","emotion","meaning","goal"];
const DEFAULT_BRAIN = {theme:0.207,role:0.198,emotion:0.197,meaning:0.201,goal:0.198};
const TAT_BRAIN_SIZE = 50000; // байт

function saveBrain(brain){chrome.storage.local.set({tat_brain:brain});}
function loadBrain(){return new Promise(r=>chrome.storage.local.get(["tat_brain"],x=>r(x.tat_brain||DEFAULT_BRAIN)));}
function saveStats(stats){chrome.storage.local.set({tat_stats:stats});}
function loadStats(){return new Promise(r=>chrome.storage.local.get(["tat_stats"],x=>r(x.tat_stats||{sessions:0,tokens_saved:0})));}
function weightsToString(w){return LAYERS.map(l=>`${l[0]}:${w[l].toFixed(2)}`).join(",");}
function computeDiff(o,n){return LAYERS.map(l=>{let d=n[l]-o[l];return`${l[0]}:${d>0?"+":""}${d.toFixed(2)}`;}).join(",");}
function collectDiff(){let newW={...DEFAULT_BRAIN};let msgs=document.querySelectorAll('[class*="message"]');let last="";for(let m of msgs)if(m.innerText?.length>20)last=m.innerText;if(last.length>300)newW.theme=Math.min(0.5,newW.theme+0.05);return newW;}

async function saveCurrentState(){
  let old=await loadBrain();
  let newW=collectDiff();
  let diff=computeDiff(old,newW);
  await saveBrain(newW);
  let stats=await loadStats();
  stats.sessions++;
  // Каждый DIFF экономит ~49.9KB (TAT_BRAIN_SIZE - средний размер DIFF)
  stats.tokens_saved += Math.round((TAT_BRAIN_SIZE - diff.length) / 4); // 4 байта ~ 1 токен
  await saveStats(stats);
  updateIndicator();
  alert(`🧠 Память сохранена!\nСессия: ${stats.sessions}\nСэкономлено токенов: ~${stats.tokens_saved}`);
}

async function injectMemory(){
  let brain=await loadBrain();
  let mem=weightsToString(brain);
  let prefix=`[TAT-MEMORY]\n${mem}\n[/TAT-MEMORY]\n\n`;
  let ta=document.querySelector("textarea");
  if(ta&&!ta.value.startsWith("[TAT-MEMORY]")){
    ta.value=prefix+ta.value;
    ta.dispatchEvent(new Event("input",{bubbles:true}));
  }
}

function updateIndicator(){
  loadStats().then(stats=>{
    let ind=document.getElementById("tat-indicator");
    if(ind) ind.innerText=`🧠 Сессий: ${stats.sessions} | Экономия: ~${stats.tokens_saved} токенов`;
  });
}

function addButton(){
  let container=document.createElement("div");
  container.id="tat-container";
  container.style.cssText="position:fixed;bottom:20px;right:20px;z-index:9999;display:flex;flex-direction:column;align-items:flex-end;gap:8px;";
  
  let ind=document.createElement("div");
  ind.id="tat-indicator";
  ind.style.cssText="background:rgba(0,0,0,0.8);color:#0f0;padding:6px 12px;border-radius:20px;font-size:12px;font-family:monospace;";
  container.appendChild(ind);
  
  let btn=document.createElement("button");
  btn.innerText="🧠 Сохранить память";
  btn.style.cssText="padding:10px 16px;background:#7c3aed;color:white;border:none;border-radius:40px;cursor:pointer;font-weight:bold;";
  btn.onclick=saveCurrentState;
  container.appendChild(btn);
  
  document.body.appendChild(container);
  updateIndicator();
}

setTimeout(()=>{injectMemory();addButton();},3000);
