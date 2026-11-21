# Oscar — Opération Omer · Plan complet du jeu

> Document de conception de référence. Toute décision de jeu validée par le propriétaire du projet est écrite ici.
> Ne pas inventer de règle de jeu sans validation : proposer dans `docs/JOURNAL.md` (section « Questions ouvertes »).

## 1. Résumé

Jeu d'action-aventure 3D, solo pour l'instant (multijoueur prévu plus tard, objectif : 12 000 joueurs).
Un soldat d'élite canadien, **Oscar**, traverse le Canada pour retrouver sa femme **Eva** et son fils **Cédric**, enlevés par le chef criminel **Omer**.
Le jeu mêle enquête, infiltration, négociation, combat à mains nues et armé, et survie face au climat canadien.

## 2. Personnages

### Oscar (héros)
- Soldat d'élite canadien, vit à **Toronto**.
- Famille : **Eva** (sa femme) et **Cédric** (son fils).
- Ne connaît pas Omer et ne sait pas où il se cache au début.

### Omer (antagoniste)
- Chef d'un réseau criminel actif **au Brésil et au Canada** : usines de drogue, trafic d'armes.
- Apparence : visage dur de gangster, cicatrice, barbe mal rasée, regard froid, bijoux en or, manteau long en cuir.
- Habitudes : fume sans arrêt (cigares, cigarettes), se drogue, boit, imprévisible et violent.
- Vit dans une résidence luxueuse et sécurisée à **Montréal**, entouré de femmes, de fêtes, de gardes armés (portes, toits, chiens), d'un **bras droit** et de **lieutenants** dans chaque province.
- **Mobile** : vengeance. Oscar a détruit ses usines et ses ventes d'armes au Brésil et fait arrêter ses hommes. Les gangs brésiliens ont donné le nom d'Oscar à Omer.

### Eva et Cédric
- Enlevés à Toronto pendant qu'Oscar était au Brésil.
- Enfermés **dans le sous-sol de la résidence d'Omer à Montréal**, du début à la fin.

### Le personnage mystérieux
- C'est lui qui passe l'**appel anonyme** à Oscar au Brésil.
- Revient pendant l'aventure, toujours caché (capuche, ombre, de dos, derrière une vitre) : on ne voit jamais bien son visage.
- Laisse des indices quand Oscar est bloqué. Allié ou piège : le doute reste.
- Identité : à décider (garder le mystère ou révéler à la fin).

## 3. Le mot d'Omer
> « Tu as détruit ce que j'ai bâti il y a un mois. Alors je me venge. Tu vas payer, et tu vas savoir ce qu'est la souffrance. »

## 4. Ouverture (cinématiques, le joueur regarde)
1. **Brésil, la nuit** : arrivée en hélicoptère d'Oscar et de son unité.
2. **L'assaut** sur les armureries et laboratoires de drogue d'Omer : explosions, fusillades, arrestations.
3. **Victoire** : les usines brûlent.
4. **L'appel anonyme** : sa femme et son fils ont été enlevés.
5. **Flash-back Toronto** : soirée calme (Eva prépare le souper, Cédric fait ses devoirs, appel vidéo coupé), véhicules noirs, Omer entre avec ses hommes, enlèvement, Omer pose le mot sur la table. Le joueur voit le visage d'Omer, Oscar non.
6. **Repaire d'Omer à Montréal** : fête, fumée, gardes ; on lui annonce la capture ; il lève son verre : « Maintenant, le soldat va comprendre. »
7. **Retour d'Oscar** dans la maison vide, il lit le mot → le joueur prend le contrôle (niveau 1).

## 5. Les niveaux, les saisons et le climat

L'histoire avance de l'automne vers le cœur de l'hiver. Chaque province est plus difficile que la précédente.

