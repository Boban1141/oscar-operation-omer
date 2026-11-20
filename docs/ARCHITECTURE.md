# Architecture technique

## État actuel (v0.2.0)
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
