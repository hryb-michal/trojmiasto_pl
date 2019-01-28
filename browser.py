#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:58:22 2018

@author: hrymimakos
"""
import urllib2
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from answering import answer

def to_utf(string):
    return unicode(string, "utf-8", errors="ignore")

def participate(contest_address, start_time):



    #options = Options()
    #options.headless = True    #TODO enable when program would be able to answer question on its own
    #driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    driver.get(contest_address)

    current_time = time.localtime()
    wait_hours = start_time[0] - current_time.tm_hour
    wait_min = start_time[1] - current_time.tm_min
    wait_sec = start_time[2] - current_time.tm_sec
    time_delta = wait_sec + wait_min*60 + wait_hours*3600
    print 'going to sleep for ' + str(time_delta) + ' seconds...'
    time.sleep(time_delta + 1)
    
    contest_page = urllib2.urlopen(contest_address)   #time: ~0.4s
    contest_soup = BeautifulSoup(contest_page, 'html.parser')
    question_box = contest_soup.find('h2', attrs={'class':'title'})
    question = question_box.text
    print question

    #driver = webdriver.Firefox()
    driver.get(contest_address)

    elem = driver.find_element_by_name("answer")
    elem.clear()
    ans = answer(question)
    elem.send_keys(ans)
    name_box = driver.find_element_by_name("name")
    name_box.clear()
    name_box.send_keys(to_utf("Grzegorz"))
    surname_box = driver.find_element_by_name("surname")
    surname_box.clear()
    surname = to_utf("Brzęczyszczykiewicz")
    surname_box.send_keys(surname)
    mail_box = driver.find_element_by_name("email")
    mail_box.clear()
    mail_box.send_keys(to_utf("abc@niepodam.pl"))
    checkbox1 = driver.find_element_by_name("rodo[pytania][11]")
    checkbox1.click()
    checkbox2 = driver.find_element_by_name("rodo[pytania][14]")
    checkbox2.click()
    #elem.submit()

    print time.localtime()
    #driver.close() 


#def participate(contest_address):
    
    
    
