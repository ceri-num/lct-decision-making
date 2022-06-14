#!env python3
import matplotlib.pyplot as plt
from gameConfront421 import Game
from playerSimple import PlayerRandom as Player

# Parameters:
nd= 100

# Play:
p= Player('Arty')
pBis= Player('Boby')
g= Game()
g.start(p, pBis, nd)

# Statistics:
average= sum(p.results)/nd
print( f'Average scores:\t{average}' )

# Plot:
plt.plot( p.results )
plt.plot( [average for i in range(nd)] )

plt.ylim(-1, 1)
plt.ylabel( "scores" )
plt.show()
