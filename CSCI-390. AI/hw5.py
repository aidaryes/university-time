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

def addToChildren(newlist, finalist, seclist, array, power):
    
    for i in range(len(array)):
        if seclist[array[i]] == "wall" or newlist[array[i]].get("smell") > power:
            return
        else:         
            newlist[array[i]].update({"smell": power})
            addToChildren(newlist, finalist, seclist, finalist[array[i]], power/2)
            

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
    clock = 0
    degree = 0
    
    tay = 1
    
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
            addToChildren(newlist, finalist, seclist, finalist[i], tay/2)
        elif seclist[i] == "pit":
            newlist[i].update({"wind": 1})
            
    print (newlist)
    
    flag = False
    
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
                    newlist[i].update({"wumpus": 0})
                    newlist[i].update({"smell": 0})
                    
                    newlist[inx].update({"wumpus": 1})
                    newlist[inx].update({"smell": 1})
                
                    addToChildren(newlist, finalist, seclist, finalist[inx], tay/2)
        
        if flag == True:
            break
        
        if clock == 180:
            break
        
        clock = clock + 1
        degree = (clock * math.pi / 180)
            
        print ("")
        print ("Clock is:", clock)
        print (newlist)
        print ("")
    
    print ("")
    print ("")
    print ("Find 5 different cells with minimal smell:")
    
    listMin = {}
    for i in range(5):
        listMin[i] = {}
    
    addlist = copy.deepcopy(newlist)
    
    for i in range(5):
        listMin[i] = minForMon(addlist)
        addlist[listMin[i]].update({"smell": 10000})
    
    justList = []
    for i in listMin:
        justList.append(listMin[i])
    
    print (justList)
    print ("")
    print ("")
    print ("Coloring by using degree heuristic:")
    
    color = ["b", "r", "g", "w"]
    
    colorlist = {}
    for i in range(N):
        colorlist[i] = {"b": 0, "r": 0, "g": 0, "w": 0}   
    
    maxInd = 0
    index = 0
    si = 0
    ti = 0
    fi = 0    
    
    for i in justList:
        for j in finalist[i]:            
            if len(finalist[j]) > maxInd:
                maxInd = len(finalist[j])
                index = j
                
        colorlist[index].update({"b": 1})
        for i in finalist[index]:
            colorlist[i].update({"b": 0})
            
            
            
        maxInd = 0    
        for j in finalist[i]:
            if j != index:            
                if len(finalist[j]) > maxInd:
                    maxInd = len(finalist[j])
                    si = j
                
        colorlist[si].update({"r": 1})
        for i in finalist[si]:
            colorlist[i].update({"r": 0})
            
            
            
        maxInd = 0    
        for j in finalist[i]: 
            if j != index and j != si:
                if len(finalist[j]) > maxInd:
                    maxInd = len(finalist[j])
                    ti = j
                
        colorlist[ti].update({"g": 1})
        for i in finalist[ti]:
            colorlist[i].update({"g": 0})
            
        
        
        maxInd = 0
        for j in finalist[i]:
            if j != index and j != si and j != ti:          
                if len(finalist[j]) > maxInd:
                    maxInd = len(finalist[j])
                    fi = j
                
        colorlist[fi].update({"w": 1})
        for i in finalist[fi]:
            colorlist[i].update({"w": 0})
            
            
        
        print (colorlist)
        print ("")
        print ("")
        maxInd = 0
        index = 0
        si = 0
        ti = 0
        fi = 0  
        
    #end
    #print (newlist)
    inx = random.randint(0, len(finalist[i]))
    for i in range(N):
        newlist[i].update({"wumpus": 0})
    
    newlist[inx].update({"wumpus": 1})
    newlist[inx].update({"smell": newlist[inx].get("smell")*4})

    addToChildren(newlist, finalist, seclist, finalist[inx], tay/2)
    print (newlist)