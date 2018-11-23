# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
#from datetime import datetime

#TODO measure application time

main_address = "https://konkursy.trojmiasto.pl/"
main_page = urllib2.urlopen(main_address)
soup = BeautifulSoup(main_page, 'html.parser')

contests = soup.find_all('li', attrs={'class':' item'})
contests.extend(soup.find_all('li', attrs={'class':' first_in_row item'}))

number_of_contests = len(contests)

if (number_of_contests < 1):
    print "no contests available"
else:
    print (number_of_contests, ' contest(s) available')
    for contest in contests:
        print contest.attrs['onclick'][17:-1]

''' #TODO only when there's at least 1 contest
contest_address = contests[-1].attrs['onclick'][17:-1]  #TODO add possibility of contest choice
contest_page = urllib2.urlopen(contest_address)
contest_soup = BeautifulSoup(contest_page, 'html.parser')


question_box = contest_soup.find('div', attrs={'class':'question'})
question = question_box.find('p', attrs={'class':'frame'})
print(question.text)
'''

#TODO check time of the contest
#current_time = datetime.now().time()

#time_message_box = contest_soup.find('div', attrs={'class': 'message'})
#time_message.find('h2').text

#for word in 

#time_message_text = time_message_box.fi


#TODO check if the contest is open
''' #TODO only when contest is online
driver = webdriver.Firefox( )
driver.get(contest_address)
elem = driver.find_element_by_name("answer")
elem.clear()
elem.send_keys("33")
elem2 = driver.find_element_by_name("name")
elem2.clear()
elem2.send_keys(repr("Michał")) #TODO send polish letters
elem3 = driver.find_element_by_name("rodo[pytania][11]")
elem3.click()
'''
'''
elem.submit()
'''
#driver.close()

