# Expected Results

Le meilleur joueur possible à Zombie-Dice 2 joueurs.

## Rendu :

Le rendu attendu s'appuie sur 3 fichiers:

- Le fichier python `zombiePlayer.py`: qui contient à minima une class *AutoPlayer*.
- Un fichier `support.json` en json, dans lequel *AutoPlayer* peut puiser des ressources.
- Un fichier `README.md` en markdown, avec un descriptif concis des technique retenue et mise en œuvre.

Le rendu est à déposer sur MyLearningSpace.

## Code python et mise en œuvre :

Le fichier python `zombiePlayer.py` contient à minima une class *AutoPlayer* capable de jouer à zombieDice dans ça version *2* joueur.

Cependant, le comportement de ce joueur IA peut être la résultante de tout un processus d'apprentissage. Dans ce cas le fichier peut être composé d'autre class (potentiel d'autre joueur) par exemple un *LearnerPlayer* comme autant de témoignages de l'approche que vous avez mis en place pour construire votre *AutoPlayer*.

La confrontation entre vos *AutoPlayers* s'effectuera de la façon suivante:

- Une série de 10000 matchs pour "pofiner" les *AutoPlayer* au besoin.
- Une série de 10000 matchs pour établir statistiquement quel "AutoPlayer" prend l'avantage sur l'autre.

Les tests pourront ressembler à ça:

```python
#!env python3
from repertoire_grpX.zombiePlayer import AutoPlayer as Player1
from repertoire_grpY.zombiePlayer import AutoPlayer as Player2
from gameZombies2 import Engine

gameEngine= Engine()
players= [ Player1(), Player2() ]
demiSample= 5000

for i in range(demiSample):
    gameEngine.run( players[1], players[0] )
    gameEngine.run( players[0], players[1] )

players[0].go()
players[1].go()

total= [0, 0]

for i in range(demiSample):
    gameEngine.run( players[1], players[0] )
    total[0]+= players[0].score
    total[1]+= players[0].score
    gameEngine.run( players[0], players[1] )
    total[0]+= players[0].score
    total[1]+= players[0].score

print( players[0].students + ": " + str( total[0]/(demiSample*2)) )
print( players[1].students + ": " + str( total[1]/(demiSample*2)) )

if total[0] > total[1] :
    print( "Winner: "+ players[0].students )
else :
    print( "Winner: "+ players[1].students )
```

**Notez qu'en plus d'être compatible avec le jeu la classe devra posséder un attribut avec le nom des étudiants du groupe.**

Vous êtes fortement encouragé à tester vous-même votre classe en condition.
Des points peuvent être retirés pour non-respect des consignes.

## Fichier support :

Il est évident que *AutoPlayer* ne pourra que difficilement apprendre à jouer correctement sur 10 000 parties puis être efficace sur 10 000 autres sans qu'il ne possède une connaissance de base.

Dans la mesure où la connaissance ici est essentiellement codée sous forme de tableaux et de dictionnaire, le plus simple est de se reposer sur un fichier json pour enregistrer et charger des états de connaissance (Q, V, $\pi$, ...) 

Python dispose d'une exelente librairie pour charger et decharger des donné au format json sur [docs.python.org](https://docs.python.org/fr/3/library/json.html).
On trouve aussi un bon tutoriel sur l'interaction avec des fichiers en python sur [w3schools.com](https://www.w3schools.com/python/python_file_write.asp).

- Pour le déchargement dans un fichier:

```python
fille = open( "myFile.json", "w" )
fille.write( json.dumps( myDictionary, sort_keys=True, indent=2) )
fille.close()
```

- Pour le chargement:

```python
fille = open( "myFile.json", "r" )
myDictionary= json.loads( fille.read() )
fille.close()
```

Notez que le format `json` est un format texte éditable donc avec tout bon éditeur de texte (VSCode par exemple).

## Fichier de description :

Le `README.md` décrit brièvement donc la stratégie adoptée pour avoir un *AutoPlayer* opérationnel.
Notez que la démarche est plus importante ici que le résultat.
Par exemple il sera apprécié à ça juste valeur qu'une IA joue correctement sur la base d'un apprentissage limité à 10 000 jeux, sans ou avec peu de connaissance a priori (pas d'usage des fichiers support), même si cette IA ne figure pas au final sur le podium des meilleures IA.

Le `README.md` est d'autant plus important que le code de l'*AutoPlayer* n'est pas forcément représentatif du travail fourni.
Par exemple il se contente de charger un politique stocké dans le fichier support.
Il faut alors expliciter comment cette politique a été créée (vous pouvez comme indiqué précédemment laisser des éléments de code dans d'autres class, à côté de l'*AutoPlayer*).

Le format [Markdown](https://fr.wikipedia.org/wiki/Markdown) et un format texte du type "Wath you see is wath you get". 
Il s'édite donc avec un éditeur de texte spécialisé (GoshtRiter par exemple) ou plus générique: typiquement VSCode (qui propose des pluggin spécifiques).
Un rappel des membres du groupe dans ce fichier sera apprécié.
