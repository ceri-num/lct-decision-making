from game421 import Engine

# Default game interface :
def main():
    total= 0
    for i in range(10000) :
        gameEngine= Engine()
        player= PlayerDT()
        gameEngine.run( player )
        total+= player.score
    print( "Average score: " + str( total/10000.0 ) )

# Agent as a very simple UI
class PlayerDT :

    def __init__(self):
        self.actionStr= "keep-keep-keep"
        self.score= 0

    def perceive(self, perceptionStr, reward):
        values= [ int(x_str) for x_str in perceptionStr.split("-") ]
        gameState= { "H":values[0],  "D1":values[1],  "D2":values[2],  "D3":values[3] }
        self.score+= reward
        # print( "Perception: "+ perceptionStr  +" with reward : " + str(reward) )
        
        if gameState["D3"] == 1 :
            if gameState["D2"] == 2 :
                if gameState["D1"] == 4 :
                    self.actionStr= "keep-keep-keep"
                else: 
                    self.actionStr= "roll-keep-keep"
            else: 
                self.actionStr= "roll-roll-keep"
        else: 
            self.actionStr= "roll-roll-roll"

    def action(self, isValidAction ) :
        # print( "Action: " + self.actionStr)
        return self.actionStr

# Activate default interface :
if __name__ == '__main__':
    main()
