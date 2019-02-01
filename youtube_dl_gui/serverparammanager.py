#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import os.path
import json
from threading import Thread

from urllib2 import urlopen, URLError, HTTPError
from json import load

from .utils import (
    YOUTUBEDL_BIN,
    check_path,
    getSplashInterval,
    getBottomAdUrl,
    getSplashAdUrl,
    getLastestResolverUrl
)

from .info import (
    __statisticUrl__
)

class ServerParamThread(Thread):

    def __init__(self, opt_manager):
        super(ServerParamThread, self).__init__()
        self.optManager = opt_manager;
        self.start()

    def run(self):
        # at the begining, should post the last time statistic info to server
        self.statisticThread = Thread(target=self.updateStatisticInfo, name="update_statistic_info")
        self.statisticThread.start()

        # to make the request more quickly, use more sub thread to request
        self.splashIntervalThread = Thread(target=self.updateSplashInterval, name="update_splash_interval")
        self.splashIntervalThread.start()

        self.splashAdUrlThread = Thread(target=self.updateSplashAdUrl, name="update_splash_ad_url")
        self.splashAdUrlThread.start()

        self.adBarUrlThread = Thread(target=self.updateAdBarUrl, name="update_ad_bar_url")
        self.adBarUrlThread.start()

        self.resolverUrlThread = Thread(target=self.updateSplashInterval, name="update_resolver_url")
        self.resolverUrlThread.start()
        
    def updateStatisticInfo(self):
        header = {'Content-Type': 'application/json'}
        payload = { 
                    'IP_ADDRESS': self.getLocalIp(),
                    'SPLASH_URL': self.optManager.options["splash_ad_url"],
                    'SPLASH_INTERVAL': self.optManager.options["splash_time"],
                    'SPLASH_SKIP': self.optManager.options["statistic_splash_skip"],
                    'SPLASH_CLICK': self.optManager.options["statistic_splash_click"],
                    'BOTTOM_AD_BAR_URL': self.optManager.options["ad_bar_url"],
                    'BOTTOM_AD_BAR_CLICK': self.optManager.options["statistic_ad_bar_click"],
                    'USE_DURATION': self.optManager.options["statistic_duration"],
                    'DOWNLOAD_TOTAL': self.optManager.options["statistic_download_total"],
                    'DOWNLOAD_FAILED': self.optManager.options["statistic_download_failed"],
                    'UPDATE_RESOLVER_TOTAL': self.optManager.options["statistic_update_resolver_total"],
                    'UPDATE_RESOLVER_FAILED': self.optManager.options["statistic_update_resolver_failed"],
                    'IS_FIRST_BOOT': (not self.optManager.options["terms_status"])
                  }
        try:
            result = requests.post(__statisticUrl__, headers=header, data=json.dumps(payload), timeout=5)
            # no need to check the result
            print str(result.status_code)
            print str(result.content) 
        except requests.exceptions.RequestException as e:
            # do nothing
            print str(e)
            print 'error then upload statistic'

    def getLocalIp(self):
        try:
            my_ip = urlopen('http://ip.42.pl/raw').read()
            return my_ip
        except:
            try:
                my_ip = load(urlopen('http://jsonip.com'))['ip']
                return my_ip
            except:
                return 'unknown'


    def updateSplashInterval(self):
        self.optManager.options["splash_time"] = getSplashInterval()
    
    def updateResolverUrl(self):
        self.optManager.options["lastest_resolver_url"] = getLastestResolverUrl()
    
    def updateSplashAdUrl(self):
        self.optManager.options["splash_ad_url"] = getSplashAdUrl()

    def updateAdBarUrl(self):
        self.optManager.options["ad_bar_url"] = getBottomAdUrl()
        
