# Oscar — Opération Omer

![Tests](https://github.com/Boban1141/oscar-operation-omer/actions/workflows/ci.yml/badge.svg)

Adresse prévue pour la version en ligne : https://boban1141.github.io/oscar-operation-omer/ (publication indisponible lors de la vérification du 25 novembre 2026).

Jeu d'action-aventure 3D : Oscar, soldat d'élite canadien, traverse sept provinces pour libérer sa femme Eva et son fils Cédric, enlevés par le chef criminel Omer.

## Jouer
```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000/game/
```
Commandes : ZQSD/WASD se déplacer · Maj courir · Espace sauter · E interagir · souris regarder · molette zoom · T accélérer le temps · Échap pause.

## Documentation
- `docs/PLAN.md` — plan complet du jeu (histoire, personnages, niveaux, règles)
- `docs/ROADMAP.md` — feuille de route par blocs et avancement
- `docs/ARCHITECTURE.md` — architecture technique et plan multijoueur
- `docs/JOURNAL.md` — journal de travail et questions ouvertes
- `AGENTS.md` — règles pour Codex, Claude et tout contributeur

Version actuelle : **1.31.1** (prise en main à Toronto, voix des personnages) — le jeu complet, 7 niveaux enchaînés : Toronto, Colombie-Britannique, Terre-Neuve, Alberta, Nouvelle-Écosse, Manitoba, Montréal (final).

Test logique : `python3 tests/run_logic_tests.py`. Commandes complètes : voir `docs/PLAN.md` (section Commandes).

Directives artistiques obligatoires : `docs/DIRECTIVES_REALISME.md`.
