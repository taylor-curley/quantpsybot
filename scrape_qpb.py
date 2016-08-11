#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import datetime
import feedparser
from bs4 import BeautifulSoup

# Get date and time for log
time = datetime.datetime.now()

################################################################################
# Elsevier journal websites #
ejournal_web = [
"http://www.journals.elsevier.com/journal-of-mathematical-psychology/recent-articles", 
"http://www.journals.elsevier.com/journal-of-mathematical-psychology/open-access-articles"
]

# Elsevier journal titles (cannot exceed 50 characters)
ejournal_title = [
"Journal of Mathematical Psychology", 
"Journal of Mathematical Psychology"
]

etitle = []
eurl = []
ejournal = []

# Loop through Elsevier journals
y = 0
for x in ejournal_web:
    # Read site
    o = urllib.request.urlopen(ejournal_web[y])
    site = BeautifulSoup(o, "lxml")
    
    # Pull 3 most current postings (rawish data)
    titleOne = site.find_all("div", class_="pod-listing-header", limit=3)
    titleOne = BeautifulSoup(str(titleOne), 'html.parser')
    titleTwo = titleOne.find_all("a", title=True)
    
    # Keep track of published articles
    f = open('/home/taylor/Documents/bots/quantpsy/tweeted_pubs_qpb.txt', 'a+')
    g = open('/home/taylor/Documents/bots/quantpsy/tweeted_pubs_qpb.txt', 'r')
    g = [line.rstrip('\n') for line in g]
    
    for i in range(3):
        entry = titleTwo[i]['title']
        if entry in g:
            print('Redundant entry... ' + str(time))
        else:
            etitle.append(titleTwo[i]['title'])
            eurl.append(titleTwo[i]['href'])
            ejournal.append(str(ejournal_title[y]))
            # Log article names + URLs 
            f.write(str(entry) + '\n' + str(titleTwo[i]['href']) + '\n')  
              
    f.close()
    y = y + 1


################################################################################
# Springer,T&F, Cell, and APA journal websites

sjournal_web = [
"http://journal.frontiersin.org/journal/psychology/section/quantitative-psychology-and-measurement/rss", 
"http://apm.sagepub.com/rss/ahead.xml", 
"http://content.apa.org/journals/met.rss?_ga=1.83802198.1778712730.1470808369", 
"http://content.apa.org/journals/pas.rss?_ga=1.78363476.1778712730.1470808369", 
"http://onlinelibrary.wiley.com/rss/journal/10.1111/(ISSN)2044-8317"
]

sjournal_title = [
"Quantitative Psychology and Measurement", 
"Applied Psychological Measurement", 
"Psychological Methods", 
"Psychological Assessment", 
"British Journal of Math & Stat Psych"
]

stitle = []
surl = []
sjournal = []

y = 0
for x in sjournal_web:
    # Read XML feed
    site = feedparser.parse(sjournal_web[y])

    # Keep track of published articles
    f = open('/home/taylor/Documents/bots/quantpsy/tweeted_pubs_qpb.txt', 'a+')
    g = open('/home/taylor/Documents/bots/quantpsy/tweeted_pubs_qpb.txt', 'r')
    g = [line.rstrip('\n') for line in g]

    for i in range(len(site['entries'])):
        entry = site['entries'][i]['title']
        entry_url = site['entries'][i]['link']
        if entry in g:
            print('Redundant entry... ' + str(time))
        else:
            # Log article names + URLs 
            stitle.append(site['entries'][i]['title'])
            surl.append(site['entries'][i]['link'])
            sjournal.append(sjournal_title[y])
            f.write(str(entry) + '\n' + str(entry_url) + '\n') 
              
    f.close()
    y = y + 1
