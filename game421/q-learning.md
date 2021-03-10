# Q-Learning

**Q-Learning** seems quite simple and we aim to implement it for learning to play to **421** game.

1. Implement a new *PlayerQ*
2. At initialization **Q** is created empty with the other required variable.
3. At perception steps the player update its **Q-value** and choose a new action to perform accordingly to **Q-Learning** algorithm.

## Ints for implementing Q

A simple way to implement **Q** in python language is to implement it as a Dictionnary of dictionaries.

- [Python documentation](https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries)
- [On w3school](https://www.w3schools.com/python/python_dictionaries.asp)

Initilizing an empty **Q** will look like:

```python
Q= {}
```

Initilizing action values for a given state will look like:

```python
if "2-6-3-2" not in Q.keys() :
    Q["2-6-3-2"]= { "keep-keep-keep":0.0, "roll-keep-keep":0.0, "keep-roll-keep":0.0, "roll-roll-keep":0.0, "keep-keep-roll":0.0, "roll-keep-roll":0.0, "keep-roll-roll":0.0, "roll-roll-roll":0.0 }
```

Then modifying a value in **Q** will look like:

```python
Q["2-6-3-2"]["roll-roll-roll"]= ...
```

Finally PLayerQ will look like :

```python
class PlayerQ
	state= ""
	qvalue= {}

def perceive(self, perceptionStr, reward )

	if self.state != "" : 
    	self.updateQ( self.state, self.actionStr, perceptionStr, reward)
    self.state= perceptionStr
    #selecte self.actionStr:
    self.actionStr= self.argMax( self.qvalue[perceptionStr] ) # for the best known action
    
```


## Going further:

1. *PlayerQ* save its learned **Q-values** on a file.
2. *PlayerQ* initialize its **Q-values** by loading a file.
3. A new *PlayerBestQ* simply play the best action always from a given **Q-values** dictionary (without upgrading **Q**).
4. You are capable of plotting the sum over **Q** with one point per episode (with [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) for instance).

