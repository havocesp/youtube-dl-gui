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

# from .mainframe import MainFrame

class Terms(wx.Frame):
    def __init__(self, opt_manager, log_manager, youtubedl_path):
        wx.Frame.__init__(self, None, title="Terms of Use", size=opt_manager.options["main_win_size"])
        self.optManager = opt_manager
        self.logManager = log_manager
        self.youtubedlPath = youtubedl_path

        mainTermsText = wx.TextCtrl(self, -1, value="xxx", 
            style= wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2 | wx.TE_BESTWRAP, name="Terms of Use Text")

        agreeButton = wx.Button(self, -1, label="Agree")
        self.Bind(wx.EVT_BUTTON, self._onAgree, agreeButton)

        disagreeButton = wx.Button(self, -1, label="Disagree")
        self.Bind(wx.EVT_BUTTON, self._onDisagree, disagreeButton)

        textSizer = wx.BoxSizer(wx.VERTICAL) 
        textSizer.Add(mainTermsText, 0, wx.EXPAND, 0)

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL) 
        buttonSizer.Add(agreeButton,0 , wx.EXPAND, 0)
        buttonSizer.AddSpacer((10, -1))
        buttonSizer.Add(disagreeButton,0 , wx.EXPAND, 0)

        frameSizer = wx.BoxSizer(wx.VERTICAL) 
        frameSizer.Add(textSizer, 1, wx.EXPAND, 0)
        frameSizer.Add(buttonSizer, 0, wx.EXPAND, 0)

        # create main frame 
        # self._frame = MainFrame(self.optManager, self.logManager)

        self.SetSizer(frameSizer)
        self.Center()
        self.SetMinSize(opt_manager.options["main_win_size"])


    def _onAgree(self, event):
        print "yes"

    def _onDisagree(self, event):
        self._close()

    def _close(self):
        self.Close()
        # self._openMainFrame()
        

    # def _openMainFrame(self):
    #     self._frame.Center()
    #     self._frame.Show()

    #     if self.optManager.options["disable_update"] and not os_path_exists(self.youtubedlPath):
    #         wx.MessageBox(_("Failed to locate youtube-dl and updates are disabled"), _("Error"), wx.OK | wx.ICON_ERROR)
    #         self._frame.close()


