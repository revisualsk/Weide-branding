const {chromium}=require('playwright');
(async()=>{const [,,inp,outdir]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:2600,height:2600}});
await p.goto('file://'+inp);await p.waitForTimeout(300);
for(const el of await p.$$('.l')){const n=await el.getAttribute('data-n');await el.screenshot({path:`${outdir}/${n}.png`,omitBackground:true});}
await b.close();})();
