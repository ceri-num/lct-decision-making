# Kick-off

The first series of tutorials is based on a customized version of the dice game **421**.
The goal of this game is to make the best combination with 3 dice after 2 roll-again possibility.
The proposed version of the game is implemented in **Python3**.

## Install

First configure a proper **Python3** environment.
We suggest working under Linux operating system and the editor **Visual Studio Code**.

Virtual machines under this configuration is available on IMT-Lille-Douai servers.

- [mydesktop.imt-lille-douai.fr](https://mydesktop.imt-lille-douai.fr) - use the web client, and the **MAD** machine.
- Open a workspace with Visual Studio Code on a new directory.
- Execute `python3` command in a terminal then `exit()` to test your configuration.

Then you can download the **421** game (a unique python file)

- Download [game421.py](https://raw.githubusercontent.com/ceri-num/module-DUU/master/codes/game421.py)) in your new workspace.
- Execute the game to test it: `python3 game421.py`

## Shared workspace


## Play 421

The simple *Python* implementation of **421** come with a very simple User Interface (UI).
At each time step, the game state is printed then an action is asked until the game reach a final state (a horizon equals to 0).
The state format is 'h-d1-d2-d3' where h is the horizon, d1, d2, d3 the values of the tree dice.
The action format is 'a1-a2-a3' with a1, a2 and a3 as *'keep'* or *'roll'*.

For instance, in state, '2-4-3-1', you will be capable of rolling the dice 2 times and the current value of your dice is 4, 3, and 1.
You can try to roll again only the second dice (d2) with value 3 by expecting a **421**.
This way, you type: *keep-roll-keep*.

Try the game until understand correctly the scoring mechanism.

