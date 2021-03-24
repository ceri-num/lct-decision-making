---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Q Learning <br /> applied to 421

<br />
<br />
<br />
<br />

Guillaume Lozenguez

[@imt-lille-douai.fr](mailto:guillaume.lozenguez@imt-lille-douai.fr)

![bg](../style/bg-tittle.svg)

---

## Q-Learnin: the basics


<br />
<br />
<br />

- Iterative update on (State, Action) interest.
- Q-value equation:

$$Q(s^t, a) = (1-\alpha)Q(s^t,a) + \alpha \left(r + \gamma \max_{a^*\in A} Q(s^{t+1}, a^*)\right)$$

- Parrameters:<br />*$\alpha$* - learning rate ; *$\epsilon$* - thexploration-Exploitation ratio ; *$\gamma$* - discount factor

---

## Q-Learnin: Game 421 (Single PLayer)

<br />

- State Space: Horizon $\in [2, 0]$, Dice $\in [1, 6] \times 3$ : (~ 168 états)
- Action Space: **Keep** or **Roll** each dice $2^3$ : (8 actions)
- Potentially **$168 \times 8 \times 168$** Transition.
- Game score (unique final reward): [0 (*2-2-1*), 800 (*4-2-1*)]
- Random policy score : **~170**

<br />
<br />

- Correction: [playerQ.py (raw file)](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/playerQ.py)

---

## Q-Learnin: Game 421 (Single PLayer)

- With **500** steps of **500** games:

![](../figs/q421-v1.svg)

- *$\alpha$* : 0.1 ; *$\qquad \epsilon$* :  0.1 ; *$\qquad \gamma$* : 0.99

---

## Convergence: effect of the learning rate

- With **500** steps of **500** games:

![](../figs/q421-v2.svg)

- *$\alpha$* : 0.01 ; *$\qquad \epsilon$* :  0.1 ; *$\qquad \gamma$* : 0.99

---

## Convergence: effect of the exploration ratio

- With **500** steps of **500** games:

![](../figs/q421-v3.svg)

- *$\alpha$* : 0.01 ; *$\qquad \epsilon$* :  0.6 ; *$\qquad \gamma$* : 0.99

---

## Playing with the parameters:

<br />
<br />
<br />
<br />
<br />

- Generated rapidly "good" policies
- Converge on maximal and stable Q values <br />(an indicator for optimal policy)

<br />
<br />

- Be reactive to system modification (recovery)
  (no more equiprobable dice for instance)

---

## Optimize Q-Learning:

<br />

### A first solution: use dynamic parameters

- Balance **learning rate** and **exploration ratio**<br /> by taking into account known and unknown areas:

*Typically*: Count the number of performed transitions, for each couple of (state, action)

*Problem*: The dynamic will depend on other parameters

*Danger*: Quid of the recovery mode

---

## Optimize Q-Learning:

<br />

### A second solution: use expert kownledge

- Drive the exploration with an expert knowledge.

*Typically*: initialize the Q(s, a) with coherent value to take advantage<br /> of exploitation from the very beginning.

*Problem*: calibrate the "weight" of the initial knowledge.

*Danger*: Wrong initialization could slow down the learning process.

---
<!-- --------------------------------------------------------------- -->

<br />
<br />
<br />
<br />
<br />

#### Let's play to a more complicated game: Zombie Dice....
