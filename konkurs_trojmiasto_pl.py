# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#driver = webdriver.Firefox()

main_page = "https://konkursy.trojmiasto.pl/"
page = urllib2.urlopen(main_page)
soup = BeautifulSoup(page, 'html.parser')

contests = soup.find_all('li', attrs={'class':' item'})
contests.append(soup.find('li', attrs={'class': ' first_in_row item'}))
for contest in contests:
    #print contest.text
    print contest.attrs['onclick'][17:-1]

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

'''
page = driver.get("https://rozrywka.trojmiasto.pl/Przemek-Dyakowski-Nie-jestem-zapiekly-na-cokolwiek-n129478.html")
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find("input", attrs={"type": "checkbox"})
print name_box.text
'''

#question_box = soup.find('div', attrs={'class':'question'})
#question = question_box.find('p', attrs={'class':'frame'})
#question_text = question.text
#print question_text



#print(name_box)


