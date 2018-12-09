#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import time
from writer import add_new_competition
from reader import in_file
from functions import to_utf

def monitor_page(main_page_address, filename):
    index = 1   
    no_contests = True
    if(no_contests): #TODO change to while
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

        '''
        upcoming_contests_soup = soup.find('div', attrs={'class':'upcoming-contests'}) #TODO apply interface changes
        if (upcoming_contests_soup):
            upcoming_contests = upcoming_contests_soup.find_all('li', attrs={'class':' item'})
            upcoming_contests.extend(upcoming_contests_soup.find_all('li', attrs={'class':' first_in_row item'}))
        #number_of_contests = len(upcoming_contests)
    
        current_contests_soup = soup.find('div', attrs={'class':'upcoming-contests'})
        if (current_contests_soup):
            current_contests = current_contests_soup.find_all('li', attrs={'class':' item'})
            current_contests.extend(current_contests_soup.find_all('li', attrs={'class':' first_in_row item'}))
        
            if (len(current_contests) > 0):
                no_contests = False
                print "contest found", time.localtime()[3:6]
        else:
            print "no contests available", time.localtime()[3:6]
            #TODO handle upcoming contests
            #time.sleep(60)    
    '''
