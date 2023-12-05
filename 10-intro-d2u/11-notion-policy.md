---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

<!-- link rel="stylesheet" href="../style/imt.css" -->

# Decision Under<br />Uncertainty

### States, Actions and Policies

<br />

**Guillaume.Lozenguez**
[@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)

![bg](../style/bg-tittle-lite.svg)

---

<!-- --------------------------------------------------------------- -->


##  Acting over a dynamic system: the agent

<br />

![](../figs/agent.svg)

Rarely deterministic, Mostly uncertain

---
<!-- --------------------------------------------------------------- -->


## Rational Agent 

<br />
<br />

#### "I act, therefore I am."

<br />

- My actions have an effect over the world **AND** I have the choice.
- _AI_: Model the effect **AND** explore the choices

<br />

### Deliberativ Architecture - BDI:

 - _Believe_: refers to the knowledge of the agent
 - _Desire_:  agent's goals (classically states to reach)
 - _Intention_: succession of actions to perform oriented toward the goals

---
<!-- --------------------------------------------------------------- -->


## Acting over a system : formally

### Markov Chain (Andreï Markov 1856-1922)

A tuple: $\langle States\ (S),\ Transitions\ (T) \rangle$


- **States**: set of configurations defining the studied system
- **Transitions**: Describe the possible evolution of the system state

$$T : S \times S \rightarrow [0, 1]$$
$$T(s_t,\ s_{t+1}) = P(s_{t+1} | s_t)$$

<br />

_Vocabulary Parrenthesis_: Hidden Markov Chain
$\quad$_>_ The system state is not directly observable.

---
<!-- --------------------------------------------------------------- -->

## Acting over a system : formally

### Impact of the actions

- **Actions**: finite set of possible actions to perform

### Updated Transition function:

The probabilistic evolution depends on the performed action.

$$T : S \times A \times S \rightarrow [0, 1]$$

$T(s^t,\ a,\ s^{t+1})$ return the probability to reach $s^{t+1}$ by doing $a$ from $s^t$:

$$T(s^t,\ a,\ s^{t+1}) = P(s^{t+1} | s^t,  a)$$

<!-- Hypothesis of Markov: l'évolution ne dépend pas de l'historique
_ou_ l'état contient l'ensemble des informations nécessaires.-->

---
<!-- --------------------------------------------------------------- -->

## Multi-Variable Systems

### State and Action space:

*>* Cartesian product over  State and Action variables 

### Multi-variable Transition function:

The probabilistic evolution depends on the performed action.

$$T : S \times A \times S \rightarrow [0, 1]\qquad
T\left( \left[\begin{array}{c}
   x_1 \\
   x_2 \\
   \vdots \\
   x_n 
\end{array}\right],\ 
\left[\begin{array}{c}
   a_1 \\
   a_2 \\
   \vdots \\
   a_n 
\end{array}\right],
\left[\begin{array}{c}
   x'_1 \\
   x'_2 \\
   \vdots \\
   x'_n 
\end{array}\right]
\right) \in [0, 1]
$$

---
<!-- --------------------------------------------------------------- -->

## Model of 421: States and actions

- **States**:
  - The value of each die's face ($d_n \in [1, 6]$)
    and the re-roll number ($h \in [2, 0]$)
  - So:  **168** states (56 combinations over a horizon of 3).
- **Actions**:
  - The choice of roll again each die: $[\mathit{roll},\ \mathit{keep}]$
  - so **8** actions ($2^3$)

### Action Example :

By choosing to "roll-*keep*-roll" in state: "6-*4*-3 (2)" to expect a "4-2-1 (1)"

---
<!-- --------------------------------------------------------------- -->


## Model of 421: Transition function with 421-game

- **Transitions**: 
  - All reachable states by rolling some dice 
    with the probability to reach them.


$$
T\left( \left[\begin{array}{c}
   d_1 \\
   d_2 \\
   d_3 \\
   h \\
\end{array}\right],\ 
\left[\begin{array}{c}
   a_1 \\
   a_2 \\
   a_3 \\
\end{array}\right],
\left[\begin{array}{c}
   d'_1 \\
   d'_2 \\
   d'_3 \\
   h'
\end{array}\right]
\right) \in [0, 1]
\quad\text{example:}\  

