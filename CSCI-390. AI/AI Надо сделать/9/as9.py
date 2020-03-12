# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:41:10 2017

@author: Aidar Yessembayev
data taken from Tauyekel Kunzhol
"""
import csv

with open('new.csv', 'r') as file:
    arr = []
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        arr.append(row)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = arr[i][j].split(', ')


onelist = []

for i in range(len(arr)):
    for j in range (len(arr[i])):
        onelist.append(arr[i][j])  

R2list = []
R6list = []

for i in range(len(onelist)):
    if onelist[i][0] == 'R2':
        R2list.append(onelist[i])
    elif onelist[i][0] == 'R6':
        R6list.append(onelist[i])
        
for i in range(len(R2list)):
    R2list[i][1] = float(R2list[i][1])
    R2list[i][2] = float(R2list[i][2])
    R2list[i][3] = int(R2list[i][3])
    R2list[i][4] = int(R2list[i][4])

for i in range(len(R6list)):
    R6list[i][1] = float(R6list[i][1])
    R6list[i][2] = float(R6list[i][2])
    R6list[i][3] = int(R6list[i][3])
    R6list[i][4] = int(R6list[i][4])

R2sorlist = sorted(R2list, key=lambda x: float(x[1]))
R6sorlist = sorted(R6list, key=lambda x: float(x[1]))

#Wind
numOfBucWind = 36

#R2
minWind = float(R2sorlist[0][1])
maxWind = float(R2sorlist[len(R2sorlist)-1][1])

difWind = (maxWind - minWind)/numOfBucWind

for i in range(len(R2sorlist)):
    whichBuc = int((float(R2sorlist[i][1]) - minWind) / difWind)
    if whichBuc != 36:
        R2sorlist[i][1] = whichBuc
    else:
        R2sorlist[i][1] = whichBuc - 1
        
#R6
minWind = float(R6sorlist[0][1])
maxWind = float(R6sorlist[len(R6sorlist)-1][1])

difWind = (maxWind - minWind)/numOfBucWind

for i in range(len(R6sorlist)):
    whichBuc = int((float(R6sorlist[i][1]) - minWind) / difWind)
    if whichBuc != 36:
        R6sorlist[i][1] = whichBuc
    else:
        R6sorlist[i][1] = whichBuc - 1
        
#Smell
R2sorlist = sorted(R2list, key=lambda x: float(x[2]))
R6sorlist = sorted(R6list, key=lambda x: float(x[2]))

numOfBucSmell = 100

#R2
minSmell = float(R2sorlist[0][2])
maxSmell = float(R2sorlist[len(R2sorlist)-1][2])

difSmell = (maxSmell - minSmell)/numOfBucSmell

for i in range(len(R2sorlist)):
    whichBuc = int((float(R2sorlist[i][2]) - minSmell) / difSmell)
    if whichBuc != 100:
        R2sorlist[i][2] = whichBuc
    else:
        R2sorlist[i][2] = whichBuc - 1

#R6
minSmell = float(R6sorlist[0][2])
maxSmell = float(R6sorlist[len(R6sorlist)-1][2])

difSmell = (maxSmell - minSmell)/numOfBucSmell

for i in range(len(R6sorlist)):
    whichBuc = int((float(R6sorlist[i][2]) - minSmell) / difSmell)
    if whichBuc != 100:
        R6sorlist[i][2] = whichBuc
    else:
        R6sorlist[i][2] = whichBuc - 1
        
#Print
R2sorlist = sorted(R2list, key=lambda x: float(x[1]))
R6sorlist = sorted(R6list, key=lambda x: float(x[1]))

#print ("Sorted list with R2 dividing wind and smell into buckets:")
#print (R2sorlist)
#print ("")
#
#print ("Sorted list with R6 dividing wind and smell into buckets:")
#print (R6sorlist)
#print ("")

#Priors
#Wind
R2windProb = []

count = 0
for i in range(numOfBucWind):
    for j in range(len(R2sorlist)):
        if R2sorlist[j][1] == i:
            count += 1
    R2windProb.append(round((count/len(R2sorlist)), 4))
    count = 0
    

R6windProb = []

count = 0
for i in range(numOfBucWind):
    for j in range(len(R6sorlist)):
        if R6sorlist[j][1] == i:
            count += 1
    R6windProb.append(round((count/len(R6sorlist)), 4))
    count = 0

#Smell
R2smellProb = []

count = 0
for i in range(numOfBucSmell):
    for j in range(len(R2sorlist)):
        if R2sorlist[j][2] == i:
            count += 1
    R2smellProb.append(round((count/len(R2sorlist)), 4))
    count = 0


R6smellProb = []

count = 0
for i in range(numOfBucSmell):
    for j in range(len(R6sorlist)):
        if R6sorlist[j][2] == i:
            count += 1
    R6smellProb.append(round((count/len(R6sorlist)), 4))
    count = 0
    
#Gold
R2goldProb = []

count = 0
for i in range(2):
    for j in range(len(R2sorlist)):
        if R2sorlist[j][3] == i:
            count += 1
    R2goldProb.append(round((count/len(R2sorlist)), 4))
    count = 0
    

R6goldProb = []

count = 0
for i in range(2):
    for j in range(len(R6sorlist)):
        if R6sorlist[j][3] == i:
            count += 1
    R6goldProb.append(round((count/len(R6sorlist)), 4))
    count = 0

#Joint
R2wsgJoint = []

for i in R2windProb:
    for j in R2smellProb:
        for k in R2goldProb:
            R2wsgJoint.append(round((i*j*k), 4))

print("R2 Wind-Smell-Gold Joint")
print(R2wsgJoint)
print("")

R6wsgJoint = []

for i in R6windProb:
    for j in R6smellProb:
        for k in R6goldProb:
            R6wsgJoint.append(round((i*j*k), 4))
            
#print("R6 Wind-Smell-Gold Joint")
#print(R6wsgJoint)
#print("")

ArpgR2_00 = []
ArpgR2_01 = []
ArpgR2_02 = []
ArpgR2_03 = []
ArpgR2_04 = []
ArpgR2_05 = []
ArpgR2_06 = []

for i in R2sorlist:
    if i[4] == 0:
        ArpgR2_00.append(i)
    if i[4] == 1:
        ArpgR2_01.append(i)
    if i[4] == 2:
        ArpgR2_02.append(i)
    if i[4] == 3:
        ArpgR2_03.append(i)
    if i[4] == 4:
        ArpgR2_04.append(i)
    if i[4] == 5:
        ArpgR2_05.append(i)
    if i[4] == 6:
        ArpgR2_06.append(i)

ArpgR6_00 = []
ArpgR6_01 = []
ArpgR6_02 = []
ArpgR6_03 = []
ArpgR6_04 = []
ArpgR6_05 = []
ArpgR6_06 = []

for i in R6sorlist:
    if i[4] == 0:
        ArpgR6_00.append(i)
    if i[4] == 1:
        ArpgR6_01.append(i)
    if i[4] == 2:
        ArpgR6_02.append(i)
    if i[4] == 3:
        ArpgR6_03.append(i)
    if i[4] == 4:
        ArpgR6_04.append(i)
    if i[4] == 5:
        ArpgR6_05.append(i)
    if i[4] == 6:
        ArpgR6_06.append(i)

#0
R2final = []
countArpgR2_00 = 0

for i in ArpgR2_00:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_00 += R2wsgJoint[number]
    
print("Prob. for R2 act. 0:")
print(round(countArpgR2_00, 4))
print("")

R2final.append(round(countArpgR2_00, 4))
    
#1
countArpgR2_01 = 0

for i in ArpgR2_01:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_01 += R2wsgJoint[number]
    
print("Prob. for R2 act. 1:")
print(round(countArpgR2_01, 4))
print("")

R2final.append(round(countArpgR2_01, 4))

#2
countArpgR2_02 = 0

for i in ArpgR2_02:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_02 += R2wsgJoint[number]
    
print("Prob. for R2 act. 2:")
print(round(countArpgR2_02, 4))
print("")

R2final.append(round(countArpgR2_02, 4))  

#3
countArpgR2_03 = 0

for i in ArpgR2_03:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_03 += R2wsgJoint[number]
    
print("Prob. for R2 act. 3:")
print(round(countArpgR2_03, 4))
print("")

R2final.append(round(countArpgR2_03, 4))

#4
countArpgR2_04 = 0

for i in ArpgR2_04:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_04 += R2wsgJoint[number]
    
print("Prob. for R2 act. 4:")
print(round(countArpgR2_04, 4))
print("")

R2final.append(round(countArpgR2_04, 4))

#5
countArpgR2_05 = 0

for i in ArpgR2_05:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_05 += R2wsgJoint[number]
    
print("Prob. for R2 act. 5:")
print(round(countArpgR2_05, 4))
print("")

R2final.append(round(countArpgR2_05, 4))

#6
countArpgR2_06 = 0

for i in ArpgR2_06:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR2_06 += R2wsgJoint[number]
    
print("Prob. for R2 act. 6:")
print(round(countArpgR2_06, 4))
print("")

R2final.append(round(countArpgR2_06, 4))

#0
R6final = []
countArpgR6_00 = 0

for i in ArpgR6_00:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_00 += R6wsgJoint[number]
    
print("Prob. for R6 act. 0:")
print(round(countArpgR6_00, 4))
print("")

R6final.append(round(countArpgR6_00, 4))
    
#1
countArpgR6_01 = 0

for i in ArpgR6_01:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_01 += R6wsgJoint[number]
    
print("Prob. for R6 act. 1:")
print(round(countArpgR6_01, 4))
print("")

R6final.append(round(countArpgR6_01, 4))

#2
countArpgR6_02 = 0

for i in ArpgR6_02:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_02 += R6wsgJoint[number]
    
print("Prob. for R6 act. 2:")
print(round(countArpgR6_02, 4))
print("")

R6final.append(round(countArpgR6_02, 4))  

#3
countArpgR6_03 = 0

for i in ArpgR6_03:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_03 += R6wsgJoint[number]
    
print("Prob. for R6 act. 3:")
print(round(countArpgR6_03, 4))
print("")

R6final.append(round(countArpgR6_03, 4))

#4
countArpgR6_04 = 0

for i in ArpgR6_04:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_04 += R6wsgJoint[number]
    
print("Prob. for R6 act. 4:")
print(round(countArpgR6_04, 4))
print("")

R6final.append(round(countArpgR6_04, 4))

#5
countArpgR6_05 = 0

for i in ArpgR6_05:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_05 += R6wsgJoint[number]
    
print("Prob. for R6 act. 5:")
print(round(countArpgR6_05, 4))
print("")

R6final.append(round(countArpgR6_05, 4))

#6
countArpgR6_06 = 0

for i in ArpgR6_06:
    number = i[1]*100*2 + i[2]*2 + i[3]*2
    countArpgR6_06 += R6wsgJoint[number]
    
print("Prob. for R6 act. 6:")
print(round(countArpgR6_06, 4))
print("")

R6final.append(round(countArpgR6_06, 4))

print("ARPG for R2 final list:")
print(R2final)
print("")

print("ARPG for R6 final list:")
print(R6final)
print("")
