'''
This script reads in a JSON file from the command line, and then
downloads all podcasts from each URL in the list.

JSON should be in the following format:

    {"feeds":["URL",...]}

In order words, there should be a single list named 'feeds'

Author: Dustin Saunders <dustin.saunders@sofiac.us>
'''

import feedparser
import json
import os
import re
import sys
import urllib2

audioRe = re.compile("audio/")

# Check args
if len(sys.argv) != 2:
    print 'USAGE: python download-all.py *FILE_NAME*'
    sys.exit(-1)

# Read all URLs into an object
filename = sys.argv[1]
with open(filename) as data_file:
    data = json.load(data_file)

# Set up overall master directory
masterDir = 'feeds'
if not os.path.exists(masterDir):
    os.makedirs(masterDir)

# Loop through each feed in our dictionary
for feedUrl in data['feeds']:
    feed = feedparser.parse(feedUrl)
    
    # Set up podcast directory
    if not os.path.exists(masterDir+'/'+feed.feed.title):
        os.makedirs(masterDir+'/'+feed.feed.title)

    print 'Downloading for Feed:', feed.feed.title

    # For each podcast entry 
    for entry in feed.entries:
        audioUrl = ''
        audioOutFile = masterDir+'/'+feed.feed.title+'/'+entry.title+'.mp3'

        # Check the links, we want the audio one
        for link in entry.links:
            if audioRe.match(link.type):
                audioUrl = link.url
                break

        # Check that our podcast doesn't already exist

        # Download the file
        if (len(audioUrl) >= 1):
            print "\tDownloading", entry.title
            u = urllib2.urlopen(audioUrl)
            f = open(audioOutFile, "w")
            mp3Bytes = u.read()
            f.write(mp3Bytes)
            f.close()
            print "\t...Done."
