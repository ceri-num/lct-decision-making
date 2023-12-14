#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created the 03/11/20

@author: guillaume 
"""
import game421

def main():
    state= "4-2-1"
    deep= 100

    for x in range(deep) :
        action= pi421(state)
        print( state + ' ('+ str( game421.score( [ int(x) for x in state.split('-') ] ) ) +'): ' + action  )
        state, reward= game421.simulateSequential421( state, action )
        print('    > ' + str(reward) )

def pi421(s_str):
    s= [int(s_str[0:1]), int(s_str[2:3]), int(s_str[4:5])]
    action= ["roll", "roll", "roll"]
    
    for d in [4,2,1]:
        if d in s :
            action[ s.index(d) ]= "keep"

    return "-".join(action)

if __name__ == "__main__":
    # execute only if run as a script
    main()
