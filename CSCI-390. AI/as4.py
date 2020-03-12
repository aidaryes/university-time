# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:19:39 2017

@author: Aidar Yessembayev
"""
import random

def findMin(listin):
    minVal = 10000
    index = 0
    
    for i in listin:
        if listin[i] < minVal:
            if listin[i] != 0:
                minVal = listin[i]
                index = i
                
    if minVal == 10000:
        return minVal
        
    return index

def findMax(listin):
    maxVal = -10000
    index = 0
    
    for i in listin:
        if listin[i] > maxVal:
            if listin[i] != 0 and i != findMin(listin):
                maxVal = listin[i]
                index = i
            
    if maxVal == -10000:
        return maxVal
    
    return index

def addToChildren(finallist, array, chlist, parlist, string, decay):
    
    for i in range(len(array)):
        if parlist[array[i]] == "wall":
            finallist[array[i]].update({})
            
        else:
            finallist[array[i]].update({string: decay})
            #for each in array
            #finallist = addToChildren(finallist, chlist[array[i]], chlist, parlist, string, decay/2)
        
    return finallist

N = int(input("Number of node N: "))
K = int(input("Number of border nodes K: "))
S = int(input("Number of edges of the K border nodes k: "))
P = int(input("P edges: "))

zeroCheck = True
firstCheck = True
secCheck = True

if N < K:
    print("Number of nodes can not be less than the Number of border nodes")
    zeroCheck = False

if S <= 2:
    print("Number of edges of the K border nodes have to be greater than 2")
    firstCheck = False
    
arithmetic = ((N - K)*P + K*S)/2
intarithmetic = int(arithmetic)

if arithmetic != intarithmetic:
    print("Prof Tyler's formula gives an error")
    secCheck = False
    
if zeroCheck == False or firstCheck == False or secCheck == False:
    print("There is a mistake, please restart the program")
else:
    
    #array creation
    array = []
    for i in range(N):
        array.append(i)
    #end    
    
    #list creation
    listcr = {}
    for i in range(N):
        listcr[i] = []

    F = N - K
    for i in range(F):
        listcr[i] = P    
    
    for i in range(F, N):
        listcr[i] = S
        
    #end
    
    #finalist creation
    finalist = {}
    for i in range(N):
        finalist[i] = []
        
    #end
    
    print ("")
    print ("")
    
    #First Task
    while(True):
        minim = findMin(listcr)
        maxim = findMax(listcr)
        
        if minim == 10000 or maxim == -10000:
            break
        
        if minim == maxim:
            print ("There is a mistake, we can not connect node with itself")
            
        finalist[minim].append(maxim)
        finalist[maxim].append(minim)
        
        listcr[minim] = listcr[minim] - 1
        listcr[maxim] = listcr[maxim] - 1
              
    print (listcr)
    print (finalist)
    #end
    
    print ("")
    print ("")
    
    #Second Task
    wall = 0
    pit = 0
    gold = 0
    monster = 0
    
    wall = random.randint(0, N)
    
    if wall < N:
        pit = random.randint(0, N-wall)
        if (N-wall-pit) > 0:
            gold = random.randint(0, N-wall-pit)
            if (N-wall-pit-gold) > 0:
                monster = random.randint(0, N-wall-pit-gold)
       
    
    allvar = {"wall":wall, "pit":pit, "gold":gold, "monster":monster}
    print (allvar)
    
    arrall = ["wall", "pit", "gold", "moster"]
    
    total = wall + pit + gold + monster
    
    seclist = {}
    for i in range(N):
        seclist[i] = []
    
    for i in range(total):
        if allvar["wall"] > 0:
            seclist[i] = "wall"
            allvar["wall"] = allvar["wall"] - 1
            
        elif allvar["pit"] > 0:
            seclist[i] = "pit"
            allvar["pit"] = allvar["pit"] - 1
            
        elif allvar["gold"] > 0:
            seclist[i] = "gold"
            allvar["gold"] = allvar["gold"] - 1
            
        elif allvar["monster"] > 0:
            seclist[i] = "monster"
            allvar["monster"] = allvar["monster"] - 1
            
    print (seclist)
                
    #end
    
    print ("")
    print ("")

    #Third task
    chlist = finalist
    parlist = seclist    
    
    newlist = {}
    for i in range(N):
        newlist[i] = {}
        
    decay = 1
        
    for i in range(N):
        if parlist[i] == "monster":
            
            newlist = addToChildren(newlist, chlist[i], chlist, parlist, "smell", decay/2)
            newlist[i] = {"smell": decay}
            
        elif parlist[i] == "pit":
            
            newlist = addToChildren(newlist, chlist[i], chlist, parlist, "wind", decay/2)
            newlist[i] = {"wind": decay}

    print (newlist)
    
    

    
    
    
