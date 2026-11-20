# Directives maîtresses : incarnation humaine authentique (zéro effet robot / CGI)

> **Obligatoires** pour tout personnage, environnement, cinématique, texte descriptif et ressource 3D du projet.
> Données par le propriétaire du projet le 2026-11-20. À relire avant chaque tâche visuelle.

Chaque personnage et chaque environnement doit être conçu, modélisé et décrit avec un réalisme brut, vivant et imparfait. Aucun aspect lisse, symétrique, artificiel ou « généré par ordinateur ».

## 1. Visages et anatomie (fin de la vallée de l'étrange)
- **Peau réelle** : texture organique avec pores visibles, micro-imperfections, variations de teinte, cernes de fatigue, rougeurs légères, poils follets, rides d'expression naturelles. Jamais de peau lisse ou plastique.
- **Regard vivant** : yeux humides avec reflets lumineux naturels (catchlights), paupières légèrement relâchées, regard mobile (jamais fixe ou vide).
- **Asymétrie naturelle** : traits légèrement décalés (sourcils, sourire, épaules), comme chez tout être humain réel.

## 2. Mains et langage corporel
- **Mains expressives et détaillées** : toujours visibles, naturelles et anatomiquement justes (articulations, veines légères, ongles naturels, plis de peau). Jamais pendantes et rigides : tenir une tasse, ajuster des lunettes, pianoter, une main dans la poche, gesticuler en parlant.
- **Démarche et posture organiques** : pas de démarche robotique. Poids réel : transfert d'une jambe à l'autre, appui contre un mur ou une table, épaules voûtées par la fatigue ou penchées en avant par la concentration.

## 3. Vêtements et apparence quotidienne
- **Textiles vivants** : plis naturels aux coudes et aux genoux, col légèrement déformé, manches retroussées de façon asymétrique, usure, froissements dus aux mouvements de la journée.
- **Cohérence sociale et météo** : la tenue reflète le vécu, l'humeur et l'activité (tenue décontractée froissée à la maison, veste posée sur une chaise, chaussures marquées par la marche).

## 4. Comportements et actions du quotidien
- **Interactions naturelles** (courriels, écrans, tâches) : ne pas fixer l'écran comme une machine. Plisser les yeux, se pencher, soupirer, hésiter avant de taper, boire une gorgée de café, se frotter la nuque.
- **Micro-actions permanentes** : cligner des yeux, respirer visiblement, changer de position, détourner le regard pour réfléchir.

## 5. Lieux et maisons vivantes (pas de décors de catalogue)
- **Trace de vie humaine** : jamais de showroom vide. Une veste sur le dossier d'une chaise, une tasse à moitié vide, des câbles, des livres, des clés, du courrier posés de façon réaliste.
- **Éclairage et atmosphère naturels** : lumière naturelle par les fenêtres, ombres douces, poussière subtile dans l'air, textures imparfaites (bois vécu, tissus froissés, reflets réalistes).

---

## Application dans le projet

### Liste de contrôle (à vérifier pour chaque personnage ou lieu livré)
- [ ] Peau texturée, non uniforme ; aucun personnage parfaitement symétrique
- [ ] Yeux avec reflets, clignements, regard qui bouge
- [ ] Mains visibles, occupées ou en mouvement naturel
- [ ] Respiration et transfert de poids à l'arrêt
- [ ] Vêtements froissés / usés, au moins un détail asymétrique
- [ ] Au moins une micro-action du quotidien par personnage
- [ ] Lieux avec objets laissés par des humains ; murs et sols usés ; lumière naturelle

### Ce que fait déjà le prototype navigateur (v0.2.0)
- Squelette organique : bassin, colonne, cou, tête ; épaule-coude-poignet-main avec doigts et pouce ; hanche-genou-cheville.
- Peau avec texture de taches et de pores (procédurale) ; tissus avec trame et plis ; yeux (sclérotique + iris brillant pour les reflets), sourcils et bouche asymétriques, oreilles, nez, barbe pour certains.
- Chaque passant a sa taille, sa carrure, sa posture voûtée, son inclinaison de tête, son asymétrie d'épaules et de balancement des bras.
- Respiration visible, clignements aléatoires, regard qui se déplace, transfert de poids à l'arrêt, genou relâché.
- Mains occupées : téléphone (tête baissée), tasse de café (gorgées), sac, main dans la poche, parapluie sous la pluie, se toucher la nuque de temps en temps ; les gens qui discutent gesticulent et hochent la tête.
- Oscar : respiration plus forte quand il est essoufflé, penché en avant quand il court, manche droite retroussée, barbe.
- Façades salies (coulures, taches), trottoirs en dalles usées, asphalte fissuré, poubelles vertes de Toronto, bornes-fontaines, distributeurs de journaux.
- Niveau de détail : les détails du visage et des doigts ne sont dessinés qu'à moins de 22 m pour garder un jeu fluide.

### Limite honnête
Un navigateur avec des formes simples ne peut pas atteindre le photoréalisme demandé (pores réels, yeux humides, veines, tissus simulés). Pour respecter pleinement ces directives dans le jeu final, la cible recommandée est **Unreal Engine 5 + MetaHuman** (visages et peau photoréalistes, mains et animations capturées sur de vrais acteurs, tissus simulés, éclairage Lumen). Le prototype navigateur sert à valider le gameplay, les règles et l'histoire. Décision du moteur : propriétaire du projet (voir `docs/JOURNAL.md`).