| Niv. | Lieu | Saison | Météo | Difficulté |
|---|---|---|---|---|
| 1 | Toronto (Ontario) | Début de l'automne | Doux, averses | ★ |
| 2 | Colombie-Britannique | Automne | Pluie constante, brouillard, forêts, montagnes | ★★ |
| 3 | Terre-Neuve | Fin de l'automne | Vents violents, tempêtes en mer, brouillard | ★★★ |
| 4 | Alberta | Début de l'hiver | Froid sec −25 °C, neige des Rocheuses | ★★★★ |
| 5 | Nouvelle-Écosse | Hiver | Tempête côtière, verglas | ★★★★★ |
| 6 | Manitoba | Plein hiver | Blizzard −40 °C, journées très courtes | ★★★★★★ |
| 7 | Montréal (Québec) | Cœur de l'hiver | Tempête de neige et de verglas pendant l'assaut final | ★★★★★★★ |

Le parcours fait des allers-retours d'un bout à l'autre du pays : chaque indice envoie Oscar vers la province suivante (Omer brouille la piste).

**Effets du climat** : jauge de chaleur corporelle, équipement d'hiver à trouver/acheter, visibilité réduite (brouillard, nuit, blizzard), déplacements ralentis (neige, verglas), visée moins stable et armes qui s'enrayent dans le froid, endurance réduite, nuits plus longues.

**Ce qui augmente aussi** : nombre et intelligence des ennemis, méfiance des témoins, risque d'être démasqué en infiltration, pièges tendus par Omer.

### Structure type d'un niveau
Arrivée → enquête (indices, témoins) → infiltration ou négociation → combats → affrontement contre le **lieutenant d'Omer** → dernier indice vers la province suivante.

### Lieux réels reconnaissables (exemples)
- Toronto : tour CN, Kensington Market, le port, King Street et son tramway.
- Colombie-Britannique : port de Vancouver, forêt pluviale, montagnes.
- Terre-Neuve : St. John's et ses maisons colorées, port de pêche.
- Alberta : Calgary, les Rocheuses, champs pétroliers.
- Nouvelle-Écosse : port d'Halifax, côte rocheuse.
- Manitoba : Winnipeg, plaine glacée, silos à grain.
- Montréal : Vieux-Montréal, métro, port, mont Royal. Résidence d'Omer.

### Niveau 7 — final
Pendant la tempête de verglas, Oscar entre dans la résidence d'Omer, traverse les gardes et la fête, affronte Omer et descend au sous-sol libérer Eva et Cédric.

