# Journal de développement

Entrées les plus récentes en haut. Voir le modèle dans `AGENTS.md`.

## Questions ouvertes
- **À valider** : le contenu de l'enquête du niveau 1 (personnages Henderson, Lina, Marcus, Jayden, Kowalski ; indices ; piste de l'entrepôt 7) a été proposé par Claude — voir `docs/PLAN.md` §10b.
- ~~Moteur final~~ → **tranché : on continue dans le navigateur (Three.js)**, sans Epic. Unreal reste possible plus tard (`docs/PLAN_UNREAL.md`).
- Identité du personnage mystérieux : révélée à la fin ou mystère gardé ?
- Titre définitif du jeu (provisoire : « Oscar — Opération Omer »).
- Apparence d'Oscar (provisoire dans le code : peau foncée moyenne, cheveux noirs courts, veste kaki, sac à dos).
- Durée exacte du chronomètre de chaque niveau (provisoire niveau 1 : 72 h de jeu ; 1 seconde réelle = 1 minute de jeu).

---

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
