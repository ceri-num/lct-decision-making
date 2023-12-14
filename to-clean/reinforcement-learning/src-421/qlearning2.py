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
    sEnd= "s3"

    Qlearning( simulateGrid, s0, sEnd, actions)

def Qlearning(simulate, s0, isEnd, actions,
              epsilon= 0.1, learning_rate= 0.1, episode= 1000, horizon= 1000 ):
    # Initialize state-action matrice Q to zero
    Q= { s0 : { a:0.0 for a in actions } }
    printQ("Episod 0", Q)
    
    # Perform n episodes/iterations of Q-learning
    for i in range(episode):
        Q= learnEpisode(simulate, s0, isEnd, actions, epsilon, learning_rate, horizon, Q)
    
    printQ("Episod "+ str(episode), Q)
    return Q

def learnEpisode(simulate, s0, isEnd, actions, epsilon, learning_rate, horizon, Q):
    state= s0 #set cursor to initial state
    h= 0;
    while isEnd(state) and h < horizon :
        if random.random() <= epsilon :
            action= random.choice( actions )
        else :
            action= argmax( Q[state] )
        next_state, reward= simulate(state, action)    
        h+= 1

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
    print( "\n".join( [ state + ": "+ str_Qline( Q[state] ) for state in Q ] ) )
    print( "best actions:\n\t"+ str({ state: argmax(Q[state]) for state in Q }) )

def str_Qline( values ):
    return ", ".join( [ action+": "+ str(round( values[action], 2 )) for action in values ] )
