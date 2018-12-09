#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:59:44 2018

@author: hrymimakos
"""
import csv

def read_competitions(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            temp = list(row)
            fmt = u'{:<15}'*len(temp)
            print fmt.format(*[s.decode('utf-8') for s in temp])
            
def in_file(filename, arg):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if (row[1] == arg.encode('utf-8')): #check: if arg... in row
                return True
        return False