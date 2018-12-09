#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
#import time
from writer import add_new_competition
from reader import in_file

def monitor_page(main_page_address, filename):
    index = 1   
    no_contests = True
    if(no_contests): #TODO wrap into while loop when put into thread
        main_page = urllib2.urlopen(main_page_address)   #time: ~0.4s
        soup = BeautifulSoup(main_page, 'html.parser')  #time: ~0.2s
        
        all_contests = soup.find_all('div', attrs={'class':'CompetitionBox__content'}) #TODO seclude only the active ones
        for contest in all_contests:
            contest_name = contest.find('h3').text.strip()
            contest_address = contest.find('a').get('href')
            if not (in_file(filename, contest_name)):
                add_new_competition(filename, index, contest_name.encode("utf-8"), contest_address)
                index += 1
            else:
                print "already in file"
        #time.sleep(60)

#TODO handle upcoming contests
#time.localtime()[3:6]
  