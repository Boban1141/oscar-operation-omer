# Feuille de route — blocs de développement

Statuts : `[ ]` à faire · `[~]` en cours · `[x]` terminé.
Mettre à jour cette page **à la fin de chaque étape** (voir `AGENTS.md`).

## Bloc 1 — Moteur et Toronto 3D `[x]` (v0.1.0)
- [x] Architecture en couches : DATA / CORE / STATE / SIM / VIEW / UI
- [x] Ville générée de façon déterministe (graine) : quartiers résidentiel, commerçant, tours, parc
- [x] Tour CN, lac Ontario, King Street et tramway rouge
- [x] Passants (parapluies sous la pluie), voitures, taxis, vélos ; densité selon l'heure et la météo
- [x] Cycle jour/nuit (soleil, lune, étoiles, fenêtres et lampadaires), météo (soleil, nuages, averses), température
- [x] Oscar jouable à la 3e personne, caméra avec anticollision
- [x] Chronomètre de niveau, 3 vies, vies bonus (max 2, persistantes), santé, chaleur, endurance
- [x] Écrans titre, pause, échec ; sauvegarde automatique ; minicarte ; objectif « Lina's Diner »
- [ ] Test visuel complet dans un navigateur (non encore fait par un humain)

## Bloc 2 — Intérieurs, dialogues, indices `[ ]`
- [ ] Intérieur de la maison d'Oscar (scène du mot, désordre, premiers indices)
- [ ] Intérieur du Lina's Diner, habitués interrogeables
- [ ] Système de dialogue à choix (confiance, argent, menace) avec conséquences
- [ ] Inventaire et carnet d'indices
- [ ] Voisin témoin ; informateur lié aux gangs brésiliens
- [ ] Première tâche secondaire donnant une vie bonus

## Bloc 3 — Combat `[ ]`
- [ ] Combat à mains nues (poings, pieds, esquive, blocage)
- [ ] Armes : obtention, munitions, visée, enrayement par le froid
- [ ] IA ennemie (poursuite, couverture, alerte), dégâts et mort d'Oscar
- [ ] Lieutenant d'Omer de Toronto (combat de fin de niveau)

## Bloc 4 — Cinématiques `[ ]`
- [ ] Assaut au Brésil
- [ ] Appel anonyme
- [ ] Enlèvement à Toronto (modèle d'Omer)
- [ ] Repaire d'Omer à Montréal
- [ ] Vidéos d'Omer pendant le jeu ; cinématique d'échec

## Bloc 5 — Infiltration et négociation avancées `[ ]`

## Blocs 6 à 11 — Provinces `[ ]`
- [ ] 6 Colombie-Britannique · [ ] 7 Terre-Neuve · [ ] 8 Alberta · [ ] 9 Nouvelle-Écosse · [ ] 10 Manitoba · [ ] 11 Montréal (final)
- Systèmes d'hiver : neige, verglas, blizzard, équipement d'hiver

## Bloc 12 — Multijoueur `[ ]`
- [ ] Serveur autoritaire, comptes, sauvegardes serveur — voir `docs/ARCHITECTURE.md`

## Question technique à trancher
- Rester sur navigateur (Three.js) ou migrer vers Unity/Unreal pour des villes réalistes. Décision du propriétaire du projet.
