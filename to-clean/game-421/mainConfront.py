#!env python3
import matplotlib.pyplot as plt
from tqdm import tqdm as processBar
import json
from gameConfront421 import Game
from playerQ import PlayerQ2 as Player
from playerMDP import PlayerBadPi

# Parameters:
nd= 1000

# Play:
f = open("policyMDP.json", "r")
pPi= PlayerBadPi( json.loads( f.read() ) )
f.close()

p= Player('Learner')
g= Game()

sizes= []
averageScores= []
averageMaxQs= []

for i in processBar( range(1000) ) :
    g.start(p, pPi, nd)
    sizes.append( len(p.qvalues) )
    averageScores.append( sum(p.results)/nd )
    averageMaxQs.append( sum( [ p.maxQ(s) for s in p.qvalues ] )/nd )
    p.results= []

# Plot:
plt.plot( sizes )
plt.ylabel( "size" )
plt.show()

plt.plot( averageScores )
plt.ylabel( "scores" )
plt.show()

plt.plot( averageMaxQs )
plt.ylabel( "average max Q" )
plt.show()
