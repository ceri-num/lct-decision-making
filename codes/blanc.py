from game421 import Engine

# Default game interface :
def main():
    gameEngine= Engine()
    gameEngine.run( MyPlayer() )

# Agent as a very simple UI
class MyPlayer :

    def __init__(self):
        self.actionStr= "keep-keep-keep"

    def wakeUp( self, initialStateStr, actionSpace ):
        print( "Perception: "+ initialStateStr )

    def perceive(self, reachedStateStr, reward):
        print( "Perception: "+ reachedStateStr  +" with reward : " + str(reward) )

    def action(self, isValidAction ):
        self.actionStr= "keep-keep-keep"
        print( "Action: " + self.actionStr)
        return self.actionStr

    def kill( self, score ):
        print( "Game end on score: "+ str(score) )
        self.score= score

# Activate default interface :
if __name__ == '__main__':
    main()