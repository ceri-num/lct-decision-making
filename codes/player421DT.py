from game421 import Engine

# Default game interface :
def main():
    total= 0
    samples= 10000
    for i in range(samples) :
        gameEngine= Engine()
        player= PlayerDT()
        gameEngine.run( player )
        total+= player.score
    print( "Average score: " + str( total/samples ) )

# Agent as a very simple UI
class PlayerDT :

    def wakeUp(self, initialStateStr, actionSpace):
        values= [ int(x_str) for x_str in initialStateStr.split("-") ]
        self.state= { "H":values[0],  "D1":values[1],  "D2":values[2],  "D3":values[3] }

    def perceive(self, reachedStateStr, reward):
        values= [ int(x_str) for x_str in reachedStateStr.split("-") ]
        self.state= { "H":values[0],  "D1":values[1],  "D2":values[2],  "D3":values[3] }
        
    def action(self, isValidAction ) :
        # print( "Action: " + self.actionStr)
        if self.state["D3"] == 1 :
            if self.state["D2"] == 2 :
                if self.state["D1"] == 4 :
                    self.actionStr= "keep-keep-keep"
                else: 
                    self.actionStr= "roll-keep-keep"
            else: 
                self.actionStr= "roll-roll-keep"
        else: 
            self.actionStr= "roll-roll-roll"

        return self.actionStr

    def kill(self, score ) :
        # print( "Game end on score: "+ str(score) )
        self.score= score

# Activate default interface :
if __name__ == '__main__':
    main()
