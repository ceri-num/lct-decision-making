import game421 as game
import random 
import matplotlib.pyplot as plt

# Default game interface :
def main():
    player= AgentQ( explorationRatio=0.1, learningRate= 0.1 )
    stats= { "exploration": [], "average score": [], "average best Q": [] }
    samples= 500
    step= 500
    gameEngine= game.System()
    for v in range(step) :
        total= 0
        # Perfrom `samples` games, by reccording the reached score:
        for i in range(samples) :
            gameEngine.run( player )
            total+= player.score
        # Annalyse the qvalue object after `samples` games:
        # Record exploration indicator: the number of visited states:
        sizeQ= len(player.qvalues)
        stats["exploration"].append( sizeQ )
        # Record the average score:
        sumQ= 0
        for s in player.qvalues :
            aStar= player.bestAction(s)
            sumQ+= player.qvalues[s][aStar]
        stats["average score"].append( total/samples )
        # Record the average best Q value for each state:
        stats["average best Q"].append( sumQ/sizeQ )

    for elt in stats :
        plt.plot( stats[elt] )
        plt.ylabel( elt )
        plt.show()

# Agent as a very simple UI
class AgentQ :

    # Initialization:
    def __init__(self, explorationRatio=0.1, discountFactor=0.99, learningRate= 0.1 ):
        self.epsilon= explorationRatio
        self.gamma= discountFactor
        self.alpha= learningRate
        self.qvalues= {}

    # Agent interfase:
    def wakeUp( self, initialState, stateDsc, actionSpace ):
        # Reccord initial state:
        self.state= initialState
        # Reccord the list of all possible actions:
        self.actions= actionSpace
        # Initialize a new state in Q if necessary:
        if self.state not in self.qvalues.keys() :
            self.qvalues[self.state]= { a: 0.0 for a in self.actions }

    def perceive(self, reachedState, reward ):
        # Initialize a new state in Q if necessary:
        if reachedState not in self.qvalues.keys() :
            self.qvalues[reachedState]= { a: 0.0 for a in self.actions }
        # update Q( self.state, self.action ) with reachedState, reward
        self.updateQ( self.state, self.action, reachedState, reward )
        # Switch the new state:
        self.state= reachedState

    def decide(self, isValidAction) : # pure exploration: 
        if random.random() < self.epsilon :
            self.action= random.choice( self.actions )
        else :
            self.action= self.bestAction( self.state )
        return self.action

    def sleep(self, score ) :
        # print( "Game end on score: "+ str(score) )
        self.score= score

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

    def printQ(self) :
        print( "Q: " )
        for s in self.qvalues :
            print( s + ": " + str( self.qvalues[s] ) )

# Activate default interface :
if __name__ == '__main__':
    main()
