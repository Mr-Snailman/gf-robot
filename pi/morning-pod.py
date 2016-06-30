'''
Script inspired by Brett Farkas: https://youtu.be/1oIWW5d-0CA

This will see if it is 4:30 AM on a weekday before downloading
and playing the latest BBC Daily Commute Podcast through the
command line version of VLC on the base OS (Linux).

Author: Dustin Saunders <dustin.saunders@sofiac.us>
'''
import time
import feedparser
import os
import json
import urllib2
import re

audioRe = re.compile("audio/")
bbcFeedUrl = "http://www.bbc.co.uk/programmes/p02nrsmt/episodes/downloads.rss"

# Not using the CNN Anderson Cooper 360 podcast currently, but here's the link
#cnnFeedUrl = "http://rss.cnn.com/services/podcasting/ac360/rss.xml"

from datetime import datetime

while (1):
  now = datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  day = datetime.today().weekday()

  print now
  if hour == 4 and minute == 30 and day < 5:

    morningFeed = feedparser.parse(bbcFeedUrl)
    audioUrl = ""
    print "... Found feed data. Parsing for audio link."
    for link in morningFeed.entries[0].links:
      if audioRe.match(link.type):
        print "...Found audio link."
        audioUrl = link.url
        break

    # Download the file
    print "Downloading the file."
    audioOutFile = morningFeed.entries[0].title + ".mp3"
    u = urllib2.urlopen(audioUrl)
    f = open(audioOutFile, "w")
    mp3Bytes = u.read()
    f.write(mp3Bytes)
    f.close()
    print "... Download Complete. Playing podcast..."

    # play the file
    os.system("cvlc '" + audioOutFile + "'")

    print "...Podcast complete. Removing file, and resuming loop..."
    os.system("rm '" + audioOutFile + "'")
