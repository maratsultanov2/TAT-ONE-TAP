// TAT-Secretary v1.0
// Автоматическая память для DeepSeek

const LAYERS = ["theme", "role", "emotion", "meaning", "goal"];
const DEFAULT_BRAIN = { theme: 0.207, role: 0.198, emotion: 0.197, meaning: 0.201, goal: 0.198 };

function saveBrain(brain) { chrome.storage.local.set({ tat_brain: brain }); }
function loadBrain() {
    return new Promise((resolve) => {
        chrome.storage.local.get(["tat_brain"], (r) => resolve(r.tat_brain || DEFAULT_BRAIN));
    });
}
function saveDiff(diff) { chrome.storage.local.set({ tat_diff: diff }); }
function loadDiff() {
    return new Promise((resolve) => {
        chrome.storage.local.get(["tat_diff"], (r) => resolve(r.tat_diff || null));
    });
}
function weightsToString(w) {
    return LAYERS.map(l => `${l[0]}:${w[l].toFixed(2)}`).join(",");
}
function computeDiff(oldW, newW) {
    return LAYERS.map(l => {
        const d = newW[l] - oldW[l];
        return `${l[0]}:${d > 0 ? "+" : ""}${d.toFixed(2)}`;
    }).join(",");
}
function collectDiff() {
    let newW = { ...DEFAULT_BRAIN };
    let msgs = document.querySelectorAll('[class*="message"]');
    let last = "";
    for (let m of msgs) if (m.innerText?.length > 20) last = m.innerText;
    if (last.length > 300) newW.theme = Math.min(0.5, newW.theme + 0.05);
    return newW;
}
async function saveCurrentState() {
    let old = await loadBrain();
    let newW = collectDiff();
    let diff = computeDiff(old, newW);
    await saveBrain(newW);
    await saveDiff(diff);
    alert(`TAT память сохранена\nDIFF: ${diff}`);
}
async function injectMemory() {
    let brain = await loadBrain();
    let diff = await loadDiff();
    let mem = weightsToString(brain) + (diff ? `\n[DIFF] ${diff}` : "");
    let prefix = `[TAT-MEMORY]\n${mem}\n[/TAT-MEMORY]\n\n`;
    let ta = document.querySelector("textarea");
    if (ta && !ta.value.startsWith("[TAT-MEMORY]")) {
        ta.value = prefix + ta.value;
        ta.dispatchEvent(new Event("input", { bubbles: true }));
    }
}
function addButton() {
    let btn = document.createElement("button");
    btn.innerText = "🧠 TAT-Secretary";
    btn.style.cssText = "position:fixed;bottom:20px;right:20px;z-index:9999;padding:10px 16px;background:#7c3aed;color:white;border:none;border-radius:40px;cursor:pointer;font-size:14px";
    btn.onclick = saveCurrentState;
    document.body.appendChild(btn);
}
setTimeout(() => { injectMemory(); addButton(); }, 3000);
