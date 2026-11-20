# Règles de travail pour les agents (Codex, Claude et tout autre assistant)

Ce dépôt est développé à plusieurs : le propriétaire du projet, **Claude** et **Codex**. Lisez ce fichier en entier avant de commencer.

## Avant de travailler
1. `git pull` pour récupérer la dernière version.
2. Lire, dans cet ordre : `docs/JOURNAL.md` (dernières entrées), `docs/ROADMAP.md`, `docs/PLAN.md`, `docs/DIRECTIVES_REALISME.md` (**obligatoire** pour tout ce qui est visuel), `docs/ARCHITECTURE.md`.
3. Prendre la prochaine tâche `[ ]` de la feuille de route, sauf instruction contraire du propriétaire.
4. La marquer `[~]` dans `docs/ROADMAP.md` et pousser ce changement tout de suite, pour éviter que deux agents fassent la même chose.

## Pendant le travail
- **Langue** : documentation, textes du jeu et messages de commit en français.
- **Ne jamais inventer une règle de jeu** absente de `docs/PLAN.md`. Ajouter la question dans `docs/JOURNAL.md` → « Questions ouvertes » et choisir une solution provisoire facile à changer.
- **Réalisme humain obligatoire** : tout personnage, lieu ou cinématique doit respecter `docs/DIRECTIVES_REALISME.md` et passer sa liste de contrôle. Jamais de personnage rigide, lisse ou symétrique, jamais de décor vide.
- Respecter les couches et principes de `docs/ARCHITECTURE.md` (SIM sans rendu, état sérialisable, commandes, déterminisme).
- Petites étapes, un commit par étape logique.
- Ne pas casser une fonction existante ; vérifier au minimum la syntaxe du script (`node --check` sur le module extrait).

## À la fin de CHAQUE étape (obligatoire)
1. Mettre à jour `docs/ROADMAP.md` (cases `[x]`, `[~]`).
2. Ajouter une entrée **en haut** de `docs/JOURNAL.md` avec le modèle ci-dessous.
3. Si une décision de jeu a été prise par le propriétaire : l'écrire dans `docs/PLAN.md`.
4. Si le format de sauvegarde change : augmenter `GAME_VERSION` dans `game/index.html`.
5. Commit + push sur `main` (ou une branche `codex/...` / `claude/...` + pull request si le changement est risqué).

### Modèle d'entrée de journal
```
## AAAA-MM-JJ — <Agent> — <titre court>
- Fait : ...
- Fichiers : ...
- Testé : ... (ou « non testé : raison »)
- Reste à faire / problèmes connus : ...
```

## Format des commits
`[bloc N] verbe + description` — ex. : `[bloc 2] ajoute le système de dialogue à choix`.

## Interdits
- Pas de secrets (clés, mots de passe) dans le dépôt.
- Ne pas réécrire l'historique de `main` (`push --force` interdit).
- Ne pas supprimer de décision de `docs/PLAN.md` sans accord du propriétaire.
