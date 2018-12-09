#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:01:46 2018

@author: hrymimakos
"""
import urllib2
from bs4 import BeautifulSoup

def to_utf(string_to_convert):
    return unicode(string_to_convert, "utf-8", errors="ignore")

def list_contests(contests):
    for contest in contests:
        contest_name = contest.find('p', attrs={'class':'name'})
        contest_address = contest.attrs['onclick'][17:-1]
        contest_page = urllib2.urlopen(contest_address)
        contest_soup = BeautifulSoup(contest_page, 'html.parser')
        time_message_box = contest_soup.find('div', attrs={'class': 'message'})
        print contest_name.text
        print time_message_box.find('h2').text
        print contest.attrs['onclick'][17:-1]