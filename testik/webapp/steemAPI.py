import urllib2
import json
from django.db import connection

import re

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)



class steemAPI:
    def __init__(self):
        pass
    # ziska ID sloupce podle jmena
    @staticmethod
    def getCol(cols, col):
        i=0
        for name in cols:


            if(name[0] == col):

                return i;

            i+=1

        return 0

    @staticmethod
    def parseSQL(desc, results):
        resultsList = []


        for r in results:
            i = 0
            d = {}
            while i < len(desc):
                d[desc[i][0]] = r[i]
                i = i+1
            resultsList.append(d)

        return resultsList

    @staticmethod
    def parseSingle(desc, row):
        i = 0

        d = {}
        while i < len(desc):
            setattr(d, desc[i][0], row[i])

            #d[] = row[i]
            i = i+1
        return d




    @staticmethod
    def query(q):
        cursor = connection.cursor()
        cursor.execute(q)

        rows =  cursor.fetchall()
        desc = cursor.description
        rows = steemAPI.parseSQL(desc,rows)

        return rows

    @staticmethod
    def loadPosts():

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM posts ORDER BY probability DESC LIMIT 100')

        rows =  cursor.fetchall()
        desc = cursor.description
        rows = steemAPI.parseSQL(desc,rows)


        return rows
    @staticmethod
    def getSimilar(category):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM posts WHERE category="'+category+'" ORDER BY probability DESC LIMIT 5')

        rows =  cursor.fetchall()
        desc = cursor.description
        rows = steemAPI.parseSQL(desc,rows)
        return rows

    @staticmethod
    def loadPost(pk):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM posts WHERE id='+str(pk))

        row = cursor.fetchall()
        desc = cursor.description


        row = steemAPI.parseSQL(desc,row)

        return row




    def getContent(self, author, link):
        base = 'https://api.steemjs.com/getContent?'
        author = 'author='+author
        permlink ='permlink=' + link.split('/')[3]

        url = base + author + '&' +permlink

        req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        webpage = urllib2.urlopen(req).read()

        print(webpage)

        data = json.loads(webpage.decode('utf-8'))

        regex = r'((?<!src=")https?:\/\/[A-Za-z0-9]+.[a-z]{2,3}\/[A-Za-z0-9\/?_?]+.(jpg|gif|png))'

        data['body'] = re.sub(regex, r"<br /><img src='\1' /><br />", data['body'])

        return data['body']

    def strip_tags(self, html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()
