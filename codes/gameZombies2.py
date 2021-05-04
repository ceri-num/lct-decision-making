import random
from enum import IntEnum

# Default game interface :
def main():
    gameEngine= Engine()
    player1= HumanAgent("Bob")
    player2= SimplePlayer()
    gameEngine.run( player1, player2 )

# Abstract Agent Based Model

class AbsAgent :

    # Object Methods:
    #---------------
    def __init__(self, sep="-"):
        self.separator= sep

    # Agent Methods:
    #---------------
    def wakeUp( self, initialStateStr, stateDsc, actionSpace ):
        # I wake up the agent with:
        #  - an initial state,
        #  - a description of state varibles
        #  - the collection of all possible actions
        self.descriptor= stateDsc
        self.state= initialStateStr
        self.score= 0

    def perceive( self, reachedStateStr, reward ):
        pass

    def decide( self, isValidAction ) :
        pass

    def sleep( self, score ):
        self.score= score

    # state and action manipulation:
    #-------------------------------

    def stateStr( self ):
        return self.state
    
    def stateVector( self ):
        return self.state.split( self.separator )

    def stateDico( self ):
        return { k:val for k, val in zip( self.descriptor, self.stateVector() ) }

# Agent as a very simple UI
class HumanAgent(AbsAgent) :

    def wakeUp( self, initialStateStr, stateDsc, actionSpace ):
        super().wakeUp( initialStateStr, stateDsc, actionSpace )
        print( "Start a new game, possible actions are:" )
        print( actionSpace )
        print( "Perception: "+ initialStateStr )

    def perceive(self, reachedStateStr, reward):
        self.state= reachedStateStr
        print( "Perception: "+ self.state +" with reward : " + str(reward) )

    def decide(self, isValidAction ) :
        print( "Action ?")
        actionStr= ""
        while not isValidAction( actionStr ) :
            actionStr= input()
        return actionStr

    def sleep(self, score):
        super().sleep( score )
        print( "Game end on score: "+ str(score) )

class SimplePlayer:

    def __init__( self ):
        self.told= 0.5

    def stateDico(self):
        stateVariables= self.state.split("-")
        return {
            "brain": int( stateVariables[0] ),
            "shoot": int( stateVariables[1] ),
            "d1": stateVariables[2],
            "d2": stateVariables[3],
            "d3": stateVariables[4],
            "easy": int( stateVariables[5] ),
            "medium": int( stateVariables[6] ),
            "hard": int( stateVariables[7] ),
            "score": int( stateVariables[9] ),
            "oponent": int( stateVariables[10] ),
        }

    def wakeUp( self, initialStateStr, stateDsc, actionSpace ):
        # I wake up the agent with:
        #  - an initial state,
        #  - a description of state varibles
        #  - the collection of all possible actions
        self.descriptor= stateDsc
        self.state= initialStateStr
        self.score= 0

    def perceive(self, reachedStateStr, reward):
        self.state= reachedStateStr
    
    def decide(self, isValidAction):
        stDico= self.stateDico()
        if stDico["brain"] < 1 or random.random() < self.told :
            return "go"
        return "stop"

    def sleep(self, score):
        self.score= score

# Zombie Game elements:

class DiceType(IntEnum):
    EASY= 0
    MEDIUM= 1
    HARD= 2
    UNDEF= 3

class DiceFace(IntEnum):
    BRAIN= 0
    GUN= 1
    RUN= 2

DiceType_str= ["EASY", "MEDI", "HARD","UNDEF"]
DiceFace_str= ["Brain", "Gun", "Run"]
DiceFace_weight= [
    [3, 1, 2 ], #EASY
    [2, 2, 2 ], #MEDIUM
    [1, 3, 2 ], #HARD
    [0, 0, 1 ], #UNDEF
]

class Dice():
    x= 0

    # Instance initialization
    #------------------------
    def __init__(self):
        self.type= DiceType.UNDEF
        self.face= DiceFace.RUN

    def __str__(self):
        if self.type == DiceType.UNDEF :
            return "UNDEFINED"
        return DiceType_str[self.type] +"("+ DiceFace_str[self.face] +")"

    # Builder
    #--------
    def setType(self, type):
        self.type= type
        self.face= DiceFace.RUN

    # Trandom transition
    #-------------------
    def random_face(self):
        weight= DiceFace_weight[self.type]
        rand= random.randrange( sum( weight ) )
        #print("random "+ str(rand) + " in [0, "+ str(sum(weight)) +"]")
        for face in DiceFace :
            if rand < weight[face] :
                return face
            rand-= weight[face]
        return DiceFace.RUN

    def roll(self):
        self.face= self.random_face()

