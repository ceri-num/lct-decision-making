---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Learning: Scalling

<br />
<br />
<br />
<br />

Guillaume Lozenguez

[@imt-lille-douai.fr](mailto:guillaume.lozenguez@imt-lille-douai.fr)

![bg](../style/bg-tittle.svg)

---

## Model-based learning



## The Curse of Dimensionality

### Fonction de Transition:

![](../figs/transition.svg)

---

## Le fléau de la dimension


### Factored Transition function:


![](../figs/dist-trans.svg)

---

## Le fléau de la dimension


### Factored Transition function:

![](../figs/dist-BN-trans.svg)

---

---

### Lets play to a more complexe game...

---

## Example: Zombie Dice


<br />

![bg left 50%](../figs/zombie_dice.jpeg)

 **Eat maximum brains <br />
 without dying (3 damages)**


 - Players are zombies.
 - They try to catch humans <br /> three at a time.
 - Humans are dice <br /> with probability to fight back.

---

## Example: Zombie Dice


### Matrice complète

![](../figs/zombie-matrise.svg)

---

## Example: Zombie Dice

### Dynamic Bayesian Network (Continue)

![](../figs/zombie-dot.svg)
