# Formation Chef de Projet IA (Avril/mai 2021)

- Appréhender les problématiques de prise de décision sous incertitude.
- Mettre en oeuvre un premier algorithme d'apprentissage par renforcement.
- Comprendre les limites de telles approches et les solutions pour y répondre.


[[Moddle Intro. IA](https://ftlv.imt-lille-douai.fr/course/view.php?id=9&section=2)][[Forum](https://ftlv.imt-lille-douai.fr/mod/forum/view.php?id=715)]

## Introduction à la prise de décision sous incertitude.

- [Support (PDF)](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/intro.pdf)

### Mise en pratique:

Les problématiques de planification et de prise de décision sous incertitude s'intéressent au système séquentiel discret.
Des systèmes décrits par un état qui évolue dans le temps, en tentant d'influencer aux mieux cette évolution.

Pour appréhender un tel système, l'idée est d'étudier un jeu simple le 421 dans une version à $1$ joueur.

Une version python du jeu est disponible [ici](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/game421.py) que vous pouvez enregistrer sur votre machine (click droit - enregistrer sous).

**Outils**

- Wep application: [replit.com](https://replit.com/teams/join/pwhevmtommdkmcicakakdxtqprvuncig-ChefProjetIA21) (il faudra créer un compte).
  * Créer un compte.
  * Se logger sur le groupe **ChefDeProjetIA** (automatique normalement)
  * Visualiser les projets (repls) pour [jeu-421](https://replit.com/repls/@ChefProjetIA21/jeu-421)
  * Faire un **Fork** du projet **ready-421**
- Sur ça propre machine avec : spyder(Anaconda), VisualStudioCode, Atom ... 

**Comprendre le code**

Ouvrir le fichier *game421.py* et identifier les deux classes principales
La première **HumanAgent** implémente une interface pour un joueur humain..
La seconde **System** implémente le jeu *421*.

Dans votre fichier de travail, il vous suffit d'importer `game421.py`, et de lancer une partie (`run`) avec une interphase `HumanAgent`:

```python
import game421 as game

gameEngine= game.System()
player= game.HumanAgent()
gameEngine.run( player )
```

- Tester le jeu à travers 4 ou 5 parties.

**Joueur autonome**

L'étape suivante consiste à mettre en oeuvre une IA qui jouera de façons autonome. 
Pour ce faire, il nous faut créer notre propre joueur `MyPlayer` est redéfinir sont comportement lorsqu'il perçoit un état du jeu et surtout au moment de décider d'une action à réaliser.

Il est possible de partir de cet exemple qui chasse un *421*: 

```python
import game421 as game

# Agent as a very simple UI
class MyPlayer(game.AbsAgent) :

    def perceive(self, reachedStateStr, reward):
        self.state= reachedStateStr

    def decide(self, isValidAction ):
        stateDico= self.stateDico()
        if stateDico["D3"] == 1 :
            if stateDico["D2"] == 2 :
                if stateDico["D1"] == 4 :
                    self.action= "keep-keep-keep"
                else: 
                    self.action= "roll-keep-keep"
            else: 
                self.action= "roll-roll-keep"
        else: 
            self.action= "roll-roll-roll"

        print( "State: " + str(stateDico) )
        print( "Action: " + self.action )
        return self.action

gameEngine= game.System()
player= MyPlayer()
gameEngine.run( player )
print( "Score: " + str(player.score) )
```

- Modifier cette IA pour la rendre plus efficace (ou proposez en une autre).
- Mettre ne place une boucle pour tester 1000 fois votre IA.
