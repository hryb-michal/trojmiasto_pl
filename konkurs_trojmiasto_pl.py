# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from functions import to_utf
#from datetime import datetime

main_address = "https://konkursy.trojmiasto.pl/"
    
no_contests = True
while(no_contests):
    main_page = urllib2.urlopen(main_address)   #time: ~0.4s
    before = time.time()
    soup = BeautifulSoup(main_page, 'html.parser')  #time: ~0.2s
    after = time.time()
    
    contests = soup.find_all('li', attrs={'class':' item'})
    contests.extend(soup.find_all('li', attrs={'class':' first_in_row item'}))
    number_of_contests = len(contests)
    
    if (number_of_contests < 1):
        print ("no contests available", time.localtime()[3:6])
        time.sleep(60)        
    else:
        no_contests = False
        print ("contest found", time.localtime()[3:6])
    #print (after - before)

print (number_of_contests, ' contest(s) available')
for contest in contests:
    contests_names = contest.find_all('p', attrs={'class':'name'})
    for contest_name in contests_names:
        print contest_name.text
    print contest.attrs['onclick'][17:-1]

if (len(contests) > 0):
    for contest in contests:
        contest_address = contest.attrs['onclick'][17:-1]  #TODO add possibility of contest choice
        contest_page = urllib2.urlopen(contest_address)
        contest_soup = BeautifulSoup(contest_page, 'html.parser')
        time_message_box = contest_soup.find('div', attrs={'class': 'message'})
        print time_message_box.find('h2').text
        

''' #TODO only when there's at least 1 contest
contest_address = contests[1].attrs['onclick'][17:-1]  #TODO add possibility of contest choice
contest_page = urllib2.urlopen(contest_address)
contest_soup = BeautifulSoup(contest_page, 'html.parser')
question_box = contest_soup.find('div', attrs={'class':'question'})
question = question_box.find('p', attrs={'class':'frame'})
print(question.text)
'''

#TODO check time of the contest
#current_time = datetime.now().time()


#time_message_text = time_message_box.fi


#TODO check if the contest is open
''' #TODO only when contest is online
driver = webdriver.Firefox( )
driver.get(contest_address)
elem = driver.find_element_by_name("answer")
elem.clear()
#elem.send_keys("33")
name_box = driver.find_element_by_name("name")
name_box.clear()
name_box.send_keys(to_utf("Michał"))
surname_box = driver.find_element_by_name("surname")
surname_box.clear()
surname_box.send_keys(to_utf("Hryb"))
mail_box = driver.find_element_by_name("email")
mail_box.clear()
mail_box.send_keys(to_utf("hryb.michal@gmail.com"))
checkbox1 = driver.find_element_by_name("rodo[pytania][11]")
checkbox1.click()
checkbox2 = driver.find_element_by_name("rodo[pytania][14]")
checkbox2.click()
'''
'''
elem.submit()
'''
#driver.close() 
