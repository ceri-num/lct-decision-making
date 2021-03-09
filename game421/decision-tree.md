# Decision Tree

The idea now is to hack the game engine implementation to propose our own autonomous player.

## Understand the code

Open *game421.py* file and identify the two main classes 
The first one **Player** implements a HumanUI player modeled as a simple agent (with perception and action).
The second one **Engine** implement the *421* game.
The method **run** permits to launch and play a game with a player.

From this town classes, a simple 2 lines main function is used to launch the game with a human player.

## Generate your own Player

You will not modify the **421** implementation and so, work on your own *python* file.

Create a new python file by importing the game421 engine, copying the main function but by calling your own player (*MyPlayer*), then implement a very simple player.

Your file must look like:

```python
from game421 import Engine

# Default game interface :
def main():
    gameEngine= Engine()
    gameEngine.run( MyPlayer() )

# Agent as a very simple UI
class MyPlayer :

    def _init_(self):
        self.actionStr= "keep-keep-keep"

    def perceive(self, perceptionStr, reward):
        print( "Perception: "+ perceptionStr  +" with reward : " + str(reward) )
        self.actionStr= "roll-roll-roll"

    def action(self, isValidAction ) :
        print( "Action: " + self.actionStr)
        return self.actionStr

# Activate default interface :
if __name__ == '__main__':
    main()
```

Try your very simple player implementation.

## Developping a first AI.

Now you are ready to propose your first AI.

The idea is to first draw the decision tree you want to implement and then implement it as a *if-then-else* script.

As in game421 Engine, it is possible to transform the `perseptionStr` into a dictionary like this:

```python
values= [ int(x_str) for x_str in perceptionStr.split("-") ]
gameState= { "H":values[0],  "D1":values[1],  "D2":values[2],  "D3":values[3] })
```

You can try your AI by computing the average score after 10 000 games (do not forget to remove the calls to `print` function).