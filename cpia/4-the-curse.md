# The Curse of Dimensionality

Tenter d'appliquer QLearning sur le jeu [ZombieDice](../gameZombies/intro.md).

* sur [replit.com](https://replit.com/repls/@ChefProjetIA21/jeu-ZombieDice)

1. Appréhender le jeu en jouant.
2. Lancer QLearning avec des paramètres cohérents...
3. chercher à accélérer l'apprentissage.

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


## Support PDF

* [Le fléau de la dimension](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/the-curse.pdf)
