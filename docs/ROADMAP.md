# Feuille de route — blocs de développement

Statuts : `[ ]` à faire · `[~]` en cours · `[x]` terminé.
Mettre à jour cette page **à la fin de chaque étape** (voir `AGENTS.md`).

## État au 2026-11-20 (v1.1.0) — le jeu solo est complet, du Brésil à Montréal
- **Niveaux 1 à 5 jouables et enchaînés** (Toronto, Colombie-Britannique, Terre-Neuve, Alberta, Nouvelle-Écosse) : blocs 1 à 4 et 6 à 9 terminés.
- **Prochaine étape proposée** : bloc 10 (niveau 6, Manitoba : blizzard à −40 °C, le Bras droit d'Omer).
- **En attente du propriétaire** : premier test visuel humain ; validation du contenu inventé par Claude (personnages et pistes du niveau 1, voir `docs/JOURNAL.md`) ; réglage de la difficulté.
- **Dépôt GitHub** (`Boban1141/oscar-operation-omer`) : **pas encore envoyé** — GitHub n'est pas relié à Claude. Le dépôt existe en local avec tout l'historique (zip remis au propriétaire).

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

## Bloc 6 — Niveau 2 : Colombie-Britannique `[x]` (v0.6.0)
- [x] Moteur multi-niveaux : arènes de combat génériques, zones et objectifs par niveau, passage au niveau suivant (vies bonus et argent conservés), écrans de fin et de départ propres à chaque niveau
- [x] Terminal de Centerm à Vancouver (pluie, grues rouges et blanches, montagnes de la rive nord), 4 hommes d'Omer, conteneur MSKU 448127
- [x] Bar The Rusty Anchor : Maggie (café chaud qui réchauffe), Earl le pêcheur, un motard ; surplus militaire (imperméable)
- [x] Climat : pluie constante et froid humide (4 à 11 °C) ; l'imperméable réduit l'effet de la pluie ; se réchauffer au bar ou dans le pick-up
- [x] Trois façons d'aller à Squamish : le pick-up d'Earl (en échange de sa promesse), le taxi (120 $), le stop (gratuit, 5 h)
- [x] Forêt pluviale de Squamish : cèdres géants, fougères, rivière avec pont gardé et tronc tombé, falaise du Chief, camp de l'Église de la Dernière Lumière
- [x] Tâche secondaire : convaincre Josh, le neveu d'Earl, de quitter la secte → vie bonus (la 2e et dernière du jeu)
- [x] Le Pasteur : négociation, combat, interrogatoire → piste du « Marie-Galante » à St. John's + dessin de Cédric (croix sur la montagne = Montréal)
- [x] Cinématique d'arrivée à Vancouver
- [x] Tests : 36 vérifications (niveaux 1 et 2)
- [ ] Test visuel et réglage par un humain

## Bloc 7 — Niveau 3 : Terre-Neuve `[x]` (v0.7.0)
- [x] Système de **vent** (tous niveaux) : ralentit la marche face au vent, rafales qui poussent, refroidissement éolien, visée moins précise, gardes qui voient et entendent moins, pluie oblique ; affiché dans la météo (km/h)
- [x] Vagues animées selon la force du vent ; roulis de la caméra à bord
- [x] Port de St. John's : maisons colorées de Water Street, Signal Hill et la tour Cabot, bateaux de pêche, ponton, quai 18
- [x] Pub The Ship's Lantern : Bridget (pilote du port), Wilf (vieux pêcheur), Liam (matelot effrayé), un violoneux (écouter réchauffe)
- [x] Quatre façons de monter à bord : mot de passe « Brume », pot-de-vin, force, ou la doris de Wilf jusqu'à l'échelle de poupe (tâche secondaire)
- [x] Abordage du Marie-Galante de nuit en pleine tempête : 6 marins armés, timonerie, capitaine Roy (négociation, combat, interrogatoire)
- [x] Piste du niveau 4 : train de marchandises vers Calgary, « l'Éleveur » ; confirmation du métro derrière Omer
- [x] Cinématique d'arrivée ; tests : 50 vérifications (niveaux 1 à 3)
- [ ] Test visuel et réglage par un humain

## Bloc 8 — Niveau 4 : Alberta `[x]` (v0.8.0)
- [x] **Neige** (tous niveaux) : chute de neige, sol enneigé, neige profonde qui ralentit hors des chemins déneigés, **traces de pas** que les gardes remarquent et suivent, **buée** de la respiration, brouillard de neige
- [x] **Froid extrême** (−17 à −26 °C) : givre sur l'écran quand Oscar a froid ; mains engourdies sans mitaines (visée instable)
- [x] **Équipement d'hiver à trouver** (pas à acheter, décision du propriétaire) : parka (atelier), mitaines (locomotive), tuque et bottes (objets perdus du relais) ; chacun réduit le froid ou la lenteur dans la neige ; visible sur Oscar
- [x] Gare de triage d'Alyth à Calgary (wagons, locomotive, feux de barils, tour de Calgary), relais routier de la route 1 (Priya, Dale), trajet au choix (camion de Dale après avoir posé ses chaînes, motoneige 90 $, à pied 6 h)
- [x] Ranch Bow Valley dans les Rocheuses : lodge, grange, dortoir, ruisseau gelé, forêt de pins enneigés ; l'Éleveur (négociation, combat, interrogatoire)
- [x] Piste du niveau 5 : « le Notaire » à Halifax ; indice final : une maison à Westmount (Montréal)
- [x] Cinématique d'arrivée ; tests : 63 vérifications (niveaux 1 à 4)
- [ ] Test visuel et réglage par un humain

## Bloc 9 — Niveau 5 : Nouvelle-Écosse `[x]` (v0.9.0)
- [x] **Verglas** : Oscar glisse (garde son élan), peut tomber s'il court ; **crampons** à trouver (boîte des dons) ; pluie verglaçante, glaçons sur les toits
- [x] **Équipement conservé d'un niveau à l'autre** (parka, mitaines, tuque, bottes, crampons)
- [x] **Caméras de surveillance** qui balaient les couloirs (cône visible) ; **coupure de courant** au tableau de fusibles (caméras aveugles, pénombre, gardes moins efficaces)
- [x] **Cloisons basses** : accroupi, Oscar est caché derrière les bureaux
- [x] **Relève de 23 h** : la porte de service reste ouverte dix minutes (le temps de jeu compte)
- [x] **Déchiqueteuse** : si l'alerte dure trop, le Notaire détruit une partie des preuves (fin différente des dossiers)
- [x] Front de mer d'Halifax (entrepôts historiques, horloge de la Citadelle), Mission des marins (Gisèle, Sam le journaliste, Bernie l'ancien combattant), cabinet Doucet & Associés
- [x] Piste du niveau 6 : le « Bras droit » d'Omer à Winnipeg (il garde les codes de la maison de Westmount)
- [x] Cinématique d'arrivée ; tests : 79 vérifications (niveaux 1 à 5)
- [ ] Test visuel et réglage par un humain

