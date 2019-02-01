#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import json
import time, threading
import os
from urllib2 import urlopen, URLError, HTTPError
from json import load


def getLastestUrl():
    url = 'http://localhost:8080/desktop/yt-dl/latest/url?platform=1'
    result = requests.get(url, timeout=5)
    rCode = result.status_code
    rContent = result.content

    if rCode==200:
        print 'success'
    else:
        print 'wrong'
        
    print result
    print rCode
    print rContent

def getSplashInterval():
    url = 'http://localhost:8080/desktop/ad/splash/interval'
    try:
        result = requests.get(url, timeout=5)
        rCode = result.status_code
        rContent = result.content

        if rCode==200:
            print rContent
        else:
            print rCode
    except requests.exceptions.RequestException as e:
        print 'interval is: '
        print e



def getSlpashAdStatus():
    url = 'http://localhost:8080/desktop/ad/splash/url'
    try:
        result = requests.get(url, timeout=5)
        rCode = result.status_code
        rContent = result.content

        if rCode==200 and not rContent:
            print 'bottom ad is true'
        else:
            print rCode

    except requests.exceptions.RequestException as e:
        print 'splash url is: '
        print e

def getBottomAdStatus():
    url = 'http://localhost:8080/desktop/ad/bar/bottom/url'
    try:
        result = requests.get(url, timeout=5)
        rCode = result.status_code
        rContent = result.content

        if rCode==200 and not rContent:
            print 'bottom ad is true'
        else:
            print rCode
    except requests.exceptions.RequestException as e:
        print 'bottom url is: '
        print e

def startThread():
    t1 = threading.Thread(target=getSplashInterval, name='splash_interval')
    t1.start()

    t2 = threading.Thread(target=getSlpashAdStatus, name='splash_url')
    t2.start()

    t3 = threading.Thread(target=getBottomAdStatus, name='bottom_url')
    t3.start()

def sendStatis():
    try:
        payload = {'ipAddress': '255.255.255.255', 'splashInterval': 5, 'useDuration':100}
        header = {'Content-Type': 'application/json'}

        url = 'http://ec2-13-58-33-98.us-east-2.compute.amazonaws.com/desktop/statistic/simple'
        url_local = "http://localhost:8080/desktop/statistic/simple"
        result = requests.post(url, headers=header, data=json.dumps(payload), timeout=5)
        rCode = result.status_code
        rContent = result.content

        print str(rCode)
        print str(rContent)
    except requests.exceptions.RequestException as e:
        print "error for : " + str(e)


if __name__=='__main__':
    sendStatis()

    # startThread()
    # print 'absolute is ' + str(os.path.exists('/Users/hzhu2/Documents/workspace/youtube-dl-gui/data'))
    # print 'relative is ' + str(os.path.exists('youtube_dl_gui/data'))

    # url = ''
    # print 'judge not is ' + str( not url)

    # if url=='':
    #     print 'judge is ' + str( url )

    # if url!='':
    #     print 'judge is not ' + str( url )