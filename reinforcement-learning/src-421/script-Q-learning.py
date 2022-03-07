# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import random

def main() :
    
    print("Simple Q-Learning")

    actions= ["right", "down", "left", "up" ]
    states= ["s0", "s1", "s2", "s3"] # "s0": the initial state, "s3": terminal state

    epsilon= 0.1
    learning_rate= 0.1
    
    Q= Qlearning(states, actions, simulateGrid, epsilon, learning_rate, 10)
    
    printQ("learned Q: ", Q)

def printQ(title, Q) :
    # print Q (a dictionnary 'state' of dictionnary 'actions' ) in a fashion way
    print("\n"+title)
    print( "\n".join( [ state + ": "+ str( Q[state] ) for state in Q ] ) )
    print( "best actions: "+ str({ state: argmax(Q[state]) for state in Q }) )

def Qlearning(states, actions, simulator, epsilon, learning_rate, n):
    # Initialize state-action matrice Q to zero
    Q= { s:{a:0 for a in actions} for s in states }
    # Perform n episodes/iterations of Q-learning
    printQ("Episod 0", Q)
    for i in range(n//2):
        Q= learnEpisode(states, actions, simulator, epsilon, learning_rate, Q)
    printQ("Episod "+ str(n//2), Q)
    for i in range(n//2, n):
        Q= learnEpisode(states, actions, simulator, epsilon, learning_rate, Q)

    return Q

def learnEpisode(states, actions, simulator, epsilon, learning_rate, Q):
    state= states[0] #set cursor to initial state
    s_terminal= states[len(states)-1]
    
    while state != s_terminal :
        if random.random() <= epsilon :
            action= random.choice(actions)
        else :
            action= argmax( Q[state] )
        next_state, reward= simulator(state, action)    
        # update rule for Q-learning
        Q[state][action]+= learning_rate * ( reward + max(Q[next_state].values()) - Q[state][action] )
        # move to next state
        state= next_state
    return Q

def argmax(dico) :
    # return the dico key wchich are the higest associated value.
    return  max( dico, key= dico.get )

def simulateGrid(state, action) :
  # Calculate next state (according to sample grid with wall)
  # Default: remain in a state if action tries to leave grid
  next_state= state
  if (state == "s0" and action == "down") :
    next_state= "s1"
  elif (state == "s1" and action == "up") :
    next_state= "s0"
  elif (state == "s1" and action == "right") :
    next_state= "s2"
  if (state == "s2" and action == "left") :
    next_state= "s1"
  if (state == "s2" and action == "up") :
    next_state= "s3"
  if (state == "s3" and action == "down") : 
    next_state= "s2"

  # Calculate reward
  if (next_state == "s3") :
    reward= 10
  else:
    reward= -1
  return next_state, reward


if __name__ == "__main__":
    # execute only if run as a script
    main()
