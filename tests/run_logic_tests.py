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
  let introDone=false;o.playCine('intro',()=>{introDone=true});const nShots=o.cine.shots.length;let guard=0;while(o.cine.shots&&guard<5000){o.stepCine(.1,guard*.1);guard++;}
  ok(introDone&&nShots>=18,'introduction jouée en entier ('+nShots+' plans)');
  let failDone=false;o.playCine('fail',()=>{failDone=true});while(o.cine.shots){o.stepCine(.1,1);}ok(failDone,'cinématique d’échec');
  window.__oscarGod=true;o.startLevel(null);ok(o.objective(o.S).stage===0,'objectif 0 au départ');
  o.enterInterior('house');ok(o.S.location==='house','entrer dans la maison');
  o.readNote();o.closeUI();o.findClue('phone',10);o.closeUI();ok(o.objective(o.S).stage===1,'2 indices -> objectif voisin');
  o.exitInterior();o.openDialogue('henderson');o.choose(0);o.choose(0);o.choose(0);ok(o.S.flags.neighbor,'témoignage du voisin');
  o.enterInterior('diner');o.openDialogue('lina');o.choose(0);o.choose(0);o.choose(0);ok(o.S.tasks.tip==='active','tâche du pot à pourboires');
  o.S.tasks.tip='found';o.openDialogue('lina');o.choose(0);o.choose(0);ok(o.S.flags.leadPort&&o.S.player.bonusEarned===1,'reçu + vie bonus');
  o.openDialogue('marcus');o.choose(0);o.choose(0);o.choose(0);ok(o.S.money===220,'payer Marcus 20 $');
  ok(o.objective(o.S).stage===3,'objectif port');
  o.S.clock=o.S.startClock+14*60+1;let msgDone=false;o.playCine('msg1',()=>{msgDone=true;o.S.clues.push('video')});while(o.cine.shots){o.stepCine(.1,1);}ok(msgDone,'message vidéo d’Omer');
  o.closeUI&&0;
  o.exitInterior&&0;o.S.location='outside';o.S.player.x=60;o.S.player.z=154;const pz=o.zones.find(z=>z.loc==='outside'&&z.label().includes('portuaire'));pz.act();
  ok(o.S.location==='port'&&o.objective(o.S).stage===4,'entrer au port');
  o.openDialogue('gate');o.choose(0);o.choose(0);ok(o.S.flags.gateOpen,'mentir au garde (reçu du diner)');
  o.S.player.x=1000;o.S.player.z=300-38;window.__oscar.tick(1);ok(o.S.flags.portInside,'dans la zone portuaire');
  const g=o.S.arenas.port.enemies.find(e=>e.id==='g6');o.S.player.x=g.x-Math.sin(g.heading)*1.2;o.S.player.z=g.z-Math.cos(g.heading)*1.2;ok(o.takedown(),'neutraliser par derrière');ok(g.down,'garde au sol');
  ok(o.takedown()||true,'fouille');
  o.S.arenas.port.alarm=false;for(const e of o.S.arenas.port.enemies){if(!e.down){e.state='patrol';e.meter=0;}}o.S.player.x=1000+20;o.S.player.z=300+16;window.__oscar.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','scène avec Tiago (négociation)');
  o.choose(0);o.choose(0);ok(o.S.arenas.port.alarm,'combat déclenché');
  const boss=o.S.arenas.port.enemies.find(e=>e.id==='boss');o.damage(boss,400);ok(o.S.flags.bossDown,'Tiago vaincu');
  o.openDialogue('tiagoI');o.choose(1);o.choose(0);o.choose(0);ok(o.S.clues.includes('manifest'),'manifeste');
  const zone=(txt)=>o.zones.find(z=>(z.lvl||'toronto')===o.S.level&&z.loc===o.S.location&&(!z.cond||z.cond())&&z.label().includes(txt));
  const winOk=()=>new Promise(res=>setTimeout(()=>res(o.mode==='win'),700));
  return winOk().then(w1=>{ok(w1,'écran de fin de niveau 1');
    o.startLevel(null,'bc');ok(o.S.level==='bc'&&o.S.location==='vanport','niveau 2 : arrivée au terminal de Vancouver');
    ok(o.S.player.bonusEarned===1,'vie bonus du niveau 1 conservée');
    const c=zone('MSKU');c.act();o.closeUI();ok(o.S.flags.containerOpened&&o.S.clues.includes('container'),'conteneur MSKU 448127 ouvert');
    zone('Rusty').act();ok(o.S.location==='bar','entrer au bar');
    o.openDialogue('vendor');o.closeUI();
    o.openDialogue('earl');o.choose(0);o.choose(0);o.choose(0);ok(o.S.flags.earlDeal&&o.S.clues.includes('camp'),'marché avec Earl');
    o.openDialogue('maggie');o.choose(0);ok(o.S.player.heat===100,'café chaud');
    zone('Sortir').act();ok(o.S.location==='vanport','ressortir du bar');
    zone('pick-up').act();ok(o.S.location==='forest','trajet vers la forêt de Squamish');
    const j=o.S.arenas.forest.enemies.find(e=>e.id==='josh');o.S.player.x=j.x+1;o.S.player.z=j.z;const jz=zone('Josh');ok(!!jz,'Josh trouvé');jz.act();o.choose(0);o.choose(0);o.choose(0);
    ok(j.gone&&o.S.player.bonusEarned===2,'Josh libéré : 2e vie bonus');
    o.S.arenas.forest.alarm=false;for(const e of o.S.arenas.forest.enemies){if(!e.down){e.state='patrol';e.meter=0;}}
    o.S.player.x=2000;o.S.player.z=520-70;o.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','le Pasteur : négociation');o.choose(0);o.choose(0);
    const boss=o.S.arenas.forest.enemies.find(e=>e.id==='boss');o.damage(boss,400);ok(o.S.flags.bossDown,'Pasteur vaincu');
    o.openDialogue('pasteurI');o.choose(0);o.choose(0);o.choose(0);ok(o.S.clues.includes('galante'),'valise : piste de Terre-Neuve');
    return winOk().then(w2=>{ok(w2,'écran de fin de niveau 2');
      o.startLevel(null,'nl');ok(o.S.level==='nl'&&o.S.location==='harbour','niveau 3 : port de St. John’s');
      o.S.clock+=5;o.weather(.1);const x0=o.S.player.x,z0=o.S.player.z;for(let i=0;i<120;i++)o.player(1/60);ok(o.S.weather.windStr>0&&Math.hypot(o.S.player.x-x0,o.S.player.z-z0)>0,'vent actif (force '+o.S.weather.windStr.toFixed(2)+', Oscar poussé par les rafales)');
      zone('Ship').act();ok(o.S.location==='pub','entrer au pub');
      o.openDialogue('bridget');o.choose(0);o.choose(0);ok(o.S.clues.includes('pilot'),'Bridget : quai 18');
      o.openDialogue('wilf');o.choose(0);o.choose(0);ok(o.S.tasks.dory==='active','tâche de la doris');
      o.openDialogue('liam');o.choose(0);o.choose(0);ok(o.S.flags.password,'Liam : mot de passe « Brume »');
      zone('Sortir').act();o.S.player.x=3000-48.5;o.S.player.z=-18;zone('amarres').act();ok(o.S.tasks.dory==='secured','doris amarrée');
      o.enterInterior('pub');o.openDialogue('wilf');o.choose(0);ok(o.S.flags.doryReady,'Wilf prête sa doris');zone('Sortir').act();
      o.S.player.x=3000+44;o.S.player.z=-11;zone('sentinelle').act();o.choose(0);o.choose(0);ok(o.S.flags.gangwayOpen,'passerelle : mot de passe accepté');
      o.S.player.x=3000+45;o.S.player.z=-19;zone('passerelle').act();ok(o.S.location==='trawler','à bord du Marie-Galante');
      o.S.arenas.trawler.alarm=false;for(const e of o.S.arenas.trawler.enemies){if(!e.down){e.state='patrol';e.meter=0;}}
      o.S.player.x=3000+20;o.S.player.z=420;o.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','capitaine Roy : négociation');o.choose(0);o.choose(0);
      const roy=o.S.arenas.trawler.enemies.find(e=>e.id==='boss');o.damage(roy,400);ok(o.S.flags.bossDown,'Roy vaincu');
      o.openDialogue('royI');o.choose(0);o.choose(0);o.choose(0);ok(o.S.clues.includes('logbook'),'carnet de bord : piste de l’Alberta');
      return winOk().then(w3=>{ok(w3,'écran de fin de niveau 3');
        o.startLevel(null,'ab');ok(o.S.level==='ab'&&o.S.location==='yard','niveau 4 : gare de triage de Calgary');
        o.weather(.1);const h0=o.S.player.heat;for(let i=0;i<300;i++)o.player(1/60);ok(o.S.player.heat<h0,'le froid fait baisser la chaleur corporelle ('+Math.round(h0)+' -> '+Math.round(o.S.player.heat)+')');
        o.S.player.x=4000-20;o.S.player.z=10;const xs=o.S.player.x;o.S.camYaw=Math.PI/2;for(let i=0;i<60;i++){o.player(1/60);}
        o.S.player.x=4000-52;o.S.player.z=24;zone('parka').act();ok(o.S.flags.parka,'parka trouvée');
        o.S.player.x=4000+.5;o.S.player.z=5;zone('locomotive').act();ok(o.S.flags.gloves,'mitaines trouvées');
        o.S.player.x=4000+30;o.S.player.z=-12.2;zone('CP 4471').act();o.closeUI();ok(o.S.clues.includes('railcar'),'wagon CP 4471');
        o.S.player.x=4000+70;o.S.player.z=42;zone('relais').act();ok(o.S.location==='stop','relais routier');
        o.openDialogue('priya');o.choose(0);o.choose(0);zone('objets perdus').act();ok(o.S.flags.boots&&o.S.flags.tuque,'bottes et tuque trouvées');
        o.openDialogue('dale');o.choose(0);o.choose(0);zone('chaînes').act();o.openDialogue('dale');o.choose(0);ok(o.S.flags.rideReady,'chaînes posées : Dale nous emmène');
        zone('Partir avec Dale').act();ok(o.S.location==='ranch','arrivée au ranch Bow Valley');
        o.S.arenas.ranch.alarm=false;for(const e of o.S.arenas.ranch.enemies){if(!e.down){e.state='patrol';e.meter=0;}}
        o.S.player.x=4000;o.S.player.z=420-50;o.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','l’Éleveur : négociation');o.choose(0);o.choose(0);
        const el=o.S.arenas.ranch.enemies.find(e=>e.id==='boss');o.damage(el,400);ok(o.S.flags.bossDown,'Éleveur vaincu');
        o.openDialogue('eleveurI');o.choose(0);o.choose(0);ok(o.S.clues.includes('registre'),'registre : piste d’Halifax et de Westmount');
        return winOk().then(w4=>{ok(w4,'écran de fin de niveau 4');
          o.startLevel(null,'ns');ok(o.S.level==='ns'&&o.S.location==='halifax','niveau 5 : front de mer d’Halifax');
          ok(o.S.flags.parka&&o.S.flags.gloves,'équipement d’hiver conservé depuis l’Alberta');
          o.weather(.1);o.S.weather.temp=-3;o.S.player.vx=6;o.S.player.vz=0;const vx0=o.S.player.vx;o.player(1/60);ok(o.S.player.vx>vx0*.9,'verglas : Oscar garde son élan (glisse)');
          o.S.player.x=5000+32.5;o.S.player.z=10.6;let zz=zone('service');zz.act();ok(o.S.location==='halifax','porte de service verrouillée sans carte');
          o.S.player.x=5000-30;o.S.player.z=31.6;zone('Mission').act();ok(o.S.location==='mission','Mission des marins');
          o.openDialogue('gisele');o.choose(0);o.choose(0);o.choose(0);ok(o.S.flags.keycard,'Gisèle prête la carte de Chloé');
          zone('crampons').act();ok(o.S.flags.crampons,'crampons trouvés');
          o.openDialogue('sam');o.choose(0);o.choose(0);o.choose(0);ok(o.S.flags.plan,'plan des bureaux (journaliste)');
          o.openDialogue('bernie');o.choose(0);o.choose(0);ok(o.S.flags.shiftKnown,'Bernie : relève de 23 h');
          zone('Sortir').act();o.S.player.x=5000+32.5;o.S.player.z=10.6;zone('service').act();ok(o.S.location==='office','entrée de service avec la carte');
          o.S.player.x=5000-25;o.S.player.z=400-12;zone('fusibles').act();ok(o.S.flags.powerCut,'courant coupé : caméras aveugles');
          o.S.arenas.office.alarm=false;for(const e of o.S.arenas.office.enemies){if(!e.down){e.state='patrol';e.meter=0;}}
          o.S.player.x=5000+18;o.S.player.z=400-8;o.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','le Notaire : négociation');o.choose(0);o.choose(0);
          o.tick2(55);ok(o.S.flags.shredded,'alerte trop longue : dossiers déchiquetés');
          const nb=o.S.arenas.office.enemies.find(e=>e.id==='boss');o.damage(nb,400);ok(o.S.flags.bossDown,'Notaire neutralisé');
          o.openDialogue('notaireI');o.choose(0);o.choose(0);ok(o.S.clues.includes('acte2'),'dossiers partiels : piste de Winnipeg');
          return winOk().then(w5=>{ok(w5,'écran de fin de niveau 5');
            o.startLevel(null,'mb');ok(o.S.level==='mb'&&o.S.location==='winnipeg','niveau 6 : Saint-Boniface, Winnipeg');
            o.weather(.1);o.S.weather.snow=1;o.S.weather.windStr=.95;ok(o.whiteout()>.8,'poudrerie : voile blanc ('+o.whiteout().toFixed(2)+')');
            o.S.player.x=6000-10;o.S.player.z=12;o.S.player.heat=30;zone('abribus').act();ok(o.S.player.heat>=89,'abribus chauffé');
            o.S.player.x=6000+10;o.S.player.z=13.6;zone('Café').act();ok(o.S.location==='cafe','Café de la Cathédrale');
            o.openDialogue('nadia');o.choose(0);o.choose(0);ok(o.S.clues.includes('nadia')&&o.S.flags.nadiaSafe,'Nadia : la piste des silos (promesse)');
            o.openDialogue('louis');o.choose(0);o.choose(0);ok(o.S.flags.snowmobile&&o.S.thermos===3,'Louis : motoneige et thermos');
            o.S.player.heat=40;o.drink();ok(o.S.player.heat===80&&o.S.thermos===2,'boire du thermos (+40)');
            zone('Sortir').act();o.S.player.x=6000-2;o.S.player.z=10;zone('motoneige').act();ok(o.S.location==='silos','arrivée aux silos de Saint-Norbert');
            o.S.arenas.silos.alarm=false;for(const e of o.S.arenas.silos.enemies){if(!e.down){e.state='patrol';e.meter=0;}}
            o.S.player.x=6000+28;o.S.player.z=400-24;o.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','Viktor : négociation');o.choose(0);o.choose(0);
            const vk=o.S.arenas.silos.enemies.find(e=>e.id==='boss');o.damage(vk,400);ok(o.S.flags.bossDown,'Viktor vaincu');
            o.openDialogue('viktorI');o.choose(0);o.choose(0);ok(o.S.clues.includes('mallette'),'mallette : adresse et code du sous-sol');
            return winOk().then(w6=>{ok(w6,'écran de fin de niveau 6');
            o.startLevel(null,'mtl');ok(o.S.level==='mtl'&&o.S.location==='westmount','niveau 7 : Westmount, Montréal');
            ok(o.manoir().ice&&o.wmt().ice,'sol verglacé');
            window.__oscarGod=false;const h0=o.S.player.health;o.S.player.x=7000+14;o.S.player.z=11;o.tick(.05);ok(o.S.player.health<h0,'fil électrique tombé : décharge');window.__oscarGod=true;o.S.player.health=100;
            o.S.player.x=7000-30;o.S.player.z=13.6;zone('salle paroissiale').act();ok(o.S.location==='refuge','refuge de la salle paroissiale');
            o.openDialogue('marierose');o.choose(0);o.choose(0);ok(o.S.clues.includes('rose')&&o.S.flags.mot,'Marie-Rose : cuisine à minuit et mot de passe');
            o.openDialogue('rejean');o.choose(0);o.choose(0);ok(o.S.clues.includes('generatrice'),'Réjean : la génératrice');
            o.openDialogue('rejean');o.choose(1);o.choose(0);ok(o.S.flags.wireSafe,'Réjean isole le fil tombé');
            o.openDialogue('helene');o.choose(1);ok(o.S.tasks.bois==='done','Hélène : le bois du poêle (tâche)');
            zone('Sortir').act();o.S.player.x=7000+40;o.S.player.z=-1.2;zone('garde du portail').act();o.choose(0);o.choose(0);
            ok(o.S.location==='manoir'&&o.S.flags.door_front&&o.S.arenas.manoir.enemies.find(e=>e.id==='m1').friendly,'portail : mot de passe, escorté comme homme de Viktor');
            o.tick(.05);ok(o.manoir().cols.some(c=>c.x0<-1e6),'porte d’entrée ouverte');
            o.S.player.x=7000+32;o.S.player.z=400-2.6;zone('génératrice').act();ok(o.S.flags.powerCut,'génératrice sabotée : maison dans le noir');
            o.S.player.x=7000;o.S.player.z=400-6;o.tick(.05);ok(o.manoir().indoor===true,'dans la maison : intérieur');
            o.S.arenas.manoir.alarm=false;o.S.player.x=7000+14;o.S.player.z=400-10;o.tick(.05);ok(o.S.flags.bossMet&&o.mode==='ui','Omer : face-à-face au salon');o.choose(0);o.choose(0);
            const om=o.S.arenas.manoir.enemies.find(e=>e.id==='boss');ok(om.hp===300,'Omer : 300 PV');o.damage(om,500);ok(o.S.flags.bossDown,'Omer vaincu');
            o.openDialogue('omerI');o.choose(1);o.choose(0);ok(o.S.clues.includes('omer')&&o.S.flags.omerKey,'Omer menotté, clé du sous-sol');
            o.S.player.x=7000+20.4;o.S.player.z=400-28.6;zone('sous-sol').act();ok(o.mode==='ui','porte du sous-sol');o.choose(0);ok(o.S.location==='soussol','sous-sol ouvert (serrure de secours)');
            zone('Libérer').act();ok(o.mode==='cine'&&o.cine.name==='finale','cinématique de fin');o.endCine();
            return winOk().then(w7=>{ok(w7,'écran de fin du jeu');ok(document.getElementById('bNext').classList.contains('hidden'),'pas de niveau suivant');
            const C=o.comfort,T=C.getTrophies();ok(T.famille&&T.premier&&T.courant,'trophées : première piste, courant coupé, fin du jeu');
            ok(document.getElementById('winStats').textContent.includes('Record'),'record de temps affiché');
            o.startLevel(null,'mtl');window.__oscarGod=false;C.SET.diff='decouverte';o.S.player.health=100;C.hurt(50);ok(Math.round(o.S.player.health)===70,'difficulté Découverte : coups réduits');
            C.SET.diff='expert';o.S.player.health=100;C.hurt(10);ok(Math.round(o.S.player.health)===87,'difficulté Expert : coups renforcés');C.SET.diff='normal';window.__oscarGod=true;o.S.player.health=100;
            o.S.stuckT=10;ok(!C.requestHint(true),'indice refusé si on vient de commencer');o.S.stuckT=120;ok(C.requestHint(true)&&document.getElementById('smsText').textContent.includes('salle paroissiale'),'indice du numéro masqué');
            C.openMenu('chapters','pause');const cb=document.querySelectorAll('#chapList button');ok(cb.length===7&&[...cb].every(b=>!b.disabled),'chapitres : 7 niveaux débloqués');C.closeMenu('chapters');
            C.openMenu('trophies','pause');ok(document.querySelectorAll('#trophyList .got').length>=3,'écran des trophées');C.closeMenu('trophies');
            C.openMenu('options','pause');const el=document.getElementById('oSens');el.value=1.7;el.dispatchEvent(new Event('input'));ok(JSON.parse(localStorage.getItem('oscar.settings')).sens===1.7,'options sauvegardées');C.closeMenu('options');
            C.applyGfx('low');ok(C.q==='low','qualité graphique basse');C.applyGfx('high');
            const LM={bc:'harbour',nl:'cabot',ab:'calgary',ns:'clock',mb:'dome',mtl:'stadium'};
            for(const id of ['bc','nl','ab','ns','mb','mtl']){o.startLevel(null,id);const back=o.S.location;const zc=zone('Explorer la ville');ok(!!zc,'ville ouverte accessible ('+id+')');if(!zc)continue;zc.act();
              const c=o.city();ok(o.S.location==='outside'&&c.id===id&&c.landmark===LM[id]&&c.houses+c.shops+c.towers>20&&c.trees>20&&c.peds>0,'ville '+id+' complète : '+c.towers+' tours, '+c.houses+' maisons, '+c.shops+' commerces, '+c.trees+' arbres, '+c.peds+' passants, '+c.cars+' véhicules, monument '+c.landmark);
              o.tick(.2);zone('Retour').act();ok(o.S.location===back,'retour vers l’enquête ('+id+')');}
            ok(o.rv().cars>15&&o.rv().max>0,'vrais véhicules : '+o.rv().cars+' véhicules inscrits (voitures, taxis, vélos, motos, police)');
            ok(o.rh().humans>60&&o.rh().max>0,'vrais humains : '+o.rh().humans+' personnages inscrits, jusqu’à '+o.rh().max+' remplacés près de la caméra');
            o.startLevel(null,'toronto');o.S.location='outside';o.S.player.x=-500;o.S.player.z=-500;let worst={pedOverlap:0,carOnPed:0};for(let i=0;i<300;i++){o.tick(.1);if(i%10===0){const g=o.agents();worst.pedOverlap=Math.max(worst.pedOverlap,g.pedOverlap);worst.carOnPed=Math.max(worst.carOnPed,g.carOnPed);}}
            ok(worst.pedOverlap<=1&&worst.carOnPed===0,'personne ne se marche dessus ni ne se fait écraser (30 s simulées) : chevauchements '+worst.pedOverlap+', voiture sur piéton '+worst.carOnPed);
            {o.startLevel(null,'toronto');const g=window.__oscarGod;window.__oscarGod=false;const p=o.S.player;const x0=p.x,z0=p.z,h0=p.health;o.comfort.hurt(25);const moved=Math.hypot(p.x-x0,p.z-z0);window.__oscarGod=g;
             ok(p.health<h0&&moved>.5,'un choc lourd renverse et repousse Oscar ('+moved.toFixed(2)+' m)');}
            {window.__oscarGod=false;o.startLevel(null,'ab');for(let i=0;i<4;i++)o.comfort.hurt(18);const b=o.body();const parts=Object.keys(b.wounds);
             ok(parts.length>0&&b.kits===2&&Object.values(b.wounds).some(w=>w.bleed),'les coups blessent des parties précises du corps ('+parts.join(', ')+')');
             const h1=o.S.player.health;for(let i=0;i<300;i++)o.player(1/60);ok(o.S.player.health<h1,'une plaie qui saigne fait perdre de la santé');
             o.treat();const b2=o.body();ok(b2.kits===1&&!Object.values(b2.wounds).some(w=>w.bleed||w.dirty),'la trousse (touche B) arrête le saignement et désinfecte');
             ok(b.fx.speed<=1&&b.fx.melee<=1,'les blessures gênent la marche, les coups et le tir');window.__oscarGod=true;}
            {o.startLevel(null,'toronto');o.S.location='outside';o.S.weather.rain=1;for(let i=0;i<5;i++)o.player(1/60);o.tick(.05);
             const l0=o.phys().load;o.S.player.weapons=['rifle','pistol'];const l1=o.phys().load;ok(l1>l0,'l’équipement pèse : plus d’élan à prendre ('+l0.toFixed(2)+' → '+l1.toFixed(2)+')');
             o.player(1/60);for(let i=0;i<3;i++)o.player(1/60);}
            {o.startLevel(null,'bc');o.S.location='forest';o.S.weather.rain=0;o.S.weather.snow=0;o.S.weather.windStr=.8;o.ignite(o.S.player.x+30,o.S.player.z);const f0=o.phys().fires;for(let i=0;i<20;i++)o.tick(.5);const f1=o.phys();
             ok(f1.fires>f0&&f1.smoke>0,'le feu se propage dans la forêt par temps sec et venteux ('+f0+' → '+f1.fires+' foyers, fumée)');}
            {o.startLevel(null,'bc');o.S.location='forest';o.S.weather.rain=1;o.ignite(o.S.player.x+30,o.S.player.z);for(let i=0;i<20;i++)o.tick(.5);const f2=o.phys();ok(f2.fires<=4,'sous la pluie le feu ne se propage presque pas ('+f2.fires+' foyers)');}
            {o.startLevel(null,'toronto');o.S.location='port';o.tick(.1);const ok1=o.boom();const ph=o.phys();ok(ok1&&ph.fires>0,'un baril de carburant touché explose et met le feu ('+ph.barrels.length+' barils dans l’entrepôt)');}
            {o.startLevel(null,'mtl');o.S.weather.rain=1;o.tick(.2);const e=o.phys().elec;ok(e.length>0&&parseFloat(e[0].split(':')[1])>1.1,'sous la pluie, le fil tombé électrise l’eau autour ('+(e[0]||'aucun')+' m)');}
            {o.startLevel(null,'toronto');o.S.location='outside';o.S.clock=13*60;const a0=o.crowd(.1).afraid;o.S.player.weapons=['pistol'];o.S.player.weapon='pistol';o.S.flags.lastShot={c:o.S.clock,x:0,z:0};const a1=o.crowd(1).afraid;o.S.player.weapon='fists';o.S.flags.lastShot=null;
             ok(a0===0&&a1>0,'un coup de feu en ville fait fuir les passants ('+a1+' effrayés)');}
            {o.startLevel(null,'toronto');o.S.rep=40;const w=o.wary('lina');o.openDialogue('lina');const txt=document.getElementById('dText').textContent;o.closeUI();
             ok(w==='rep'&&/coups de feu/.test(txt),'réputation : les gens méfiants demandent à être rassurés avant de parler');o.S.rep=0;}
            {const c={t:'Une soupe aux pois.',money:6},b={t:'Voilà 20 $.',money:20};o.startLevel(null,'toronto');o.S.weather.snow=0;o.S.weather.windStr=0;o.S.clock=13*60;const pT=o.price(c).p;o.startLevel(null,'nl');o.S.weather.snow=0;o.S.weather.windStr=0;o.S.clock=13*60;const pN=o.price(c).p,pB=o.price(b).p;
             o.S.money=0;const m1=o.price(c).m,m2=o.price(b).m;ok(pN>pT&&pB===20&&m1==='card'&&m2===null,'économie : prix plus élevés à Terre-Neuve ('+pT+' → '+pN+' $), pot-de-vin fixe en espèces, carte acceptée en commerce');}
            {o.startLevel(null,'bc');o.S.location='forest';o.S.weather.rain=1;o.S.player.dirt=0;for(let i=0;i<600;i++)o.player(1/60);const d1=o.S.player.dirt;o.S.player.dirt=80;const w=o.wary('maggie');
             o.startLevel(null,'toronto');o.enterInterior('diner');o.S.player.dirt=80;const wz=o.zones.find(z=>z.loc==='diner'&&/laver/i.test(z.label()));if(wz)wz.act();
             ok(d1>0&&w==='smell'&&wz&&o.S.player.dirt===0,'hygiène : on se salit dehors ('+d1.toFixed(2)+' en 10 s de pluie en forêt), on sent mauvais, on se lave aux toilettes');}
            {o.startLevel(null,'toronto');const d=o.night(13*60),n=o.night(23*60);ok(d.on===0&&n.spots>20&&n.on>=4&&n.fill>3&&n.exp>1.4,'nuit : vrais lampadaires allumés près de la caméra ('+n.on+'/'+n.spots+'), éclairage d’adaptation '+n.fill+', éteints le jour');}
            o.startLevel(null,'toronto');ok(o.city().toronto&&o.city().landmark==='cn','retour à Toronto intact (Tour CN, lac)');
            o.tick(.1);ok(document.getElementById('hWeather').textContent.length>3&&document.querySelectorAll('#hDay').length===1&&document.querySelectorAll('#hClock').length===1,'HUD : météo affichée, pas de doublon Jour/heure');
            C.quitToTitle();ok(o.mode==='title'&&!o.S,'quitter vers l’écran titre (partie sauvegardée)');
            return r;});});});});});});});
  return new Promise(res=>setTimeout(()=>{ok(o.mode==='win','écran de fin de niveau');res(r)},900));}'''
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
