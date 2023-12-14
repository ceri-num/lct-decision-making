# DS - Décision Statistique

UV-MAD - 2019/2020 - All documents/computer authorized.

Guillaume Lozenguez

## The yam's game

*Yam's* is a kind of dice-poker game.
We study here a simplified version of this game.

Two players face up to generate the best **5** dices combinations and to cumulate a maximum of points.
In **4** rounds, each player roll **5** standard dice (**6** faces identified with numbers from **1** to **6**).
If the player is not pleased with his combination, he can choose, **2** times, to roll again any number of the **5** dice.

Each combination worst a certain number of points depending on the difficulty to generate it.

In this version, we consider those combinations :

Combinations | Description | Value
-------------|-------------|-----------
Full         | *3*+*2* identic dice | *30*
Quads        | *4* identic dice     | *40*
Small Flush  | Flush with *4* dice  | *45*
Quinte Flush | Flush with *5* dice  | *50* + sum(dice)
Yam’s        | *5* identic dice     | *60* + sum(dice)
Nothing      | *else...*            | *0*

Player turn ends after he rolls *2* times the dice or he chose to stop. Then, its combination value is added to his score and the dice-set goes to his opponent.

Example of a first round :

Player-1, the first to play, get **2** dice **one**, **1** die **two**, **1** die **three** and **1** die **four**. He decides to roll again **1** die **one** to reach a *Quinte Flush*.
He get a *four*, roll again and get a final *six*.
With, **1** die in each value: **one**, **two**, **three**, **four** and **six**, he scores **45** points (*Small Flush*).

At Player-2 turn, dice give: **1** - **one**, **1** - **three** and **3** - **five**.
Player-2 keeps the **fives** and roll again the **2** other dice.
He gets **2** dice **one** he chooses to keep them for a *Full* worthing **47** points (30 + 3 × 5 + 2).

Then, the game continues for **3** other rounds.

### Question 1

Enumerate all the variables useful for decision-making (roll again or not *1* to *5* dice). Provide the variable domain.

### Question 2

Calculate the number of possible states considering the enumerated variables (provide both the equation and the result).

### Question 3

How many possible actions a player can choose at each time step of its turn ?

### Question 4

The next script provides an autonomous behavior based on function:

- *nb(x)*: returning the number of dice on the face *x*.

The script returns a list of dice face values for which the player aims to roll again the dice.
For instances, returning the list **[1, 2]** mean that all the dice on **1** or **2** would be rolling again.

```python
if  nb(6) > 3 :
  return [1,2,3,4,5]
elif  nb(5) > 3 :
    return [1,2,3,4,6]
elif nb(4) > 3 :
    return [1,2,3,5,6]
elif  nb(6) > 2 :
  return [1,2,3,4,5]
elif  nb(5) > 2 :
    return [1,2,3,4,6]
elif nb(4) > 2 :
    return [1,2,3,5,6]
else :
  return [1,2,3]
```

- **Question 4-a**: Model this script as a decision tree.
- **Question 4-b**: What is the purpose of this behavior ?

### Question 5

The *Combinations Value* depends on the **5** dice together. I would like to model it on a Bayesian network (the *Combinations Value* and all the variable permiting to reach it).

### Question 6

What is the size of the condition table associated to *Combination Value node* in the proposed Bayesian network. Provide *3* lines of this table as an example.

### Question 7

Let consider only one of the **5** dice (*die-1*). The evolution of the face of *die-1* depends on an action *roll-die-1* that could be *true* or *false*. Finally, rolling the die depends of the last gotten face.
In this scenario the player is waiting a *5* or a *6*.

- **Question 7.a**: Propose a *dynamic Bayesian network* modeling the evolution of *die-1* with all the condition tables.
- **Question 7.b**: At the begining, the player get a *one*. What is the distributions of probabilities over each of the variables modeled on the *dynamic Bayesian network*, for the time step *0* and the time step *1*.

### Question 8

Let consider again the **5** dice. The player get a full (*3* - *fives* and *2* - *ones*).
The player consider rolling again the *2* one-dot-dice.

- **Question 8.a**: What are the reachable states and their probabilities ?
- **Question 8.b**: What is the value of its current state and the value of "rolling the *2* one-dot-dice once" ? Considering this calculus, is it worthwhile for the player to roll those dice again ?
- **Question 8.c**: What would be the impact on the value of "rolling *2* one-dot-dice" if we consider it would be possible to roll it *2* times if necessary ? (Argue your position without providing the exact calculation).
