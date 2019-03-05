#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import time
import sys

argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:
# keep the quotes, replace this with your consumer key
CONSUMER_KEY = 'NpEuVl4SDK7r54aKk5KMbK4lr'
# keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = '9C4C2eDk8PcY8C64DGoNuYFLUmcEj0xKuHUnjO0bspSrHHWjps'
# keep the quotes, replace this with your access token
ACCESS_KEY = '1041318627281055745-uUeb9ehgekzmW3FJYnTd5NhS2s3yGU'
# keep the quotes, replace this with your access token secret
ACCESS_SECRET = 'jE1C38TXWOMij3N81iOB2wzGn2tNQOXj0gxEG7r4zTDsT'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)  # Tweet every 15 minutes
