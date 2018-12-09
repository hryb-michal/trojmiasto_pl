#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:09:08 2018

@author: hrymimakos
"""

import csv

def add_new_competition(filename, index, title, web_addr):
    with open(filename, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([index, title, 'no', web_addr])