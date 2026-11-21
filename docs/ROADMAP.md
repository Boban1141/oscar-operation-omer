# Feuille de route — blocs de développement

Statuts : `[ ]` à faire · `[~]` en cours · `[x]` terminé.
Mettre à jour cette page **à la fin de chaque étape** (voir `AGENTS.md`).

## État au 2026-11-20 (v0.5.0)
- **Niveau 1 (Toronto) complet, avec ses cinématiques** : blocs 1, 1b, 2, 3 et 4 terminés.
- **Prochaine étape proposée** : bloc 6 (niveau 2, Colombie-Britannique).
- **En attente du propriétaire** : premier test visuel humain ; validation du contenu inventé par Claude (personnages et pistes du niveau 1, voir `docs/JOURNAL.md`) ; réglage de la difficulté.
- **Dépôt GitHub** (`Boban1141/DUXIA`) : **pas encore envoyé** — GitHub n'est pas relié à Claude. Le dépôt existe en local avec tout l'historique (zip remis au propriétaire).

## Bloc 1 — Moteur et Toronto 3D `[x]` (v0.1.0)
- [x] Architecture en couches : DATA / CORE / STATE / SIM / VIEW / UI
- [x] Ville générée de façon déterministe (graine) : quartiers résidentiel, commerçant, tours, parc
- [x] Tour CN, lac Ontario, King Street et tramway rouge
- [x] Passants (parapluies sous la pluie), voitures, taxis, vélos ; densité selon l'heure et la météo
- [x] Cycle jour/nuit (soleil, lune, étoiles, fenêtres et lampadaires), météo (soleil, nuages, averses), température
- [x] Oscar jouable à la 3e personne, caméra avec anticollision
- [x] Chronomètre de niveau, 3 vies, vies bonus (max 2, persistantes), santé, chaleur, endurance
- [x] Écrans titre, pause, échec ; sauvegarde automatique ; minicarte ; premier objectif (remplacé par l'enquête complète au bloc 2)
- [ ] Test visuel complet dans un navigateur (non encore fait par un humain)

## Bloc 1b — Réalisme humain (directives maîtresses) `[x]` (v0.2.0)
- [x] `docs/DIRECTIVES_REALISME.md` créé et rendu obligatoire dans `AGENTS.md`
- [x] Squelette organique (coudes, genoux, mains avec doigts), visages avec yeux, sourcils, bouche asymétriques
- [x] Textures de peau et de tissu imparfaites ; asymétries individuelles
- [x] Respiration, clignements, regard mobile, transfert de poids, micro-gestes
- [x] Mains occupées : téléphone, café, sac, poche, parapluie ; gestes en conversation
- [x] Façades usées, trottoirs et asphalte texturés, mobilier urbain
- [ ] Test visuel par un humain

## Moteur
**Décision du propriétaire (2026-11-20) : on continue sans Epic/Unreal**, dans le navigateur (Three.js). Le plan Unreal est conservé en attente dans `docs/PLAN_UNREAL.md`.

## Bloc 2 — Intérieurs, dialogues, indices `[x]` (v0.3.0)
- [x] Intérieur de la maison d'Oscar, habité (veste d'Eva sur la chaise, chaise renversée, devoirs de Cédric, tasse à moitié vide, clés et courrier, lumière du matin et poussière dans l'air)
- [x] Intérieur du Lina's Diner (comptoir, banquettes, juke-box, menu, lampes) avec 4 habitués à qui parler
- [x] Système de dialogue à choix (vérité, argent, menace) avec coût en temps et en argent, conséquences (Lina se fâche si on la menace)
- [x] Carnet d'indices (touche C), argent (240 $ au départ)
- [x] Voisin témoin (M. Henderson) ; chaîne d'indices maison → voisin → diner → port
- [x] Première tâche secondaire : retrouver le pot à pourboires volé de Lina → vie bonus (règle du maximum 2 respectée)
- [x] Objectifs dynamiques avec marqueur 3D et minicarte ; points de sauvegarde
- [x] Test logique automatique : `tests/run_logic_tests.py`
- [ ] Test visuel par un humain

## Bloc 3 — Port, infiltration, combat `[x]` (v0.4.0) — **niveau 1 jouable de bout en bout**
- [x] Zone portuaire de Harbourfront : conteneurs, grue, cargo, projecteurs, clôture, entrepôt 7 (intérieur)
- [x] Entrée au choix : soudoyer le garde (100 $), lui mentir (reçu du diner), le provoquer, ou passer par le trou de la clôture
- [x] Discrétion : champ de vision des gardes, jauge de repérage, s'accroupir, nuit et pluie qui réduisent la vue, gilet de docker (déguisement), corps découverts → alerte
- [x] Neutralisation silencieuse par derrière (F), fouille des corps (armes, munitions, argent)
- [x] Combat à mains nues : poing, coup de pied, blocage ; armes : pistolet, fusil d'assaut, visée, recharge, tirs à la tête
- [x] IA ennemie : patrouille, enquête, combat (distance, déplacement latéral, rafales), corps à corps
- [x] Lieutenant d'Omer, Tiago « Faca » Moreira : négociation avant le combat, combat (couteau + pistolet), interrogatoire → piste de Vancouver
- [x] Fin du niveau 1 : écran de bilan, progression sauvegardée (vies bonus conservées)
- [x] Sons synthétisés (tirs, coups, sirène d'alerte)
- [x] Test automatique étendu : 19 vérifications
- [ ] Test visuel et réglage de la difficulté par un humain

## Bloc 4 — Cinématiques `[x]` (v0.5.0)
- [x] Moteur de cinématiques : plans, caméra en mouvement et « à l'épaule », sous-titres, titres de lieu, bandes noires, bouton Passer (Espace)
- [x] Assaut au Brésil (nuit, pluie, hélicoptère, fusillade, explosion du labo, arrestations)
- [x] Appel anonyme (voix déformée)
- [x] Enlèvement à Toronto : Eva cuisine, Cédric fait ses devoirs, appel vidéo coupé, VUS noirs, Omer entre (cicatrice, chaîne en or, manteau de cuir, cigare), le mot posé sur la table
- [x] Repaire d'Omer à Montréal (fête, gardes, fumée, « Maintenant, le soldat va comprendre. ») et le sous-sol
- [x] Retour d'Oscar trois jours plus tard → début du jeu
- [x] Messages vidéo d'Omer pendant le niveau (à 14 h, 34 h et 54 h de jeu), avec un indice caché (corne de navire + métro)
- [x] Cinématique d'échec (Omer dans le sous-sol)
- [x] Tests : 22 vérifications automatiques, dont l'intro complète (20 plans)
- [ ] Voix parlées (doublage) : à décider
- [ ] Test visuel par un humain

## Bloc 5 — Infiltration et négociation avancées `[~]`
- [x] Bases faites au bloc 3 : vision des gardes, déguisement, neutralisation silencieuse, négociation avec le garde et le lieutenant
- [ ] Se faire passer pour un bandit dans un cercle criminel (réputation, mots de passe, épreuves)
- [ ] Négociations à enjeux (otages, échanges, mensonges détectés)
- [ ] Gardes qui communiquent par radio, alarme qui se calme si Oscar se cache longtemps

## Blocs 6 à 11 — Provinces `[ ]`
- [ ] 6 Colombie-Britannique · [ ] 7 Terre-Neuve · [ ] 8 Alberta · [ ] 9 Nouvelle-Écosse · [ ] 10 Manitoba · [ ] 11 Montréal (final)
- Systèmes d'hiver : neige, verglas, blizzard, équipement d'hiver

## Bloc 12 — Multijoueur `[ ]`
- [ ] Serveur autoritaire, comptes, sauvegardes serveur — voir `docs/ARCHITECTURE.md`

