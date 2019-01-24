# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import time

from browser import participate
from monitor import monitor_page
from monitor import read_time
from reader import print_competitions
from reader import get_contests_address
from reader import is_participating


main_address = "https://konkursy.trojmiasto.pl/"
contests_filename = 'competitions.csv'
open(contests_filename,"w+")

participating = False
while not(participating):
    monitor_page(main_address, contests_filename)
    participating = is_participating(contests_filename)
    time.sleep(5)
    
print 'Participating...'

contest_address = get_contests_address(contests_filename)
print str(contest_address)
time_to_start = read_time(contest_address)
current_time = time.localtime()
    
print time_to_start

if (time_to_start == 15):
    print  'Less than 15 minutes till the contest begins...'
elif (time_to_start == -1):
    print  'More than 12 hours till the contest begins, please run the program again later.'
else:
    print  'Less than ' + str(time_to_start) + ' hours till the contest begins, calculating exact time (it might take up to 1 hour)...'
    
    new_time = read_time(contest_address)
    while (new_time == time_to_start):
        print 'sleeping' + str(time.localtime()[3:6])
        time.sleep(28)
        new_time = read_time(contest_address)
        print 'read new time'

    print 'different!'
    current_time = time.localtime()
    start_time = current_time[3:6]
    start_time = list(start_time)
    if (new_time == 15):
        if (start_time[1] > 44):
            start_time[0] += 1
            start_time[1] += (15 - (60 - start_time[1]))
            start_time[2] = 0
        else:
            start_time[1] += 15
            start_time[2] = 0
    else:
            start_time[0] += time_to_start - 1
            start_time[2] = 0
            
    start_timestamp = (10000 * start_time[0]) + (100 * start_time[1]) + (start_time[2])
    print 'Calculated, contest will take place at ' + str(start_timestamp)
    participate(contest_address, start_time)

print 'Thanks for participating :)'

    
