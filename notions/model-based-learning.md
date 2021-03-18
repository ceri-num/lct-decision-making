---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Model-based learning 
### the other RL technic

<br />
<br />
<br />
<br />

Guillaume Lozenguez

[@imt-lille-douai.fr](mailto:guillaume.lozenguez@imt-lille-douai.fr)

![bg](../style/bg-tittle.svg)

---

## Model-based learning

### Main Idea:

- Random trajectories (a lot)
- Until each transition is visited several times.
- Compute an optimal policy.

### Potentially: 

- Require driving exploration
- Only incomplete exploration can be performed

---
<!-- --------------------------------------------------------------- -->


## Markov Decision Process

<br />

**MDP:** $\langle S, A, T, R \rangle$:

*S :* set of system's states
*A :* set of possible actions
*T :* S × A × S → [0, 1] : transitions
*R :* S × A → R : cost/rewards

![bg right 100%](../figs/MDP.svg)

**Optimal policy:**

The policy $\pi^*$ maximizing Bellman

---
<!-- --------------------------------------------------------------- -->

## Solving MDP: Value Iteration

*Input:* an **MDP:** $\langle S, A, T, R \rangle$ ; precision error: *$\epsilon$* ; discount factor *$\gamma$* ; initial $V(s)$
1. Repeat until the **maximal delta** < $\epsilon$
For each state $s \in S$
      - Search the action $a^*$ maximizing the Bellman Equation
      - Update $\pi(s)$ and $V(s)$ by considering action $a^*$
      - Compute the delta value between the previous and the new $V(s)$

*Output:* an optimal **$\pi^*$** and associated **V-values**.

$$V^\pi(s)= R(s, a) + \gamma \sum_{s'\in S} T(s,a,s') \times V^\pi(s')$$

---
<!-- --------------------------------------------------------------- -->

## Application to 421

- Python implementation - [playerMDP.py](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/playerMDP.py) :

```Python
solver= MDP()
solver.learnModel( Engine() )
solver.valueIteration()

player= PiPlayer( solver.policy() )
```
<br />

- Learning phase: Estimate **t** and **r**:
  - *10 000* simulations for each couple (s, a)
- Value iteration:
  - *3* iterations (directed and finit game)
- Average score (100 000 games): **~338**

(To notice: decreasing the learning phase impact the average score)

---
<!-- --------------------------------------------------------------- -->

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
