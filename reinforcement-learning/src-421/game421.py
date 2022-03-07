# -*- coding: utf-8 -*-
"""
Script MDP 421 
"""
import random

def main() :

    print("\nSimple 421 implementation")

    print( game421.stateSpace421() )
    print( len(game421.stateSpace421()) )

    print("\nSimple 421 implementation (Contimious)")

    state= "6-2-2"
    action= "roll-keep-roll" #pi421(state) # 
    deep= 10000
    
    reachable, rewards= test( simulateContinous421, state, action, deep)

    print("\nTransitions: from "+ state +" by doing "+ action + " ("+ str(len(reachable)) +")" )
    print('\n'.join( [key+': '+ str(reachable[key]/100) + "\t: "+ str(rewards[key])
                            for key in reachable ]  ) )

    print("\nSimple 421 implementation (sequential)")

    state= "6-2-2"
    action= "keep-keep-keep" #pi421(state) # 
    deep= 10000
    
    reachable, rewards= test( simulateSequential421, state, action, deep)

    print("\nTransitions: from "+ state +" by doing "+ action + " ("+ str(len(reachable)) +")" )
    print('\n'.join( [key+': '+ str(reachable[key]/100) + "\t: "+ str(rewards[key])
                            for key in reachable ]  ) )

    state= "6-2-2"
    action= "keep-roll-roll" #pi421(state) # 
    deep= 10000
    
    reachable, rewards= test( simulateSequential421, state, action, deep)

    print("\nTransitions: from "+ state +" by doing "+ action + " ("+ str(len(reachable)) +")" )
    print('\n'.join( [key+': '+ str(reachable[key]/100) + "\t: "+ str(rewards[key])
                            for key in reachable ]  ) )

def simulateContinous421(state_str, act_str):
    state= [ int(x_str) for x_str in state_str.split("-") ]
    new_state= randomTransition421(state, act_str.split("-"))
    reward= score(new_state) - score(state)
    return str(new_state[0]) + '-'+ str(new_state[1]) + '-'+ str(new_state[2]), reward

def simulateSequential421(state_str, act_str):
    state= [ int(x_str) for x_str in state_str.split("-") ]
    if act_str == "keep-keep-keep" :
        reward= score(state)
        new_state= randomTransition421(state, "roll-roll-roll".split("-"))
    else:
        reward= 0
        new_state= randomTransition421(state, act_str.split("-"))
    return '-'.join( [str(x) for x in new_state] ), reward

def randomTransition421(state, act):
    new_state= []
    for die, act in zip(state, act) :
        if act == "roll" or act == "r" :
            new_state.append( random.choice( range(1,7) ) )
        else :
            new_state.append(die)
    new_state.sort(reverse=True)
    return new_state

def score(s):
    if s[0] == 4 and s[1] == 2 and s[2] == 1 : 
        return 800
    
    if s[0] == 1 and s[1] == 1 and s[2] == 1 : 
        return 700
    
    if s[1] == 1 and s[2] == 1 : 
        return 400 + s[0]
    
    if s[1] == s[0] and s[2] == s[0] : 
        return 300 + s[0]
    
    if s[1] == s[0]-1 and s[2] == s[0]-2 : 
        return 200 + s[0]
    
    if s[0] == 2 and s[1] == 2 and s[2] == 1 : 
        return 0
    
    return 100 + s[0]

def noEnd421(state):
    return False

def stateSpace421():
    space= []
    for i1 in range(1, 7) :
        for i2 in range(1, i1+1) :
            for i3 in range(1, i2+1) :
                space.append( str(i1)+'-'+str(i2)+'-'+str(i3) )
    return space

def test(simulator, state, action, deep):
    reachable= {}
    rewards= {}
    for i in range(deep) :
        new_state, reward= simulator(state, action)
        if new_state in list(reachable.keys()) :
            reachable[new_state]+= 1
        else :
            reachable[new_state]= 1
            rewards[new_state]= reward
    return reachable, rewards

if __name__ == "__main__":
    # execute only if run as a script
    main()