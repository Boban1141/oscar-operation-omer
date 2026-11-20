"""Test logique du jeu sans carte graphique ni internet.
Remplace Three.js par un faux moteur (stub) et joue le scénario du niveau 1 dans Chrome headless.
Usage : python3 tests/run_logic_tests.py   (nécessite : pip install playwright ; Chrome ou Chromium installé)
"""
import asyncio, os, re, sys, tempfile, shutil
from playwright.async_api import async_playwright
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def build(tmp):
    html=open(os.path.join(ROOT,'game','index.html'),encoding='utf-8').read()
    names=sorted(set(re.findall(r'THREE\.([A-Za-z0-9_]+)',html)))
    stub=("const h={get(t,k){if(k===Symbol.toPrimitive)return()=>0;if(k==='then')return undefined;if(k===Symbol.iterator)return function*(){};"
          "if(!(k in t))t[k]=mk();return t[k]},set(t,k,v){t[k]=v;return true},apply(){return mk()},construct(){return mk()}};"
          "function mk(){return new Proxy(function(){},h)}\n"+"\n".join(f"export const {n}=mk();" for n in names))
    open(os.path.join(tmp,'three.js'),'w').write(stub)
    html=re.sub(r'"three":"[^"]+"','"three":"./three.js"',html).replace('<link href="https://fonts.googleapis.com','<link data-x href="data:,')
    open(os.path.join(tmp,'index.html'),'w',encoding='utf-8').write(html)
SCENARIO='''()=>{const o=window.__oscar,r=[];const ok=(c,m)=>r.push((c?'OK   ':'FAIL ')+m);
  o.startLevel(null);ok(o.objective(o.S).stage===0,'objectif 0 au départ');
  o.enterInterior('house');ok(o.S.location==='house','entrer dans la maison');
  o.readNote();o.closeUI();o.findClue('phone',10);o.closeUI();ok(o.objective(o.S).stage===1,'2 indices -> objectif voisin');
  o.exitInterior();o.openDialogue('henderson');o.choose(0);o.choose(0);o.choose(0);ok(o.S.flags.neighbor,'témoignage du voisin');
  o.enterInterior('diner');o.openDialogue('lina');o.choose(0);o.choose(0);o.choose(0);ok(o.S.tasks.tip==='active','tâche du pot à pourboires');
  o.S.tasks.tip='found';o.openDialogue('lina');o.choose(0);o.choose(0);ok(o.S.flags.leadPort&&o.S.player.bonusEarned===1,'reçu + vie bonus');
  o.openDialogue('marcus');o.choose(0);o.choose(0);o.choose(0);ok(o.S.money===220,'payer Marcus 20 $');
  ok(o.objective(o.S).stage===3,'objectif port');return r;}'''
async def main():
    tmp=tempfile.mkdtemp();build(tmp)
    exe=shutil.which('google-chrome') or shutil.which('chromium') or None
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=exe,args=['--no-sandbox','--allow-file-access-from-files'])
        pg=await b.new_page();errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file://'+os.path.join(tmp,'index.html'));await pg.wait_for_timeout(3500)
        res=await pg.evaluate(SCENARIO);await pg.wait_for_timeout(1000);await b.close()
    for x in res:print(x)
    for e in errs:print('ERREUR JS',e)
    sys.exit(1 if errs or any(x.startswith('FAIL') for x in res) else 0)
asyncio.run(main())
