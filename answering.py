#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re

def to_utfs(string):
    return unicode(string, "utf-8", errors="ignore")

#question = to_utfs('Na czym gra Adam Golicki?')

def search(dictionary, question):
    for key in dictionary:
        if (re.search(key, question, re.IGNORECASE)):
            return dictionary[key]

pairs = {'album' : 'Junior',
            'płyta' : 'Junior',
            '2017' : 'Junior',
            'nazwisk' : 'Zagrodni',
            'kompo' : 'Wojciech Bergiel',
            'gatun' : 'synthwave',
            'nagrod' : 'WARTO',
            'festiw' : 'Open\'er',
            'singiel' : 'Retman',
            'perkus' : 'Marcin Mrówka',
            'Marcin Mrówka' : 'perkusja'} 


def answer(question):
    return to_utfs(search(pairs, question))

#print to_utfs(search(pairs, question))
