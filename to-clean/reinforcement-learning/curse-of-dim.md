---
marp: true
theme: imt
paginate: true
---

## Représentation factorisée : arbre de décision


![](fig/qtable-tree.svg)

**Au 421:** si l'adversaire possède un *4-2-1* il y a *56* combinaisons,<br />
mais seulement *4* possibilités: j'ai *4-2-1*, il me manque 1, 2, ou 3 dés

<br />

- Méthode concurrente: **Les réseaux de neurones**

---

## Le fléau de la dimension (model base)


### Fonction de Transition:

![](fig/transition.svg)

---

## Le fléau de la dimension


### Factored Transition function:


![](fig/dist-trans.svg)

---

## Le fléau de la dimension


### Factored Transition function:

![](fig/dist-BN-trans.svg)

---

## Example: Zombie Dice


<br />

![bg left 50%](fig/zombie_dice.jpeg)

 **Eat maximum brains <br />
 without dying (3 damages)**


 - Players are zombies.
 - They try to catch humans <br /> three at a time.
 - Humans are dice <br /> with probability to fight back.

---

## Example: Zombie Dice


### Matrice complète

![](fig/zombie-matrise.svg)

---

## Example: Zombie Dice

### Dynamic Bayesian Network (Playing)

![](fig/zombie-dot.svg)
