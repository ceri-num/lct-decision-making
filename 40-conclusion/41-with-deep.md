---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Reinforment with <br /> Deep Learning
### a Discution

<br />
<br />

**Guillaume.Lozenguez**
[@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)

![bg](../style/bg-tittle-lite.svg)

<br />

---
<!-- --------------------------------------------------------------- -->

## Basic approach - Random Exploration Tree

#### Explore locally possible evolution from the current state.

![](./deep-decision-arch.svg)

---
<!-- --------------------------------------------------------------- -->

## Basic approach - Incorporate Neural Networks

#### Incorporate Intuition as Deep Learning based Estimation

![](./deep-decision-arch1.svg)

- Cut exploration branches based on a heuristic value function

---
<!-- --------------------------------------------------------------- -->

## Le Deep-Learning: un cerveau à un neurone


### Le perceptron:

<div class="line">
<div class="one2">


$$\mathit{si:}  \quad \left( p_1 \cdot x + p_2 \cdot y > b \right)$$

Les paramètres:

- les poids: $p_1, p_2$ 
- un seuil: $b$

</div>
<div class="one2">

![width:400](./perceptron-example.svg)

</div>
</div>

> Le grand problème des data-sciences: Classifier

---
<!-- --------------------------------------------------------------- -->

## Le Deep-Learning: un cerveau à un neurone


### Le perceptron:

<div class="line">
<div class="one2">

![width:400](./perceptron.svg)

</div>
<div class="one2">

![width:400](./perceptron-example.svg)

</div>
</div>

> Le grand problème des data-sciences: Classifier

---
<!-- --------------------------------------------------------------- -->

## Le Deep-Learning: des réseaux de neurones profonds

![width:500](./neural-net.svg)

<div class="line">
<div class="one2">

- **La rétropropagation:**

LeNet (1989-1998) _Yan LeCun et al._

Livre: _Quand la machine Apprend_

</div>
<div class="one2">

![width:180](./ocr-32x32-4.svg)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Le Deep-Learning: des réseaux de neurones profonds

#### Une démocratisation de l'usage des CNN

![](./cnn-example.png)

**La classification:** pour n'importe qui, avec des donnés.


---
<!-- --------------------------------------------------------------- -->

## La "killing Architecture" - AlphaZero

#### Use both policy and value estimation.

![](./deep-decision-arch2.svg)

1. Iterative process: (Play phase // Analysis phase)
2. Suppose a model of the systems (game)

---
<!-- --------------------------------------------------------------- -->

## Le Deep Reinforcement Learning

#### Both policy and value estimation, but in Reinforcement Learning approach 

![](./deep-learning-arch.svg)

Classical _Actor-Critic architecture_ (see [PPO](https://en.wikipedia.org/wiki/Proximal_policy_optimization) algorithm for example).
