# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:37:52 2017

@author: Aidar Yessembayev
data taken from Tauyekel Kunzhol
"""

from sklearn.neural_network import MLPClassifier
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

print (onelist)
#R2list = []
#R6list = []
#
#for i in range(len(onelist)):
#    if onelist[i][0] == 'R2':
#        R2list.append(onelist[i])
#    elif onelist[i][0] == 'R6':
#        R6list.append(onelist[i])
#        
#for i in range(len(R2list)):
#    R2list[i][1] = float(R2list[i][1])
#    R2list[i][2] = float(R2list[i][2])
#    R2list[i][3] = int(R2list[i][3])
#    R2list[i][4] = int(R2list[i][4])
#
#for i in range(len(R6list)):
#    R6list[i][1] = float(R6list[i][1])
#    R6list[i][2] = float(R6list[i][2])
#    R6list[i][3] = int(R6list[i][3])
#    R6list[i][4] = int(R6list[i][4])
#
#R2sorlist = sorted(R2list, key=lambda x: float(x[1]))
#R6sorlist = sorted(R6list, key=lambda x: float(x[1]))
#
#R2 = []
#R2small = []
#
#for i in range(len(R2sorlist)):
#    R2small.append(R2sorlist[i][1])
#    R2small.append(R2sorlist[i][2])
#    R2small.append(R2sorlist[i][3])
#    R2small.append(R2sorlist[i][4])
#    
#    R2.append(R2small)
#    R2small = []
#    
#R6 = []
#R6small = []
#
#for i in range(len(R6sorlist)):
#    R6small.append(R6sorlist[i][1])
#    R6small.append(R6sorlist[i][2])
#    R6small.append(R6sorlist[i][3])
#    R6small.append(R6sorlist[i][4])
#    
#    R6.append(R6small)
#    R6small = []
#    
#    
#XforR2 = []
#XforR2small = []
#yforR2 = []
#
#for i in range(len(R2)):
#    XforR2small.append(R2[i][0])
#    XforR2small.append(R2[i][1])
#    XforR2small.append(R2[i][2])
#    
#    XforR2.append(XforR2small)
#    XforR2small = []
#    yforR2.append(R2[i][3])
#
#XforR6 = []
#XforR6small = []
#yforR6 = []
#
#for i in range(len(R6)):
#    XforR6small.append(R6[i][0])
#    XforR6small.append(R6[i][1])
#    XforR6small.append(R6[i][2])
#    
#    XforR6.append(XforR6small)
#    XforR6small = []
#    yforR6.append(R6[i][3])
#
#
##Simple
##MLP
##R2
#X = XforR2
#y = yforR2
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
#clf.fit(X, y)
##
##print (clf.predict([[0.2531, 0.2584, 0]]))
#
##MLP
##R6
#X = XforR6
#y = yforR6
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
#clf.fit(X, y)
##
##print (clf.predict([[0.2531, 0.2584, 0]]))
#
#
##One hidden
##MLP
##R2
#X = XforR2
#y = yforR2
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2), random_state=1)
#clf.fit(X, y)
##
##print (clf.predict([[0.2531, 0.2584, 0]]))
#
##MLP
##R6
#X = XforR6
#y = yforR6
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2), random_state=1)
#clf.fit(X, y)
##
##print (clf.predict([[0.2531, 0.2584, 0]]))
#
#
##Two hidden
##MLP
##R2
#X = XforR2
#y = yforR2
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
#clf.fit(X, y)
##
##print (clf.predict([[0.2531, 0.2584, 0]]))
#
##MLP
##R6
#X = XforR6
#y = yforR6
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
#clf.fit(X, y)
##
##print (clf.predict([[0.2531, 0.2584, 0]]))
#
#
#
#
#
#
#
#
#











