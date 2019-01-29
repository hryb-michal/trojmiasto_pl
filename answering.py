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

pairs = {'kontrabas' : 'Adam Żuchowski',
            'pian' : 'Dominik Kisiel',  #fortepian, pianista
            'perkusja' : 'Adam Golicki',
            'saksofon' : 'Wojciech Bergiel',
            'kompo' : 'Wojciech Bergiel',   #kompozycje, skomponował
            'Wojciech Bergiel' : 'saksofon tenorowy',
            'Adam Żuchowski' : 'kontrabas',
            'Dominik Kisiel' : 'fortepian',
            'Adam Golicki' : 'perkusja'} 


def answer(question):
    return to_utfs(search(pairs, question))

#rint to_utfs(search(pairs, question))
