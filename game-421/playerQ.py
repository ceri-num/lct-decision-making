#!env python3
"""
First 421 player 
"""
import random

actions= []
for a1 in ['keep', 'roll']:
    for a2 in ['keep', 'roll']:
        for a3 in ['keep', 'roll']:
            actions.append( a1+'-'+a2+'-'+a3 )

class PlayerQ() :
    def __init__(self, name='QLearning'):
        self.results= []
        self.name= name
        # initialize q-values :
        self.qvalues= {}
        self.alpha= 0.1
        self.epsilon= 0.1

    # Tools :
    def maxQ(self, s):
        return self.qvalues[s][ self.argmaxQ(s) ]
    
    def argmaxQ(self, s):
        bestActionForS= ''
        for a in self.qvalues[s] :
            if bestActionForS == '' or self.qvalues[s][a] > self.qvalues[s][bestActionForS] :
                bestActionForS= a
        return bestActionForS

    # AI interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        self.scores= [ 0 for i in range(numberOfPlayers+1) ]
        self.id= playerId
        self.model= tabletop
        self.state= ''

    def perceive(self, turn, scores, pieces):
        self.reward= scores[ self.id ] - self.scores[ self.id ]
        # Define the new state
        newState= str(turn)+'-'+str(pieces[0])+'-'+str(pieces[1])+'-'+str(pieces[2])
        if newState not in self.qvalues :
            self.qvalues[newState]= { "keep-keep-keep": 0.0 }
        # Update the old state (if state != '')
        if self.state != '' :
            if self.action not in self.qvalues[self.state] :
                self.qvalues[self.state][self.action]= 0.0
            self.qvalues[self.state][self.action]= (1-self.alpha)*self.qvalues[self.state][self.action]
            self.qvalues[self.state][self.action]+= self.alpha*( self.reward + self.maxQ(newState) )
        self.state= newState

    def decide(self):
        self.action= random.choice( actions )
        # Epsilon-greedy Exploitation
        if random.random() > self.epsilon :
            self.action = self.argmaxQ(self.state)
        return self.action
    
    def sleep(self, result):
      self.results.append(result)

class PlayerQ2() :
    def __init__(self, name='QLearning'):
        self.results= []
        self.name= name
        # initialize q-values :
        self.qvalues= {}
        self.alpha= 0.1
        self.epsilon= 0.1

    # Tools :
    def maxQ(self, s):
        return self.qvalues[s][ self.argmaxQ(s) ]
    
    def argmaxQ(self, s):
        bestActionForS= ''
        for a in self.qvalues[s] :
            if bestActionForS == '' or self.qvalues[s][a] > self.qvalues[s][bestActionForS] :
                bestActionForS= a
        return bestActionForS

    # AI interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        self.id= playerId
        self.op= playerId+1
        if self.op > 2 :
            self.op= 1
        self.model= tabletop
        self.state= ''
    
    def fullState(self, turn, scores, pieces):
        newState= str(self.id)+'-'+str(scores[self.op])+'-H'+str(turn)
        newState+= '-'+str(pieces[0])+'-'+str(pieces[1])+'-'+str(pieces[2])
        return newState

    def dtState(self, turn, scores, pieces):
        s= int(scores[self.op])%100
        base= str(self.id)+'-'+str(s)+'-'+str(turn)
        if pieces[2] == 1 :
            if pieces[1] == 2 :
                if pieces[0] == 4 :
                    return base+'-4-2-1'
                else :
                    return base+'-X-X-1'
            elif pieces[1] == 1 :
                if pieces[0] == 1 :
                    return base+'-1-1-1'
                else :
                    return base+'-X-1-1'
        return base+'-X-X-X'

    def perceive(self, turn, scores, pieces):
        self.reward= 0.0
        if turn == 99 :
            if scores[self.id] > scores[self.op] :
                self.reward= 1.0
            elif scores[self.id] < scores[self.op] :
                self.reward= -1.0
        # Define the new state
        newState= self.fullState(turn, scores, pieces)
        #print(f'{newState} ":" {scores}')
        if newState not in self.qvalues :
            self.qvalues[newState]= { "keep-keep-keep": 0.0 }
        # Update the old state (if state != '')
        if self.state != '' :
            if self.action not in self.qvalues[self.state] :
                self.qvalues[self.state][self.action]= 0.0
            self.qvalues[self.state][self.action]= (1-self.alpha)*self.qvalues[self.state][self.action]
            self.qvalues[self.state][self.action]+= self.alpha*( self.reward + self.maxQ(newState) )
            #print(f'{self.state} > {self.action} > {newState}')
            #print(self.qvalues[self.state])
        self.state= newState

    def decide(self):
        self.action= random.choice( actions )
        # Epsilon-greedy Exploitation
        if random.random() > self.epsilon :
            self.action = self.argmaxQ(self.state)
        return self.action
    
    def sleep(self, result):
      self.results.append(result)