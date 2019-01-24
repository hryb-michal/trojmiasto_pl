#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import time
from writer import add_new_competition
from reader import in_file
from threading import Thread
from browser import to_utf

def monitor_page(main_page_address, filename):
    index = 1
    main_page = urllib2.urlopen(main_page_address)   #time: ~0.4s
    soup = BeautifulSoup(main_page, 'html.parser')  #time: ~0.2s
    
    awaiting = soup.find('div', attrs={'class':'BoxWrap CompetitionSection CompetitionSection--future'})
    
    future_contests = awaiting.find_all('div', attrs={'class':'CompetitionBox__content'})
    #future_contests = soup.find_all('div', attrs={'class':'CompetitionBox__content'}) #TODO includes inactive contests for testing
    
    for contest in future_contests:
        contest_name = contest.find('h3').text.strip()
        contest_address = contest.find('a').get('href')
        if not (in_file(filename, contest_address)):
            add_new_competition(filename, index, contest_name.encode("utf-8"), contest_address)
            print 'New contest found! ' + contest_name
            index += 1
            
def read_time(page_address):
    contest_page = urllib2.urlopen(page_address)   #time: ~0.4s
    soup = BeautifulSoup(contest_page, 'html.parser')
            
    time_box = soup.find('span', attrs = {'class':'TimeToStart__time'})
    time_box_text = time_box.text
    
    if (to_utf('mniej')) in time_box_text:
        if (to_utf('godzinę')) in time_box_text:
            return 1
        if (to_utf('godzin')) in time_box_text:
            s = ""
            for t in time_box_text[10:-8]:
                s += t
            return int(s)
        else:
            return 15
    else:
        return -1
    
  
