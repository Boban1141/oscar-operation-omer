# Journal de développement

Entrées les plus récentes en haut. Voir le modèle dans `AGENTS.md`.

## Questions ouvertes
- **À décider** : l'identité du personnage mystérieux (la fin garde le mystère et ouvre une suite).
- **À valider** : tout le niveau 7 (Hélène, Marie-Rose, Réjean, le mot de passe, la fin, Omer livré à la police) — `docs/PLAN.md` §10j.
- **À valider** : tout le niveau 6 (Mireille, Nadia, Louis, Viktor, le code 1967, la tempête de verglas) — `docs/PLAN.md` §10i.
- **À valider** : tout le niveau 5 (Gisèle, Chloé, Sam, Bernie, le Notaire, le Bras droit à Winnipeg) — `docs/PLAN.md` §10h.
- **À valider** : tout le niveau 4 (Priya, Dale, l'Éleveur, le Notaire, Westmount) — `docs/PLAN.md` §10g.
- **À valider** : tout le niveau 3 (Bridget, Wilf, Liam, la doris, le capitaine Roy, « l'Éleveur ») — `docs/PLAN.md` §10f.
- **À valider** : tout le niveau 2 (Earl, Josh, Maggie, le Pasteur, l'Église de la Dernière Lumière, le « Marie-Galante », le dessin de Cédric) — `docs/PLAN.md` §10e.
- **À valider** : Tiago « Faca » Moreira, le port, « le Pasteur » et la piste de Vancouver (`docs/PLAN.md` §10c).
- **À régler après test humain** : difficulté (vitesse de repérage, précision des gardes), durée du chronomètre du niveau 1 (72 h de jeu = 72 minutes réelles).
- **À valider** : le contenu de l'enquête du niveau 1 (personnages Henderson, Lina, Marcus, Jayden, Kowalski ; indices ; piste de l'entrepôt 7) a été proposé par Claude — voir `docs/PLAN.md` §10b.
- ~~Moteur final~~ → **tranché : on continue dans le navigateur (Three.js)**, sans Epic. Unreal reste possible plus tard (`docs/PLAN_UNREAL.md`).
- Identité du personnage mystérieux : révélée à la fin ou mystère gardé ?
- Titre définitif du jeu (provisoire : « Oscar — Opération Omer »).
- Apparence d'Oscar (provisoire dans le code : peau foncée moyenne, cheveux noirs courts, veste kaki, sac à dos).
- Durée exacte du chronomètre de chaque niveau (provisoire niveau 1 : 72 h de jeu ; 1 seconde réelle = 1 minute de jeu).

---

## 2026-11-25 — Claude — Tenue civile dans les rues de toutes les villes (v1.13.3)
- Vérifié sur le PC de Boban (commit f841c4d) : aucune erreur. Les 7 niveaux démarrent bien. Oscar était en tenue civile à Toronto, mais en militaire au point de départ des niveaux 2 à 7. Ces départs (Vanport, port de St. John's, cour de triage, Halifax, Winnipeg, Westmount) sont des zones de jeu ouvertes (`ARENAS`) pleines de passants.
- La tenue militaire ne sert plus que dans les lieux de mission armée (`HOSTILE` : entrepôt du port, forêt et chapelle, chalutier, ranch, bureau du notaire, silos, manoir, sous-sol, cour de triage). Partout ailleurs, tenue civile ; la touche G reste disponible.

## 2026-11-25 — Claude — Passagers visibles (v1.13.2)
- Vérifié sur le PC de Boban (commit ab47c3a) : en 10 s de jeu réel, aucun passant l'un dans l'autre, aucune voiture sur un piéton. La tenue militaire reste noire en jeu, alors que ses 4 parties sont visibles et ont leur texture chargée (`__oscar.skin()`). Ajout de `__oscar.dbg(f)` (accès de diagnostic à la scène) pour chercher la cause directement sur son PC.
- Tenue militaire noire : cause trouvée sur le PC de Boban avec `__oscar.dbg`. Les textures, les normales et l'éclairage sont corrects. En blanc uni le soldat est bien éclairé, et avec sa texture sans éclairage il est visible. C'est le camouflage, très sombre, qui tombait au noir sous la lumière du jeu. Correction : la texture éclaire en partie d'elle-même (`emissiveMap`, intensité 0,45). Essayé en direct : le camouflage vert-brun est bien visible.
- Demande de Boban : on doit voir la tête des passagers dans les bus et les trains. Le jeu n'a ni bus ni train, mais il a les tramways de Toronto, et leur bande de fenêtres était opaque.
  - Vitres teintées transparentes, et un plancher intérieur.
  - 7 passagers par tramway : 5 assis le long des vitres, 2 debout, certains au téléphone. Ce sont des personnages comme les autres, qui deviennent de vrais humains de près.
  - Les taxis transportent un client assis à l'arrière, visible même quand le taxi est un vrai modèle 3D.

## 2026-11-25 — Claude — Plus personne ne se marche dessus (v1.13.1)
- Signalé par Boban : les personnages se traversaient, entraient dans leur ami, et les voitures roulaient sur les humains.
- Passants :
  - Chacun garde sa droite : deux files sur le trottoir selon le sens de marche.
  - Derrière quelqu'un qui va dans le même sens, on ralentit ou on s'arrête. Devant quelqu'un qui arrive en face ou qui est arrêté, on s'écarte en douceur.
  - Les groupes qui discutent se tenaient parfois au milieu d'un bâtiment, tournés n'importe comment. Ils sont maintenant sur le trottoir, côté façades, en cercle serré et face les uns aux autres.
- Véhicules : chaque voiture, taxi, moto ou vélo regarde devant son capot, sur une distance qui grandit avec la vitesse. Elle s'arrête pour un piéton, une personne arrêtée ou un autre véhicule, y compris aux carrefours (à égalité, un seul passe, pour éviter le blocage).
- Soldat KSK : sur le PC de Boban (commit e77cf2b), la tenue civile s'affiche bien et la touche G fonctionne, mais la tenue militaire reste noire. Hors du jeu, le même modèle s'affiche texturé, y compris en marchant. Le jeu laisse maintenant FBXLoader charger lui-même les images `Tex_*.jpg`. Un point de diagnostic `__oscar.skin()` est ajouté pour la vérification suivante.
- Test ajouté : 30 secondes de ville simulées, aucun passant l'un dans l'autre, aucune voiture sur un piéton (146/146).

## 2026-11-25 — Claude — Oscar change de tenue (v1.13.0)
- Question de Boban : Oscar peut-il changer de vêtements ? En tenue militaire dans certains lieux, il ferait peur aux gens. Choix de Boban : changement automatique, plus une touche.
- Deux tenues sur le même corps animé :
  - civile : t-shirt gris et jean, le corps scanné de Nathan par-dessus ;
  - militaire : le soldat KSK lui-même, casque, gilet et camouflage.
  Les armes suivent la main de la tenue portée.
- Automatique (`autoOutfit`) : tenue militaire dans les lieux de combat (`ARENAS` : port, entrepôts, forêt, silos, manoir…), tenue civile partout ailleurs (ville, maisons, diner, bars, pub, café, refuge…). À chaque changement de lieu, le jeu choisit de nouveau.
- Touche G (`toggleOutfit`) : Oscar change à la main ; un message dit quelle tenue il enfile. Ce choix vaut jusqu'au prochain changement de lieu. La touche est indiquée dans l'aide des commandes.
- Nathan reste réservé à Oscar : il n'est pas parmi les passants.

## 2026-11-25 — Claude — Oscar devient l'opérateur KSK (v1.12.0)
- Boban a téléchargé deux soldats sur Sketchfab (« German KSK operator rigged », « American soldier rigged ») et a choisi le KSK : visage réel, casque, gilet tactique, camouflage.
- Le fichier (déjà passé par Mixamo, squelette `mixamorig`) pointait vers des textures .dds d'un autre ordinateur. Elles ont été intégrées dans le FBX (`embed.py`, à partir des PNG fournis), puis réduites par `fbx_shrink.py` : 16 Mo → 2,4 Mo, `assets/characters/oscar_ksk.fbx`. Le camouflage de l'ancien soldat reste en secours.
- Ce modèle utilise des unités 20 fois plus grandes : la taille est recalée à la hauteur de la tête, et les clés de bassin de toutes les animations d'Oscar (marche, course, coups, armes) sont recalées sur son corps.
- La tenue scannée de Nathan n'est plus portée par Oscar (`OSCAR_LOOK=null`). Nathan retourne parmi les passants.
- v1.12.1 : à l'écran (commit 9916b17), Oscar apparaissait tout noir. Les textures intégrées n'étaient pas reliées aux matières dans le FBX, et FBXLoader ne les chargeait pas. Les trois images sont maintenant fournies à côté du modèle (`assets/characters/Tex_0002_0.jpg`, `Tex_0006_0.jpg`, `Tex_0010_0.jpg`, 1024 px) et branchées par le jeu : casque, visage, corps.
- Licence : modèle Sketchfab, auteur et licence à confirmer avec la page d'origine (à ajouter dans `CREDITS.md`).

## 2026-11-25 — Claude — Chiens tenus en laisse (v1.11.3)
- Vérifié sur le PC de Boban (commit 6260884) : un seul Oscar, tenue de Nathan, en marchant comme à l'arrêt.
- Signalé par Boban : des animaux traversaient la route seuls, en zigzag. Les chiens ajoutés par Kimi erraient au hasard dans la ville. Leur modèle regardait sur le côté, si bien qu'ils avançaient en crabe.
- Correction : chaque chien est maintenant tenu en laisse par un passant qui marche. Il trotte à côté de lui sur le trottoir, s'arrête quand son maître s'arrête et renifle de temps en temps.
  - On voit la laisse, de la main du maître au collier.
  - Le chien est tourné dans le sens de la marche, ses pattes bougent selon sa vitesse, sa taille varie, et il a maintenant un museau.
  - Un chien n'a jamais pour maître un passant assis ou en pleine discussion.

## 2026-11-25 — Claude — Un seul Oscar (v1.11.1)
- Vérifié sur le PC de Boban (commit a64f29d) : Oscar porte bien la tenue de Nathan (t-shirt gris, jean), marche sur le passage piéton, pieds au sol, sans erreur.
- Signalé par Boban : Oscar apparaissait en double. Le chargement de son modèle était lancé deux fois en même temps, par l'écran titre et par les réglages, d'où deux corps. Le second restait figé, superposé au premier : invisible à l'arrêt, visible en marchant. C'était sans doute aussi une cause de l'impression de glissade. Correction : un seul chargement à la fois (`OM.loading`), et l'ancien corps est retiré si le modèle est remonté.
- v1.11.2 : les réglages posaient déjà `OM.loading` avant d'appeler le chargement, qui s'arrêtait donc aussitôt. Oscar restait en forme simple (vu sur le PC de Boban, commit fdfa6c1). Le drapeau n'est plus posé que par `loadOscarModel` lui-même.

## 2026-11-25 — Claude — Oscar change de tenue, pieds au sol (v1.11.0)
- Demande de Boban : changer les vêtements d'Oscar et le rendre plus humain. Il traversait le sol et les tables, et glissait sans qu'on voie ses pieds.
- Tenue : Boban a choisi Nathan, scanné par Renderpeople (visage réel, tenue civile). Le soldat Mixamo reste invisible dessous : il garde les animations, les armes et les cinématiques, et Nathan le suit à chaque image (`dressOscar`, `rpDrive`). Nathan est retiré des passants, pour qu'on ne croise pas de sosie d'Oscar.
- Pieds dans le sol : la marche, le repos et la course d'Oscar venaient du soldat d'exemple de three.js, sans recalage de la hauteur du bassin. Ils sont remplacés par les animations Mixamo du jeu (repos, marche, jogging), dont la hauteur du bassin est recalée sur le corps d'Oscar. La course des passants passe aussi par le jogging recalé.
- Glissade : la vitesse de chaque animation de marche est mesurée dans le fichier, avant de la fixer sur place. La foulée suit exactement la vitesse de déplacement, pour Oscar comme pour les passants.
- Tables et sièges : tabourets et chaises du diner, ainsi que les chaises ajoutées sous les gens assis, sont maintenant des obstacles.

## 2026-11-25 — Claude — Personnages scannés Renderpeople (v1.10.0)
- Boban a choisi d'utiliser quand même les 6 personnages Renderpeople, malgré la clause 4.3 (fichiers facilement téléchargeables dans un dépôt public).
- `assets/characters/rp/` : textures réduites à 1024 px par `fbx_shrink.py`. Claudia, Carla et Eric pèsent environ 1 Mo chacun, Sophia 3,6 Mo, Nathan 2,0 Mo, Manuel 7,1 Mo (il garde son animation de danse dans le fichier).
- Leur squelette n'est pas celui de Mixamo (`hip`, `spine_01`, `upperarm_l`…). Chaque personnage scanné suit à chaque image un squelette Mixamo invisible qui joue les animations du jeu (`rpDrive`, segment par segment). Ils marchent, s'assoient, conduisent, se battent et tombent comme les autres.
- Ajoutés aux listes : femmes (Claudia, Carla, Sophia) et hommes (Eric, Nathan, Manuel).
- Crédits : `CREDITS.md` et Options.
- Vérifié sur le PC de Boban (commit fd13ff1) : les 6 personnages se chargent sans erreur. Au diner, Claudia est debout derrière le comptoir, Eric sert, Nathan et Manuel sont assis aux banquettes, au milieu des personnages Mixamo. Pièce bien éclairée.

## 2026-11-25 — Claude — Cheveux visibles sur les personnages Mixamo (v1.9.2)
- Vérifié sur le PC de Boban (commit 0696699) : bar et nuits nettement plus clairs, aucun message d'erreur.
- Maggie avait bien un corps de femme, mais ses cheveux (comme ceux de toutes les femmes Mixamo) étaient invisibles. FBXLoader branche la texture des cheveux comme `alphaMap`. Three.js lit alors la teinte (cheveux foncés) comme de la transparence. Correction au chargement : transparence prise du canal alpha (`alphaTest` 0,42, deux faces). Contrôlé dans une vue de test : les 4 femmes ont leurs cheveux.
- Personnages RenderPeople téléchargés par Boban (Manuel, Claudia, Sophia, Carla, Nathan, Eric) : non intégrés pour l'instant. Leurs conditions (section 4.3) interdisent de rendre les fichiers 3D facilement téléchargeables par des tiers, ce que ferait un dépôt GitHub public. Décision laissée à Boban.

## 2026-11-25 — Claude — Plus personne n'est assis dans le vide (v1.9.1)
- Signalé par Boban : des gens assis sans table, chaise ni fauteuil.
- Causes et corrections :
  - Diner : les clients ajoutés par Kimi étaient placés au hasard, à 50 cm du sol et tournés n'importe comment. Ils s'assoient maintenant sur les vrais sièges du diner (5 tabourets, 5 places de banquette, 3 chaises), face au comptoir ou à leur table. Marcus et M. Kowalski gardent leur place.
  - Serveur du diner : il marchait côté clients, à 50 cm du sol. Il marche maintenant au sol, derrière le comptoir.
  - Rue : une personne sur quatre parmi les gens qui discutent « s'asseyait » sur rien. Ils restent debout.
  - Niveaux : chaises ajoutées sous Bridget (pub), Dale (Truck Stop), Nadia et Louis (café), Marie-Rose et Réjean (refuge). Tabouret ajouté pour Wilf au comptoir du pub. Earl est remonté sur son tabouret du bar (`SIT_FIX`, `fixSeats`).
- Signalé par Boban : la serveuse du bar n'était pas comme les autres. Maggie (barmaid du Rusty Anchor) recevait un corps d'homme en t-shirt blanc : son apparence de base portait une barbe, et le choix homme/femme se faisait sur « cheveux longs sans barbe ». Les personnages nommés ont maintenant un rôle fixe (`FEMMES`, `assignRoles`). Lina, Maggie, Bridget, Priya, Gisèle, Mireille, Nadia, Hélène, Marie-Rose et Eva sont des femmes. Louis, qui a les cheveux longs, garde un corps d'homme.
- Signalé par Boban : la nuit et dans certains lieux, l'image était trop noire.
  - Dehors la nuit : lumière du ciel et de la lune nettement plus fortes (ciel 0,42 → 0,85, lune 0,32 → 0,62), teinte plus claire, exposition 1,3.
  - Intérieurs : lumière d'ambiance chaude 0,18–0,40 → 0,60–0,85, lampes toujours allumées pleinement (avant, réduites de moitié le jour), exposition 1,2.
  - Qualité haute : le post-traitement sortait l'image sans conversion de couleurs (pas d'`OutputPass`), ce qui l'assombrissait. Corrigé. Vignette plus légère (0,42 → 0,30).
- Véhicules vérifiés à l'écran et avec des vues de profil : voitures, taxi, police et vélo dans le bon sens. La moto roulait à l'envers, corrigé (`flip:true`).

## 2026-11-25 — Claude — Vrais véhicules, conducteurs et motos (v1.9.0)
- Boban a téléchargé 7 modèles Sketchfab, tous sous licence CC-BY 4.0. Les auteurs sont cités dans `CREDITS.md` et dans Options → Crédits des modèles 3D.
  - Voitures : Honda Civic, Toyota Corolla AE86, Range Rover Evoque.
  - Taxi Crown Victoria, Chevrolet Tahoe de police, moto Honda CB 750, vélo classique.
  - Animation Mixamo « Driving », pour les conducteurs.
- `tools/glb_shrink.py` réduit les textures à 512 px (taxi 12,5 → 2,2 Mo, Evoque 8,3 → 2,4 Mo) dans `assets/vehicles/`.
- Section 12 : chaque véhicule créé est inscrit dans `CARS`. Les plus proches de la caméra (22, 14 ou 8 selon la qualité, jusqu'à 90 m) reçoivent le vrai modèle, mis à la bonne longueur et posé au sol.
  - Concernés : voitures, taxis, police, VUS d'Omer, vélos et motos.
- Chaque voiture en circulation a maintenant un conducteur, qui devient un vrai humain au volant quand il est proche.
- Des motos circulent avec les voitures, environ une pour six voitures.
- Les voitures de police des cinématiques utilisent le Tahoe, et les VUS noirs d'Omer l'Evoque.
- Tests : 145/145.

## 2026-11-25 — Claude — Tout le monde devient humain (v1.8.0)
- Demande de Boban : « rend tout le monde en humain », sans exception.
- Boban a téléchargé sur Mixamo 11 personnages réalistes et 9 animations. Les deux personnages de style dessin animé (« Breathing Idle (1) » et « (2) ») sont écartés.
- `assets/characters/pnj/` : 13 personnages, textures réduites à 512 px par `tools/fbx_shrink.py` (≈3 Mo chacun).
  - 4 hommes : t-shirt blanc, sweat blanc, chemise en jean, capuche.
  - 4 femmes : veste brune, haut à fleurs, t-shirt rayé, pull beige.
  - 4 hommes d'Omer : noir 1, noir 2, pull rouge tatoué, tactique (SWAT).
  - 1 enfant.
- `assets/animations/pnj/` : marche homme et femme, repos, assis, assis qui parle, téléphone, texto, marche en textant, discussion. La course vient du soldat d'Oscar.
- Système unique (section 11) : chaque personnage créé par `createHuman` est inscrit dans `HUMANS`. Les plus proches de la caméra reçoivent un vrai humain : 16 en qualité haute, 10 en moyenne, 5 en basse, jusqu'à 40 m.
  - Concernés : passants, gens assis, cyclistes, hommes d'Omer, personnages des lieux et des cinématiques.
  - L'ancien squelette donne toujours la position, la vitesse et le mode. En cinématique, au sol, arme au poing ou parapluie ouvert, sa pose est recopiée sur le vrai corps.
  - Les noms d'os Mixamo numérotés (`mixamorig12:`) sont normalisés.
- Les passants des villes de province marchent maintenant, avant ils restaient figés hors de Toronto.
- Option ajoutée : « Passants et personnages » : vrais humains ou simples (plus léger).
- Tests : 144/144.
- Vérifié sur le PC de Boban (commit 19ca5f7) : aucun message d'erreur ; vrais humains assis et qui discutent au diner, passants à Toronto, hommes d'Omer au port ; 31 images/s en qualité basse.
- Deuxième série d'animations téléchargée par Boban :
  - Combat : pistolet (attente, marche), fusil en visée, coup de poing, deux réactions aux coups, chute en arrière, chute en avant, à genoux.
  - Quotidien : marche et attente d'une personne âgée, jogging.
  - Branchement : les hommes d'Omer visent, frappent, encaissent, tombent (sans retomber quand ils redeviennent réels) et se rendent à genoux. Les personnes âgées marchent à leur rythme et les passants pressés font du jogging.
- Cyclistes : pas d'animation de vélo sur Mixamo pour l'instant. Le vrai corps assis recopie le pédalage, le dos penché et les mains au guidon du squelette simple.
- Retouche après vérification : plus de vrais humains à la fois (8 en basse, 12 en moyenne, 18 en haute, au moins 12 à l'intérieur) et rayon porté à 45 m, car au diner certains clients restaient simples.

## 2026-11-24 — Claude — Villes ouvertes des provinces, complètes comme Toronto (v1.7.0)
- Demande de Boban : remettre les villes que Kimi voulait créer, mais complètes comme Toronto.
- Un seul générateur pour toutes les villes : `generateCity(seed, CITY_PROFILES[id])`. Chaque profil fixe les quartiers, les commerces, les couleurs des maisons et des toits, la hauteur des tours, les arbres, l'hiver, l'eau, le tram et le monument.
- Six villes : Vancouver (Harbour Centre, Burrard Inlet), St. John's (maisons « Jellybean », Cabot Tower), Calgary (Calgary Tower, neige, sans eau), Halifax (horloge de la Citadelle), Winnipeg (Palais législatif, rivière gelée), Montréal (Stade olympique, Saint-Laurent).
- Chaque ville a des tours, des maisons, des commerces, des arbres (conifères à Vancouver), des lampadaires, des bancs, des passants et des voitures. En hiver, la pelouse et les toits sont enneigés. La mini-carte montre les noms et le point de retour.
- Dans les niveaux 2 à 7, une porte « Explorer la ville » se trouve près du point de départ, et « Retour » ramène à l'enquête. Toronto reste intacte : le titre, l'intro et le niveau 1 la reconstruisent (`ensureCity`).
- Changer de ville libère l'ancien monde (géométries, façades, passants). L'écorce et les bancs réels sont gardés en mémoire et réappliqués.
- Tests : 143/143 (nouveau : les 6 villes sont complètes, l'aller-retour fonctionne, Toronto est intacte au retour).

## 2026-11-24 — Kimi (contribution) + Claude (intégration) — v1.6.0
- Apport de Kimi (fichier `game/index.html` transmis par Boban, sans journal ni commit) : passants plus vivants (assis sur les bancs, groupes qui discutent, téléphone, regards), oiseaux, chiens, avions, vie dans les intérieurs (clients), pluie plus réaliste (éclaboussures, asphalte mouillé, voile de pluie à l'écran), voitures détaillées (jantes, feux de freinage), visages plus humains (grain de peau, rousseur, joues, nez asymétrique, silhouettes féminines), post-traitement (halo, vignettage, grain, aberration chromatique), HUD plus compact.
- Corrigé par Claude à la demande de Boban (version de Kimi conservée) :
  1. plantage au lancement de chaque niveau (`initPlanes` : variable `r` manquante ; traînées non retirées) ;
  2. « villes ouvertes » par province retirées : générateurs sans bâtiments qui faisaient planter les niveaux 2 à 7, et inutiles (ces niveaux ont leurs propres décors) ; plus de reconstruction du monde à chaque niveau ; densités des niveaux 2 à 7 remises à 0 ;
  3. Toronto rétabli : lac Ontario et digue, trottoirs, carte (King St, Lac Ontario, Tour CN) ;
  4. météo de retour dans le HUD, doublon Jour/heure supprimé ;
  5. performances : effets de cinéma réglables (Options) et coupés automatiquement si la qualité graphique baisse ; voile de pluie sans réallocation à chaque image ; post-traitement redimensionné avec la fenêtre ;
  6. documentation mise à jour.
- Tests : 124/124 (nouvelle vérification : météo affichée, pas de doublon Jour/heure).
- Vérifié sur le PC de Boban (v1.6.0) : niveaux sans plantage, météo affichée, feuillage d'érables réel. v1.6.1 : la rue était presque noire (bitume rendu métallique par le code de pluie) → bitume jamais métallique, plus clair par temps sec, plus lisse et brillant sous la pluie.
- Rappel pour tous les agents (Codex, Kimi, Claude) : lancer `python tests/run_logic_tests.py` et mettre à jour JOURNAL/ROADMAP avant chaque envoi (AGENTS.md).

## 2026-11-21 — Claude — Arbres, écorce et bancs réalistes (v1.5.0)
- Les arbres 3D de Poly Haven sont des numérisations de cinéma (66 Mo à 958 Mo, 1,6 à 17 millions de triangles) : inutilisables dans un navigateur. À la place : feuillage en grappes de feuilles/aiguilles avec transparence (cartes instanciées, teintées par arbre), fonctionne hors ligne ; écorce photographiée (bark_brown_02) sur les troncs.
- Bancs des parcs de Toronto : vrai modèle Poly Haven `painted_wooden_bench` (1 000 triangles).
- Mesures des modèles Poly Haven (PC de Boban) : baril 3k tri, banc 1k, voiture bâchée 13k, poubelle 14k, lampadaires 20–31k, borne-fontaine 86k → lampadaires et bornes seulement près d'Oscar (à faire).
- Consigne de Boban : regrouper le travail pour réduire le nombre de petits envois.

## 2026-11-21 — Claude — Personnages Mixamo réels et lieux photographiques (v1.3.0 → v1.4.1)
- Personnages : Boban a téléchargé des personnages Mixamo très lourds (jusqu'à 142 Mo, textures 4096 px). Nouvel outil `tools/fbx_shrink.py` : réécrit le FBX binaire avec des textures réduites (1024 px JPEG), sans toucher au modèle ni au squelette (relecture vérifiée, fin de fichier conforme au chargeur three.js). 374 Mo → 18 Mo pour 5 personnages ; 3 civils ajoutés ensuite. Rangés dans `assets/characters/`, animations dans `assets/animations/`. Page `game/apercu_personnages.html` pour les voir en 3D.
- Oscar = soldat en camouflage (candidat 5, choisi par Boban), animations capturées : repos/marche/course (Soldier.glb, réorientées : squelette source tourné de −90°), coup de poing, coup de pied, garde, visée, tir, rechargement, impact. Arme dans la vraie main droite. GitHub Pages publie aussi `assets/` (étape ajoutée au workflow).
- Lieux : matières photographiées Poly Haven (CC0) chargées à l'exécution : asphalte, dalles de trottoir, neige, parquet, plâtre, tôle ; 60 façades repeintes sur fond de vraie brique/béton en gardant fenêtres et lumières de nuit. Option « Matières photographiques ».
- Vérifié sur le vrai rendu (PC de Boban) : Oscar debout, marche, garde ; façades et trottoirs réels.
- Décision de Boban : TOUTES les personnes du jeu doivent être des humains réalistes, sans exception (passants, assis, cyclistes, ennemis, acteurs des cinématiques). Reporté : il faut encore télécharger ~10 personnages (Eva, Omer, femmes, hommes âgés, costume, ouvrier, policier, manteau) + animations de vie courante.

## 2026-11-20 — Claude — Oscar en modèle 3D (v1.2.0)
- Fait : Oscar affiché par un modèle squelettique animé (Soldier.glb des exemples three.js, rig Mixamo : Idle/Walk/Run) chargé depuis le CDN. L'ancien squelette tourne en coulisse ; ses poses (coups, blocage, visée, accroupi, chute, cinématiques) sont recopiées sur le modèle par alignement des os (`retarget`, section 8). Orientation, taille et côtés mesurés au chargement. Repli automatique sur l'Oscar classique ; option « Personnage d'Oscar » (nouveau / classique).
- Vérifié sur le vrai rendu (PC de Boban) : repos, marche, accroupi, blocage, visée.
- Limites : le modèle d'exemple porte une armure futuriste (pas un soldat canadien) ; licence Mixamo à vérifier avant toute commercialisation ; sur ce PC la qualité graphique baisse automatiquement (moins de 26 images/s).
- Suite proposée : créer le vrai Oscar (uniforme, visage, barbe) sur un compte Mixamo et ajouter des animations de combat capturées.

## 2026-11-20 — Claude — Premier test visuel réel (v1.1.1)
- Testé dans le navigateur intégré, sur le PC de Boban (vrai rendu, Intel Iris Xe) : écran titre, Toronto, diner, intro, Manitoba, Montréal, salon d'Omer.
- Corrigé : le HUD restait affiché par-dessus les cinématiques ; la caméra sortait des petites pièces (entrée du diner) ; Westmount et la maison d'Omer presque noirs (lumière d'appoint `nightFill`, lampes plus fortes) ; la météo promise (blizzard au Manitoba, verglas à Montréal) n'était pas garantie au début (`firstWeather`) ; cinématiques de nuit éclaircies.
- Reste à voir : les humains sont encore faits de formes simples (point 2 du plan d'amélioration).

## 2026-11-20 — Claude — GitHub Actions
- Fait : `.github/workflows/ci.yml` (tests à chaque push et PR ; publication de `game/` sur GitHub Pages si les tests passent sur main). Badge dans le README, règles dans AGENTS.md.
- À faire par Boban : Settings → Pages → Source « GitHub Actions ».

## 2026-11-20 — Claude — Confort de jeu (v1.1.0)
- Fait : options, chapitres, trophées et records, musique adaptative et ambiances, indices du numéro masqué (I), manette, astuces, quitter vers le titre, F1, indicateur de sauvegarde, qualité graphique automatique.
- Tests : 123/123 ; essai réel (menus, manette simulée, indices, quitter/continuer) sans erreur.

## 2026-11-20 — Claude — Niveau 7 : Montréal, le final (v1.0.0)
- Fait : tempête de verglas (branches, fil tombé), panne générale, refuge, trois entrées dans la maison d'Omer, génératrice, boss Omer, sous-sol, cinématique de fin et écran de fin du jeu.
- Corrigé : les gardes au corps à corps ne blessaient Oscar qu'au port de Toronto ; `startBossFight` ne réveillait pas les gardes de la pièce ; `syncCameras` généralisé.
- Tests : 112/112 ; passage réel 6 → 7 et cinématique de fin sans erreur console.
- Suite : test humain complet, réglage, identité du personnage mystérieux.

## 2026-11-20 — Claude — Niveau 6 : Manitoba (v0.10.0)
- Fait : blizzard −40 °C, voiles blancs (vue réduite pour Oscar et les gardes), thermos (H), abris chauffés, Saint-Boniface, café, silos de Saint-Norbert, boss Viktor, mallette ; enchaînement Nouvelle-Écosse → Manitoba.
- Tests : 91/91 ; passage réel niveau 5 → 6 sans erreur console.
- Suite : bloc 11, Montréal (final).

## 2026-11-20 — Claude — Niveau 5 : Nouvelle-Écosse (v0.9.0)
- Fait : verglas (glissade, chutes, crampons), équipement conservé entre niveaux, caméras + coupure de courant, cloisons basses, ouverture de la porte à la relève de 23 h, déchiqueteuse à retardement ; front de mer d'Halifax, Mission des marins, cabinet du Notaire ; cinématique ; piste de Winnipeg.
- Fichiers : `game/index.html` (0.9.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 79/79 vérifications automatiques (niveaux 1 à 5), passage réel niveau 4 → 5, chute sur le verglas en courant. **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 6 (Manitoba), puis le final à Montréal.

## 2026-11-20 — Claude — Niveau 4 : Alberta (v0.8.0)
- Fait : neige (chute, sol, neige profonde, traces suivies par les gardes, buée, brouillard), froid extrême avec givre à l'écran et mains engourdies ; équipement d'hiver **à trouver** (décision du propriétaire) ; gare de triage d'Alyth, relais routier, ranch Bow Valley, l'Éleveur ; cinématique ; piste d'Halifax + indice de Westmount.
- Fichiers : `game/index.html` (0.8.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 63/63 vérifications automatiques (niveaux 1 à 4), passage réel niveau 3 → 4, marche dans la neige sans erreur. **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 5 (Nouvelle-Écosse).

## 2026-11-20 — Claude — Niveau 3 : Terre-Neuve (v0.7.0)
- Fait : système de vent (déplacement, rafales, froid éolien, visée, repérage, pluie oblique, affichage), vagues animées, roulis à bord ; port de St. John's, pub, tâche de la doris, quatre façons d'aborder le Marie-Galante, combat sur le pont en tempête, capitaine Roy ; cinématique d'arrivée ; piste vers l'Alberta.
- Fichiers : `game/index.html` (0.7.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 50/50 vérifications automatiques (niveaux 1 à 3), passage réel niveau 2 → 3 et combat sur le chalutier sans erreur. **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 4 (Alberta).

## 2026-11-20 — Claude — Niveau 2 : Colombie-Britannique (v0.6.0)
- Fait : moteur rendu multi-niveaux (arènes génériques, zones/objectifs par niveau, passage de niveau, progression conservée). Niveau 2 complet : terminal de Vancouver, bar, surplus, trajet vers Squamish (3 options), forêt pluviale et camp du Pasteur, tâche de Josh (2e vie bonus), boss, interrogatoire, piste de Terre-Neuve ; imperméable et café chaud ; cinématique d'arrivée.
- Fichiers : `game/index.html` (0.6.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 36/36 vérifications automatiques (niveaux 1 et 2), passage réel niveau 1 → cinématique → niveau 2 sans erreur, IA de la forêt rapide (18 ms pour 5 s simulées). **Rendu visuel non vu par un humain.**
- Reste à faire : niveau 3 (Terre-Neuve).

## 2026-11-20 — Claude — Bloc 4 : cinématiques (v0.5.0)
- Fait : moteur de cinématiques ; introduction complète en 20 plans (Brésil, appel anonyme, enlèvement à Toronto, repaire d'Omer, sous-sol, retour d'Oscar) ; messages vidéo d'Omer pendant le jeu (+ indice « métro et corne de navire ») ; cinématique d'échec ; écran « Prendre le contrôle d'Oscar » ; bouton « Revoir l'introduction » ; sons (hélicoptère, explosion, sonnerie, basses de la fête).
- Fichiers : `game/index.html` (0.5.0), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 22/22 vérifications automatiques + parcours réel (Nouvelle partie → intro → Passer → jeu) sans erreur. **Rendu visuel des cinématiques non vu par un humain.**
- Reste à faire : niveau 2 (Colombie-Britannique) ; décider s'il faut des voix parlées.

## 2026-11-20 — Claude — Bloc 3 : port, infiltration, combat (v0.4.0) — niveau 1 complet
- Fait : zone portuaire (conteneurs, grue, cargo, entrepôt 7), 4 façons d'entrer, discrétion (vision des gardes, jauge, accroupi, déguisement, corps découverts), neutralisation silencieuse, fouille, combat mains nues (poing, pied, blocage), pistolet et fusil (visée, recharge, tête), IA ennemie, lieutenant Tiago (négociation, combat, interrogatoire), écran de fin de niveau, sons synthétisés, minicarte du port avec gardes.
- Fichiers : `game/index.html` (0.4.0, anciennes sauvegardes ignorées), `docs/*`, `tests/run_logic_tests.py`.
- Testé : 19/19 vérifications automatiques (de la maison jusqu'à l'écran de fin), repérage d'un garde en ~2 s à découvert, tirs ennemis, mort et réapparition au point de sauvegarde du port. **Rendu visuel et sensations de combat non testés par un humain.**
- Reste à faire : bloc 4 (cinématiques), niveau 2 (Colombie-Britannique).

## 2026-11-20 — Claude — Bloc 2 : intérieurs, dialogues, indices (v0.3.0)
- Fait : maison d'Oscar et Lina's Diner jouables de l'intérieur (lieux habités, soleil par la fenêtre, poussière, lampes) ; 5 personnages avec dialogues à choix (vérité / argent / menace, coût en temps et en argent) ; carnet d'indices (touche C) ; argent ; objectifs dynamiques avec marqueur ; tâche secondaire avec vie bonus ; voisin dehors ; mode « assis » pour les personnages.
- Fichiers : `game/index.html` (0.3.0, anciennes sauvegardes ignorées), `docs/*`, `tests/run_logic_tests.py`.
- Testé : syntaxe + scénario complet du niveau 1 automatisé (8/8 OK, 0 erreur JS) avec un faux moteur 3D. **Rendu visuel non testé.**
- Reste à faire / problèmes connus : contenu de l'enquête à valider par le propriétaire ; bloc 3 (infiltration du port, combat) ; l'intérieur est plus grand que la maison vue de dehors (normal dans les jeux).

## 2026-11-20 — Claude — Décision Unreal Engine et plan de migration
- Fait : choix du moteur enregistré (Unreal Engine 5.8, visuels simples d'abord puis MetaHuman). Plan de migration `docs/PLAN_UNREAL.md` (structure du projet, correspondance prototype → Unreal, règles techniques, étapes U0 à U9). Dossier `Unreal/` avec `.gitignore` et `.gitattributes` (Git LFS).
- Sur le PC du propriétaire : Epic Games Launcher installé ; disque C: nettoyé (Docker Desktop désinstallé à sa demande, fichiers temporaires supprimés) → 126 Go libres. PC : i7-1165G7, 16 Go, Intel Iris Xe intégrée → assez pour construire en greybox, pas pour MetaHuman/Lumen.
- Testé : sans objet (documentation).
- Reste à faire : ~~installer UE 5.8~~ — **annulé** : le propriétaire a choisi de continuer sans Epic. Suite : bloc 2 dans le navigateur.

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
