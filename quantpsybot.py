#!/usr/bin/env python
# Taylor Curley - 2016 - taylorcurley.co

from twython import Twython
from pyshorteners import Shortener
import datetime
from secret_qpb import c_key, cs_key, a_token, as_token, google_api
from scrape_qpb import ejournal, etitle, eurl, sjournal, stitle, surl

time = datetime.datetime.now()

api = Twython(c_key, cs_key, a_token, as_token)
api_key = google_api
shortener = Shortener('Google', api_key=api_key)

title = etitle + stitle
journal = ejournal + sjournal
url = eurl + surl

x = 0
for i in title:
    link = format(shortener.short(url[x]))
    print('Tweeting out: "' + str(title[x]) + '" at ' + str(time)) # Mirror in console
    if len(str(title[x])) > 65:
        tweet = 'From ' + journal[x] + ': "' + str(title[x][:65]) + '..." ' + '\n' + link
        api.update_status(status=tweet)
    else:
        tweet = 'From ' + journal[x] + ': "' + str(title[x]) + '" ' + '\n' + link
        api.update_status(status=tweet)
    x = x + 1
     

# Log posts
t = open('/home/taylor/Documents/bots/quantpsy/qpb_log.txt', 'a+')
t.write(str(time) + '  # of tweets: ' + str(len(title)) + '\n')
t.close()
