# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

#quote_page = "https://konkursy.trojmiasto.pl/konkurs-14234/"
#page = urllib2.urlopen(quote_page)
#soup = BeautifulSoup(page, 'html.parser')

driver = webdriver.Firefox()


#driver.get("https://duckduckgo.com")
'''
driver.get("https://rozrywka.trojmiasto.pl/Przemek-Dyakowski-Nie-jestem-zapiekly-na-cokolwiek-n129478.html")
elem = driver.find
#elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.submit()
'''
#print driver.page_source

#driver.close()

#search_form = browser.find_element_by_id('search_form_input_homepage')
#results = browser.find_elements_by_class_name('result_title')


page = driver.get("https://rozrywka.trojmiasto.pl/Przemek-Dyakowski-Nie-jestem-zapiekly-na-cokolwiek-n129478.html")
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find("input", attrs={"type": "checkbox"})
print name_box.text
#question_box = soup.find('div', attrs={'class':'question'})
#question = question_box.find('p', attrs={'class':'frame'})
#question_text = question.text
#print question_text



#print(name_box)


