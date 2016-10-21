#!/usr/bin/env python

from __future__ import print_function
import twitter
import pprint
import json
import re

CONSUMER_KEY = 'oqjW5kJDvwUA6dzCTNoKamx4c'
CONSUMER_SECRET = 'ZNEkrOoH9N4nBhRmnFw27NUhKiUQ8jaUy5V8TJ9k7RhiXpNJrL'
ACCESS_TOKEN = '788043168348573704-9MslsLYzYdlzUI3Y8JA64Sxd753oalC'
ACCESS_SECRET = 'b9BX3YDAkK3zIvNoA8CFzfiiJ7C0e15Gv859fHeLnE8Z2'

TWITTER_USER = 'BaxterThings'

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET)

statuses = api.GetUserTimeline(screen_name=TWITTER_USER)
#pprint.pprint(statuses)

f = open('latestTwitterID.txt')
latestID = f.read()
f.close()

print('Latest ID: ' + latestID)

for tweet in reversed(statuses):
    if int(tweet.id) > int(latestID):
        print ('New tweet!')

        tweet.text = re.sub(r'Mouthbreather .*? says ' , '', tweet.text, flags=re.IGNORECASE)
        tweet.text = re.sub(r'BaxterThings' , '', tweet.text, flags=re.IGNORECASE)
        tweet.text = re.sub(r'RT [^ ]+ ' , '', tweet.text, flags=re.IGNORECASE)
        tweet.text = re.sub(r'http(s)?://[^ ]+' , '', tweet.text, flags=re.IGNORECASE)
        tweet.text = re.sub(r'[^a-z ]+' , '', tweet.text, flags=re.IGNORECASE)
        
        print (tweet.text)
        
        #Write the tweet to the file
        tweetsFile = open('tweets.txt', 'a')
        tweetsFile.write(tweet.text.strip())
        tweetsFile.write('\n')
        tweetsFile.close()
        
        #Modify the lastest ID
        #f = open('latestTwitterID.txt', 'w')
        #f.truncate()
        #f.write(str(tweet.id))
        #f.close()
    else:
        print ('Old tweet')
        pprint.pprint(tweet)
