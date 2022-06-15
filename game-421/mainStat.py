#!env python3
import matplotlib.pyplot as plt
from tqdm import tqdm as processBar
from gameSingle421 import Game
from playerQ import PlayerQ as Player

# Parameters:
nd= 100

# Play:
p= Player('Arty')
g= Game()

sizes= []
averageScores= []
averageMaxQs= []

for i in processBar(range(2000)) :
    g.start(p, nd)
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
