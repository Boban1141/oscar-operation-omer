# Journal de développement

Entrées les plus récentes en haut. Voir le modèle dans `AGENTS.md`.

## Questions ouvertes
- Moteur final : rester sur navigateur (Three.js) ou passer à Unity/Unreal ?
- Identité du personnage mystérieux : révélée à la fin ou mystère gardé ?
- Titre définitif du jeu (provisoire : « Oscar — Opération Omer »).
- Apparence d'Oscar (provisoire dans le code : peau foncée moyenne, cheveux noirs courts, veste kaki, sac à dos).
- Durée exacte du chronomètre de chaque niveau (provisoire niveau 1 : 72 h de jeu ; 1 seconde réelle = 1 minute de jeu).

---

## 2026-11-20 — Claude — Création du dépôt et bloc 1
- Fait : plan complet du jeu (`docs/PLAN.md`), feuille de route, architecture, règles de collaboration (`AGENTS.md`), code du bloc 1 (Toronto 3D jouable).
- Fichiers : `game/index.html`, `docs/*`, `AGENTS.md`, `CLAUDE.md`, `README.md`.
- Testé : syntaxe JavaScript validée (`node --check`). **Non testé visuellement** dans un navigateur (pas d'accès au rendu depuis l'environnement de Claude).
- Reste à faire / problèmes connus :
  - Faire un premier test visuel et corriger ce qui ne s'affiche pas.
  - Pas de commandes tactiles (mobile).
  - Les véhicules « sautent » légèrement aux virages (lissés visuellement seulement).
  - Le verrouillage de la souris peut être refusé dans certains cadres : la caméra passe alors en mode « cliquer-glisser ».
