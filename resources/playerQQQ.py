#!env python3
"""
# Our Q learner applied on 421

Group: NOM Prenom, NOM Prenom

"""
import random

# MAIN: 

def main() :
    import game421 as game

    gameEngine= game.Engine()
    player= PlayerQ()
    numberOfGames= 100
    rewards= gameEngine.start( player, numberOfGames )
    print( "Average: " + str( sum(rewards)/len(rewards) ) )

# ACTIONS: 

actions= []
for a1 in ['keep', 'roll']:
    for a2 in ['keep', 'roll']:
        for a3 in ['keep', 'roll']:
            actions.append( a1+'-'+a2+'-'+a3 )

# Q LEARNER: 

class PlayerQ() :
    def __init__(self):
        self.results= []
    
    # State Machine :
    def stateStr(self):
        s= str(self.turn)
        for d in self.dices :
            s += '-' + str(d)
        return s

    # AI interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        self.scores= [ 0 for i in range(numberOfPlayers) ]
        self.id= playerId
        self.model= tabletop
        self.turn= 9
        self.dices= [1, 1, 1]
        self.action= 'roll-roll-roll'

    def perceive(self, turn, scores, pieces):
        self.reward= scores[ self.id ] - self.scores[ self.id ]
        self.scores= scores
        self.turn= turn
        self.dices= pieces

    def decide(self):
        self.action= random.choice( actions )
        print( f'state: { self.stateStr() }, action: { self.action }')
        return self.action
    
    def sleep(self, result):
        self.results.append(result)


# SCRIPT EXECUSION: 
if __name__ == '__main__':
    print("Let's go !!!")
    main()
