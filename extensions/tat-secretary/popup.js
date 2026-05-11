document.getElementById("save").onclick = () => {
    chrome.tabs.query({active:true,currentWindow:true},(tabs)=>{
        chrome.tabs.sendMessage(tabs[0].id,{action:"saveMemory"},(r)=>{
            document.getElementById("status").innerHTML = `✅ ${r?.diff || "OK"}`;
        });
    });
};
document.getElementById("clear").onclick = () => {
    chrome.tabs.query({active:true,currentWindow:true},(tabs)=>{
        chrome.tabs.sendMessage(tabs[0].id,{action:"clearMemory"});
        document.getElementById("status").innerHTML = "🗑️ Очищено";
    });
};
chrome.tabs.query({active:true,currentWindow:true},(tabs)=>{
    chrome.tabs.sendMessage(tabs[0].id,{action:"getStatus"},(r)=>{
        if(r) document.getElementById("status").innerHTML = `🧠 BRAIN: ${r.brain}<br>📝 DIFF: ${r.diff || "нет"}`;
    });
});