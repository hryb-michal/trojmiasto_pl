#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:58:22 2018

@author: hrymimakos
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def participate(contest_address):
    #options = Options()
    #options.headless = True    #TODO enable when program would be able to answer question on its own
    #driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    driver.get(contest_address)
    '''
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
    elem.submit()
    '''
    #driver.close() 
