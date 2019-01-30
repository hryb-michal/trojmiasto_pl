#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re

def to_utfs(string):
    return unicode(string, "utf-8", errors="ignore")

#question = to_utfs('Na czym gra Adam Golicki?')

def search(dictionary, question):
    for key in dictionary:
        if (re.search(to_utfs(key), question, re.IGNORECASE)):
            return dictionary[key]

pairs = {'przekład' : ' Barbara Grzegorzewska ł',
            'które' : 'drugie',
            'tremiszewski' : 'limo',
            'limo' : 'tremiszewski',
            'ad hoc' : 'próchniewicz',
            'próchniewicz' : 'ad hoc'} 


def answer(question):
    return search(pairs, question)

#print to_utfs(search(pairs, question))