class Engine :

    # Instance initialization
    #------------------------
    def __init__(self, nbDice=3, stockEASY=6, stockMEDIUM=4, stockHARD=3):
        self.nbDice= nbDice
        self.stockEASY= stockEASY
        self.stockMEDIUM= stockMEDIUM
        self.stockHARD= stockHARD

    # Instance initialization
    #------------------------
    def initializeTurn( self ):
        self.hand= [0] * self.nbDice
        for i in range( 0, self.nbDice ) :
            self.hand[i]= Dice()
        self.brain= 0
        self.shot= 0
        self.stock= [ self.stockEASY, self.stockMEDIUM, self.stockHARD ]
        self.reward= 0

    # Engine
    #--------
    def valideAction(self, action) :
        return action in ( "go", "stop" )

    def run( self, player1, player2 ):
        self.player= player1
        self.score= 0
        self.oponent= player2
        self.opScore= 0
        
        self.turn( True )
        self.switchPlayer()
        self.turn( True )
        self.switchPlayer()

        while self.opScore < 13 :            
            self.turn( False )
            self.switchPlayer()

        self.initializeTurn()
        self.player.perceive( self.stateStr(), -1 )
        self.player.sleep( self.score )

        self.switchPlayer()
        self.player.perceive( self.stateStr(), self.score )
        self.player.sleep( self.score )

    def turn( self, first ):
        self.initializeTurn()

        if first :
            self.player.wakeUp( self.stateStr(),
                [ "Brain", "Shoot", "D1", "D2", "D3", "EASY", "MEDIUM", "HARD" ],
                ["go", "stop"] )
        else :
            self.player.perceive( self.stateStr(), 0.0 )

        stop= False
        while not stop :
            # ask
            action= self.player.decide( self.valideAction )

            if action == "go" :
                self.step()

            if action == "stop" or self.remaining_dice() < 3 :
                self.score+= self.brain
                stop= True
            elif self.shot > 2 :
                stop= True
            else :
                self.player.perceive( self.stateStr(), 0.0 )

    def switchPlayer(self):
        p= self.player
        s= self.score
        self.player= self.oponent
        self.score= self.opScore
        self.oponent= p
        self.opScore= s

    # Accessor
    #---------
    def handDieType(self, idice):
        if self.hand[idice].face == DiceFace.RUN :
            return self.hand[idice].type
        return DiceType.UNDEF

    def remaining_dice(self) :
        count= sum( self.stock )
        for die in self.hand :
            if die.face == DiceFace.RUN :
                count+= 1
        return count

    def remaining_dice(self) :
        count= sum(self.stock)
        for die in self.hand :
            if die.face == DiceFace.RUN :
                count+= 1
        return count

    def state(self):
        return {
            "brain": self.brain,
            "shoot": self.shot,
            "d1": str(self.hand[0]),
            "d2": str(self.hand[1]),
            "d3": str(self.hand[2]),
            "easy": self.stock[DiceType.EASY],
            "medium": self.stock[DiceType.MEDIUM],
            "hard": self.stock[DiceType.HARD],
            "score": self.score,
            "oponent": self.opScore
        }

    def stateStr(self):
        values= [
            self.brain,
            self.shot,
            str(self.hand[0]),
            str(self.hand[1]),
            str(self.hand[2]),
            self.stock[DiceType.EASY],
            self.stock[DiceType.MEDIUM],
            self.stock[DiceType.HARD],
            "score:", self.score,
            self.opScore
        ]
        return "-".join( [ str(x) for x in values ] )

    # String
    #-------
    def __str__(self):
        stockSum= 0
        for s in self.stock :
            stockSum= stockSum + s

        myStr= "Stock("+ str(stockSum) +"/"+ str(self.remaining_dice()) +"): "
        myStr+= "EASY("+ str(self.stock[DiceType.EASY]) +") "
        myStr+= "MEDIUM("+ str(self.stock[DiceType.MEDIUM]) +") "
        myStr+= "HARD("+ str(self.stock[DiceType.HARD]) +") "
        myStr+= "\t| Dice: "+ str(self.hand[0])
        for i in range(1, len(self.hand) ) :
            myStr+= " - "+ str(self.hand[i])

        return myStr +"\t| Brain: "+ str(self.brain) +" | Shoot: "+ str(self.shot)

    # random transition:
    #-------------------
    def randomType(self):
        rand= random.randrange( sum(self.stock) )
        for type in DiceType :
            if rand < self.stock[type] :
                return type
            rand-= self.stock[type]
        return DiceType.EASY

    def pullRandomDie(self):
        type= self.randomType()
        self.stock[type]-= 1
        return type

    def step(self) :
        for aDie in self.hand :
            # new dice ?
            if aDie.type == DiceType.UNDEF or not( aDie.face == DiceFace.RUN ) :
                type= self.pullRandomDie()
                aDie.setType(type)

            # roll and result:
            aDie.roll()
            if aDie.face == DiceFace.BRAIN :
                self.brain+= 1
            if aDie.face == DiceFace.GUN :
                self.shot+= 1


# Activate default interface :
if __name__ == '__main__':
    main()