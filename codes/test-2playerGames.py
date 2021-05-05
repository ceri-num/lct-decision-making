#!env python3
from zombieQ import AgentQ as Player1
from gameZombies2 import System, SimplePlayer as Player2

players= [ Player1(), Player2() ]
demiSample= 10000
gameEngine= System()

print("# " + players[0].name + " vs "+ players[1].name )
print("Entrainement (" + str( 2*demiSample ) + " parties)")

for i in range(demiSample):
    gameEngine.run( players[1], players[0] )
    gameEngine.run( players[0], players[1] )

#players[0].go()
#players[1].go()

total= [0, 0]

print("Confrontation (" + str( 2*demiSample ) + " parties)")

for i in range(demiSample):
    gameEngine.run( players[1], players[0] )
    total[0]+= players[0].score
    total[1]+= players[1].score
    gameEngine.run( players[0], players[1] )
    total[0]+= players[0].score
    total[1]+= players[1].score

print( players[0].name + ": " + str( total[0]/(demiSample*2)) )
print( players[1].name + ": " + str( total[1]/(demiSample*2)) )

if total[0] > total[1] :
    print( "Winner: "+ players[0].name )
else :
    print( "Winner: "+ players[1].name )
