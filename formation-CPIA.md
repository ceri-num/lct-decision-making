# Formation Chef de Projet IA (Avril/mai 2021)

- Apréhender les problématique de prise de décision sous incertitude.
- Mettre en oeuvre un premier algorythm d'apprentissage par renforcement.
- Comprendre les limites de tels approches et les solutions pour y répoondre.

## Introduction à la prise de decision sous incertitude.

- [Support (PDF)](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/intro.pdf)

### Mise en pratique:

Les problématique de plannification et de prise de decision sous incertitude s'intéresse au systéme séquentiel discret.
Des systémes décrit par un état qui évolue dans le temps, en tentant d'imfluencer aux mieux cette évolution.

Pour appréhender un tel systémes, l'idée est d'étudier une jeux simple le 421 dans une version à $1$ joueur.

Une version python du jeu est disponible [ici](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/game421.py) que vous pouvez enregistrer sur votre machine ().





## Understand the code

Ouvrir le fichier *game421.py* et identifierles deux classes principales
La premiére **HumanPlayer** implemente une interface pour un joueur humain..
La seconde **System** implemente le jeu *421*.

From this town classes, a simple 2 lines main function is used to launch the game with a human player.

## Generate your own Player

You will not modify the **421** implementation and so, work on your own *python* file.

Create a new python file by importing the game421 engine, copying the main function but by calling your own player (*MyPlayer*), then implement a very simple player.

Your file must look like:

```python
from game421 import Engine

# Default game interface :
def main():
    gameEngine= Engine()
    gameEngine.run( MyPlayer() )

# Agent as a very simple UI
class MyPlayer :

    def __init__(self):
        self.actionStr= "keep-keep-keep"

    def wakeUp( self, initialStateStr, actionSpace ):
        print( "Perception: "+ initialStateStr )

    def perceive(self, reachedStateStr, reward):
        print( "Perception: "+ perceptionStr  +" with reward : " + str(reward) )

    def action(self, isValidAction ):
        self.actionStr= "keep-keep-keep"
        print( "Action: " + self.actionStr)
        return self.actionStr

    def kill( self, score )
        print( "Game end on score: "+ str(score) )
        self.score= score

# Activate default interface :
if __name__ == '__main__':
    main()
```

Try your very simple player implementation.

## Player protocol

The player protocol followed by a game start by waking-up a player (method *wakeUp*).
This step informs the player about its initial state and the possible actions during the game.
Then the engine iteratively asks the player for an action (method *action()*), and inform the player about the reached situation (method *perceive()*).
The reached game situation is composed of a game state and a gained reward (or cost in case of negative reward).
The methods *action()* then *perceive()* are called until the player reached a final state.
Then at the end of the game, the player is virtually killed to inform in that the game end for him.

## Developping a first AI.

Now you are ready to propose your first AI.

The idea is to first draw the decision tree you want to implement and then implement it as a *if-then-else* script.

As in game421 Engine class, it is possible to transform the `reachedStateStr` into a dictionary like this:

```python
values= [ int(x_str) for x_str in reachedStateStr.split("-") ]
gameState= { "H":values[0],  "D1":values[1],  "D2":values[2],  "D3":values[3] }
```

You can try your AI by computing the average score after 10 000 games (do not forget to remove the calls to `print` function).
















Pour 

Le jeu 421:


## Apprentissage par renforcement

- [Support (PDF)](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/reinforcement.pdf)

### Mise en pratique:

Le jeu 421:

## Appréhender un systéme plus complexe

Le jeu Zombie Dice:

<!--

### Retour sur l'apprentissage sur le 421

* [Q-Learning on 421](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/qlearning421.pdf)

-->
