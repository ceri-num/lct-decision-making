#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:56:02 2020

@author: guillaume 
"""

import random
import qlearning2 as ql

def main() :
    print("Simple Q-Learning")
    actions= ["keep-keep-keep", "keep-keep-roll", "keep-roll-keep", "keep-roll-roll",
             "roll-keep-keep", "roll-keep-roll", "roll-roll-keep", "roll-roll-roll"]

    ql.Qlearning(simulate421, "2-2-1", "4-2-1", actions,
                 episode= 10000, horizon= 3)

def simulate421(s_str, a):
    dice= [int(s_str[0:1]), int(s_str[2:3]), int(s_str[4:5])]
    new_dice= []
    for die, act in zip(dice, a.split("-")) :
        if act == "roll" :
            new_dice.append( random.choice( range(1,7) ) )
        else :
            new_dice.append(die)
    new_dice.sort(reverse=True)
    reward= score(new_dice) - score(dice)
    return str(new_dice[0]) +'-'+ str(new_dice[1]) +'-'+ str(new_dice[2]), reward

def score(s):
    if s[0] == 4 and s[1] == 2 and s[2] == 1 : 
        return 800
    
    elif s[0] == 1 and s[1] == 1 and s[2] == 1 : 
        return 700
    
    elif s[1] == 1 and s[2] == 1 : 
        return 400 + s[0]
    
    elif s[1] == s[0] and s[2] == s[0] : 
        return 300 + s[0]
    
    elif s[1] == s[0]-1 and s[2] == s[0]-2 : 
        return 200 + s[0]
    
    elif s[0] == 2 and s[1] == 2 and s[2] == 1 : 
        return 0
    
    else:
        return 100 + s[0] - 0.1

if __name__ == "__main__":
    # execute only if run as a script
    main()

