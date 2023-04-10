# RPLiDAR-Visualization
This repo is dedicated to the point map data visualization of the RPLiDAR A2 M12 for the ARGO Drone Project

## ARGO : LiDAR Point Map Visualization

<img width="1303" alt="LiDAR Visualization" src="https://user-images.githubusercontent.com/71334330/230931038-665c2b24-5cbb-462d-8b02-fdd2a36fcebf.png">


## Description:
Ce projet permet de visualiser les données collectées par les RPLidar sèrie A de Slamtec, dans le cadre du projet ARGO. Les données sont affichées sur un écran en utilisant le module pygame.

## Installation:

Pour utiliser ce projet, il est necessaire d'avoir installé Python 3, ainsi que les librairies necessaires. <br>
Une fois Python installé, vous pouvez cloner ce dêpot en utilisant la commande suivante sur le terminal : <br>

```bash
git clone https://github.com/yaxsomo/RPLiDAR-Visualization.git
cd RPLiDAR-Visualization
```

Ensuite, vous devez installer les dépendances nécessaires en utilisant pip. Vous pouvez le faire en exécutant la commande suivante: <br>

```bash
pip install -r requirements.txt
```

Assurez-vous de vous trouver dans le répertoire racine de votre projet avant d'exécuter cette commande.


## Utilisation

Pour exécuter le programme, vous pouvez ensuite exécuter la commande suivante: <br>

```bash
python3 visualize_data.py --port /dev/ttyUSB0 --size 1920 1080
```

Cette commande lancera le programme en utilisant les ports série '/dev/ttyUSB0' et une résolution d'écran de '1920x1080'.


## Arguments

Les arguments actuellement supportés sont les suivants : <br>

- '--port' : L'argument 'port' permet de specifier le port auquel le RpLiDAR est branché <br>
- '--size' : L'argument 'size' permet de specifier la taille de la fênetre d'affichage (format WxH) <br>

Vous pouvez arrêter le programme à tout moment en appuyant sur la touche Ctrl-C dans le terminal.

## Fonctionnement

Le programme utilise le module pygame pour afficher les données collectées par le lidar. Les données sont affichées sous forme de points blancs sur un écran noir. La taille et la position des points représentent la distance et la direction des objets détectés par le lidar. 

Le lidar collecte des données à 360 degrés, ce qui signifie que le programme doit afficher les données de manière à représenter une vue à 360 degrés. Pour ce faire, le programme lit les données collectées par le lidar et les organise en un tableau à une dimension de 360 éléments. Chaque élément du tableau représente la distance entre le lidar et un objet détecté à un angle particulier. Le programme utilise ensuite les données du tableau pour calculer la position de chaque point à afficher sur l'écran.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Contributions

Les contributions sont les bienvenues ! Pour les erreurs de frappe mineures ou les améliorations mineures, n'hésitez pas à ouvrir une demande d'extraction (pull request). Pour les améliorations plus importantes ou les changements majeurs, veuillez d'abord ouvrir une issue pour discuter des modifications proposées.

## Credits : 

### Yassine DEHHANI
### Emile BAILEY
