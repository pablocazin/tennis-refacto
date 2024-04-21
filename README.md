# Changements apportés au fichier Tennis1

------------------------------------------------


## 1 Conventions de nommage
Les noms des variables n’étaient pas cohérents (exemple : Player1name et p1Points)

## 2 Modification de la condition pour ajouter un point
La condition comparait avec une donnée en dur (« player1 »).
Cela n’est pas correct car si l’utilisateur rentre un nom est différent pour le joueur 1 cela ne fonctionnera pas. 

## 3 Utilisation du nom des joueurs pour les résultats
Suppression de l’affichage des joueurs en dur (‘player 1’). On concatène la chaîne de caractères avec la variable contenant le nom du joueur

## 4 Ajout de commentaires
Ajout de commentaires dans le code pour apporter de la clarté.

## 5 Création de la fonctionnalité de traduction
Création de la fonctionnalité de traduction pour prendre en charge plusieurs langues.

## 6 Ajout d'une classe Player
Ajout d'une classe Player pour rendre le code modulable et améliorer la clarté. Avec cette classe on pourrait améliorer le code plus facilement.

## 7 Ajout d'une classe Langue
Ajout d'une classe Langue permettant de gérer la traduction en fonction de la langue. Les langues et leurs traductions sont situés dans un fichier Json permettant l'ajout de nouvelles langues dans le futur.
