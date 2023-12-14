# Decision Under Uncertainty

### Planning

### UV - MAD

Guillaume Lozenguez <br />
[at imt-lille-douai.fr](mailto:Guillaume Lozenguez)


## Recap:

### 1st, state definition

- A collection of variables

- Each variables defined in a domain


### Problem complexity: Search space

- Number of states (by combining domains)

- Number of succession of states


## Recap:

### 2nd, A plan or policy

- Action to perform in each state

- Potentially modeled as a decision tree

### How modeling successions of actions ?

## Recap:

### Problem: variables' evolution could-be uncertain

- **Bayesian Network**: model variables' dependency.

Require to define conditional distributions (matrices)

- **Dynamic Bayesian Network**: for variables with discrete time evolution

### Providing a transition function

- Reachable states at time *t+1* weighted with probabilities

## On ZombieDice

- *Bayesian Network*

- *Transition Function*

## Optimizing Decision Making:

### Bellman Equation (finit horizon):

$$a^* = \mathit{argmax}_{a} V^h(s, a) = r(s, a) + \sum_{s'} t(s,a,s')V^{h-1}(s')$$

- $t(s,a,s')$: transition function
- $r(s,a)$: reward function

<br />

<br />

### Markov Decision Process: Tuple: **S, A, t, r**

## Solving MDP:

### Short term horizon algorithm:

At each time step:

- Evaluate all reachable states
- But on a restricted horizon

### Monte-Carlo algorithm:

randomized search in constrained times

At each time step:

- Deep evaluation of state evolutions
- Limited in random trajectories

### Optimal Solving

Offline exploration of every evolution trajectories


## TD03: Decision Making

- From WillDie3 (correction of Dinamic Bayesian Network implementation for zombie dice)

- Optimize decision-making at horizon "1"

(compare immediate gains to probable gains)

- Optimize decision under a given horizon *n*

(recursive value function)

- Deeper horizon but with randomized evolution exploration
