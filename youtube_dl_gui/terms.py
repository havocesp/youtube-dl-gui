#coding=utf-8

import os
import gettext
import wx
import webbrowser
import wx.html
import wx.html2
import wx.lib.agw.hyperlink as hyperlink
import wx.lib.buttons as buttons
import wx.stc as stc

from .utils import (
    get_data_dir,
    get_config_path,
    get_locale_file,
    os_path_exists,
    YOUTUBEDL_BIN
)

from .info import (
    __license_CN__,
    __licensefull__
)

from locale import (
    getlocale
)

from .mainframe import MainFrame

class Terms(wx.Frame):
    def __init__(self, opt_manager, log_manager, youtubedl_path):
        wx.Frame.__init__(self, None, title="Terms of Use", size=opt_manager.options["main_win_size"])
        self.optManager = opt_manager
        self.logManager = log_manager
        self.youtubedlPath = youtubedl_path
        self.Bind(wx.EVT_CLOSE ,self._on_close)

        fullText = __licensefull__ + '\n'
        argeeLable = 'Agree'
        disagreeLable = 'Disagree'

        if opt_manager.options["locale_name"] == 'zh_CN' :
            fullText = __license_CN__ + '\n'
            argeeLable = u'同意'
            disagreeLable = u'不同意'

        mainTermsText = wx.TextCtrl(self, -1, value=fullText, size=opt_manager.options["main_win_size"], 
            style= wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2 | wx.TE_BESTWRAP, name="Terms of Use Text")

        agreeButton = wx.Button(self, -1, label=argeeLable)
        self.Bind(wx.EVT_BUTTON, self._onAgree, agreeButton)

        disagreeButton = wx.Button(self, -1, label=disagreeLable)
        self.Bind(wx.EVT_BUTTON, self._onDisagree, disagreeButton)

        textSizer = wx.BoxSizer(wx.VERTICAL) 
        textSizer.Add(mainTermsText, 0, wx.EXPAND | wx.ALL, 0)

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL) 
        buttonSizer.Add((20,20), 1)
        buttonSizer.Add(agreeButton,0 , wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)
        buttonSizer.Add((10,10), 1)
        buttonSizer.Add(disagreeButton,0 , wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)
        buttonSizer.Add((20,20), 1)

        frameSizer = wx.BoxSizer(wx.VERTICAL) 
        frameSizer.Add(textSizer, 0, wx.EXPAND | wx.ALL, 0)
        frameSizer.Add((10,10), 1)
        frameSizer.Add(buttonSizer, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)
        frameSizer.Add((10,10), 1)

        # create main frame 
        self._frame = MainFrame(self.optManager, self.logManager)

        self.SetSizer(frameSizer)
        self.Center()
        self.SetMinSize(opt_manager.options["main_win_size"])

        frameSizer.Fit(self)
        frameSizer.SetSizeHints(self)

    def _onAgree(self, event):
        self._openMainFrame()
        self.Destroy()

    def _onDisagree(self, event):
        self._frame.Destroy()
        self.Destroy()

    def _on_close(self, event):
        if self._frame :
            self._frame.Destroy()
        self.Destroy()

    def _openMainFrame(self):
        self._frame.Center()
        self._frame.Show()

        if self.optManager.options["disable_update"] and not os_path_exists(self.youtubedlPath):
            wx.MessageBox(_("Failed to locate youtube-dl and updates are disabled"), _("Error"), wx.OK | wx.ICON_ERROR)
            self._frame.close()


