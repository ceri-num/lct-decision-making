---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

![bg](../style/bg-tittle.svg)

# Decision Under<br />Uncertainty

### An introduction

Guillaume Lozenguez

[@imt-lille-douai.fr](mailto:guillaume.lozenguez@imt-lille-douai.fr)

---

## Last improvement in Artificial Intelligence

- *Nov. 2007*, Carnegie-Mellon win the Darpa Urban Challenge ($2M\$$)

![right](../figs/boss.svg)

- *Oct. 2015*, Victory of d'**AlphaGo** over professional player

![](../figs/goban.svg)

---

## Last improvement in Artificial Intelligence

<br />
<br />

In France:

- *March 2018*, Rapport Villani - [www.aiforhumanity.fr](http://www.aiforhumanity.fr) -

---

## The notion of complexity (Go)

GO: $10^{170}$ positions, $10^{600}$ games (chess: $10^{120}$ games)

![](../figs/jeugo.svg)


---

## The notion of complexity (Go)

<br />

**A classical $3$ GHz computer:** $3\times10^9$ op. per second
$\rightarrow$ $~ 2.6 \times 10^{14}$ op. a day $\rightarrow$ $~ 10^{17}$ op. a year


**Enumerating all games:** $O(n)$ with $n=10^{600}$: arround $10^{583}$ years.
$\rightarrow$ requires decomposed model and statistics...

**Sun life:** arround $10^{30}$ years

---

## Decision Making Problem

<br />

#### How to compute ~~optimal~~ appropriate responces<br />to control dynamical systems ?

**Knowing that:**

- Model could require very large exploration
- We potentially do not have the model
- Evolution are generally uncertain

---

## Introduction - This Course

### Decision Under Uncertainty

Is an introduction to models and algorithms<br />
to perform decision-making at a time step *t*<br />
by considering potential effects.

- 19 hours (5 sessions)
- Mainly as tutorials
- Simple dice games as a playground

---

1. Introduction
2. Class of problems
3. The notion of Agent
4. Decision Making Process of an agent

---

## Class of problems - Deterministic Planning

is the process that determines *a succession of actions*<br />
to drive a system from an initial state to a target state.

![](resources/color-domino.svg)

**Deterministic case**:

- the effects, by doing an action, from a specific state<br /> is certain.
---

## Class of problems - Deterministic Planning

Is the process that determines *a succession of actions*<br />
to drive a system from an initial state to a target state.

![](resources/color-domino-plan.svg)

**Deterministic case**:

- The effects, by doing an action, from a specific state<br /> is certain.
---

## Class of problems - Determine a Plan

Finding a *path* in a *graph* modeling all possible evolutions

![](resources/domino-graph.svg)
---

## Class of problems - Plan Optimization

Finding an *optimized* path in a *weighted* Graph

![](resources/domino-graph-2.svg)

---

## Class of problems - Stokastic Planning

Build a *policy*:

- Associate an *action* to perform <br />
*to each* reachable *state*

![](resources/color-domino-policy.svg)

---

## Class of problems - Stokastic Planning

Then the effective succession of actions remains stochastic

![](resources/color-domino-policy2.svg)
---

## Class of problems - Game theory

*Few entities* control the same system (with different goals)

![](resources/echec.jpg)

- Which actions for each entity ?
- Which consequences ?
---

## Class of problems - Game theory

Few entities control the same system<br />
With different goals.

![](resources/echec_graph.svg)

- *Uncertainty*: At last on the actions of the others.
---

## Class of problems - Control Complex systems

Complex systems:
- A lot of entities in interactions

![](resources/prisonarchitect.jpg)

- *Uncertainty*: ...

---

## Vocabulary

<br />
<br />

- **graph** composed of **node** and **edges**
- **graph** composed of **state** and **action** (State Automata)
- **planning**: finding a valid succession of **actions**
- **determinist** versus **uncertain** / **stochastic**
- **system**, **control** (automation)
- **Multi-Agent System**, **Decision Making** (AI)
---

## Notion of Agent

<div class="center">
<br />
<br />
**"I act therefore I am"**
<br />
<br />
<br />
</div>

- my actions have an effect on the world
- **and** I have the choice to act or not

<br />
<br />
<br />
<br />
<br />
<br />

cf. "BullShit Jobs" - David Graeber (2019)
(p.132-133 fr. in version )

or the joy to be cause - Karl Groos (1901)

<!-- Pour approfondir: : broucek francis « the sense of self » 1977 - Klein G. S. « the vital pleasures » 1976.-->
---

## Notion of Agent - Simple definition

<br />
<br />
<br />
<div class="center">
### Entity capable of perception and action<br /> evolving in an environment.
</div>

<br />
<br />
<br />

### Question:

<div class="center">
### How to choose appropriate action to perform<br /> considering the perception at a each time step ?
</div>

<br />
<br />
<br />
---

## Notion of Agent - Simple definition

### Open loop control

![](resources/agent.svg)

rarely determinist, mostly uncertain (even stochastic)

---

## Notion of Agent - Complementary Notions

### Agent:

- defining by a perception-state, goals and a policy to achieve its<br />
(*BDI* model: Belief - Desire - Intention)
- with different positions in social structure<br />
(*AGR* model: Agent - Group - Role )
- capable of communication
- capable of adaptation (learning)
- driven by emotions
- ...
---

## Course notion to acquire
<br /><br />

<div class="two5">
  From *reactive control*
</div>
<div class="one5">
  **to**
</div>
<div class="two5">
  *deliberative control*
</div>

<div class="two5">
  Immediate response<br />
  to stimuli

  <br />

  Script:  <br />
  if .... then ...   <br />
  else if ...  <br />

</div>
<div class="one5">
  <br /><br /><br /><br />
  **versus**
</div>
<div class="two5">
  model and statistical<br />
  decision-making

![](resources/domino-graph-2.svg)

</div>
---

## Course notion to acquire

<br /><br /><br /><br />

### Decision-making under uncertainty

- Script, Policy and Decision Tree
- Statistical evolution: Bayesian Network
- Planning: Markov Decision Process
---

## Zombie dice

### A Stokastic Dice Game

<div class="one2">
![](resources/zombie_dice.jpeg)
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
![](resources/zombie_dice2.png)
</div>

<div class="one3">
**Decision:**

- Score or Continue

**Uncertainty:**

- dice selection
- dice result
- score evolution
</div>
