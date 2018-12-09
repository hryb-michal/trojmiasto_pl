# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import time

from browser import participate
from monitor import monitor_page
from reader import print_competitions
from reader import get_contests

#import csv
#from datetime import datetime

main_address = "https://konkursy.trojmiasto.pl/"
filename = 'competitions.csv'
open(filename,"w+")

monitor_page(main_address, filename)
print_competitions(filename)

target = False
while not (target):
    target = get_contests(filename)
    
    if (target):
        participate(target)   
    time.sleep(3)
    
    
#TODO calculate time of the contest
#current_time = datetime.now().time()
    
    
    
    
    
