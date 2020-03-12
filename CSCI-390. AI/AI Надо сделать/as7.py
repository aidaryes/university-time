# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:00:03 2017

@author: Aidar Yessembayev
"""

import random
import math

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

N = 60
K = 18
S = 2
P = 4

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
          
print (finalist)
#end

print ("")
print ("")

#Second Task
wall = 3
pit = 5
gold = 3
monster = 3

allvar = {"wall":wall, "pit":pit, "gold":gold, "monster":monster}

total = wall + pit + gold + monster

seclist = {}
for i in range(N):
    seclist[i] = []

randval = 0    
i = 0
while i != total:
    if allvar["wall"] > 0:
        randval = random.randint(0, N)
        if seclist[randval] == []:
            i += 1
            seclist[randval] = "wall"
            allvar["wall"] = allvar["wall"] - 1
    
    elif allvar["gold"] > 0:
        randval = random.randint(0, N)
        if seclist[randval] == []:
            i += 1
            seclist[randval] = "gold"
            allvar["gold"] = allvar["gold"] - 1
        
    elif allvar["pit"] > 0:
        randval = random.randint(0, N)
        if seclist[randval] == []:
            i += 1
            seclist[randval] = "pit"
            allvar["pit"] = allvar["pit"] - 1
        
    elif allvar["monster"] > 0:
        randval = random.randint(0, N)
        if seclist[randval] == []:
            i += 1
            seclist[randval] = "monster"
            allvar["monster"] = allvar["monster"] - 1

print (seclist)           
#end

print ("")
print ("")

#Third task
clock = 0
degree = 0

tay = 1.0

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
    newlist[i].update({"agent": 0})
            
ranvalue = random.randint(0, N)
newFlag = 0

if seclist[ranvalue] == "monster" or seclist[ranvalue] == "pit":
    print ("Game is over before start")
    newFlag = 1
else:
    newlist[ranvalue].update({"agent": 1})

if newFlag != 1:
    for i in range(N):
        if seclist[i] == "monster":
            newlist[i].update({"smell": 1})
            newlist[i].update({"wumpus": 1})
            addToChildren(newlist, finalist, seclist, finalist[i], tay/2)
        elif seclist[i] == "pit":
            newlist[i].update({"wind": 1})
            
    print (newlist)
    
    doNothing = 0
    left = [2]
    right = [2]
    flagToStop = 0
    
    while True:
        
        for i in range(N):
            if seclist[i] != "wall":
                newlist[i].update({"wind": round(abs(math.cos(degree)), 4)})
        
        for i in range(N):
            if newlist[i].get("wumpus") == 1:
                
                inx = random.randint(0, len(finalist[i]))
                
                if seclist[inx] == "pit":
                    newlist[i].update({"wumpus": 0})
                    newlist[i].update({"smell": 0})
                    print ("The wumpus died")
                    
                elif newlist[inx].get("wumpus") == 1:
                    doNothing = 1
                    
                else:
                    newlist[i].update({"wumpus": 0})
                    newlist[i].update({"smell": 0})
                    
                    newlist[inx].update({"wumpus": 1})
                    newlist[inx].update({"smell": 1})
                
                    addToChildren(newlist, finalist, seclist, finalist[inx], tay/2)
        

            
        print ("")
        print ("Clock is:", clock)
        
        for i in range(N):
            if newlist[i].get("agent") == 1:
                
                howMany = len(finalist[i])
                if howMany == 2:
                    left.append(finalist[i][0])
                    right.append(finalist[i][1])
                else:
                    left.append(finalist[i][0])
                    left.append(finalist[i][1])
                    right.append(finalist[i][2])
                    right.append(finalist[i][3])
                    
                whereToGo = random.randint(0, 1)
                if whereToGo == 0:
                    print ("The agent goes left")
                    whichCell = random.randint(0, len(left)-1)
                    
                    newlist[i].update({"agent": 0})
                    newlist[left[whichCell]].update({"agent": 1})
                    
                else:
                    print ("The agent goes right")
                    whichCell = random.randint(0, len(right)-1)
                    
                    newlist[i].update({"agent": 0})
                    newlist[right[whichCell]].update({"agent": 1})
                    
                left = []
                right = []
                break
            
        print (newlist) 
           
        for i in range(N):
            if newlist[i].get("agent") == 1:
                if newlist[i].get("wumpus") == 1:
                    print("Game is over, agent was killed by monster")
                    flagToStop = 1
                    break
                elif seclist[i] == "pit":
                    print("Game is over, the agent fell into a pit")
                    flagToStop = 1
                    break
                elif seclist[i] == "gold":
                    print("The agent found a gold")
                    flagToStop = 1
                    break
        if flagToStop == 1:
            break
        
        if clock == 10000:
            break

        clock = clock + 1
        degree = (clock * math.pi / 180)        

        
        print ("")


#end
#print (newlist)


##Third task
#clock = 0
#degree = 0
#
#tay = 0.5
#
#newlist = {}
#for i in range(N):
#    newlist[i] = {}
#
#for i in range(N):
#    newlist[i].update({"wind": 0})
#
#for i in range(N):
#    newlist[i].update({"smell": 0})
#            
#for i in range(N):
#    if seclist[i] == "monster":
#        newlist[i].update({"smell": 1})
#        addToChildren(newlist, finalist, seclist, finalist[i], tay/2)
#    elif seclist[i] == "pit":
#        newlist[i].update({"wind": 1})
#        
#print (newlist)
#
#flag = False
#doNothing = 0
#
#while True:
#    
#    for i in range(N):
#        if seclist[i] != "wall":
#            newlist[i].update({"wind": round(abs(math.cos(degree)), 4)})
#    
#    for i in range(N):
#        if seclist[i] == "monster":
#            
#            inx = random.randint(0, len(finalist[i]))
#            
#            if seclist[inx] == "pit":
#                seclist[i] = []
#                print ("The monster was killed")
#                
#            elif seclist[inx] == "monster":
#                doNothing = 1
#                
#            else:
#
#                newlist[i].update({"smell": 0})
#                
#                newlist[inx].update({"wumpus": 1})
#                newlist[inx].update({"smell": 1})
#            
#                addToChildren(newlist, finalist, seclist, finalist[inx], tay/2)
#    
#    if flag == True:
#        break
#    
#    if clock == 180:
#        break
#    
#    clock = clock + 1
#    degree = (clock * math.pi / 180)
#        
#    print ("")
#    print ("Clock is:", clock)
#    print (newlist)
#    print ("")
#
#print ("")
#print ("")
#print ("Find 5 different cells with minimal smell:")
#
#listMin = {}
#for i in range(5):
#    listMin[i] = {}
#
#addlist = copy.deepcopy(newlist)
#
#for i in range(5):
#    listMin[i] = minForMon(addlist)
#    addlist[listMin[i]].update({"smell": 10000})
#
#justList = []
#for i in listMin:
#    justList.append(listMin[i])
#
#print (justList)
#print ("")
#print ("")
#print ("Coloring by using degree heuristic:")
#
#color = ["b", "r", "g", "w"]
#
#colorlist = {}
#for i in range(N):
#    colorlist[i] = {"b": 0, "r": 0, "g": 0, "w": 0}   
#
#maxInd = 0
#index = 0
#si = 0
#ti = 0
#fi = 0    
#
#for i in justList:
#    for j in finalist[i]:            
#        if len(finalist[j]) > maxInd:
#            maxInd = len(finalist[j])
#            index = j
#            
#    colorlist[index].update({"b": 1})
#    for i in finalist[index]:
#        colorlist[i].update({"b": 0})
#        
#        
#        
#    maxInd = 0    
#    for j in finalist[i]:
#        if j != index:            
#            if len(finalist[j]) > maxInd:
#                maxInd = len(finalist[j])
#                si = j
#            
#    colorlist[si].update({"r": 1})
#    for i in finalist[si]:
#        colorlist[i].update({"r": 0})
#        
#        
#        
#    maxInd = 0    
#    for j in finalist[i]: 
#        if j != index and j != si:
#            if len(finalist[j]) > maxInd:
#                maxInd = len(finalist[j])
#                ti = j
#            
#    colorlist[ti].update({"g": 1})
#    for i in finalist[ti]:
#        colorlist[i].update({"g": 0})
#        
#    
#    
#    maxInd = 0
#    for j in finalist[i]:
#        if j != index and j != si and j != ti:          
#            if len(finalist[j]) > maxInd:
#                maxInd = len(finalist[j])
#                fi = j
#            
#    colorlist[fi].update({"w": 1})
#    for i in finalist[fi]:
#        colorlist[i].update({"w": 0})
#        
#        
#    
#    print (colorlist)
#    print ("")
#    print ("")
#    maxInd = 0
#    index = 0
#    si = 0
#    ti = 0
#    fi = 0  
#    
##end
##print (newlist)
#inx = random.randint(0, len(finalist[i]))
#for i in range(N):
#    newlist[i].update({"wumpus": 0})
#
#newlist[inx].update({"wumpus": 1})
#newlist[inx].update({"smell": newlist[inx].get("smell")*4})
#
#addToChildren(newlist, finalist, seclist, finalist[inx], tay/2)
#print (newlist)