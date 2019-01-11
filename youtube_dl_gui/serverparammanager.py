#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os.path
from threading import Thread

from .utils import (
    YOUTUBEDL_BIN,
    check_path,
    getSplashInterval,
    getBottomAdUrl,
    getSplashAdUrl,
    getLastestResolverUrl
)

class ServerParamThread(Thread):

    def __init__(self, opt_manager):
        super(ServerParamThread, self).__init__()
        self.optManager = opt_manager;
        self.start()

    def run(self):
        # to make the request more quickly, use more sub thread to request
        self.splashIntervalThread = Thread(target=self.updateSplashInterval, name="update_splash_interval")
        self.splashIntervalThread.start()

        self.splashAdUrlThread = Thread(target=self.updateSplashAdUrl, name="update_splash_ad_url")
        self.splashAdUrlThread.start()

        self.adBarUrlThread = Thread(target=self.updateAdBarUrl, name="update_ad_bar_url")
        self.adBarUrlThread.start()

        self.resolverUrlThread = Thread(target=self.updateSplashInterval, name="update_resolver_url")
        self.resolverUrlThread.start()
        
    
    def updateSplashInterval(self):
        self.optManager.options["splash_time"] = getSplashInterval()
    
    def updateResolverUrl(self):
        self.optManager.options["lastest_resolver_url"] = getLastestResolverUrl()
    
    def updateSplashAdUrl(self):
        self.optManager.options["splash_ad_url"] = getSplashAdUrl()

    def updateAdBarUrl(self):
        self.optManager.options["ad_bar_url"] = getBottomAdUrl()
        
