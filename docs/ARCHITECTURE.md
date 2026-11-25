# Architecture technique

## État actuel (v1.6.0)
- Vie (Kimi) : `initBirds/updateBirds`, `initDogs/updateDogs`, `initPlanes/updatePlanes` (lancés par `startLevel`), `initInteriorLife/updateInteriorLife` (à l'entrée d'un intérieur) ; comportements des passants (`behavior` : walk, phone_walk, look_around, group, sit).
- Rendu (Kimi) : `initComposer()` (EffectComposer : RenderPass, UnrealBloomPass, vignettage, grain, aberration) ; utilisé seulement si `SET.postfx` et qualité `high` ; `updateRainOverlay()` (canvas `#rainOverlay`).
- Une seule ville extérieure : Toronto (`generateCity`). Les niveaux 2 à 7 se jouent dans leurs lieux (`INTERIORS`).

## État v1.4.1
- Section 8 : Oscar = `assets/characters/candidat5_camouflage.fbx` (FBXLoader) + clips `OSCAR_CLIPS` ; `reorientClips()` adapte les clips d'un squelette tourné ; `inPlace()` bloque le déplacement des hanches ; superpositions `OM.over` (punch, kick, guard, aim, fire, reload, hit) ; `OM.gunAnchor` suit la main droite. Chemins essayés : `assets/...` (GitHub Pages) puis `../assets/...` (dépôt).
- Section 9 : `loadRealSurfaces()` ; `realSwap(texture, idPolyHaven, saturation, relief)` remplace l'image d'une texture canvas existante par une photo ramenée à la même couleur moyenne (`detailCanvas`) et ajoute une carte de normales ; `FACADES` + `paintFacade()` repeignent les façades sur fond photo.
- Section 10 : `TREES` (couronnes instanciées + matériau du tronc + type broad/conifer/snow) → `buildFoliage()` au démarrage ; `realTrees()` (écorce), `phModel(id)` (charge un modèle glTF Poly Haven via l'API), `BENCHES` → `realBenches()`.
- `tools/fbx_shrink.py` : réduction des textures intégrées des FBX Mixamo.

## État v1.2.0
- Section 8 (OSCAR EN 3D) : `loadOscarModel()` (import `three/addons/loaders/GLTFLoader.js`), `setupOscarModel()`, `updateOscarModel(dt)` appelé juste avant le rendu. `retarget(os, enfant, débutPrimitif, finPrimitif, poids)` aligne un os du modèle sur le segment correspondant de l'ancien squelette, sans hypothèse sur les axes du fichier. `OM.body` = maillages de l'ancien corps masqués ; armes et vêtements restent attachés à l'ancien squelette.

## État précédent (v1.1.0)
- Section 7 (CONFORT, en fin de module) : `SET` (localStorage `oscar.settings`), `DIFFK()` appliqué dans `hurtPlayer` et la jauge de repérage ; bus audio `AUD` (tous les sons passent par `AOUT()`), `stepAudio` ; `HINTS[niveau][étape]` + `S.stuckT` ; `TROPHIES`, `unlock()`, `trophiesOnWin()` (appelé par `levelComplete`) ; `oscar.trophies`, `oscar.records` ; manette `padPoll()` ; `stepComfort(dt,t)` appelé au début de `frame()`.
- Niveau 7 (section 5j) : lieux `westmount`, `refuge`, `manoir`, `soussol`. `MANOIR.indoor`/`ice` basculent chaque pas selon `inHouse(p)` (la maison est dans une arène extérieure). Portes : `MANOIR.doors[k]` + `S.flags.door_<k>` (`syncDoors`). `stormHazards()` : branches et fil tombé. `camMeshesFor(I,cams)` + `syncCameras()` générique (toutes les arènes avec `cams`). Cinématique `finale` → `levelComplete()`.
- Niveau 6 (section 5i) : lieux `winnipeg`, `cafe`, `silos` ; `whiteout()` (0–1, neige × vent sur les lieux `snow`) réduit le brouillard et la détection des gardes (×(1−0,5·whiteout)) ; `S.thermos` + `drinkThermos()` (touche H).
- Jeu navigateur, un seul fichier : `game/index.html`.
- **Three.js 0.160.0** chargé depuis `cdn.jsdelivr.net` (import map). Aucune étape de build.
- Lancer en local : servir le dossier `game/` (`python3 -m http.server -d game 8000`) puis ouvrir `http://localhost:8000`.

## Couches (dans l'ordre du fichier)
| Couche | Rôle | Règle |
|---|---|---|
| 1. DATA | `LEVELS`, constantes de ville, palettes | Données pures. Ajouter une province = ajouter une entrée. |
| 2. CORE | RNG déterministe `mulberry32`, `bus` d'événements, `store` (sauvegarde) | Aucune dépendance au rendu. |
| 3. STATE | `createState()` : état de partie **100 % sérialisable** (JSON) | Tout ce qui doit être sauvegardé ou synchronisé vit ici. |
| 4. SIM | `step*()` à pas fixe 60 Hz : horloge, météo, joueur, PNJ, trafic, mission | Ne touche **jamais** à Three.js. Le joueur agit uniquement via l'objet `cmd`. |
| 5. VIEW | Construction des meshes, `syncView`, environnement, caméra | Lit l'état, ne le modifie pas (sauf la caméra). |
| 6. UI | HUD, menus, minicarte, entrées clavier/souris → `cmd` | |

## Systèmes du bloc 2
- **Données d'histoire** (`CLUES`, `DIALOGUES`, `objective()`) : section « 1b. STORY DATA ». Ajouter un dialogue = ajouter des nœuds `{text, choices:[{t, next|end, min, money, need, fx}]}`.
- **Intérieurs** (`INTERIORS`, section « 5b ») : chaque lieu est un groupe placé loin de la ville (x = 1000), avec ses propres collisions, lumières (lampes + soleil par la fenêtre) et zones. `enterInterior / exitInterior / applyLocation`.
- **Zones d'interaction** (`storyZones()`) : `{loc, x, z, r, label(), act(), cond?, auto?}` ; la plus proche est proposée avec la touche E.
- **État** : `S.location`, `S.money`, `S.clues[]`, `S.tasks{}`, `S.flags{}` (sauvegardés).
- **Accès de test** : `window.__oscar` (état et fonctions) ; test automatique `tests/run_logic_tests.py` (faux moteur Three.js, Chrome headless).

## Systèmes du bloc 3
- **Lieux extérieurs séparés** : `INTERIORS.port` (`indoor:false`) garde le ciel, la météo et les ombres ; `house` et `diner` ont `indoor:true`.
- **Ennemis** : `ENEMY_DEFS` (données : type, route ou poste) + `ETYPE` (vie, vitesse, dégâts, cadence, précision). État dans `S.port.enemies` (sauvegardé). IA dans `stepCombat()` : perception (champ de vision, portée selon nuit/pluie, `losClear()` contre les collisions), jauge de repérage, états `patrol / investigate / combat / flee`.
- **Combat** : objet `CB` (cadences, visée, blocage, accroupi, recharge) ; `playerAttack`, `tryFire` (rayon depuis la caméra, tête ×2,2), `takedownOrLoot`, `hurtPlayer`, `damageEnemy`, `alarm`. Armes dans `WEAPONS`.
- **Appels de dialogue** : un choix peut déclencher une action du jeu avec `fx.call` → `CALLS` (`openGate`, `gateFight`, `bossFight`, `levelComplete`).
- **Mode test** : `window.__oscarGod = true` rend Oscar invincible ; `__oscar.tick(sec)` fait avancer l'IA.

## Système du bloc 4 (cinématiques)
- Section « 5d » : décors `CSET` (brazil, lair, basement) placés loin de la ville ; acteurs `A.*` créés avec `createHuman` (mêmes règles de réalisme) ; poses dans `pose.*`.
- Un script = liste de plans `{set, d, clock, rain, cloud, indoor, center, title, cam:[départ, arrivée, regard départ, regard arrivée], sub:[[t, qui, texte]], enter(), upd(t,k,dt,T)}`. Scripts : `CINES_intro`, `CINES_msg(n)`, `CINES_fail`.
- `playCine(nom, fin)` passe en mode `cine` ; `endCine()` rend la main.

## Multi-niveaux (bloc 6)
- `LEVELS[id]` : saison, météo, températures, `coldFactor`, `start` (lieu de départ), `next`, textes `ready` / `win` / `startToast`.
- Lieux : `INTERIORS[id]` (`indoor`, `label`, `exitLoc`). Arènes de combat : `ARENAS[id]` (`area`, `defs`, `room`, `boss`, `elook`, `bossLook`, `bossDeco`, `lvl`). État : `S.arenas[id]`. Accès : `AR()` (arène du lieu actuel), `AS()` (son état).
- Zones : propriété `lvl` (par défaut `toronto`). Objectifs : `objective()` choisit `objectiveToronto` / `objectiveBC`.
- Progression entre niveaux : `localStorage['oscar.progress']` (`levelsDone`, vies bonus, argent) ; `createState(levelId)` la relit.
- **Ajouter une province** : `LEVELS.xx`, un module « 5x » (décors, PNJ, `ARENAS.xx`, `CLUES`, `DIALOGUES`, `objectiveXX`, zones), une cinématique `xxIntro`, et des vérifications dans `tests/run_logic_tests.py`.

## Vent (bloc 7)
- `LEVELS[id].wind = {base, gust, dir}` → `S.weather.windStr` (0 à 1) et `windDir`, calculés dans `stepWeather`. Effets : `stepPlayer` (vitesse face au vent, poussée, froid), `stepCombat` (portée de vue), `tryFire` (dispersion), pluie oblique (`WIND`), vagues (`animWaves`), HUD.

## Neige et froid (bloc 8)
- Météo `snow` (si `LEVELS[id].weather.snow`), `S.weather.snow`. Lieux `INTERIORS[id].snow` : neige profonde hors `ARENAS[id].paths`, traces (`stepFootprints`, `FOOT`), détection des traces dans `stepCombat`, buée (`stepBreath`), flocons (`updateSnow`).
- Équipement : drapeaux `parka`, `gloves`, `tuque`, `boots` ; `gearFactor()` réduit l'exposition au froid ; `applyGear()` les affiche sur Oscar.

## Verglas, caméras, cloisons basses (bloc 9)
- Lieux `INTERIORS[id].ice` : inertie dans `stepPlayer` (sauf `flags.crampons`), chutes (`CB.fall`).
- `ARENAS[id].cams` : caméras (`stepCameras`, `syncCameras`), désactivées par `flags.powerCut`. `needPlan` : ennemis visibles sur la minicarte seulement avec `flags.plan`.
- Collisions `low:true` : bloquent le passage mais pas la vue, sauf si Oscar est accroupi (`losClear`).
- `defs[].hp` remplace les points de vie du type. Progression : `oscar.progress.gear` conserve l'équipement.

## Principes à respecter
1. **Déterminisme** : la ville vient de `generateCity(seed)`. Même graine → même ville chez tous les joueurs.
2. **Commandes** : les entrées produisent des commandes (`cmd`) ; la simulation les applique. C'est le format qu'un serveur recevra.
3. **Séparation SIM / VIEW** : la simulation doit pouvoir tourner sans rendu (sur un serveur Node.js).
4. **Versionnage** : `GAME_VERSION` et la clé de sauvegarde changent quand le format de l'état change.
5. **Événements** : la communication entre systèmes passe par `bus.emit/on` (`death`, `fail`, `objective`).

## Évolution prévue
1. Découper `game/index.html` en modules ES (`src/data`, `src/core`, `src/sim`, `src/view`, `src/ui`) quand le fichier dépasse ~2000 lignes, avec Vite.
2. Extraire SIM dans un paquet partagé client/serveur.

## Multijoueur — cible 12 000 joueurs
Le jeu est solo et scénarisé ; le multijoueur se fera par **sessions** (coopération à petit nombre) plutôt que par un monde unique de 12 000 personnes.
- **Serveur autoritaire** Node.js (ou Go) qui exécute la couche SIM ; clients = VIEW + UI + prédiction.
- **Transport** : WebSocket (puis WebRTC/UDP si besoin), messages binaires compacts, 20 Hz serveur.
- **Instances** : 1 session = 1 à 4 joueurs dans un niveau ; un processus gère plusieurs dizaines de sessions.
- **Mise à l'échelle** : orchestrateur (Kubernetes ou service géré) qui lance des processus de jeu à la demande ; 12 000 joueurs ≈ 3 000–4 000 sessions ≈ quelques dizaines de machines.
- **Services** : comptes/authentification, sauvegardes en base (PostgreSQL), matchmaking/invitations, Redis pour la présence.
- **Mises à jour** : versions de client/serveur vérifiées à la connexion ; migrations du format de sauvegarde.
- Coût d'hébergement à la charge du propriétaire du projet.
