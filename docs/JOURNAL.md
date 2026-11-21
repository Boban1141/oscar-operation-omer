# Journal de développement

Entrées les plus récentes en haut. Voir le modèle dans `AGENTS.md`.

## Questions ouvertes
- **À décider** : l'identité du personnage mystérieux (la fin garde le mystère et ouvre une suite).
- **À valider** : tout le niveau 7 (Hélène, Marie-Rose, Réjean, le mot de passe, la fin, Omer livré à la police) — `docs/PLAN.md` §10j.
- **À valider** : tout le niveau 6 (Mireille, Nadia, Louis, Viktor, le code 1967, la tempête de verglas) — `docs/PLAN.md` §10i.
- **À valider** : tout le niveau 5 (Gisèle, Chloé, Sam, Bernie, le Notaire, le Bras droit à Winnipeg) — `docs/PLAN.md` §10h.
- **À valider** : tout le niveau 4 (Priya, Dale, l'Éleveur, le Notaire, Westmount) — `docs/PLAN.md` §10g.
- **À valider** : tout le niveau 3 (Bridget, Wilf, Liam, la doris, le capitaine Roy, « l'Éleveur ») — `docs/PLAN.md` §10f.
- **À valider** : tout le niveau 2 (Earl, Josh, Maggie, le Pasteur, l'Église de la Dernière Lumière, le « Marie-Galante », le dessin de Cédric) — `docs/PLAN.md` §10e.
- **À valider** : Tiago « Faca » Moreira, le port, « le Pasteur » et la piste de Vancouver (`docs/PLAN.md` §10c).
- **À régler après test humain** : difficulté (vitesse de repérage, précision des gardes), durée du chronomètre du niveau 1 (72 h de jeu = 72 minutes réelles).
- **À valider** : le contenu de l'enquête du niveau 1 (personnages Henderson, Lina, Marcus, Jayden, Kowalski ; indices ; piste de l'entrepôt 7) a été proposé par Claude — voir `docs/PLAN.md` §10b.
- ~~Moteur final~~ → **tranché : on continue dans le navigateur (Three.js)**, sans Epic. Unreal reste possible plus tard (`docs/PLAN_UNREAL.md`).
- Identité du personnage mystérieux : révélée à la fin ou mystère gardé ?
- Titre définitif du jeu (provisoire : « Oscar — Opération Omer »).
- Apparence d'Oscar (provisoire dans le code : peau foncée moyenne, cheveux noirs courts, veste kaki, sac à dos).
- Durée exacte du chronomètre de chaque niveau (provisoire niveau 1 : 72 h de jeu ; 1 seconde réelle = 1 minute de jeu).

---

## 2026-11-21 — Claude — Personnages Mixamo réels et lieux photographiques (v1.3.0 → v1.4.1)
- Personnages : Boban a téléchargé des personnages Mixamo très lourds (jusqu'à 142 Mo, textures 4096 px). Nouvel outil `tools/fbx_shrink.py` : réécrit le FBX binaire avec des textures réduites (1024 px JPEG), sans toucher au modèle ni au squelette (relecture vérifiée, fin de fichier conforme au chargeur three.js). 374 Mo → 18 Mo pour 5 personnages ; 3 civils ajoutés ensuite. Rangés dans `assets/characters/`, animations dans `assets/animations/`. Page `game/apercu_personnages.html` pour les voir en 3D.
- Oscar = soldat en camouflage (candidat 5, choisi par Boban), animations capturées : repos/marche/course (Soldier.glb, réorientées : squelette source tourné de −90°), coup de poing, coup de pied, garde, visée, tir, rechargement, impact. Arme dans la vraie main droite. GitHub Pages publie aussi `assets/` (étape ajoutée au workflow).
- Lieux : matières photographiées Poly Haven (CC0) chargées à l'exécution : asphalte, dalles de trottoir, neige, parquet, plâtre, tôle ; 60 façades repeintes sur fond de vraie brique/béton en gardant fenêtres et lumières de nuit. Option « Matières photographiques ».
- Vérifié sur le vrai rendu (PC de Boban) : Oscar debout, marche, garde ; façades et trottoirs réels.
- Décision de Boban : TOUTES les personnes du jeu doivent être des humains réalistes, sans exception (passants, assis, cyclistes, ennemis, acteurs des cinématiques). Reporté : il faut encore télécharger ~10 personnages (Eva, Omer, femmes, hommes âgés, costume, ouvrier, policier, manteau) + animations de vie courante.

## 2026-11-20 — Claude — Oscar en modèle 3D (v1.2.0)
- Fait : Oscar affiché par un modèle squelettique animé (Soldier.glb des exemples three.js, rig Mixamo : Idle/Walk/Run) chargé depuis le CDN. L'ancien squelette tourne en coulisse ; ses poses (coups, blocage, visée, accroupi, chute, cinématiques) sont recopiées sur le modèle par alignement des os (`retarget`, section 8). Orientation, taille et côtés mesurés au chargement. Repli automatique sur l'Oscar classique ; option « Personnage d'Oscar » (nouveau / classique).
- Vérifié sur le vrai rendu (PC de Boban) : repos, marche, accroupi, blocage, visée.
- Limites : le modèle d'exemple porte une armure futuriste (pas un soldat canadien) ; licence Mixamo à vérifier avant toute commercialisation ; sur ce PC la qualité graphique baisse automatiquement (moins de 26 images/s).
- Suite proposée : créer le vrai Oscar (uniforme, visage, barbe) sur un compte Mixamo et ajouter des animations de combat capturées.

## 2026-11-20 — Claude — Premier test visuel réel (v1.1.1)
- Testé dans le navigateur intégré, sur le PC de Boban (vrai rendu, Intel Iris Xe) : écran titre, Toronto, diner, intro, Manitoba, Montréal, salon d'Omer.
- Corrigé : le HUD restait affiché par-dessus les cinématiques ; la caméra sortait des petites pièces (entrée du diner) ; Westmount et la maison d'Omer presque noirs (lumière d'appoint `nightFill`, lampes plus fortes) ; la météo promise (blizzard au Manitoba, verglas à Montréal) n'était pas garantie au début (`firstWeather`) ; cinématiques de nuit éclaircies.
- Reste à voir : les humains sont encore faits de formes simples (point 2 du plan d'amélioration).

## 2026-11-20 — Claude — GitHub Actions
- Fait : `.github/workflows/ci.yml` (tests à chaque push et PR ; publication de `game/` sur GitHub Pages si les tests passent sur main). Badge dans le README, règles dans AGENTS.md.
- À faire par Boban : Settings → Pages → Source « GitHub Actions ».

## 2026-11-20 — Claude — Confort de jeu (v1.1.0)
- Fait : options, chapitres, trophées et records, musique adaptative et ambiances, indices du numéro masqué (I), manette, astuces, quitter vers le titre, F1, indicateur de sauvegarde, qualité graphique automatique.
- Tests : 123/123 ; essai réel (menus, manette simulée, indices, quitter/continuer) sans erreur.

## 2026-11-20 — Claude — Niveau 7 : Montréal, le final (v1.0.0)
- Fait : tempête de verglas (branches, fil tombé), panne générale, refuge, trois entrées dans la maison d'Omer, génératrice, boss Omer, sous-sol, cinématique de fin et écran de fin du jeu.
- Corrigé : les gardes au corps à corps ne blessaient Oscar qu'au port de Toronto ; `startBossFight` ne réveillait pas les gardes de la pièce ; `syncCameras` généralisé.
- Tests : 112/112 ; passage réel 6 → 7 et cinématique de fin sans erreur console.
- Suite : test humain complet, réglage, identité du personnage mystérieux.

## 2026-11-20 — Claude — Niveau 6 : Manitoba (v0.10.0)
- Fait : blizzard −40 °C, voiles blancs (vue réduite pour Oscar et les gardes), thermos (H), abris chauffés, Saint-Boniface, café, silos de Saint-Norbert, boss Viktor, mallette ; enchaînement Nouvelle-Écosse → Manitoba.
- Tests : 91/91 ; passage réel niveau 5 → 6 sans erreur console.
- Suite : bloc 11, Montréal (final).

## 2026-11-20 — Claude — Niveau 5 : Nouvelle-Écosse (v0.9.0)
- Fait : verglas (glissade, chutes, crampons), équipement conservé entre niveaux, caméras + coupure de courant, cloisons basses, ouverture de la porte à la relève de 23 h, déchiqueteuse à retardement ; front de mer d'Halifax, Mission des marins, cabinet du Notaire ; cinématique ; piste de Winnipeg.
- Fichiers : `game/index.html` (0.9.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 79/79 vérifications automatiques (niveaux 1 à 5), passage réel niveau 4 → 5, chute sur le verglas en courant. **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 6 (Manitoba), puis le final à Montréal.

## 2026-11-20 — Claude — Niveau 4 : Alberta (v0.8.0)
- Fait : neige (chute, sol, neige profonde, traces suivies par les gardes, buée, brouillard), froid extrême avec givre à l'écran et mains engourdies ; équipement d'hiver **à trouver** (décision du propriétaire) ; gare de triage d'Alyth, relais routier, ranch Bow Valley, l'Éleveur ; cinématique ; piste d'Halifax + indice de Westmount.
- Fichiers : `game/index.html` (0.8.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 63/63 vérifications automatiques (niveaux 1 à 4), passage réel niveau 3 → 4, marche dans la neige sans erreur. **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 5 (Nouvelle-Écosse).

## 2026-11-20 — Claude — Niveau 3 : Terre-Neuve (v0.7.0)
- Fait : système de vent (déplacement, rafales, froid éolien, visée, repérage, pluie oblique, affichage), vagues animées, roulis à bord ; port de St. John's, pub, tâche de la doris, quatre façons d'aborder le Marie-Galante, combat sur le pont en tempête, capitaine Roy ; cinématique d'arrivée ; piste vers l'Alberta.
- Fichiers : `game/index.html` (0.7.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 50/50 vérifications automatiques (niveaux 1 à 3), passage réel niveau 2 → 3 et combat sur le chalutier sans erreur. **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 4 (Alberta).

## 2026-11-20 — Claude — Niveau 2 : Colombie-Britannique (v0.6.0)
- Fait : moteur rendu multi-niveaux (arènes génériques, zones/objectifs par niveau, passage de niveau, progression conservée). Niveau 2 complet : terminal de Vancouver, bar, surplus, trajet vers Squamish (3 options), forêt pluviale et camp du Pasteur, tâche de Josh (2e vie bonus), boss, interrogatoire, piste de Terre-Neuve ; imperméable et café chaud ; cinématique d'arrivée.
- Fichiers : `game/index.html` (0.6.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 36/36 vérifications automatiques (niveaux 1 et 2), passage réel niveau 1 → cinématique → niveau 2 sans erreur, IA de la forêt rapide (18 ms pour 5 s simulées). **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 3 (Terre-Neuve).

## 2026-11-20 — Claude — Bloc 4 : cinématiques (v0.5.0)
- Fait : moteur de cinématiques ; introduction complète en 20 plans (Brésil, appel anonyme, enlèvement à Toronto, repaire d'Omer, sous-sol, retour d'Oscar) ; messages vidéo d'Omer pendant le jeu (+ indice « métro et corne de navire ») ; cinématique d'échec ; écran « Prendre le contrôle d'Oscar » ; bouton « Revoir l'introduction » ; sons (hélicoptère, explosion, sonnerie, basses de la fête).
- Fichiers : `game/index.html` (0.5.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 22/22 vérifications automatiques + parcours réel (Nouvelle partie → intro → Passer → jeu) sans erreur. **Rendu visuel des cinématiques non vu par un humain.**
- Reste à faire : niveau 2 (Colombie-Britannique) ; décider s'il faut des voix parlées.

## 2026-11-20 — Claude — Bloc 3 : port, infiltration, combat (v0.4.0) — niveau 1 complet
- Fait : zone portuaire (conteneurs, grue, cargo, entrepôt 7), 4 façons d'entrer, discrétion (vision des gardes, jauge, accroupi, déguisement, corps découverts), neutralisation silencieuse, fouille, combat mains nues (poing, pied, blocage), pistolet et fusil (visée, recharge, tête), IA ennemie, lieutenant Tiago (négociation, combat, interrogatoire), écran de fin de niveau, sons synthétisés, minicarte du port avec gardes.
- Fichiers : `game/index.html` (0.4.0, anciennes sauvegardes ignorées), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 19/19 vérifications automatiques (de la maison jusqu'à l'écran de fin), repérage d'un garde en ~2 s à découvert, tirs ennemis, mort et réapparition au point de sauvegarde du port. **Rendu visuel et sensations de combat non testés par un humain.**
- Reste à faire : bloc 4 (cinématiques), niveau 2 (Colombie-Britannique).

## 2026-11-20 — Claude — Bloc 2 : intérieurs, dialogues, indices (v0.3.0)
- Fait : maison d'Oscar et Lina's Diner jouables de l'intérieur (lieux habités, soleil par la fenêtre, poussière, lampes) ; 5 personnages avec dialogues à choix (vérité / argent / menace, coût en temps et en argent) ; carnet d'indices (touche C) ; argent ; objectifs dynamiques avec marqueur ; tâche secondaire avec vie bonus ; voisin dehors ; mode « assis » pour les personnages.
- Fichiers : `game/index.html` (0.3.0, anciennes sauvegardes ignorées), `docs/*`, `tests/run_logic_tests.py`.
- Testé : syntaxe + scénario complet du niveau 1 automatisé (8/8 OK, 0 erreur JS) avec un faux moteur 3D. **Rendu visuel non testé.**
- Reste à faire / problèmes connus : contenu de l'enquête à valider par le propriétaire ; bloc 3 (infiltration du port, combat) ; l'intérieur est plus grand que la maison vue de dehors (normal dans les jeux).

## 2026-11-20 — Claude — Décision Unreal Engine et plan de migration
- Fait : choix du moteur enregistré (Unreal Engine 5.8, visuels simples d'abord puis MetaHuman). Plan de migration `docs/PLAN_UNREAL.md` (structure du projet, correspondance prototype → Unreal, règles techniques, étapes U0 à U9). Dossier `Unreal/` avec `.gitignore` et `.gitattributes` (Git LFS).
- Sur le PC du propriétaire : Epic Games Launcher installé ; disque C: nettoyé (Docker Desktop désinstallé à sa demande, fichiers temporaires supprimés) → 126 Go libres. PC : i7-1165G7, 16 Go, Intel Iris Xe intégrée → assez pour construire en greybox, pas pour MetaHuman/Lumen.
- Testé : sans objet (documentation).
- Reste à faire : ~~installer UE 5.8~~ — **annulé** : le propriétaire a choisi de continuer sans Epic. Suite : bloc 2 dans le navigateur.

## 2026-11-20 — Claude — Directives de réalisme humain (v0.2.0)
- Fait : directives maîtresses du propriétaire enregistrées (`docs/DIRECTIVES_REALISME.md`), rendues obligatoires (`AGENTS.md`, `docs/PLAN.md` §10). Personnages refaits avec un squelette organique, visages, mains, asymétries, respiration, clignements, regard, transfert de poids, objets tenus en main, gestes. Façades usées, sols texturés, poubelles, bornes-fontaines, distributeurs de journaux.
- Fichiers : `game/index.html` (version 0.2.0 : les anciennes sauvegardes sont ignorées), `docs/*`, `AGENTS.md`.
- Testé : syntaxe validée (`node --check`). **Non testé visuellement.**
- Reste à faire / problèmes connus : photoréalisme impossible dans le navigateur → décision de moteur à prendre (recommandation : Unreal Engine 5 + MetaHuman). Nombre de passants réduit de 46 à 38 pour compenser le coût des modèles plus détaillés.

## 2026-11-20 — Claude — Création du dépôt et bloc 1
- Fait : plan complet du jeu (`docs/PLAN.md`), feuille de route, architecture, règles de collaboration (`AGENTS.md`), code du bloc 1 (Toronto 3D jouable).
- Fichiers : `game/index.html`, `docs/*`, `AGENTS.md`, `CLAUDE.md`, `README.md`.
- Testé : syntaxe JavaScript validée (`node --check`). **Non testé visuellement** dans un navigateur (pas d'accès au rendu depuis l'environnement de Claude).
- Reste à faire / problèmes connus :
  - Faire un premier test visuel et corriger ce qui ne s'affiche pas.
  - Pas de commandes tactiles (mobile).
  - Les véhicules « sautent » légèrement aux virages (lissés visuellement seulement).
  - Le verrouillage de la souris peut être refusé dans certains cadres : la caméra passe alors en mode « cliquer-glisser ».
