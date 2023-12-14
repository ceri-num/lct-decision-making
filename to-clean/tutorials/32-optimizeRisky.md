# Kick-off on Risky game

### MAD - Decision Under Uncertainty

The second series of tutorials is based on a simple two players turn based strategic game **Risky**.
The goal of this game is to take the control over a maximum of position, and to destroy the opponent armies.

## Apply Q-Learning

The followed script provide a first implementation to use Q-Learning on Risky game.

- [Risky 1st Learner](https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/resources/gameRisky-playerQ.py)

However, this basic implementation is slow to converge on an acceptable playing policy.

To try it, open 3 terminals, and from the `hackagames` directory start the server and 2 AI: 

```sh
cd /path/to/hackagames
game-risky/hg-risky-hidden 100
```

Will wait for two players to seat on the game (connect to the server), and then run 100 games.

So in a different terminal: 

```sh
python3 game-risky/simplePlayer.py
```

and finally in the third terminal

```sh
python3 gameRisky-playerQ.py
```

**To notice that:**

- A `Control-C` in the game-server terminal would stop the game and the AIs**
- The arrows on the keyboard permit users to retrieve old commands.

## Objectives

The goal of this last and open exercise is to autonomously learn the best game-policy possible by using some heuristics to drive the learning process.

At the end the students would return between 2 and 3 text file:

- A `grpName-player.py` in python with the code learning by playing to Risky game.
- A `README.md` in [Mardown syntax](https://daringfireball.net/projects/markdown/basics), with a sort explanation of the student strategy to converge to this `grpName-player.py` solution. Do not forget the developers’ names at the beginning of the file. 
- A `qvalues.json` (optional) with an export of the qvalue dictionary.

The export of the qvalue dictionary in a file allows the player to be initialized with the last learning qvalues, in order to capitalize from one learning phase to another.

```python
# save a dictionary on a file:
f= open( 'qvalue.json', 'w' )
f.write( json.dump(qvalue) )
f.close()

# get a dictionary from a file:
f= open( 'qvalue.json', 'r' )
qvalue= json.loads( f.read() )
f.close()
```

**Good Luck** (and hard work)
