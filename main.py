# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import urllib2
import thread
from bs4 import BeautifulSoup
import time
from functions import to_utf
from functions import list_contests
from browser import participate
from monitor import monitor_page

import csv

from writer import add_new_competition
from reader import read_competitions
from reader import in_file
#from datetime import datetime

main_address = "https://konkursy.trojmiasto.pl/"
filename = 'competitions.csv'

#if not (in_file(filename, 'initialize')):
add_new_competition(filename, 0, 'initialize', 'blank')
    
monitor_page(main_address, filename)

#index = 1
read_competitions(filename)

#list_contests(upcoming_contests)    #TODO add possibility of contest choice
#list_contests(current_contests)

        

''' #TODO only when there's at least 1 open contest
contest_address = contests[1].attrs['onclick'][17:-1]  #TODO add possibility of contest choice
contest_page = urllib2.urlopen(contest_address)
contest_soup = BeautifulSoup(contest_page, 'html.parser')
question_box = contest_soup.find('div', attrs={'class':'question'})
question = question_box.find('p', attrs={'class':'frame'})
print(question.text)
'''

#TODO check time of the contest
#current_time = datetime.now().time()

#TODO check if the contest is open
#participate("https://google.com")   #TODO pass contest address, run when contest is active