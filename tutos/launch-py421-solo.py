#!env python3
"""
Launcher for HackaGame - Py421-Solo
"""

# Get a game:
from hackagames.gamePy421.gameEngine import GameSolo as Game
from tuto_qlearning.bot import Bot

# Instanciate and start 100 games
game= Game()
player= Bot( learningRate=0.1 )

results= game.testPlayer( player, 100000 )

# Annalyse the results:
print( f"Average score: {sum(results)/len(results)}" )

# Plot: 
import matplotlib.pyplot as plt

scores= []
size= len(results)
for i in range(0, size, 500) :
    s= min(i+500, size)
    scores.append( sum([ x for x in results[i:s] ]) / (s-i) )
plt.plot( [ 500*i for i in range(len(scores)) ], scores )
plt.show()

#player.dump( "py421Duo-qvalues.json" )
#player.dumpPolicy( "py421-policy.json" )
