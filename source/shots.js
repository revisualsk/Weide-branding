const {chromium}=require('playwright');
(async()=>{const [,,inp,outdir]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
await p.goto('file://'+inp);await p.addStyleTag({content:'.deck{padding:0!important;gap:0!important}.sw{max-width:none!important}.slide{box-shadow:none!important}'});
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
const els=await p.$$('.slide');for(let i=0;i<els.length;i++){await els[i].screenshot({path:`${outdir}/slide-${String(i+1).padStart(2,'0')}.png`});}
await b.close();})();