## Bloc 10 — Niveau 6 : Manitoba `[x]` (v0.10.0)
- [x] **Blizzard à −40 °C** : froid très rapide, même bien équipé ; journées courtes (nuit dès 16 h 30)
- [x] **Poudrerie (voiles blancs)** : brouillard à 4–46 m quand neige et vent forts ; la vue des gardes est réduite de moitié
- [x] **Thermos** (touche **H**, 3 gorgées, +40 de chaleur) offert par Louis ; ligne dans le HUD
- [x] **Abris chauffés** : abribus à lampe chauffante, Café de la Cathédrale, moteurs tièdes des camions aux silos
- [x] Saint-Boniface : ruines de la cathédrale, Esplanade Riel, rivière Rouge gelée, dôme doré du Palais législatif
- [x] Café de la Cathédrale : Mireille (soupe aux pois, tourtière), Nadia (ex-comptable, promesse ou menace → alerte), Louis (guide métis, motoneige)
- [x] Deux trajets : motoneige (1 h) ou marche sur la rivière gelée (5 h, gros coup de froid)
- [x] Silos de Saint-Norbert : silos en béton, élévateur à grain, voie ferrée, hangar, avion, piste balisée ; bureau de Viktor
- [x] Boss **Viktor, le Bras droit** ; indice final : la mallette (adresse à Westmount, code du sous-sol 1967, relève à minuit, tempête de verglas vendredi)
- [x] Cinématique d'arrivée ; tests : 91 vérifications (niveaux 1 à 6)
- [ ] Test visuel et réglage par un humain

