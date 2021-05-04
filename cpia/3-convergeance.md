# Converger sur les Q-valeurs optimaux

Observer l'évolution des Q-Valeurs et déterminer la fin de la phase d'apprentissage.

## Monitorer l'apprentissage :

Observer l'évolution des Q-Valeurs au cours du temps:

- Le nombre d'états visités `sizeQvalues= len(player.qvalues)`.
- Le score obtenu sur les dernières parties `sample= player.score`
- la somme des meilleures valeurs enregistrée `sumBestQvalue+= player.qvalues[s][aStar]` pour chaque état (`aStar` la meilleure action dans `s`).

En supposant que notre objet `qvalues` est un dictionnaire de dictionnaires (respectivement définie sur les états et les actions).

[Cf. les dictionnaires en python]

## Les graphiques en python :

Dessiner avec [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) :

En 3 lignes sur la base d'une séquence de valeurs `valueLst`:

```python
import matplotlib.pyplot as plt

plt.plot( valueLst )
plt.ylabel('plot label')
plt.show()
```

## Retour sur l'apprentissage au 421

Analyse du Q-Learning sur cet exemple et présentation de l'apprentissage basé modèle.

* [Q-Learning on 421](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/qlearning421.pdf)
* [Model Based Learning](https://raw.githubusercontent.com/ceri-num/module-DUU/master/notions/model-based-learning.pdf)
