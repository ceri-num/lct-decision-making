---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Projet Int. Art.<br />and Optimization

### An introduction

Guillaume Lozenguez

[@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)

![bg](../style/bg-tittle.svg)

---

## Last improvement in Artificial Intelligence

- *Nov. 2007*, Carnegie-Mellon win the Darpa Urban Challenge ($2M\$$)
- *Oct. 2015*, First release of Tesla Autopilot

![](../figs/boss.svg)

- *Oct. 2015*, Victory of d'**AlphaGo** over professional player

![](../figs/goban.svg)

---

## Our topic: Autonomous Decision Making

- Model the capability of actions
- Learn action interest
- Model dynamic systems and plan
- Plan paths of actions
- Handle large problem with optimization techniques 


###

---

## The notion of complexity (Go)

GO: $10^{170}$ positions, $10^{600}$ games (chess: $10^{120}$ games)

![](../figs/jeugo.svg)

---

## The notion of complexity (Go)

<br />

**A classical $3$ GHz computer:** $3\times10^9$ op. per second
$\rightarrow$ $~ 2.6 \times 10^{14}$ op. a day $\rightarrow$ $~ 10^{17}$ op. a year


**Enumerating all games:** $O(n)$ with $n=10^{600}$: around $10^{583}$ years.
$\rightarrow$ requires decomposed model and statistics...

**Sun life:** around $10^{30}$ years

---

## Decision Making Problem

<br />

#### How to compute ~~optimal~~ appropriate responses<br />to control dynamic systems ?

**Knowing that:**

- Model could require very large exploration
- We potentially do not have the model
- Evolution is generally uncertain

---

## Introduction to Decision Under Uncertainty

<br />
<br />
<br />
<br />

1. Introduction
2. Class of problems (not class of complexity)
3. The notion of Agent
4. Decision Making Process

---

## Class of problems - Deterministic Planning

Determining *a succession of actions* to drive a system from an initial state to a target state.

![](../figs/color-domino.svg)

**Deterministic case**:

- The effects, by doing an action, from a specific state is certain.

---

## Class of problems - Deterministic Planning

Determining *a succession of actions* to drive a system from an initial state to a target state.

![](../figs/color-domino-plan.svg)

**Deterministic case**:

- The effects, by doing an action, from a specific state is certain.

---

## Class of problems - Determine a Plan

Finding a *path* in a *graph* modeling all possible evolutions

![](../figs/domino-graph.svg)

*Class of Complexity:* NP Hard (i.e. Non Polynomial over the number of nodes)

---

## Class of problems - Plan Optimization

Finding an *optimized* path in a *weighted* Graph

![](../figs/domino-graph2.svg)

---

## Class of problems - Stokastic Planning

Build a *policy*:

- Associate an *action* to perform *to each* reachable *state*

![](../figs/color-domino-policy.svg)

---

## Class of problems - Stokastic Planning

Execute a *policy*:

- Then, the effective succession of actions remains stochastic

![](../figs/color-domino-policy2.svg)

---

## Class of problems - Game theory

*Few entities* control the same system (with different goals)

![](../figs/echec.svg)

- Which actions for each entity ?
- Which consequences ?

---

## Class of problems - Game theory

*Few entities* control the same system (with different goals)

![](../figs/echec-graph.svg)

- *Uncertainty*: At last on the actions of the other players.

---

## Class of problems - Control Complex systems

Complex systems:

- A lot of entities in interactions

![](../figs/prison-architect.svg)

- *Uncertainty*: ...

---

## Class of problems - Other components

- Sequential vs Simultaneous
- Finit or infinite horison
- Multi-action per turn
- Complete observation
   * Informations are hidden
   * Different information over actors (players)
   * Require a memory
- Cooperative
- ...


<!-- Classifier des jeux... -->

---

## Vocabulary

<br />
<br />
<br />

- **graph** composed of **node** and **edges**
- **graph** composed of **state** and **action** (State Automata)
- **planning**: finding a valid succession of **actions**
- **determinist** versus **uncertain** / **stochastic**
- **system**, **control** (automation)
- **multi-agent system**, **decision-making** (AI)
- **observability**

---

## Notion of Agent

<br />
<br />

#### "I act therefore I am"

- my actions have an effect on the world
- **and** I have the choice to act or not

<br />
<br />
<br />
<br />

cf. "BullShit Jobs" - David Graeber (2019)
(p.132-133 fr. in version )

or the joy to be cause - Karl Groos (1901)

<!-- Pour approfondir: : Broucek Francis « the sense of self » 1977 - Klein G. S. « the vital pleasures » 1976.-->

---

## Notion of Agent - Simple definition

<br />
<br />

**An agent:**

#### An entity capable of perception and action<br /> evolving in an environment.

<br />

**Question:**

#### How to choose appropriate action to perform<br /> considering the perception at a each time step ?

---

## Notion of Agent - Simple definition

![](../figs/agent.svg)

rarely determinist, mostly uncertain (even stochastic)

---

## Notion of Agent - Complementary Notions

### Agent:

- defining by a perception state, goals and a policy to achieve its goals<br />(*BDI* model: Belief - Desire - Intention)
- with different positions in social structure<br />(*AGR* model: Agent - Group - Role )
- capable of communication
- capable of adaptation (learning)
- driven by emotions
- ...

---

## Course notions

From *reactive control* **to** *deliberative control*

- Immediate response to stimuli

```
Script:
if .... do ...
else if ... do ...
```

**versus**

- Model-based decision-making
  * with an opponent
  * and non-trivial optimization

---

## Course notions

<br />

### Decision-making under uncertainty (with me)

- Script, Policy and Decision Tree
- Reinforcement Learning: 
  - Q-Learning (learn the policy)
  - Model-Learning (learn the model, compute the policy)
- Factored Model

### Game theory and adversarial technic
### Combinatorial Optimization technic

---

## Today Game: 421

![bg right 60%](../figs/421_dice.jpg)

<br />

- Get the best combination
- by rolling 3 dices

### Goal :

- Optimize the 2 re-roll possibility
- by choosing dices to roll again.

---

<br />
<br />
<br />
<br />
<br />

#### Let's go....