## Bloc 11 — Niveau 7 : Montréal (final) `[x]` (v1.0.0)
- [x] **Tempête de verglas** : pluie verglaçante, sol glissant, **branches chargées de glace qui tombent** (craquement d'alerte, 1,5 s pour s'écarter), **fil électrique tombé** sous tension
- [x] **Panne générale** : Westmount dans le noir, bougies aux fenêtres ; seule la maison d'Omer brille (génératrice)
- [x] Refuge de la salle paroissiale : Hélène (Croix-Rouge, soupe, tâche du bois → vie bonus), Marie-Rose (cuisinière d'Omer), Réjean (monteur d'Hydro-Québec)
- [x] Trois entrées : le **portail** (mot de passe, escorté comme homme de Viktor), la **ruelle de service** (porte de la cuisine ouverte de minuit à minuit 15), le **mur du jardin** (escalade risquée sans crampons) puis la porte-fenêtre (bruit)
- [x] La maison : hall, cuisine, salle à manger, bibliothèque, grand salon ; vraies portes ; caméras ; **génératrice à saboter** (noir total, caméras aveugles, mais le pavé du sous-sol s'éteint)
- [x] Boss **Omer** (300 PV) ; choix final : le frapper ou le livrer à la police (Oscar s'arrête toujours) ; clé du sous-sol ; code 1967
- [x] Le sous-sol, les dessins de Cédric au charbon ; **cinématique de fin** (retrouvailles, arrestation d'Omer, dernier appel du numéro masqué) ; écran de fin du jeu
- [x] Corrections : les gardes au corps à corps ne blessaient Oscar qu'au port de Toronto (tous les niveaux) ; le combat de boss réveille bien les gardes de la pièce ; caméras de surveillance réutilisables par tous les niveaux
- [x] Tests : 112 vérifications (niveaux 1 à 7) ; passage réel 6 → 7 et cinématique de fin sans erreur
- [ ] Test visuel et réglage par un humain

## Bloc 12 — Confort de jeu `[x]` (v1.1.0)
- [x] **Options** (sauvegardées) : sensibilité souris/manette, inverser l'axe vertical, volume général, musique et ambiance, **difficulté des combats** (Découverte / Normale / Expert : repérage et dégâts ; le chronomètre ne change jamais), **qualité graphique automatique** (baisse seule si le jeu rame), taille des sous-titres, indices, astuces, compteur d'images
- [x] **Chapitres** : rejouer tout niveau débloqué depuis l'écran titre, avec le meilleur temps
- [x] **Trophées** (12) et **records de temps** par niveau
- [x] **Musique qui suit l'action** (calme, tension quand un garde te soupçonne, percussions en combat) et **ambiance** pluie/vent, étouffée à l'intérieur
- [x] **Indices du numéro masqué** : SMS automatique après 5 min bloqué sur une étape, ou touche **I** (après 1 min 30)
- [x] **Manette** (Xbox/PlayStation standard) : jeu, dialogues, cinématiques et menus
- [x] **Astuces** contextuelles (une seule fois chacune), alerte de temps (moins d'un cinquième restant)
- [x] Pause : Options, **Quitter vers l'écran titre** (partie sauvegardée) ; **F1** aide ; indicateur « Sauvegardé »
- [x] Les sauvegardes restent valides d'une version 1.x à l'autre ; textes « en construction » retirés
- [x] Tests : 123 vérifications ; essai réel menus + manette simulée sans erreur

## Bloc 13 — Premier test visuel réel `[x]` (v1.1.1)
- [x] HUD caché pendant les cinématiques ; caméra gardée dans les petites pièces ; Montréal jouable dans la panne ; météo du début de niveau garantie

## Bloc 14 — Oscar en modèle 3D animé `[x]` (v1.2.0)
- [x] Modèle squelettique (rig Mixamo) : repos, marche, course capturés ; poses du jeu recopiées (coups, blocage, visée, accroupi, cinématiques)
- [x] Repli automatique + option « Classique » ; vérifié sur le vrai rendu
- [ ] Vrai Oscar (uniforme canadien, visage, barbe) via un compte Mixamo ; animations de combat capturées
- [ ] Puis : Eva, Cédric, Omer, gardes

## Bloc 15 — Personnages et lieux réels `[~]` (v1.3.0 → v1.4.1)
- [x] Outil de réduction FBX ; 8 personnages Mixamo réduits ; 23 animations
- [x] Oscar = soldat Mixamo avec animations capturées
- [x] Matières photographiques (Poly Haven) sur façades, sols, murs, neige
- [ ] TOUTES les personnes en humains réalistes (passants, assis, cyclistes, PNJ de l'histoire, ennemis, cinématiques) — attend ~10 personnages Mixamo de plus
- [x] Feuillage réaliste (feuilles/aiguilles), écorce photographiée, vrais bancs 3D (v1.5.0)
- [ ] Lampadaires et bornes-fontaines réels près d'Oscar ; voitures ; ciels photographiés (HDRI)

## Bloc 16 — Contribution de Kimi intégrée `[x]` (v1.6.0)
- [x] Passants vivants (bancs, groupes, téléphone), oiseaux, chiens, avions, clients dans les intérieurs
- [x] Pluie réaliste (éclaboussures, asphalte mouillé, voile), voitures détaillées, visages plus humains
- [x] Effets de cinéma (réglables), HUD compact
- [x] Corrections : plantage des niveaux, villes de province cassées retirées, Toronto rétabli, météo du HUD, performances
- [ ] Vérification visuelle sur le PC de Boban après envoi

## Bloc 17 — Villes ouvertes des provinces `[~]` (v1.7.0)
- [x] Générateur commun avec un profil par province (quartiers, commerces, couleurs, arbres, hiver, eau, monument)
- [x] Vancouver, St. John's, Calgary, Halifax, Winnipeg, Montréal : tours, maisons, commerces, arbres, bancs, passants, voitures
- [x] Porte « Explorer la ville » / « Retour » dans chaque niveau 2 à 7 ; Toronto intacte
- [ ] Vérification visuelle sur le PC de Boban après envoi

## Bloc 18 — Vrais humains pour tout le monde `[~]` (v1.8.0)
- [x] 13 personnages Mixamo (hommes, femmes, hommes d'Omer, enfant) et 9 animations du quotidien
- [x] Remplacement automatique des personnages proches (passants, assis, cyclistes, ennemis, lieux, cinématiques)
- [ ] Vérification visuelle sur le PC de Boban après envoi
- [x] Combat des hommes d'Omer : visée, coups, réactions, chutes, reddition
- [x] Personnes âgées et jogging
- [x] Cyclistes : pédalage recopié du squelette simple (pas d'animation de vélo Mixamo)

## Bloc 19 — Vrais véhicules `[~]` (v1.9.0)
- [x] 7 modèles CC-BY (3 voitures, taxi, police, moto, vélo), crédits dans le jeu
- [x] Conducteurs au volant, motos dans la circulation
- [ ] Vérifier à l'écran le sens avant/arrière de chaque modèle

## Bloc 20 — Réalisme total (liste de Boban, adaptée au Canada moderne) `[~]`
- [x] Corps et blessures : blessures localisées, saignement, infection et fièvre, froid qui engourdit, trousses (v1.15.0)
- [x] Physique du monde : élan selon l'équipement, sol mouillé et flaques glissants, eau + courant électrique, barils, feu qui se propage avec le vent, fumée (v1.16.0)
- [x] Vie des passants (v1.17.0 : peur et fuite, regards, heures d'ouverture ; v1.18.0 : réputation qui circule, méfiance et négociation avant de parler, personne n'apparaît sous les yeux ; v1.24.0 : emplois du temps — maison et travail précis, sortie le matin, retour le soir, sortie en soirée, chiens promenés aux bonnes heures)
- [x] Économie (v1.19.0 : prix selon la province, la météo et l'heure ; espèces et carte avec trace bancaire ; v1.24.0 : objets pris sur les hommes d'Omer reconnaissables, touche L)
- [x] Hygiène et odeur : saleté selon le temps, la météo et les lieux ; passants qui s'écartent, chiens qui flairent, méfiance ; se laver dans 8 lieux (v1.20.0)
- [x] Interface invisible : mode immersif sans mini-carte ni marqueur, carte sur le téléphone (M), lecture sans pause (v1.21.0)
- [x] Décors qui racontent et accents régionaux : répliques surprises dans 7 parlers, traces de captivité au sous-sol (v1.21.0)
- [x] Parler régional dans les dialogues principaux : 21 personnages accueillent Oscar dans le parler de leur province (v1.24.0)
- [x] Nuit lisible (vrais lampadaires, adaptation de l'œil, v1.22.0) ; couverts sur les tables selon le lieu, personnages face à leur table (v1.23.x)
- [ ] Couleur de peau des corps scannés accordée à chaque personnage (Marie-Rose a un corps de femme blanche) — outil `__oscar.lineup()` prêt

## Après la v1.1 `[ ]`
- [ ] Test humain complet des 7 niveaux, réglage de la difficulté et des chronomètres
- [ ] Décider l'identité du personnage mystérieux (suite possible)
- [ ] Multijoueur (base prévue au §11 du plan)
- [x] 6 Colombie-Britannique (v0.6.0, voir plus haut) · [x] 7 Terre-Neuve (v0.7.0) · [x] 8 Alberta (v0.8.0) · [x] 9 Nouvelle-Écosse (v0.9.0) · [x] 10 Manitoba (v0.10.0) · [x] 11 Montréal (final, v1.0.0)
- Systèmes d'hiver : neige, verglas, blizzard, équipement d'hiver

## Bloc 12 — Multijoueur `[ ]`
- [ ] Serveur autoritaire, comptes, sauvegardes serveur — voir `docs/ARCHITECTURE.md`

