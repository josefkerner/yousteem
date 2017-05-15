import urllib2
import json
import datetime
import csv
import time

app_id = ""
app_secret = ""
access_token = app_id + "|" + app_secret

def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try:
            response = urllib2.urlopen(req)
            if response.getCode() == 200:
                success = True