#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:59:44 2018

@author: hrymimakos
"""
import csv

def print_competitions(filename):
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
            for elem in row:
                if (elem == arg.encode('utf-8')):
                    return True
        return False
    
def is_participating(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if (row[2] == 'yes'):
                return True
            else:
                return False
    
def get_contests_address(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if (row[2] == 'yes'):
                return row[3]   #return page address
            else:
                return False