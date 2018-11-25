#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:01:46 2018

@author: hrymimakos
"""

def to_utf(string_to_convert):
    return unicode(string_to_convert, "utf-8", errors="ignore")

def time_of_start(time_to_start):
    for word in time_to_start:  #not actually word, it's letters
        if (word == "mniej"):
            return False