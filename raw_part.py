#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from answering import answer

def to_utf(string):
    return unicode(string, "utf-8", errors="ignore")

def fill_box(_driver, box_name, text):
    name_box = _driver.find_element_by_name(box_name)
    name_box.clear()
    name_box.send_keys(text)


contest_address = 'https://konkursy.trojmiasto.pl/konkurs-14417/'

driver = webdriver.Firefox()
driver.get(contest_address)

contest_page = urllib2.urlopen(contest_address)   #time: ~0.4s
contest_soup = BeautifulSoup(contest_page, 'html.parser')
question_box = contest_soup.find('h2', attrs={'class':'title'})
question = question_box.text
print question

ans = answer(question)
print 'answer in main ', ans
#fill_box(driver, "answer", ans)
#fill_box(driver, "name", to_utf("Grzegorz"))
elem = driver.find_element_by_name("answer")
elem.clear()
elem.send_keys(to_utf(ans))
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
#checkbox2.click()
#elem.submit()

print time.localtime()
