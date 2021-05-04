# Passer à l'échelle

Tenter d'appliquer QLearning sur le jeu [ZombieDice](../gameZombies/intro.md).

* sur [replit.com](https://replit.com/repls/@ChefProjetIA21/jeu-ZombieDice)

- 1 - chercher à accélérer l'apprentissage.

Astuce: il est possible de sauver et recharger simplement un dictionnaire avec `json`

```python
import json
f = open("qvalues.json", "w")
f.write( json.dumps( qvalues, sort_keys=True, indent=2) )
f.close()

f = open("qvalues.json", "r")
qvalues= AgentPi( json.loads( f.read() ) )
f.close()
```

- 2 - passer sur la version 2 joueurs

Deux joueurs s'affrontent:

```python
gameEngine= game.System()
player= game.HumanAgent()
gameEngine.run(player)
```

## Support PDF

* [Scalling](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/scalling.pdf)


## Mettre en pratique :

- Réduire artificiellement l'espace d'état (ne conserver que les variables qui vous semblent pertinentes).
- Opérer un transfert de connaissance: passer de la version 1-joueur à la version 2-joueurs
- Apprendre de façons incrémentales, augmenter progressivement les variables observées.
- ...
