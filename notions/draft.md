---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

---

## Zombie dice

### A Stokastic Dice Game

<div class="one2">

![](../figs/zombie_dice.jpeg)

</div>

<div class="one2">
- Players are Starved Zombies
- dice are humans
- Zombies eat human brains
- and can't take more than 2 shots
</div>

---

## Zombie dice

### A Stokastic Dice Game

<div class="two3">

![](../figs/zombie_dice2.png)

</div>

<div class="one3">
**Decision:**

- Score or Continue

**Uncertainty:**

- dice selection
- dice result
- score evolution

</div>




---
<!-- --------------------------------------------------------------- -->


## Choosing to optimize

Require to evaluate the interest of each action on the system evolution:

- *Reward/Cost function* (R) :

$$R : S \times A \rightarrow \mathbb{R}$$

$R(s_t,\ a)$ is the reward by doing $a$ from $s_t$.

- *Bellman Equation* :

$$V^\pi(s)= R(s, a) + \gamma \sum_{s'\in S} T(s,a,s') \times V^\pi(s')$$
$$\text{with :} \quad a=\pi(s) \text{ and } \gamma \in [0, 1[ \text{ the discount factor}$$

---


<!-- --------------------------------------------------------------- -->


## reward in 421-game

Over the final combination only with the action "*keep*-*keep*-*keep*" or when the horizon is $0$

$\mathit{score}(\text{4-2-1}) \qquad = 800$
$\mathit{score}(\text{1-1-1}) \qquad = 700$
$\mathit{score}(\text{x-1-1}) \qquad = 400 + x$
$\mathit{score}(\text{x-x-x}) \qquad = 300 + x$
$\mathit{score}(\text{(x+2)-(x+1)-x}) = 202 + x$
$\mathit{score}(\text{2-2-1}) \qquad = 0$
$\mathit{score}(\text{x-x-y}) \qquad = 100 + x$
$\mathit{score}(\text{y-x-x}) \qquad = 100 + y$

---
<!-- --------------------------------------------------------------- -->


## Recap:<br /> Markov Decision Process

**MDP:** $\langle S, A, T, R \rangle$:

*S :* set of system's states
*A :* set of possible actions
*T :* S × A × S → [0, 1] : transitions
*R :* S × A → R : cost/rewards

![bg right 100%](fig/MDP.svg)

**Optimal policy:**

The policy $\pi^*$ maximizing Bellman


---
<!-- --------------------------------------------------------------- -->


## Reinforcement Learning:


Learn the optimal policy

- Without knowledge over the transition neither the reward functions,
- but, by getting feedback from acting randomly.
