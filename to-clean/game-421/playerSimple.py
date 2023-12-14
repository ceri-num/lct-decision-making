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

class PlayerRandom() :
    def __init__(self, name='IA'):
        self.results= []
        self.name= name

    # AI interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        self.scores= [ 0 for i in range(numberOfPlayers+1) ]
        self.id= playerId
        self.model= tabletop

    def perceive(self, turn, scores, pieces):
        self.reward= scores[ self.id ] - self.scores[ self.id ]
        self.scores= scores
        self.turn= turn
        self.dices= pieces

    def decide(self):
        action= random.choice( actions )
        return action
    
    def sleep(self, result):
      print( f'--- {str(self.name)} {str(result)}' )
      self.results.append(result)

class PlayerHuman(PlayerRandom) :

    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        super().wakeUp(numberOfPlayers, playerId, tabletop)
        print('New Game...')

    def perceive(self, turn, scores, pieces):
        super().perceive(turn, scores, pieces)
        print( f'{self.name}-{self.id}' )
        print( f'Dice: {str(self.dices)} Horizon: {self.turn} Score: {scores}' )
    
    def decide(self):
        print( "Action ?")
        action= ""
        while not action in actions :
                action= input()
        return action
