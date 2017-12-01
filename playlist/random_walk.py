import pandas as pd
import numpy as np
import random

#This is the file where the random walk is made. Main part to mess with is weightedChoice
#Need only use randomWalk


#Gives a random walk over k steps. Will not repeat the last r responses.
#Array needs to be n*n and r<n.
def randomWalk(weightArray, startIndex=0, k=100, r=0):
    walkPath = np.zeros((k,), dtype=np.int)
    walkPath[0] = startIndex
    for i  in range(1,k):
        walkWeights = weightArray[int(walkPath[i-1])]
        #Remove last r songs
        for j in range(max(i-r,0),i):
            walkWeights[walkPath[j]] = 0
        walkPath[i] = weightedChoice(walkWeights)
    return walkPath


#Defines a choce function given weights. TODO make more varied weight functions
def weightedChoice(weights):
    totalWeight = np.sum(weights)
    if totalWeight == 0:
        return random.randint(0,len(weights))
    #Subtract the weight from choice at each step and return the song it gets below 0 at
    choice = random.random() * totalWeight
    for i in range(len(weights)):
        choice -= weights[i]
        if choice <= 0:
            return i
    return len(weights) - 1