## 6. Monde vivant
- Villes réelles avec circulation : voitures, autobus/tramways, vélos, piétons ; moins de monde la nuit et pendant les tempêtes.
- Lieux où Oscar entre et ressort : restaurants, cafés, bars, motels, magasins (vêtements d'hiver, nourriture), stations-service, garages, entrepôts, appartements.
- Gens à qui parler : serveurs, chauffeurs de taxi, commerçants, sans-abri, policiers — indices contre argent, service ou confiance.
- Cycle jour/nuit et météo dynamique.
- Signalisation en anglais dans les provinces anglophones, en français à Montréal.

## 7. Actions d'Oscar
- **Enquêter** : chercher des indices, interroger.
- **Infiltrer** : se faire passer pour un bandit.
- **Négocier** : dialogues à choix avec conséquences.
- **Se procurer des armes** : il n'en a pas au départ.
- **Combattre** : poings, pieds, armes.
- **Faire la guerre** : affrontements de grande ampleur.

## 8. Le temps (règle la plus importante)
- **Chaque niveau a son propre compte à rebours**, affiché à l'écran (jours/heures de jeu).
- Le temps est **normal, adapté au contenu du niveau** — il n'est **pas** réduit artificiellement d'un niveau à l'autre.
- Les actions consomment du temps : voyager, dormir, se soigner, attendre la fin d'une tempête, interroger.
- Certains choix font gagner du temps (bon indice par négociation, raccourci par infiltration, allié avec véhicule).
- Omer envoie des **messages/vidéos** (courtes cinématiques) d'Eva et Cédric dans le sous-sol ; ils contiennent parfois un petit indice caché.
- Plus le temps passe : état d'Eva et Cédric qui se dégrade (visible), lieutenants prévenus, météo pire.

## 9. Vies et échec
| Situation | Conséquence |
|---|---|
| Oscar meurt (1re ou 2e fois) | Perd une vie, reprend au dernier point de sauvegarde (indices conservés, temps perdu non rendu) |
| Oscar meurt une 3e fois | Échec → le niveau recommence |
| Temps écoulé | **Échec immédiat**, même s'il reste des vies → le niveau recommence |
| Niveau réussi | 3 vies neuves au niveau suivant ; les niveaux réussis restent acquis |

En cas d'échec : courte cinématique d'Omer (furieux ou moqueur) dans le sous-sol, puis « Mission échouée ».

### Vies bonus
- Gagnées en accomplissant des **tâches secondaires** (aider un commerçant menacé, livrer un colis, sauver quelqu'un dans une tempête, retrouver un objet volé…).
- **Maximum 2 dans tout le jeu.**
- **Elles suivent Oscar partout**, d'un niveau à l'autre, jusqu'à utilisation.
- Utilisées seulement quand les 3 vies normales du niveau sont perdues. Une vie bonus utilisée est perdue pour toujours.
- Les tâches prennent du temps : le chronomètre continue.

## 10. Direction artistique : réalisme humain
Directives maîtresses obligatoires : voir `docs/DIRECTIVES_REALISME.md`.
Résumé : peau réelle et imparfaite, regard vivant, asymétrie naturelle, mains toujours visibles et occupées, démarche avec poids réel, vêtements froissés et cohérents avec la météo, micro-actions permanentes, lieux habités avec traces de vie, lumière naturelle.
Exemple pour la maison d'Oscar (bloc 2) : veste d'Eva sur une chaise, devoirs de Cédric ouverts sur la table, tasse à moitié vide, clés, courrier, chaise renversée pendant l'enlèvement, lumière du matin par la fenêtre avec poussière dans l'air.

## 10b. Niveau 1 — Toronto : déroulement de l'enquête (bloc 2)
> Contenu **proposé par Claude**, à valider par le propriétaire (voir `docs/JOURNAL.md`).
1. **La maison** : Oscar fouille. Indices : le mot d'Omer, le téléphone de Cédric sous le canapé (photo d'un VUS noir, plaque « CJ…7 », voix en portugais), le mégot de cigare sur le perron. Détails émotionnels : les clés d'Eva, les devoirs de Cédric. Il faut 2 indices principaux sur 3.
2. **Le voisin, M. Henderson** : deux VUS noirs vers 19 h 40, des hommes parlant portugais, vus la veille au Lina's Diner.
3. **Le Lina's Diner** (sur King Street) — plusieurs façons d'obtenir la piste :
   - **Lina**, la propriétaire : dire la vérité ouvre la discussion ; la menacer la fâche et ferme cette piste. Elle a le reçu des hommes mais ne le retrouve pas : soit Oscar la dédommage (50 $, 30 min), soit il retrouve son pot à pourboires volé (tâche secondaire → **vie bonus**).
   - **Marcus**, chauffeur de taxi : a conduit un des hommes au port. 20 $, ou la vérité (plus long).
   - **Jayden**, jeune nerveux : sait où le voleur a jeté le sac (dans le parc).
   - **M. Kowalski**, vieil habitué : témoignage d'ambiance (le plus grand regardait le port).
4. **La piste** : « Harbourfront Marine Storage », **entrepôt 7** au port → suite au bloc 3 (infiltration et combat contre le lieutenant d'Omer).
- Chaque action coûte du temps de jeu (fouiller, parler). Oscar commence avec **240 $**.

## 10c. Niveau 1 — Toronto : le port (bloc 3)
> Contenu **proposé par Claude**, à valider.
- **Harbourfront Marine Storage**, zone portuaire gardée. Entrée : soudoyer le garde (100 $), lui mentir avec le nom de la société (si on a le reçu du diner), le provoquer (combat), ou se faufiler par un trou dans la clôture à l'ouest.
- **Infiltration** : 7 gardes (patrouilles et postes fixes). Se faire repérer déclenche l'alerte (sirène) : tous les gardes attaquent. Un **gilet de docker** près du bureau de chantier rend Oscar moins suspect (s'il ne court pas et n'a pas d'arme en main).
- **Armes** : Oscar n'en a pas au départ. Il les prend sur les gardes neutralisés ou dans la caisse d'armes de l'entrepôt.
- **Tiago « Faca » Moreira**, lieutenant d'Omer à Toronto (crâne rasé, bouc, chaîne en or), avec 2 gardes du corps. **Négociation** possible avant le combat (il refuse), combat, puis **interrogatoire** : il révèle le manifeste.
- **Piste du niveau 2** : conteneur MSKU 448127 parti pour le **port de Vancouver**, où attend un homme d'Omer surnommé **« le Pasteur »**. Eva et Cédric n'étaient pas à Toronto.

## 10d. Cinématiques (bloc 4)
- L'ouverture suit le §4 à la lettre. Détails ajoutés par Claude (à valider) : Eva prépare le souper et Cédric demande « Papa appelle quand ? » ; Omer dit à Eva « Ton mari a détruit ce que j'ai bâti. Maintenant, c'est son tour. » ; dans le sous-sol, Cédric demande si papa va venir.
- **Messages vidéo d'Omer** : 3 au maximum dans le niveau 1 (après 14 h, 34 h et 54 h de jeu). Le premier contient un indice pour la fin du jeu : une corne de navire et un métro qui passe (Montréal).
- **Échec** : courte scène d'Omer dans le sous-sol, puis l'écran « Mission échouée ».

## 10e. Niveau 2 — Colombie-Britannique (bloc 6)
> Contenu **proposé par Claude**, à valider.
- **Vancouver, 6 h 10, pluie** : le conteneur MSKU 448127 au terminal de Centerm, surveillé par 4 hommes d'Omer. Dedans : des fusils, des tracts « Église de la Dernière Lumière — Squamish » et un téléphone jetable.
- **The Rusty Anchor**, bar en face du terminal : Maggie (barmaid), **Earl** (pêcheur dont le neveu Josh est dans la secte), un motard qui vend l'information 80 $. Le **surplus militaire** vend un imperméable (60 $).
- **Aller à Squamish** : Earl conduit si Oscar promet de ramener Josh ; sinon taxi (120 $, 2 h) ou stop (gratuit, 5 h).
- **Le camp du Pasteur** dans la forêt pluviale, sous la falaise du Chief. Pont gardé, ou passage discret par un tronc tombé à l'ouest.
- **Josh** : on peut le convaincre de partir (vie bonus) ou le combattre.
- **Le Pasteur**, chef de secte au service d'Omer : négociation, combat, interrogatoire. **Piste du niveau 3** : le chalutier « Marie-Galante » part de **St. John's** dans quatre jours. Dans la valise, **un dessin de Cédric** : une montagne avec une grande croix lumineuse (le mont Royal, Montréal).
- Climat : 4 à 11 °C, pluie presque constante. L'imperméable divise l'effet de la pluie ; café chaud et chauffage du pick-up rendent la chaleur.

## 10f. Niveau 3 — Terre-Neuve (bloc 7)
> Contenu **proposé par Claude**, à valider.
- **St. John's, fin novembre, 18 h 45, avis de tempête** (−1 à 6 °C, vent de 60 à 110 km/h). Chronomètre : 60 h (niveau plus court).
- **Pub The Ship's Lantern** : **Bridget**, pilote du port (le quai 18) ; **Wilf**, vieux pêcheur (sa doris) ; **Liam**, matelot du Marie-Galante qui a peur (le mot de passe « Brume ») ; un violoneux.
- **Monter à bord** : mot de passe, 100 $ à la sentinelle, combat, ou par la mer avec la doris de Wilf (si on l'aide à l'amarrer dans la tempête).
- **Le capitaine Roy**, au service d'Omer : négociation, combat sur le pont, interrogatoire. **Piste du niveau 4** : la cargaison part en train vers **Calgary**, chez **« l'Éleveur »**, un ranch au pied des Rocheuses. Roy confirme le **métro** qu'on entend derrière Omer.

## 10g. Niveau 4 — Alberta (bloc 8)
> **Décision du propriétaire** : l'équipement d'hiver se **trouve** (il ne s'achète pas). Le reste est **proposé par Claude**, à valider.
- **Calgary, début décembre, 6 h 45, −22 °C.** Oscar descend d'un train de marchandises en blouson. Chronomètre : 66 h.
- Équipement à trouver : **parka** (atelier d'entretien de la gare), **mitaines** (cabine d'une locomotive), **tuque et bottes** (boîte des objets perdus du relais, avec l'accord de Priya).
- **Relais routier de la route 1** : Priya (caissière), **Dale** (camionneur : poser ses chaînes dans le froid → il emmène Oscar). Sinon motoneige (90 $) ou à pied (6 h, très dangereux).
- **Ranch Bow Valley** au pied des Rocheuses. **L'Éleveur** (chapeau, manteau en peau de mouton) : négociation, combat, interrogatoire. **Piste du niveau 5** : « **le Notaire** », un cabinet du port d'**Halifax** qui blanchit l'argent d'Omer. **Indice final** : une facture d'électricité pour une maison de **Westmount** (Montréal).
- Neige : traces de pas suivies par les gardes ; neige profonde hors des chemins déneigés.

## 10h. Niveau 5 — Nouvelle-Écosse (bloc 9)
> Contenu **proposé par Claude**, à valider.
- **Halifax, mi-décembre, 21 h, pluie verglaçante** (−5 à 0 °C). Chronomètre : 48 h. L'équipement trouvé en Alberta est conservé.
- **Mission des marins** : **Gisèle**, bénévole acadienne (la carte magnétique de sa fille Chloé, qui fait le ménage chez le Notaire ; des crampons dans la boîte des dons) ; **Sam**, journaliste d'enquête (le plan de l'étage, contre l'histoire ou 150 $) ; **Bernie**, ancien combattant (la relève de 23 h).
- **Entrer** : carte magnétique, porte de service entre 23 h et 23 h 10, ou l'escalier de secours glacé (risque de chute sans crampons).
- **Cabinet Doucet & Associés** : caméras, tableau de fusibles, cloisons basses, gardes. **Le Notaire** : il négocie, appelle la sécurité et court vers la **déchiqueteuse**. Si l'alerte dure plus d'environ 50 s, l'adresse de Montréal est détruite.
- **Piste du niveau 6** : le **« Bras droit »** d'Omer, à **Winnipeg**, payé chaque mois, garde les codes de la maison de **Westmount** (sous-sol aménagé).

## 10i. Niveau 6 — Manitoba (bloc 10)
- Winnipeg, fin décembre, 16 h 15, −38 °C, blizzard. Chronomètre : 36 h de jeu.
- Café de la Cathédrale (Saint-Boniface) : **Mireille** la propriétaire ; **Nadia**, ancienne comptable de Viktor, terrifiée (la promettre à l'abri → piste ; la menacer → elle crie, les hommes de Viktor attaquent) ; **Louis**, guide métis, motoneige et thermos (gratuit si Oscar dit la vérité, 100 $ sinon).
- Silos de Saint-Norbert : dépôt gardé (8 gardes), avion privé prêt à décoller. Boss **Viktor, le Bras droit** (manteau noir à col de fourrure, mallette en métal).
- Indice : la mallette — maison d'Omer à Westmount, code du sous-sol **1967**, relève à minuit, « Vendredi, tempête de verglas sur Montréal ».

## Commandes (v0.4)
ZQSD/WASD bouger · Maj courir · Espace sauter · X s'accroupir · E interagir · F neutraliser par derrière / fouiller · clic gauche (ou J) frapper/tirer · clic droit (ou K) coup de pied/viser · V bloquer · 1 2 3 armes · R recharger · C carnet · T accélérer le temps · Échap pause.

## 11. Multijoueur
- Reporté. Objectif futur : architecture capable de supporter **12 000 joueurs**. Voir `docs/ARCHITECTURE.md`.

## 12. Questions ouvertes
Voir `docs/JOURNAL.md` → « Questions ouvertes ».
