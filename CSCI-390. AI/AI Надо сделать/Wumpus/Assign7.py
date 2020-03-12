# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:19:30 2017

@author: Aidar Yessembayev
data taken from Tauyekel Kunzhol
"""
import csv
import copy

def findLast (arg):
    last = 0
    for i in range(len(arg)):
        last = i
    return last

with open('output.csv', 'r') as file:
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

somelist = copy.deepcopy(onelist)    


sorlist = []  
sorlist = sorted(onelist, key=lambda x: x[1])

numOfBuc = 36
numIter = int(len(onelist) / numOfBuc)
remai = len(onelist) - numIter*numOfBuc

k = 0
for i in range(numOfBuc):
    for j in range(numIter):
        sorlist[k][1] = str(i)
        k += 1
        
for i in range(remai):
    sorlist[k][1] = str(numOfBuc-1)
    k += 1

#Fifth task
print ("Sorted list with dividing wind into buckets:")
print (sorlist)
print ("")

#Sixth task
newStr = []

for i in range(len(sorlist)):
    for j in range(len(sorlist)):
        if i != j and sorlist[j][1] == sorlist[i][1] and sorlist[j][2] == sorlist[i][2] \
                                                     and sorlist[j][3] == sorlist[i][3]:
            newStr.append(sorlist[i])

rpGroup = []
found = 0

for i in newStr:
    for j in rpGroup:
        if i == j:
            found = 1
    if found == 0:
        rpGroup.append(i)
    found = 0

print ("PG grouped:")
print (rpGroup)
print ("")

rpgR2 = []
rpgR6 = []

for i in rpGroup:
    if i[0] == 'R2':
        rpgR2.append(i)
    elif i[0] == 'R6':
        rpgR6.append(i)

print ("RPG for room with 2 tunnels:")        
print (rpgR2)
print ("")

print ("RPG for room with 6 tunnels:")        
print (rpgR6)
print ("")

ArpgR2_00 = []
ArpgR2_01 = []
ArpgR2_02 = []
ArpgR2_03 = []
ArpgR2_04 = []
ArpgR2_05 = []
ArpgR2_06 = []

for i in rpgR2:
    if i[4] == '0':
        ArpgR2_00.append(i)
    if i[4] == '1':
        ArpgR2_01.append(i)
    if i[4] == '2':
        ArpgR2_02.append(i)
    if i[4] == '3':
        ArpgR2_03.append(i)
    if i[4] == '4':
        ArpgR2_04.append(i)
    if i[4] == '5':
        ArpgR2_05.append(i)
    if i[4] == '6':
        ArpgR2_06.append(i)

ArpgR6_00 = []
ArpgR6_01 = []
ArpgR6_02 = []
ArpgR6_03 = []
ArpgR6_04 = []
ArpgR6_05 = []
ArpgR6_06 = []

for i in rpgR6:
    if i[4] == '0':
        ArpgR6_00.append(i)
    if i[4] == '1':
        ArpgR6_01.append(i)
    if i[4] == '2':
        ArpgR6_02.append(i)
    if i[4] == '3':
        ArpgR6_03.append(i)
    if i[4] == '4':
        ArpgR6_04.append(i)
    if i[4] == '5':
        ArpgR6_05.append(i)
    if i[4] == '6':
        ArpgR6_06.append(i)
        
#Ninth task
count = 0
ArpgR2_00_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_00)):
            if ArpgR2_00[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_00)
                ArpgR2_00_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_00_Arr) for i in ArpgR2_00_Arr]
print ("Arpg for Room with 2 tun. and act. 0: ")
print (norm)
print ("")

count = 0
ArpgR2_01_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_01)):
            if ArpgR2_01[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_01)
                ArpgR2_01_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_01_Arr) for i in ArpgR2_01_Arr]
print ("Arpg for Room with 2 tun. and act. 1: ")
print (norm)
print ("")

count = 0
ArpgR2_02_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_02)):
            if ArpgR2_02[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_02)
                ArpgR2_02_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_02_Arr) for i in ArpgR2_02_Arr]
print ("Arpg for Room with 2 tun. and act. 2: ")
print (norm)
print ("")

count = 0
ArpgR2_03_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_03)):
            if ArpgR2_03[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_03)
                ArpgR2_03_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_03_Arr) for i in ArpgR2_03_Arr]
print ("Arpg for Room with 2 tun. and act. 3: ")
print (norm)
print ("")

count = 0
ArpgR2_04_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_04)):
            if ArpgR2_04[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_04)
                ArpgR2_04_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_04_Arr) for i in ArpgR2_04_Arr]
print ("Arpg for Room with 2 tun. and act. 4: ")
print (norm)
print ("")

count = 0
ArpgR2_05_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_05)):
            if ArpgR2_05[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_05)
                ArpgR2_05_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_05_Arr) for i in ArpgR2_05_Arr]
print ("Arpg for Room with 2 tun. and act. 5: ")
print (norm)
print ("")

count = 0
ArpgR2_06_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_06)):
            if ArpgR2_06[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR2_06)
                ArpgR2_06_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR2_06_Arr) for i in ArpgR2_06_Arr]
print ("Arpg for Room with 2 tun. and act. 6: ")
print (norm)
print ("")
print ("")


count = 0
ArpgR6_00_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_00)):
            if ArpgR6_00[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_00)
                ArpgR6_00_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_00_Arr) for i in ArpgR6_00_Arr]
print ("Arpg for Room with 6 tun. and act. 0: ")
print (norm)
print ("")

count = 0
ArpgR6_01_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_01)):
            if ArpgR6_01[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_01)
                ArpgR6_01_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_01_Arr) for i in ArpgR6_01_Arr]
print ("Arpg for Room with 6 tun. and act. 1: ")
print (norm)
print ("")

count = 0
ArpgR6_02_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_02)):
            if ArpgR6_02[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_02)
                ArpgR6_02_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_02_Arr) for i in ArpgR6_02_Arr]
print ("Arpg for Room with 6 tun. and act. 2: ")
print (norm)
print ("")

count = 0
ArpgR6_03_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_03)):
            if ArpgR6_03[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_03)
                ArpgR6_03_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_03_Arr) for i in ArpgR6_03_Arr]
print ("Arpg for Room with 6 tun. and act. 3: ")
print (norm)
print ("")

count = 0
ArpgR6_04_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_04)):
            if ArpgR6_04[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_04)
                ArpgR6_04_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_04_Arr) for i in ArpgR6_04_Arr]
print ("Arpg for Room with 6 tun. and act. 4: ")
print (norm)
print ("")

count = 0
ArpgR6_05_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_05)):
            if ArpgR6_05[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_05)
                ArpgR6_05_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_05_Arr) for i in ArpgR6_05_Arr]
print ("Arpg for Room with 6 tun. and act. 5: ")
print (norm)
print ("")

count = 0
ArpgR6_06_Arr = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_06)):
            if ArpgR6_06[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count = 1
                else:
                    count = -1/(last - j + 1)
                    
                count = count/len(ArpgR6_06)
                ArpgR6_06_Arr.append(count)
                count = 0

norm = [float(i)/sum(ArpgR6_06_Arr) for i in ArpgR6_06_Arr]
print ("Arpg for Room with 6 tun. and act. 6: ")
print (norm)
print ("")