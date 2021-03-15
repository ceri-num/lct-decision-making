from game421 import Engine
import random 
import matplotlib.pyplot as plt

# Default game interface :
def main():
    player= PlayerQ( explorationRatio=0.1, learningRate= 0.1 )
    stats= { "exploration": [], "average score": [], "average best Q": [] }
    samples= 500
    step= 500
    for v in range(step) :
        total= 0
        for i in range(samples) :
            gameEngine= Engine()
            gameEngine.run( player )
            total+= player.score
        # Record exploration indicator: the number of visited states 
        sizeQ= len(player.Q)
        stats["exploration"].append( sizeQ )
        # Record the average score:
        sumQ= 0
        for s in player.Q :
            sumQ+= player.Q[s][ player.actionMax(s) ]
        stats["average score"].append( total/samples )
        # Record the average best Q value for each state:
        stats["average best Q"].append( sumQ/sizeQ )

    for elt in stats :
        plt.plot( stats[elt] )
        plt.ylabel( elt )
        plt.show()

# Agent as a very simple UI
class PlayerQ :

    def __init__(self, explorationRatio=0.1, discountFactor=0.99, learningRate= 0.1 ):
        self.epsilon= explorationRatio
        self.gamma= discountFactor
        self.alpha= learningRate
        self.Q= {}

    def wakeUp(self, initialStateStr, actionSpace ):
        # Reccord initial state:
        self.stateStr= initialStateStr
        # Reccord the list of all possible actions:
        self.actions= actionSpace
        # Initialize a new state in Q if necessary:
        if self.stateStr not in self.Q.keys() :
            self.Q[self.stateStr]= { a: 0.0 for a in self.actions }

    def perceive(self, reachedStateStr, reward ):
        # Initialize a new state in Q if necessary:
        if reachedStateStr not in self.Q.keys() :
            self.Q[reachedStateStr]= { a: 0.0 for a in self.actions }
        # update Q( self.stateStr, self.actionStr ) with reachedStateStr, reward
        oldValue= self.Q[self.stateStr][self.actionStr]
        futureGains= self.Q[ reachedStateStr ][ self.actionMax(reachedStateStr) ]
        self.Q[self.stateStr][self.actionStr]= (1 - self.alpha) * oldValue + self.alpha * ( reward + self.gamma * futureGains )
        # Switch the new state:
        self.stateStr= reachedStateStr

    def actionMax( self, aState ) : 
        option= random.choice( self.actions )
        for a in self.Q[aState] :
            if self.Q[aState][a] > self.Q[aState][option] :
                option= a 
        return option

    def action(self, isValidAction ) : # pure exploration: 
        if random.random() < self.epsilon :
            self.actionStr= random.choice( self.actions )
        else :
            self.actionStr= self.actionMax( self.stateStr )

        return self.actionStr

    def kill(self, score ) :
        # print( "Game end on score: "+ str(score) )
        self.score= score

    def printQ(self) :
        print( "Q: " )
        for s in self.Q :
            print( s + ": " + str( self.Q[s] ) )

# Activate default interface :
if __name__ == '__main__':
    main()
