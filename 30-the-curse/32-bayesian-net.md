---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# The Curse of<br />Dimensionality

### Factorized Transitions

Guillaume Lozenguez

[@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)

![bg](../style/bg-tittle.svg)

---

![bg](../style/bg-toc.svg)

<br/>

1. **Bayesian Network**
2. **Factorized Transition Function**

---

## Before to go...

### Q-Learning over reduced state-space (and actions...) <br /> nessearly generate averaged decisions...

![](../figs/qlearning-arch.svg)

### Need a model to refine decision making from simulations

---

![bg](../style/bg-toc.svg)

<br/>

1. **Bayesian Network**
2. Factorized Transition Function

---

## Bayesian Network: General idea

#### Variables are not necessarly correlated over all the others.

**Example:**

- The probability of _Rain_ does not depend from _Car Velocity_.
- The _Car Velocity_ does not depend from _Rain_.
- Owever, the probability of _Accident_ depends from both _Rain_ and _Car Velocity_.

**Bayesian Network:**

#### A probabilistic graphical model that represents  <br /> a set of variables and their conditional dependencies

---

## Bayesian Network: Car accident Example

Graphical model: _Node:_ variable, _Orriented Edge_, dependancy

![width:600](../figs/bn-accident.svg)


**ATTENTION:** _Correlation_ is not _Conditional Dependancy_


---

## Bayesian Network: Node's Probability Table

#### Propbality dependencies are defined node by node.

![width:600](../figs/bn-accident-table.svg)

---

## Bayesian Network: Inference

#### Resulting propbality is computed recursivelly

![width:800](../figs/bn-accident-infer.svg)

---

## Bayesian Network: Level-up

#### Growing the graph $\rightarrow$ no consequencies over existing nodes

![width:600](../figs/bn-accident-2.svg)


**ATTENTION:** _Correlation_ is not _Conditional Dependancy_ $\rightarrow$ **Directed Acyclic Graph**

---

## Bayesian Network: Toolbox

<br />
<br />

- Bayesian Network [on Wikipedia](https://en.wikipedia.org/wiki/Bayesian_network)
- In python - numerous implementations
   - [pomegranate](https://pomegranate.readthedocs.io/en/latest/) - define compute inferences and more.
   - [bnlearn](https://pomegranate.readthedocs.io/en/latest/) - Learning the bayesian structure (ie. detect the dependencies)

---

![bg](../style/bg-toc.svg)

<br/>

1. Bayesian Network
2. **Factorized Transition Function**

---

## Factorized Transition Function: Problem

#### Classically a multi-varibles probabilistic evolution problem

![](../figs/transition.svg)


---

## Factorized Transition Function: As Bayesian Network

![](../figs/dist-BN-trans.svg)


Each varaible evolution is dependant from few parents
Potentially with intermediate varaibles.


---

## Factorized Transition Function: Dynamic Bayesian Network

**Bayesian Network** with duplicated variables regarding their evolution in time.

![](../figs/dynamic-BN.svg)


Considering a distribution of probability at time $t$,
it is possible to infers over the distribution of probabilities at time $t+N$


---

## Factorized Transition Function: Dynamic Bayesian Network

**Extended definition** over 3 times step.

![](../figs/dynamic-BN-1.svg)


---

## Factorized Transition Function: 421 example


![](../figs/dynamic-BN-421.svg)

- Roll step: 2 entrances - Small tables 
- Sort step: 3 entrances but deterministic 


---

## Factorized Transition Function: 421 example


![](../figs/dynamic-BN-421.svg)

- Let consider cheat dice:
Learning transitions $\rightarrow$ computing $3 \times 12$ probabilities _vs_ ( $168^2 \times 8$)

---

## Factorized Transition Function: Zombie Dice Exemple

#### Naturrally the complexity of the networks<br />grow linearly with the complexity of the game

![width:800](../figs/zombie_dice.svg)

---

## Factorized Transition Function: Zombie Dice Exemple

#### A 4 steps' game engine: 

![width:900](../figs/zombie_dice2.svg)

- **State Space ? Branching ?**

---

## Zombie Dice : Brut Transition Function (action: go)

![](../figs/zombie-matrise.svg)

---

## Zombie Dice : Factorized Transition Function (action: go)

![width:1300](../figs/zombie-dot.svg)

---

![bg](../style/bg-toc.svg)

<br/>

1. Bayesian Network
2. Factorized Transition Function


<!-- Coin flipping -->