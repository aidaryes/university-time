# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 00:46:01 2017

@author: Aidar Yessembayev
data taken from Albina Li
"""
import csv
with open('copy.csv', newline='', encoding='utf-8-sig') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=';')
    arr = []
    for row in reader:
        arr.append(row)

    arrWitEmp = []
    for i in range (len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '':
                arrWitEmp.append(arr[i][j])
        
    arrWitEmp.sort()
    print (arrWitEmp)
    
    n = 6
    x = int(len(arrWitEmp)/n)
    rem = len(arrWitEmp) - x*n
    print (x, rem)
        
    lst = {}
    for i in range(n):
        lst[i] = []
    
    