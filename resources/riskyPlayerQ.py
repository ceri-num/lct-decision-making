#!env python3
import sys, os, random
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hackagames as hg
import matplotlib.pyplot as plt

STRENGTH= 0
ACTIVATED= 1

def main():
    player= Player()
    hg.takeASeat('localhost', 14001, player )
    for feature in player.stats :
        del player.stats[feature][-1]
        print( player.stats[feature] )
        plt.plot( player.stats[feature] )
        plt.ylabel( feature )
        plt.show()

def diffScore(playerId, scores):
    playerScore= scores[playerId-1]
    oponentScore= 0
    for i in range( len(scores) ) :
        if i != playerId-1 and scores[i] > oponentScore :
            oponentScore= scores[i]
    return playerScore-oponentScore

class Player(hg.Player) :
    def __init__(self, explorationRatio=0.1, discountFactor=0.99, learningRate=0.1 ):
        super().__init__()
        self.epsilon= explorationRatio
        self.gamma= discountFactor
        self.alpha= learningRate
        self.qvalues= {}
        self.stats= {"exploration": [0], "average end": [0],"average best Q": [0]}
        self.episod= 0
    
    # State Machine :
    def stateStr(self):
        return self.fullStateStr()
    
    def fullStateStr(self):
        states= ['0-0-0' for c in self.tabletop ]
        for p in self.pieces :
            owner= '0'
            if p.owner == self.id :
                owner= '1'
            states[p.position]= owner + '-' + str(p.attributs[STRENGTH]) +'-'+ str(p.attributs[ACTIVATED])
        return '|'.join(states)
    
    def reward(self, playerId, newScores):
        return diffScore(playerId, newScores) -  diffScore(playerId, self.scores) 

    # Q learning methods:
    def updateQ( self, aStateT0, anAction, aStateT1, aReward ) : 
        oldValue= self.qvalues[aStateT0][anAction]
        futureGains= self.qvalues[aStateT1][ self.bestAction(aStateT1) ]
        self.qvalues[aStateT0][anAction]= (1 - self.alpha) * oldValue + self.alpha * ( aReward + self.gamma * futureGains )
        
    def bestAction( self, aState ) : 
        option= random.choice( list(self.qvalues[aState].keys()) )
        for a in self.qvalues[aState] :
            if self.qvalues[aState][a] > self.qvalues[aState][option] :
                option= a 
        return option

    # AI Interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        super().wakeUp(numberOfPlayers, playerId, tabletop)
        self.scores= [0 for i in range(numberOfPlayers)]
        initialState= self.stateStr()
        self.action= 'sleep'
        if initialState not in self.qvalues.keys() :
            self.qvalues[initialState]= {self.action: 0.0}

    def perceive(self, turn, scores, pieces):
        last= self.stateStr()
        reward= self.reward(self.id, scores)
        super().perceive(turn, scores, pieces)
        state= self.stateStr()
        
        # Initialize qvalues structure if required:
        if state not in self.qvalues.keys() :
            self.qvalues[state]= { self.randomAction() : 0.0 }
        if self.action not in self.qvalues[last].keys() :
            self.qvalues[last][self.action]= 0.0

        # Apply Q equation:
        self.updateQ( last, self.action, state, reward)
    
    def decide(self):
        if self.episod < 100 or random.random() < self.epsilon :
            self.action= self.randomAction()
        else :
            self.action= self.bestAction( self.stateStr() )
        #print( f'state: { self.stateStr() }, action: { self.action }')
        return self.action

    def sleep(self, result):
        super().sleep(result)

        # Compute markers
        sizeQ= len(self.qvalues)
        avBestQ= 0.0
        for s in self.qvalues :
            aStar= self.bestAction(s)
            avBestQ+= self.qvalues[s][aStar]
        avBestQ= (float)(avBestQ)/sizeQ
        print( f'exploration: {sizeQ} end: {result} average best Q: {avBestQ}' )

        # Reccords them
        xpLen= 10
        xp= self.episod // xpLen
        self.stats["exploration"][xp] += len(self.qvalues)
        self.stats["average end"][xp] += result
        self.stats["average best Q"][xp] += avBestQ

        # Prepare for a new episod:
        self.episod+=1
        if self.episod % xpLen == 0 :
            for feature in self.stats :
                self.stats[feature][xp]= self.stats[feature][xp] / xpLen
                self.stats[feature].append(0)

    # Generate possible actions :
    def randomAction(self):
        actions= [ ['sleep'] ]
        for piece in self.pieces :
            actions+= self.actionsFrom(self.id, piece)
        action= random.choice( actions )
        if( action[0] == 'move' ): #then get a random strengh:
            action[3]= random.randrange( action[3] )
        return ' '.join([str(x) for x in action])
    
    def actionsFrom( self, playerid, aPiece ):
        actions= []
        if aPiece.owner == playerid and aPiece.attributs[ACTIVATED] == 0 :
            actions.append( ['grow', aPiece.position] )
            for edge in self.tabletop[ aPiece.position ] :
                actions.append( ['move', aPiece.position, edge, aPiece.attributs[STRENGTH] ] )
        return actions

# Activate default interface :
if __name__ == '__main__':
    main()
