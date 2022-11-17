# Projet-Vlille-Mongo

Membre du groupe : - DIALLO Ibrahima / NIANG Cheikh Saliou / BAKOUBOLO Justin
## Sujet du projet:
Ecrire 2 programmes en python et mongo
Programme client :
- donne le nom des stations disponibles à côté de l'utilisateur (lat, lon) avec les dernières données (vélos et stand).

Programme professionnel - pour la ville
- trouver une station avec un nom (avec quelques lettres)
- mettre à jour / supprimer une station
- désactiver toutes les stations dans une zone
- donner toutes les stations avec un ratio vélo/stationnement total inférieur à 20% entre 18h et 19h00 (du lundi au vendredi).
## Comment reccupérer les collections?
Il faudrait mettre requirement.txt dans le dossier du projet pour avoir accés à tous les bibliothèques nécessaires,puis créer une base de connée dans MongoDB.Comme nous avions déja l'API pour reccupérer les collections nous avons installer l'extension de MongoDB sur VSCode et enfin connecter notre base de donnée à notre éditeur de code(VSCode)
## Comment marche les programmes?
Nous avons développer le projet en console ce qui permet de changer une valeur lors de l'appel de la fonction.Le projet contient au total 4 fichier de code sous format python.
-client_program:donne le nom des stations disponibles à côté de l'utilisateur avec les vélos et stand disponible
-delete_station:supprimer une station
-desactivate_in_area
-find_by_name:il faudrait préciser que cette fonction permet de retrouver une station avec quelques lettres
-update:celle ci permet de retrouver l'intégralité des stations vlille.Elle permet aussi de recovery les stations que l'on a supprimé auparavant.

