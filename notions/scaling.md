---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Scaling

<br />
<br />
<br />
<br />

Guillaume Lozenguez

[@imt-lille-douai.fr](mailto:guillaume.lozenguez@imt-lille-douai.fr)

![bg](../style/bg-tittle.svg)


---

## Decision Making

### Is about controlling linked variables:

- Learning correlation
- Optimize trajectories

### Matematically: 

- Manipulate Cartesian Product (Set Theory)
- Estimate functions
- Exploring large graph

---

## Dealing with large State Space

<br />
<br />
<br />
<br />

#### Reduce the state space

#### Work locally

#### A combination of these 2 solutions

---

## A Complete Decision Architecture

<br />
<br />
<br />

![](../figs/global-decision-arch.svg)

---

## A Complete Decision Architecture

<br />
<br />
<br />

![](../figs/decision-arch.svg)

---

## State reduction (or identification) 

### Approach:

Distance based approach:

- Principal Component Analysis (**PCA**) (+ Discretization)
- Clustering: **k-means**, Simple Vector Machine (**SVM**)

Discrete approach:

- Decision-Tree (ID3 algorithm family)

### Goals:

**Macro-States** merge states with supposed similar values.

---

## Deep-Learning-based Decision Architecture

![](../figs/deep-decision-arch.svg)

### Requirement:

Labeled data with valid *values*...

---

## Action refinement at run time

<br />

#### Local computation of the Values and the policy from current state.

- Constrained Value Iteration (from the current state, with a limited horizon)
- Monte Carlo Approach (based on deep, but random trajectories)

### Requirement:

Simulation: a model of the controlled system




---

## The Curse of Dimensionality in MDP

### Fonction de Transition:

![](../figs/transition.svg)

---

## Factored Model:


### Factored Transition function:


![](../figs/dist-trans.svg)

---

## Factored Model:


### Factored Transition function:

![](../figs/dist-BN-trans.svg)

---

## Bayesian Network:

Model complex system from local dependencies

### Example: Rain, Sprinkler and Grass Wet:

![](../figs/SimpleBayesNet-wikipedia.svg)

---

## Example: 421

![](../figs/bn-421.svg)

*Transition in two steps, but only the first isstokastic.*

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

### Dynamic Bayesian Network:

![](../figs/zombie-dot.svg)


---

## Model-Based Learning:


#### It’s more about estimate variable correlations than transition probabilities.

- Determines variable dependencies (ie. Bayesian Network)
- Learn conditional probabilities (Gaussian Noise, Poisson’s law)
- Validate the model regarding it entropy

#### Then decide from exploring limited search spaces

- Limited horizon Value or Policy Iteration
- random trajectories: Algorythm Monte-Carlo

---

#### To conclude

---

## Conclusion

- Problem: Control Dynamic System
- Hypothesis: Markov Decision Process (but unknown)
- Reinforcement Learning:
  * Model-free: QLearning
  * Model-based: Bellman Values function
- The root difficulty: the curse of dimensionality 
  * Use factored model

### 

- The solution requires to:
  * identify the model structure
  * have a lot of data 
- Optimasation from an iterative/incremental process
