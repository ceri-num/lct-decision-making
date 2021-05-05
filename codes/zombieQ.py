import random

class AgentQ :

    # Initialization:
    def __init__(self, explorationRatio=0.1, discountFactor=0.99, learningRate= 0.1 ):
        self.epsilon= explorationRatio
        self.gamma= discountFactor
        self.alpha= learningRate
        self.qvalues= {}
        self.name= "ZombieQ"

    def stateDico( self, state ):
        stVector= state.split("-")
        # [ "1", "2", "Hard(gun)" .... ]
        stDico= {
          "Brain":  (int)(stVector[0]),
          "Gun":   (int)(stVector[1]),
          "D1":     stVector[2],
          "D2":     stVector[3],
          "D3":     stVector[4],
          "Easy":   (int)(stVector[5]),
          "Medium": (int)(stVector[6]),
          "Hard":   (int)(stVector[7])
        }
        return stDico

    def reductionState(self, globaleState ):
      dico= self.stateDico( globaleState )
      #print( globaleState  )

      if dico['D1'] not in ["EASY(Run)", "MEDI(Run)", "HARD(Run)"] :
          dico['D1'] = "XXXX"
      if dico['D2'] not in ["EASY(Run)", "MEDI(Run)", "HARD(Run)"] :
          dico['D2'] = "XXXX"
      if dico['D3'] not in ["EASY(Run)", "MEDI(Run)", "HARD(Run)"] :
          dico['D3'] = "XXXX"

      if dico['Easy'] == 0 and dico['Medium'] == 0 and dico['Hard'] == 0 :
        rst= "final"
      elif dico["Brain"] == 0 :
        rst= str(dico["Brain"])
      elif dico["Gun"] >= 2 :
        rst= str(dico["Brain"]) + "-" + str(dico["Gun"])
        rst+= "-"+ dico['D1']+ "-"+ dico['D2'] +"-"+ dico['D3']
      else :
        rst= str(dico["Brain"]) + "-" + str(dico["Gun"])
      
      #print( rst )
      return rst

    # Agent interfase:
    def wakeUp( self, initialState, stateDsc, actionSpace ):
        # Reccord initial state:
        self.state= self.reductionState(initialState)
        # Reccord the list of all possible actions:
        self.actions= actionSpace

        # Initialize a new state in Q if necessary:
        if self.state not in self.qvalues.keys() :
            self.qvalues[self.state]= { 
              'stop': 0.0,
              'go'  : 0.0
            }

    def perceive(self, reachedGlobalState, reward ):
        # Initialize a new state in Q if necessary:
        reachedState= self.reductionState( reachedGlobalState )
        #print( reward )
        # Initialize a new state in Q if necessary:
        if reachedState not in self.qvalues.keys() :
            self.qvalues[reachedState]= { 
              'stop': 0.0,
              'go'  : 0.0
             }

        # update Q( self.state, self.action ) with reachedState, reward

        self.updateQ( self.state, self.action, reachedState, reward )
        # Switch the new state:
        self.state= reachedState

    def decide(self, isValidAction) : # pure exploration: 
        if random.random() < self.epsilon :
            self.action= random.choice( self.actions )
        else :
            self.action= self.bestAction( self.state )
        #print( self.action )
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
