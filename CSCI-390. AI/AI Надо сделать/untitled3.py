# -*- coding: utf-8 -*-
"""

"""

from sklearn.neural_network import MLPClassifier
import csv

with open('newoutput.csv', 'r') as file:
    newarray = []
    reader = csv.reader(file, delimiter='\n')
    for row in reader:
        newarray.append(row)

for i in range(len(newarray)):
    for j in range(len(newarray[i])):
        newarray[i][j] = newarray[i][j].split(', ')


finalarr = []
for i in range(len(newarray)):
    for j in range (len(newarray[i])):
        finalarr.append(newarray[i][j])  

#2
arrFor2tunRoom = []
arrFor6tunRoom = []
for i in range(len(finalarr)):
    if finalarr[i][0] == 'R2':
        arrFor2tunRoom.append(finalarr[i])
    elif finalarr[i][0] == 'R6':
        arrFor6tunRoom.append(finalarr[i])
        
for i in range(len(arrFor2tunRoom)):
    arrFor2tunRoom[i][1] = float(arrFor2tunRoom[i][1])
    arrFor2tunRoom[i][2] = float(arrFor2tunRoom[i][2])
    arrFor2tunRoom[i][3] = int(arrFor2tunRoom[i][3])
    arrFor2tunRoom[i][4] = int(arrFor2tunRoom[i][4])
	
	
arrWithTun2 = []
arrWithTun2add = []

for i in range(len(arrFor2tunRoom)):
    arrWithTun2add.append(arrFor2tunRoom[i][1])
    arrWithTun2add.append(arrFor2tunRoom[i][2])
    arrWithTun2add.append(arrFor2tunRoom[i][3])
    arrWithTun2add.append(arrFor2tunRoom[i][4])
    
    arrFor2tunRoom.append(arrWithTun2add)
    arrWithTun2add = []
	
XforarrWithTun2 = []
XforarrWithTun2add = []
yforarrWithTun2 = []

for i in range(len(arrFor2tunRoom)):
    XforarrWithTun2add.append(arrFor2tunRoom[i][0])
    XforarrWithTun2add.append(arrFor2tunRoom[i][1])
    XforarrWithTun2add.append(arrFor2tunRoom[i][2])
    
    XforarrWithTun2.append(XforarrWithTun2add)
    XforarrWithTun2add = []
    yforarrWithTun2.append(arrFor2tunRoom[i][3])

#6	

for i in range(len(arrFor6tunRoom)):
    arrFor6tunRoom[i][1] = float(arrFor6tunRoom[i][1])
    arrFor6tunRoom[i][2] = float(arrFor6tunRoom[i][2])
    arrFor6tunRoom[i][3] = int(arrFor6tunRoom[i][3])
    arrFor6tunRoom[i][4] = int(arrFor6tunRoom[i][4])

    
arrWithTun6 = []
arrWithTun6add = []

for i in range(len(arrFor6tunRoom)):
    arrWithTun6add.append(arrFor6tunRoom[i][1])
    arrWithTun6add.append(arrFor6tunRoom[i][2])
    arrWithTun6add.append(arrFor6tunRoom[i][3])
    arrWithTun6add.append(arrFor6tunRoom[i][4])
    
    arrFor6tunRoom.append(arrWithTun6add)
    arrWithTun6add = []

XforarrWithTun6 = []
XforarrWithTun6add = []
yforarrWithTun6 = []

for i in range(len(arrFor6tunRoom)):
    XforarrWithTun6add.append(arrFor6tunRoom[i][0])
    XforarrWithTun6add.append(arrFor6tunRoom[i][1])
    XforarrWithTun6add.append(arrFor6tunRoom[i][2])
    
    XforarrWithTun6.append(XforarrWithTun6add)
    XforarrWithTun6add = []
    yforarrWithTun6.append(arrFor6tunRoom[i][3])
    
#A simple perceptron
X = XforarrWithTun2
y = yforarrWithTun2
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
clf.fit(X, y)

X = XforarrWithTun6
y = yforarrWithTun6
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
clf.fit(X, y)



##MLP with one hidden layer and 2 hidden nodes
#X = XforarrWithTun2
#y = yforarrWithTun2
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2), random_state=1)
#clf.fit(X, y)
#
#
#X = XforarrWithTun6
#y = yforarrWithTun6
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2), random_state=1)
#clf.fit(X, y)
#
#
#
##MLP with two hidden layers each containing 3 hidden nodes
#X = XforarrWithTun2
#y = yforarrWithTun2
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
#clf.fit(X, y)
#
#
#
#X = XforarrWithTun6
#y = yforarrWithTun6
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
#clf.fit(X, y)
