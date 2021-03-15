## Zombie Dice

*GameZombies* is a freely adapted version of the game **Zombie Dice** from *Steve Jackson*.

![Zombie Dice](../figs/zombie_dice.jpeg)

## The game 

Players are zombies trying to eat humans. Humans are represented by dices giving probabilities over three outcomes:

- The zombie eats the brain of the human.
- The human run few steps forward.
- The human damages and escapes the zombie.

The player zombies run 3 humans at a time (roll tree dices) and its goal is to eat a maximum of humans without dying (get 3 damages or more.)
At each time step, the player keeps brain and damage dice then choose to stop (score its brain) or continue with the potential to score more brains in the future.

If the payer takes 3 damages, he loses all its brains and score 0.
If the player chooses to continue, he keeps running human dice in its hand and completes its hand to 3 dice from the stock.
The stock is composed of easy (6 green dice), medium (4 yellow dice) or hard (3 red dice) humans with different probabilities on "brain", "run" or "damage" outcome.

![Dice description](../figs/zombie_dice2.png)

The game ends automatically if there are no more 3 dice to roll.

## Single player game

A simple implementation of one player zombie dice is proposed to help in understanding the game and test some ideas.

- [gameZombie.py (1 players)](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/gameZombies.py)

It is implemented similarly to Game421, and players are implemented with the same methods (wakeUp, perceive, action and kill).
The state is composed of 8 variables:
- number of heated brain.
- number of taken damages
- got type and face of the first die (the player keeps all "RUN" dices)
- got type and face of the second die
- got type and face of the third die
- number of remaining ease human dice (3 brain faces, 2 run faces, 1 damage face)
- number of remaining medium human dice (2 brain  face, 2 run  faces, 2 damage faces)
- number of remaining hard human dice (1 brain  face, 2 run  faces, 3 damage  faces)

## two-player game

In the two-player version, player compete to be the first  to reach 13 ate brains (or more).
The game state is increased by the player score and the opponent score.
To notice that, contrary to the single-player game, the rewards are distributed only at the end, depending on whether the player wins the game (+10) or not (-10).

- [gameZombie2.py (2 players)](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/gameZombies2.py)







