#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import time, threading
from urllib2 import urlopen, URLError, HTTPError

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

if __name__=='__main__':
    startThread()