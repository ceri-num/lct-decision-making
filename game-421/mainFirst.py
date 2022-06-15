#!env python3
import matplotlib.pyplot as plt
from gameSingle421 import Game
from playerSimple import PlayerRandom as Player

# Parameters:
nd= 100

# Play:
p= Player('Arty')
g= Game()
g.start(p, nd)

# Statistics:
average= sum(p.results)/nd
print( f'Average scores:\t{average}' )

# Plot:
plt.plot( p.results )
plt.plot( [average for i in range(nd)] )

plt.ylim(0, 800)
plt.ylabel( "scores" )
plt.show()
