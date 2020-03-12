# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:19:39 2017

@author: Aidar Yessembayev
"""
import random
import math
import copy

def minForMon(listin):
    minVal = 10000
    index = 0
    
    for i in listin:
        if listin[i].get("smell") < minVal:
            minVal = listin[i].get("smell")
            index = i
                        
    return index

def addToChildrenSmell(newlist, finalist, seclist, array, power):
    
    doNothing = 0
    for i in range(len(array)):
        if seclist[array[i]] == "wall" or newlist[array[i]].get("smell") > power:
            doNothing = 0
        else:         
            newlist[array[i]].update({"smell": power})
            addToChildrenSmell(newlist, finalist, seclist, finalist[array[i]], power/2)
            
def addToChildrenWind(newlist, finalist, seclist, array, power):
    
    doNothing = 0
    for i in range(len(array)):
        if seclist[array[i]] == "wall" or newlist[array[i]].get("wind") > power:
            doNothing = 0
        else:         
            newlist[array[i]].update({"wind": power})
            addToChildrenWind(newlist, finalist, seclist, finalist[array[i]], power/2)            
            

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
    monster = 1
    
    gold = random.randint(0, N-1)    
    if gold < N-1:
        pit = random.randint(0, N-1-gold)
        if (N-1-gold-pit) > 0:
            wall = random.randint(0, N-1-gold-pit)
       
    
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
    smellDec = 1.0
    windDec = 1.0
    
    clock = 0
    degree = 0
    
    tay = 0.1
    
    newlist = {}
    for i in range(N):
        newlist[i] = {}
    
    for i in range(N):
        newlist[i].update({"wind": 0})
    
    for i in range(N):
        newlist[i].update({"smell": 0})
        
    for i in range(N):
        newlist[i].update({"wumpus": 0})
                
    for i in range(N):
        if seclist[i] == "monster":
            newlist[i].update({"smell": 1})
            newlist[i].update({"wumpus": 1})
            addToChildrenSmell(newlist, finalist, seclist, finalist[i], smellDec/2)
        elif seclist[i] == "pit":
            newlist[i].update({"wind": 1})
            addToChildrenWind(newlist, finalist, seclist, finalist[i], windDec/2)
            
            
    print (newlist)
    print ("")
    
    flag = False
    smelist = copy.deepcopy(newlist)
    
    while True:
        
        for i in range(N):
            if seclist[i] != "wall":
                newlist[i].update({"wind": round(abs(math.cos(degree)), 4)})
        
        for i in range(N):
            if newlist[i].get("wumpus") == 1:
                
                inx = random.randint(0, len(finalist[i]))
                
                if seclist[inx] == "wall" or seclist[inx] == "pit":
                    flag = True
                    print ("Wumpus goes to pit or wall")
                    break
                    
                else:
                    newlist[inx].update({"wumpus": 1})
                    newlist[inx].update({"smell": 1})
                
                    addToChildrenSmell(smelist, finalist, seclist, finalist[i], smellDec/2)
        
        if flag == True:
            break
        
        if clock == 180:
            break
        
        clock = clock + 1
        degree = (clock * math.pi / 180)
            
        print ("")
        print ("Clock is:", clock)
        print (smelist)
        print ("")