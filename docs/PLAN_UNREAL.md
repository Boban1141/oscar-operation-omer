# Plan de migration vers Unreal Engine 5

> **EN ATTENTE** — le 2026-11-20, le propriétaire a décidé de **continuer sans Epic/Unreal** : le jeu se poursuit dans le navigateur (Three.js). Ce plan est conservé pour plus tard.
> Idée d'origine : construire le jeu final dans **Unreal Engine 5.8** (MetaHuman inclus).
> Méthode : construire **tout le jeu d'abord avec des visuels simples** (greybox), puis remplacer les visuels par MetaHuman et des villes réalistes sur une machine plus puissante.
> Le prototype navigateur (`game/index.html`) reste la référence pour les règles et le gameplay.

## 1. Machine de développement actuelle
| | PC actuel (Dell Inspiron 7506 2-en-1) | Recommandé par Epic |
|---|---|---|
| Processeur | Intel i7-1165G7, 4 cœurs, 2,8 GHz | 4 cœurs 2,5 GHz+ ✅ |
| Mémoire | 16 Go | 32 Go ⚠️ |
| Carte graphique | Intel Iris Xe intégrée | 8 Go de mémoire graphique dédiée ❌ |
| Disque | ~126 Go libres (après nettoyage) | ✅ |

Conséquences pour le travail sur ce PC :
- Réglages de l'éditeur sur **Scalability : Low/Medium**, Lumen **désactivé** (éclairage statique ou Distance Field simplifié), pas de MetaHuman dans les scènes de travail.
- MetaHuman, Lumen et les villes détaillées seront testés plus tard sur un PC avec carte graphique dédiée (ou un PC loué dans le cloud).

## 2. Structure du projet Unreal
Projet : `Unreal/Oscar/` (C++ + Blueprints), modèle **Third Person**.
```
Unreal/Oscar/
  Source/Oscar/
    Core/        OscarGameInstance, OscarSaveGame, OscarGameMode
    Systems/     MissionClockSubsystem, WeatherSubsystem, LivesSubsystem, ObjectiveSubsystem
    Characters/  OscarCharacter, CivilianCharacter, EnemyCharacter, HumanBehaviorComponent
    AI/          CivilianAIController, TrafficSubsystem
    UI/          HUD (UMG)
  Content/
    Maps/        L_Toronto, L_ColombieBritannique, L_TerreNeuve, L_Alberta, L_NouvelleEcosse, L_Manitoba, L_Montreal, L_Bresil_Intro
    Characters/  Greybox/ (mannequins UE5) → MetaHuman/ (plus tard)
    Environment/ Greybox/ → Final/
    Cinematics/  (Sequencer) Bresil, Enlevement, RepaireOmer, MessagesOmer, Echec
    Data/        DT_Levels (DataTable), DT_Dialogues, DT_Clues
```

## 3. Correspondance prototype → Unreal
| Prototype (`game/index.html`) | Unreal |
|---|---|
| `LEVELS` (données) | DataTable `DT_Levels` (saison, météo, températures, temps limite, objectifs) |
| `createState()` / sauvegarde | `UOscarSaveGame` + `UOscarGameInstance` |
| Horloge + chronomètre (`stepClock`, `stepMission`) | `UMissionClockSubsystem` (temps de jeu, échec si temps écoulé) |
| Météo, température, chaleur corporelle | `UWeatherSubsystem` + composant `BodyHeat` sur Oscar |
| 3 vies, vies bonus (max 2, persistantes) | `ULivesSubsystem` (vies bonus stockées dans la sauvegarde globale) |
| Passants, voitures, vélos, tramway | Mass AI / Smart Objects + `TrafficSubsystem` (ou splines simples en greybox) |
| `animRig` (respiration, regard, poids, gestes) | `UHumanBehaviorComponent` + Animation Blueprint (Motion Matching, Control Rig, Look-At) |
| Minicarte, HUD | Widgets UMG |
| Cycle jour/nuit | Sky Atmosphere + Directional Light pilotés par le temps de jeu |

## 4. Règles techniques
- **Logique en C++**, réglages et visuels en Blueprints/données : changer un personnage ou une ville ne touche jamais aux règles du jeu.
- **Chaque personnage** passe par `HumanBehaviorComponent` → les directives de réalisme s'appliquent automatiquement quand on remplace le mannequin par un MetaHuman.
- **Multijoueur** : Unreal a la réplication réseau intégrée ; écrire dès maintenant les systèmes côté serveur (`HasAuthority()`), même en solo.
- **Git** : Git LFS obligatoire pour `*.uasset`, `*.umap` et les gros fichiers ; ne jamais committer `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/`.
- Claude et Codex écrivent le C++, les données et la documentation, mais **ne peuvent pas ouvrir Unreal ni compiler** : le propriétaire compile et teste, puis signale les erreurs dans `docs/JOURNAL.md`.

## 5. Étapes
| Étape | Contenu | Machine |
|---|---|---|
| U0 | Installer UE 5.8, créer le projet Third Person C++, Git LFS | PC actuel |
| U1 | Systèmes de base : horloge de mission, vies, sauvegarde, HUD | PC actuel |
| U2 | Toronto en greybox : rues, blocs, maison d'Oscar, Lina's Diner, tour CN | PC actuel |
| U3 | Passants et circulation simples, cycle jour/nuit, météo | PC actuel |
| U4 | Dialogues, indices, intérieurs (maison d'Oscar, restaurant) | PC actuel |
| U5 | Combat mains nues et armes, IA ennemie, lieutenant de Toronto | PC actuel |
| U6 | Cinématiques en Sequencer (versions simples) | PC actuel |
| U7 | Provinces 2 à 7 en greybox, systèmes d'hiver | PC actuel |
| U8 | **Passage au réalisme** : MetaHuman, villes détaillées, Lumen | PC avec carte graphique dédiée |
| U9 | Multijoueur, serveurs | Serveurs |
