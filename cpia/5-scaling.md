# Passer à l'échelle

Tenter d'appliquer QLearning sur le jeu [ZombieDice](../gameZombies/intro.md).

* sur [replit.com](https://replit.com/repls/@ChefProjetIA21/jeu-ZombieDice)

- 1 Accélérer l'apprentissage en réduisant l'espace d'état dans `qvalues`

*Astuce :* décomposer l'état:

```python
def stateDico( self, state ):
    stVector= state.split("-") # [ "1", "2", "Hard(gun)" .... ]
    stDico= {
        "Brain":  (int)(stVector[0]),
        "Shot":   (int)(stVector[1]),
        "D1":     stVector[2],
        "D2":     stVector[3],
        "D3":     stVector[4],
        "Easy":   (int)(stVector[5]),
        "Medium": (int)(stVector[6]),
        "Hard":   (int)(stVector[7])
    }
    return stDico
```

*Astuce :* recomposé une clé pour le dictionnaire:

```python
    key= str(stDico["Brain"]) + "-" + str(stDico["Brain"])
```

- 2 - passer sur la version 2 joueurs

Deux joueurs s'affrontent:

```python
gameEngine= game.System()
player= game.HumanAgent()
gameEngine.run(player)
```

Attention, l'état est complété avec les scores des deux joueurs, et la fonction de récompense ne communique une valeur qu'en fin de partie.

## Support PDF

* [Scaling](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/scaling.pdf)


## Mettre en pratique :

- Réduire artificiellement l'espace d'état (ne conserver que les variables qui vous semblent pertinentes).
- Opérer un transfert de connaissance: passer de la version 1-joueur à la version 2-joueurs
- Apprendre de façons incrémentales, augmenter progressivement les variables observées.
- ...
