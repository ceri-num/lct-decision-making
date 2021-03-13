from game421 import Engine
import random 
import matplotlib.pyplot as plt

# Default game interface :
def main():
    # Initialize MDP player:
    player= PlayerMDP()
    player.learnModel( Engine() )
    player.valueIteration()
    player.printPolicy()
    player.printStatistics()

    # Test player policy:
    total= 0
    samples= 100000
    for i in range(samples) :
        gameEngine= Engine()
        gameEngine.run( player )
        total+= player.score
        # Record exploration indicator: the number of visited states 
    print( "average score : " + str( total/samples ) )

# Agent as a very simple UI
class PlayerMDP :

    # Constructor
    def __init__(self, discountFactor=0.99, epsilon= 0.1 ):
        self.gamma= discountFactor
        self.epsilon= epsilon

    # Agent life:
    def wakeUp(self, initialStateStr, actionSpace ):
        # Reccord initial state:
        self.stateStr= initialStateStr

    def perceive(self, reachedStateStr, reward ):
        self.stateStr= reachedStateStr

    def action(self, isValidAction ) : # pure exploration: 
        self.actionStr= random.choice( self.actions )
        return self.pi[ self.stateStr ]

    def kill( self, score ):
        # print( "Game end on score: "+ str(score) )
        self.score= score

    # Markov Decision Processs life:
    def learnModel( self, engine ):
        self.transition= {}
        self.reward= {}
        self.actions= engine.allActionsStr()
        # For each state s
        allStatesStr= [ '-'.join( [str(v) for v in s.values() ] ) for s in engine.allStates() ]
        for s in allStatesStr :
            self.transition[s]= {}
            self.reward[s]= {}
            # For each action a
            for a in engine.allActionsStr() :
                self.learnTransition(engine, s, a)

    def learnTransition(self, engine, s, a ):
        self.transition[s][a]= {}
        self.reward[s][a]= 0.0
        act= engine.actionFromStr( a )
        samples= 1000
        # Get samples:
        for i in range(samples) :
            engine.setOnStateStr( s )
            self.reward[s][a]+= engine.step( act )
            sp= engine.stateStr()
            if sp not in self.transition[s][a] :
                self.transition[s][a][sp]= 1
            else : 
                self.transition[s][a][sp]+= 1

        # Compute statistics:
        self.reward[s][a]= self.reward[s][a] / samples
        for sp in self.transition[s][a] :
            self.transition[s][a][sp]= self.transition[s][a][sp] / samples

    def valueIteration(self):
        self.pi= { s: self.actions[0] for s in self.transition }
        self.values= { s: 0.0 for s in self.transition }
        maxDiffValue= self.epsilon + 1
        #while maxDiffValue > self.epsilon :
        for i in range( 10 ):
            # for each state
            maxDiffValue= 0.0
            values= { s: 0.0 for s in self.transition }
            for s in self.transition :
                bestValue= self.BelmanValueOf(s, self.pi[s] )
                # search the best couple action / value
                for a in self.transition[s] :
                    value= self.BelmanValueOf(s, a)
                    if value > bestValue :
                        bestValue= value
                        self.pi[s]= a
                if abs( bestValue - self.values[s]  ) > maxDiffValue :
                    maxDiffValue= abs( bestValue - self.values[s]  )
                values[s]= bestValue
            self.values= values
            print( maxDiffValue )

    def BelmanValueOf( self, s, a ):
        expectedGains= 0
        for sp in self.transition[s][a] :
            expectedGains+= self.transition[s][a][sp] * self.values[sp]
        return self.reward[s][a] + self.gamma * expectedGains

    def printModel(self):
        print( "MDP Model:" )
        for s in self.transition.keys() :
            for a in self.transition[s] :
                print( "Transition from "+ s +" by doing "+ a +" (reward: "+ str( self.reward[s][a] ) +"): "+ str(len(self.transition[s][a])) )
                print( self.transition[s][a] )

    def printPolicy(self):
        print( "Policy:" )
        for s in self.pi :
            print( "From "+ s +" do "+ self.pi[s] +" ("+ str( self.values[s] ) +")" )

    def printStatistics(self):
        transitionSize= 0
        for s in self.transition.keys() :
            for a in self.transition[s] :
                transitionSize+= len( self.transition[s][a] )
        print( "Transition size: "+ str( transitionSize ) )

# Activate default interface :
if __name__ == '__main__':
    main()
