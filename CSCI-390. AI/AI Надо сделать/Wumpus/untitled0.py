# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:09:56 2017

@author: MDK
"""

file = open (' lambtest .txt ')
o = Observable . from_ ( file ). filter ( lambda i: i[0] == 'T ')
o. subscribe ( lambda s: print (s))