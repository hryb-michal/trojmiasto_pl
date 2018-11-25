#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:58:09 2018

@author: hrymimakos
"""

import csv

#for word in question:
    

import re

mystr = 'This is a string, with words!'
wordList = re.sub("[^\w]", " ",  mystr).split()

print (wordList)
'''
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
 #   writer.writerow([name, price, datetime.now()])
    writer.writerow(["uga", "buga", "dorynsztoka"])
    '''