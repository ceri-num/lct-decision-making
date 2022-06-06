#!env python3
"""
# Our Q learner applied on 421

Group: NOM Prenom, NOM Prenom

"""
import sys, os, random, json
import matplotlib.pyplot as plt

xpname= 'game421-FullQ'

# MAIN: 
def main() :
    # Get the approate game:
    print( sys.path[0] )
    sys.path.insert(1, os.path.join(sys.path[0], '../game-421'))
    import game421 as game
    
    # ACTIONS: 
    actions= ['keep-keep-keep', 'keep-keep-roll', 'keep-roll-keep', 'keep-roll-roll',
        'roll-keep-keep', 'roll-keep-roll', 'roll-roll-keep', 'roll-roll-roll']
    
    stats= {"exploration": [], "average score": [],"average best Q": []}
    gameEngine= game.Engine()

    player= PlayerQ(actions, explorationRatio=0.1, discountFactor=0.99, learningRate=0.1)

    # learning episodes:
    numberOfGames= 500
    for episod in range(200) :
        rewards= gameEngine.start( player, numberOfGames )
        average= updateStats(stats, player, rewards)
        print( "Average: " + str(average) )

    # last episode:
    player.epsilon= 0
    rewards= gameEngine.start( player, 10000 )
    average= updateStats(stats, player, rewards)
    print( "Average (no exploration): " + str(average) )
    

    f= open( f'{xpname}-stats.json', 'w' )
    f.write( json.dumps( stats ) )
    f.close()

    f= open( f'{xpname}-qvalues.json', 'w' )
    f.write( json.dumps( player.qvalues ) )
    f.close()
    
    for elt in stats :
        plt.plot( stats[elt] )
        plt.ylabel( elt )
        plt.show()

def updateStats(stats, player, rewards) :
    # Record exploration indicator: the number of visited states:
    sizeQ= len(player.qvalues)
    stats["exploration"].append( sizeQ )
    # Record the average score:
    sumQ= 0
    for s in player.qvalues :
        aStar= player.bestAction(s)
        sumQ+= player.qvalues[s][aStar]
    average= sum(rewards)/len(rewards)
    stats["average score"].append( average )
    # Record the average best Q value for each state:
    stats["average best Q"].append( sumQ/sizeQ )
    return average

# Q LEARNER: 

class PlayerQ() :
    def __init__(self, actions, explorationRatio=0.1, discountFactor=0.99, learningRate=0.1 ):
        self.actions=actions
        self.results= []
        self.epsilon= explorationRatio
        self.gamma= discountFactor
        self.alpha= learningRate
        self.qvalues= {}
    
    # State Machine :
    def stateStr(self):
        return self.fullStateStr()

    def fullStateStr(self):
        s= str(self.turn)
        for d in self.dices :
            s += '-' + str(d)
        return s
    
    def decisionTreeState(self):
        if self.turn == 0 :
            return 'end'
        if self.dices[2] == 1 :
            if self.dices[1] == 2 :
                if self.dices[0] == 4 :
                    return "4-2-1"
                return "X-2-1"
            if self.dices[1] == 1 :
                return "X-1-1"
            return "X-X-1"
        return "X-X-X"

    # Q learning methods:
    def updateQ( self, aStateT0, anAction, aStateT1, aReward ) : 
        oldValue= self.qvalues[aStateT0][anAction]
        futureGains= self.qvalues[aStateT1][ self.bestAction(aStateT1) ]
        self.qvalues[aStateT0][anAction]= (1 - self.alpha) * oldValue + self.alpha * ( aReward + self.gamma * futureGains )
        
    def bestAction( self, aState ) : 
        option= random.choice( self.actions )
        for a in self.qvalues[aState] :
            if self.qvalues[aState][a] > self.qvalues[aState][option] :
                option= a 
        return option

    # AI interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        self.scores= [ 0 for i in range(numberOfPlayers) ]
        self.id= playerId
        self.model= tabletop
        self.turn= 9
        self.dices= [1, 1, 1]
        self.action= 'roll-roll-roll'
        # Initialize a new state in Q if necessary:
        st= self.stateStr()
        if st not in self.qvalues.keys() :
            self.qvalues[st]= { a: 0.0 for a in self.actions }

    def perceive(self, turn, scores, pieces):
        last= self.stateStr()
        reward= scores[ self.id ] - self.scores[ self.id ]
        self.scores= scores
        self.turn= turn
        self.dices= pieces
        # Initialize a new state in Q if necessary:
        st= self.stateStr()
        if st not in self.qvalues.keys() :
            self.qvalues[st]= { a: 0.0 for a in self.actions }
        # Update Q:
        self.updateQ( last, self.action, st, reward )

    def decide(self):
        if random.random() < self.epsilon :
            self.action= random.choice( self.actions )
        else :
            self.action= self.bestAction( self.stateStr() )
        #print( f'state: { self.stateStr() }, action: { self.action }')
        return self.action

    def sleep(self, result):
        self.results.append(result)


# SCRIPT EXECUSION:

if __name__ == '__main__':
    print("Let's go !!!")
    main()
