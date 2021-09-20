# Default game interface :
def main():
    import game421 as game
    import time, json

    samples= 1000

    # Initialize MDP player:
    solver= MDP()
    print( "LearnModel (" + str(samples) + " samples per configuration: s, a)" )
    tic= time.process_time()

    solver.learnModel( game.System(), samples )

    print( "> " + str(round(time.process_time() - tic, 2)) + " seconds" )

    solver.valueIteration()
    solver.printStatistics()

    f = open("policyMDP.json", "w")
    f.write( json.dumps( solver.policy(), sort_keys=True, indent=2) )
    f.close()

    f = open("policyMDP.json", "r")
    player= AgentPi( json.loads( f.read() ) )
    f.close()

    # Test player policy:
    total= 0
    samples= 1000
    for i in range(samples) :
        gameEngine= game.System()
        gameEngine.run( player )
        total+= player.score
        # Record exploration indicator: the number of visited states 
    print( "Average score : " + str( total/samples ) )


# Agent as a very simple UI
class MDP :

    # Constructor
    def __init__(self, discountFactor=0.99, epsilon= 0.1 ):
        self.gamma= discountFactor
        self.epsilon= epsilon

    # accessor
    def policy(self):
        return self.pi

    # Markov Decision Processs life:
    def learnModel( self, engine, samples= 100 ):
        self.transition= {}
        self.reward= {}
        self.actions= engine.allActionsStr()
        self.samples= samples
        # For each state s
        allStatesStr= [ '-'.join( [str(v) for v in s.values() ] ) for s in engine.allStates() ]
        self.logFile= open('transition.log', 'w')
        for s in allStatesStr :
            self.transition[s]= {}
            self.reward[s]= {}
            # For each action a
            for a in engine.allActionsStr() :
                self.learnTransition(engine, s, a)
        self.logFile.close()

    def learnTransition(self, engine, s, a ):
        self.transition[s][a]= {}
        self.reward[s][a]= 0.0
        act= engine.actionFromStr( a )
        # Get samples:
        for i in range( self.samples ) :
            #step:
            engine.setOnStateStr( s )
            r= engine.step( act )
            sp= engine.stateStr()

            # report:
            self.logFile.write( s +" "+ a +" "+ sp + " "+ str(r) +"\n" )

            # learn:
            self.reward[s][a]+= r
            if sp not in self.transition[s][a] :
                self.transition[s][a][sp]= 1
            else : 
                self.transition[s][a][sp]+= 1

        # Compute statistics:
        self.reward[s][a]= self.reward[s][a] / self.samples
        for sp in self.transition[s][a] :
            self.transition[s][a][sp]= self.transition[s][a][sp] / self.samples

    def valueIteration(self):
        self.pi= { s: self.actions[0] for s in self.transition }
        self.values= { s: 0.0 for s in self.transition }
        maxDiffValue= self.epsilon + 1
        self.convergeance= [0.0]
        while maxDiffValue > self.epsilon :
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
            self.convergeance.append( sum(self.values.values())/len(self.values) )

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
        print( "Transition size: "+ str( transitionSize ) + " over " + str(len(self.values)) + " states " )
        print( "Average Value: "+ str( sum(self.values.values())/len(self.values)  ) )
        print( "Convergeance: "+ str([round(av, 2) for av in self.convergeance]) )


# Agent as a very simple UI
class AgentPi :

    # Constructor
    def __init__(self, policy): # Dictionnary of action to choose for each state
        self.pi= policy

    # Agent life:
    def wakeUp( self, initialState, stateDsc, actionSpace ):
        self.state= initialState

    def perceive(self, reachedState, reward ):
        self.state= reachedState

    def decide(self, isValidAction) :
        return self.pi[ self.state ]

    def sleep(self, score ) :
        self.score= score

# Activate default interface :
if __name__ == '__main__':
    main()
