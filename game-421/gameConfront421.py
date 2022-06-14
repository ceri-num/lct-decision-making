#!env python3
"""
Script MDP 421 
"""
import random
from gameSingle421 import Game as GameSingle

class Game(GameSingle) :

    def __init__( self, horizon=6 ):
        self.horizon= horizon
        self.initialize()

    def initialize(self, horizon=0):
        dice= self.randomDice([1, 1, 1], ["roll", "roll", "roll"])
        self.state= { "H": horizon,  "D1":dice[0],  "D2":dice[1],  "D3":dice[2] }

    def start(self, playerA, playerB, numberOfGames=1 ):
        player1= playerA
        player2= playerB
        for i in range(numberOfGames):
            scores= [0.0, 0.0, 0.0]
            player1.wakeUp(2, 1, [])
            player2.wakeUp(2, 2, [])
            
            #First player:
            action= ''
            self.initialize()
            scores[1]= self.score( self.state )
            while action != 'keep-keep-keep' and self.turn() != self.horizon :
                player1.perceive( self.turn(), scores, self.dices() )
                action= player1.decide()
                self.state= self.randomTransition( self.actionFromStr(action), timeStep=1 )
                scores[1]= self.score( self.state )
            
            #Second player:
            action= ''
            self.initialize( self.state['H']-1 )
            scores[2]= self.score( self.state )
            while action != 'keep-keep-keep' and self.turn() > 0 :
                player2.perceive( self.turn(), scores, self.dices() )
                action= player2.decide()
                self.state= self.randomTransition( self.actionFromStr(action), timeStep=-1)
                scores[2]= self.score( self.state )
            
            #End of game:
            player1.perceive( 999, scores, self.dices() )
            player2.perceive( 999, scores, self.dices() )
            score1= 0
            if scores[1] > scores[2] :
                score1= 1
            elif scores[1] < scores[2] :
                score1= -1
                
            player1.sleep( score1 )
            player2.sleep( score1*-1 )
            bob= player1
            player1= player2
            player2= bob

    def randomTransition(self, action, timeStep= -1):
        dice=[ self.state["D1"], self.state["D2"], self.state["D3"] ]
        diceAct= [ action["A1"], action["A2"], action["A3"] ]
        dice= self.randomDice(dice, diceAct)
        return { "H":(self.state["H"]+timeStep),  "D1":dice[0],  "D2":dice[1],  "D3":dice[2] }
