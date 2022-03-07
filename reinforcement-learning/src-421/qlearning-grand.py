# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import random

def main() :
    print("Simple Q-Learning")

    actions= ["right", "down", "left", "up" ]
    s0= "s0"
    sEnd= "s5"
    
    epsilon= 0.1
    learning_rate= 0.1
    Qlearning( simulateGrid, s0, sEnd, actions, epsilon, learning_rate, 50000 )


def Qlearning(simulate, s0, sEnd, actions, epsilon, learning_rate, nEpisode ):
    # Initialize state-action matrice Q to zero
    Q= { s0 : { a:0.0 for a in actions } }
    printQ("Episod 0", Q)
    
    # Perform n episodes/iterations of Q-learning
    for i in range(nEpisode):
        Q= learnEpisode(simulate, s0, sEnd, actions, epsilon, learning_rate, Q)
    
    printQ("Episod "+ str(nEpisode), Q)
    return Q

def learnEpisode(simulate, s0, sEnd, actions, epsilon, learning_rate, Q):
    state= s0 #set cursor to initial state
    while state != sEnd :
        if random.random() <= epsilon :
            action= random.choice( actions )
        else :
            action= argmax( Q[state] )
        next_state, reward= simulate(state, action)    
        
        if next_state not in Q :
            Q[next_state]= { a:0.0 for a in actions }
    
        # update rule for Q-learning
        Q[state][action]+= learning_rate * ( reward + max(Q[next_state].values()) - Q[state][action] )
        # move to next state
        state= next_state
    return Q

def argmax(dico) :
    # return the dico key wchich are the higest associated value.
    return  max( dico, key= dico.get )

def printQ(title, Q) :
    # print Q (a dictionnary 'state' of dictionnary 'actions' ) in a fashion way
    print("\n"+title)
    print("\nQ ("+ str(len(Q)) +")")
    print( "\n".join( [ state + ": "+ str( Q[state] ) for state in Q ] ) )
    print( "best actions:\n\t"+ str({ state: argmax(Q[state]) for state in Q }) )

def simulateGrid(state, action) :
      # Calculate next state (according to sample grid with wall)
      # Default: remain in a state if action tries to leave grid
      next_state= state
      if (state == "s0" and action == "down") :
          next_state= "s4"
      elif (state == "s1" and action == "down") :
          next_state= "s3"
      elif (state == "s1" and action == "up") :
          next_state= "s5"
      elif (state == "s2" and action == "left") :
          next_state= "s3"
      elif (state == "s3" and action == "left") :
          next_state= "s4"
      elif (state == "s3" and action == "up") :
          next_state= "s1"
      elif (state == "s3" and action == "right") :
          next_state= "s2"
      elif (state == "s4" and action == "down") :
          next_state= "s5"
      elif (state == "s4" and action == "right") :
          next_state= "s3"
      elif (state == "s4" and action == "up") :
          next_state= "s0"
      
      
      # Calculate reward
      if (state == "s4" and next_state == "s5") :
        reward= 10
      elif (state == "s1" and next_state == "s5") :
        reward= 100
      else:
        reward= -1
      return next_state, reward

if __name__ == "__main__":
    # execute only if run as a script
    main()
