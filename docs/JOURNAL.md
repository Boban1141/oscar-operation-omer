# Journal de développement

Entrées les plus récentes en haut. Voir le modèle dans `AGENTS.md`.

## Questions ouvertes
- ~~Moteur final~~ → **tranché : Unreal Engine 5.8 + MetaHuman** (voir `docs/PLAN_UNREAL.md`).
- Machine pour le réalisme (étape U8) : PC avec carte graphique dédiée ou PC dans le cloud ?
- Identité du personnage mystérieux : révélée à la fin ou mystère gardé ?
- Titre définitif du jeu (provisoire : « Oscar — Opération Omer »).
- Apparence d'Oscar (provisoire dans le code : peau foncée moyenne, cheveux noirs courts, veste kaki, sac à dos).
- Durée exacte du chronomètre de chaque niveau (provisoire niveau 1 : 72 h de jeu ; 1 seconde réelle = 1 minute de jeu).

---

## 2026-11-20 — Claude — Décision Unreal Engine et plan de migration
- Fait : choix du moteur enregistré (Unreal Engine 5.8, visuels simples d'abord puis MetaHuman). Plan de migration `docs/PLAN_UNREAL.md` (structure du projet, correspondance prototype → Unreal, règles techniques, étapes U0 à U9). Dossier `Unreal/` avec `.gitignore` et `.gitattributes` (Git LFS).
- Sur le PC du propriétaire : Epic Games Launcher installé ; disque C: nettoyé (Docker Desktop désinstallé à sa demande, fichiers temporaires supprimés) → 126 Go libres. PC : i7-1165G7, 16 Go, Intel Iris Xe intégrée → assez pour construire en greybox, pas pour MetaHuman/Lumen.
- Testé : sans objet (documentation).
- Reste à faire : le propriétaire accepte la licence Epic et installe UE 5.8 ; ensuite étape U0 (création du projet C++).

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
