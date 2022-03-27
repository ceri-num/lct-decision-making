#!env python3
"""
# Ploting element from stat:
"""
import sys, os, random, json
import matplotlib.pyplot as plt

# Parameters:
colors= {'game421-DecTreeQ': 'b', 'game421-FullQ':'r'}
valueY= [i*500 for i in range(201)]

# variables:
allStats= {}

for name in colors :
    f= open( name+'-stats.json', 'r' )
    stats= json.loads( f.read() )
    f.close()
    for feature in stats :
        if feature not in allStats.keys() :
            allStats[feature]= {}
        allStats[feature][name]= stats[feature]

for feature in allStats :
    for name in colors :
        plt.plot(valueY, allStats[feature][name], color=colors[name], label=name)
    plt.title( feature )
    plt.legend()
    plt.show()
