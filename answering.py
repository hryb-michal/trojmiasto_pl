#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re

#music = ['tytuł', 'płyta', 'album']
#music_titles = {'2013' : 'asd'}

def to_utfs(string):
    return unicode(string, "utf-8", errors="ignore")

#question = to_utf('Jaki film zostanie pokazany 30 stycznia w kinie Helios Forum w ramach Kina Konesera?')

def answer(question):
    if re.search('koneser', question, re.IGNORECASE):
        if re.search('28', question, re.IGNORECASE):
            return to_utfs('Kto napisze naszą historię')
        if re.search('13', question, re.IGNORECASE):
            return to_utfs('Vice')
        if re.search('20', question, re.IGNORECASE):
            return to_utfs('Powrót Bena')
    if re.search('kultura', question, re.IGNORECASE):
        if re.search('31', question, re.IGNORECASE):
            return to_utfs('Dywizjon 303. Historia prawdziwa')
        if re.search('7', question, re.IGNORECASE):
            return to_utfs('Twarz')
        if re.search('21', question, re.IGNORECASE):
            return to_utfs('Jeszcze dzień życia')

#def answer(question):
#    for unit in music:
#        if unit in question:
#            return x
    
