const {chromium}=require('playwright');
(async()=>{const [,,inp,outdir,sel,w,h]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h}});
await p.goto('file://'+inp);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
const els=await p.$$(sel);for(let i=0;i<els.length;i++){await els[i].screenshot({path:`${outdir}/${String(i+1).padStart(2,'0')}.png`});}
await b.close();})();