T\left( \left[\begin{array}{c}
   6 \\
   5 \\
   1 \\
   2 \\
\end{array}\right],\ 
\left[\begin{array}{c}
   r \\
   r \\
   k \\
\end{array}\right],
\left[\begin{array}{c}
   4 \\
   4 \\
   1 \\
   1
\end{array}\right]
\right) = 1/36
$$

---

## Model of 421: Transition function with 421-game

### Transitions Example :

Choosing to "roll-*keep*-roll" from "6-*4*-3 (2)" implies *21* reachable states:

P(...) | = | [0, 1] | $\quad$ | P(...) | = | [0, 1]
-------|---|--------|-|--------|---|--------|
*4*-1-1 (1)| =  | $1/36$ | | ... 
*4*-2-1 (1)| =  | $1/18$ | | 6-*4*-4 | = | $1/18$
*4*-2-2 (1)| =  | $1/36$ | | 6-5-*4* | = | $1/18$
...        |    |          | | 6-6-*4* | = | $1/36$

---
<!-- --------------------------------------------------------------- -->

## Choosing : building a policy of actions

<br />
<br />
<br />

- *a policy* ($\pi$) : a function returning the action to perform 
    Considering the current state of the system:

<br />

$$\pi : S \rightarrow A$$

<br />

$$\pi(s): \ \text{the action to perform in } s$$

---
<!-- --------------------------------------------------------------- -->

## Choosing : building a policy  of actions

### Example of policy :

**"Always target a 4-2-1"**:  keeping only one **4**, one **2** and one **1**

$s$ | $\pi^{421}(s)$ | $\quad$ | $s$ | $\pi^{421}(s)$ |
------------|------------------|-|-----------|-------------
*1*-1-1   | *keep*-roll-roll   | | ...
*2*-*1*-1 | *keep*-*keep*-roll | | *4*-*2*-*1* | *keep*-*keep*-*keep*
3-*1*-1   | roll-*keep*-roll   | | ...
*4*-*1*-1 | *keep*-*keep*-roll | | 6-6-5 | roll-roll-roll
... |                          | | 6-6-6 | roll-roll-roll

(Invariant over the horizon h)

---
<!-- --------------------------------------------------------------- -->

## Automatize Decision Making

**Choose an action in a given context (state):**

- Evaluate tuples $\langle s,\ a \rangle$
- Selects the best action: 

<br />

$$ \pi^*(a) = \arg\max_{a \in A}\left(\ \mathit{Eval}(s, a)\ \right)$$

---
<!-- --------------------------------------------------------------- -->

## Evaluation in Game Theory

<br />
<br />
<br />

**Can be done a posteriori, with a lot of data :**

<br />

- $\mathit{Eval}(s, a) =$ the probability of winning if doing _a_ in _s_.

<br />

$$ \mathit{Eval}(s, a) = P( \mathit{win} \ |\  \pi(s)=a )$$

<br />

- But also depends on all the future actions...

<br />

**Can be done a posteriori, with a lot of _good_ data...**

<br />

(AlphaGo mars 2016 wins 4-1 the best professional player _Lee Sedol_)

---
<!-- --------------------------------------------------------------- -->

## Evaluation in _4-2-1_

**What is the optimal choices ?**

<br />


- For example, from _6-1-1 (2)_: **roll-keep-keep** or **roll-roll-keep** ?

---
<!-- --------------------------------------------------------------- -->

## Scores in 421-game

**Over the final combination (horizon $= 0$):**

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

## Evaluation in _4-2-1_

**What is the optimal choices ?**

- For example, from _6-1-1 (2)_: **roll-keep-keep** or **roll-roll-keep** ?

#### Requires to evaluate the possible final combinations <br /> after 2 roll-agains...

<br />

- **It clearly depends on the horizon:**
With an infinite costless roll-agains
it is always preferable to target the **4-2-1**

---
<!-- --------------------------------------------------------------- -->

## Exercices, compute a policy

<br />
<br />
<br />

**Basic learning process :**

- Record a player experience (trace)
- Compute average values for tuples $\langle s,\ a \rangle$
- Use those values to select the actions.

#### But depends on the initial player behavior...

<br />

**Make it iterative :**

- Use your new player to create new data _and_ learn again...

<br />

(AlphaGo Zero 2017 wins 100-0 AlphaGo Lee)


