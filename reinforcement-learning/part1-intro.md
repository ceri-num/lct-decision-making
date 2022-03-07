---
marp: true
theme: imt
paginate: true
backgroundImage: url('style/bg-imt.svg')
---

<!-- --------------------------------------------------------------- -->
![bg center 100%](style/bg-tittle.svg)

# Reinforcement Learning

### Understand Dynamic Model and <br /> Sequencial Decision Making.

<br />
<br />
<br />

Abir KARAMI
_>_ Guillaume LOZENGUEZ

<br />

---
<!-- --------------------------------------------------------------- -->


## Who are we ?

**Abir Karami**
Assistant Professor <br /> Institut Catholique de Lille
Ph.D. Computing Science and AI
Human-Centered Intelligent System
Application to compagnon robots, Smart Home, <br /> Serious-Games ... 

![bg right 70%](fig/logo-fges.svg)

---
<!-- --------------------------------------------------------------- -->

## Who are we ?

**Guillaume Lozenguez**
Assistant Professor <br /> Institut Mines Télécom Lille Douai
Ph.D. Computing Science and AI
Distributed AI and coordination
Application to mobile robotics and transport systems 

![bg right 70%](fig/logo-imtld.svg)

---
<!-- --------------------------------------------------------------- -->
![bg center 100%](style/bg-toc2.svg)

- **Introduction**
  - Reinforcement Learning in AI
  - Example: the 4-2-1 game 
- **Decision Under Uncertainty**
- **Reinforcement Learning**
- **Examples**

---
<!-- --------------------------------------------------------------- -->


## Learning in Artificial Intelligence Domain

A machine capable of **learning** from **data** to optimize an **objective**

<!-- AI regroupe toute les approches qui essaye de rendre une machine ..... machine : robot, réseaux sociaux, netflix. Données : image, vidéo/observation, fichier. Objectif : assister/aide à la décision, faire une tache, satisfaire.
Comment ? Beaucoup de travaux et des méthodes et tout dépends de type de données et des objectifs. -->

![illustration robot](fig/illustration-robot.svg)

<!-- ---
<!-- --------------------------------------------------------------- -- >

## Automatic Learning

<!--  en 1980  selon les données et l'environnement-- >

![](fig/ML.png)

- Data :
    - En position ou à découvrir ?
    - Étiquetées ou non étiquetées ?
    - Concerne mon environnement ou un environnement similaire ?
    - ...
- The environnement :
    - Statique ou dynamique ?
    - Modelisable ou pas ?
    - ...


<!--  ******************************************** -->

---
<!-- --------------------------------------------------------------- -->

## Automatic Learning

<br />
<br />
<br />

- **Supervised Learning** - Finding structure from labelled data
- **Unsupervised Learning** - Finding hidden structure
- **Unsupervised Learning** - Propagate labels over non-labelled data
- **Active Learning** - Exploring while minimizing Oracle requests

![](fig/learning-en.svg)

---
<!-- --------------------------------------------------------------- -->


## Automatic Learning 

<br />

* **Reinforcement Learning**
  - From interactions between the system and its environment

#### (natural method, human-like learning)

![](fig/learning-RL-en.svg)

---
<!-- --------------------------------------------------------------- -->


## Reinforcement Learning for Sequencial Decision Making

<br />

- Learning a _sequential behavior_
- Good responses maximize _long-term gains_ (accumulated rewards and penalties)

![](fig/sequence.svg)





---
<!-- --------------------------------------------------------------- -->


## Example with 421-game

![bg right 60%](fig/421_dice.jpg)

### Game :

- Get the best combination
- by rolling 3 dices

### Goal :

- Optimize the 2 re-roll possibility
- by choosing dices to roll again.
