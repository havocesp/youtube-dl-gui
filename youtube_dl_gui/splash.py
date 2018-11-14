import os
import gettext
import wx
import webbrowser
import wx.html
import wx.html2
import wx.lib.agw.hyperlink as hyperlink
import wx.lib.buttons as buttons
import wx.stc as stc

from .info import (
    __splash_time__,
    __splash_min_size__,
    __splash_ad_url__,
    __bottom_ad_url__,
    __home_page_url__,
    __home_page_name__
)

from .utils import (
    get_data_dir,
    get_config_path,
    get_locale_file,
    os_path_exists,
    YOUTUBEDL_BIN
)

from .mainframe import MainFrame

class Splash(wx.Frame):
    count_down = __splash_time__

    def __init__(self, opt_manager, log_manager, youtubedl_path):
        wx.Frame.__init__(self, None, title="splash", size=opt_manager.options["main_win_size"])
        self.optManager = opt_manager
        self.logManager = log_manager
        self.youtubedlPath = youtubedl_path
        
        # Set the Timer
        self._app_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._onTimer, self._app_timer)
        self._app_timer.Start(1000)

        # add main show info
        defaultWelcomePage = os.path.join(get_data_dir(), "index.html")
        print defaultWelcomePage
        self.htmlView = wx.html2.WebView.New(self, url=defaultWelcomePage, size=__splash_min_size__, 
            backend=wx.html2.WebViewBackendDefault, style=wx.FRAME_FLOAT_ON_PARENT | wx.STAY_ON_TOP, 
            name="splashMainWindow")    # todo: remove the scroll bar
        # self.htmlView.LoadURL(__splash_ad_url__)
        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_LOADED, self._onHtmlLoaded)
        
        # add skip link
        self._skipLinkPanel = wx.Panel(self, -1, style=0)
        self._skipLinkPanel.Bind(wx.EVT_LEFT_UP, self._quickSkip)
        self._skipLinkPanel.SetBackgroundColour("white")

        self._staticSkipLabel = wx.StaticText(self._skipLinkPanel, -1, "skip this splash ")
        self._staticSkipLabel.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self._staticSkipLabel.Bind(wx.EVT_LEFT_UP, self._quickSkip)

        self._dynamicSkipLabel = wx.StaticText(self._skipLinkPanel, -1, bytes(self.count_down))
        self._dynamicSkipLabel.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self._dynamicSkipLabel.Bind(wx.EVT_LEFT_UP, self._quickSkip)

        self._homePageLink = hyperlink.HyperLinkCtrl(self._skipLinkPanel, -1, __home_page_name__)
        self._homePageLink.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self._homePageLink.AutoBrowse(False)
        self._homePageLink.EnableRollover(True)
        self._homePageLink.SetUnderlines(False, False, True)
        self._homePageLink.Bind(wx.EVT_LEFT_UP, self._onClickHomepage)

        labelSizer = wx.GridSizer(rows=1, cols=4, hgap=0, vgap=0)
        labelSizer.Add(self._staticSkipLabel, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        labelSizer.Add(self._dynamicSkipLabel, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL, 0)
        labelSizer.Add(wx.StaticText(self._skipLinkPanel, -1), 0, 0, 0)
        labelSizer.Add(self._homePageLink, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        self._skipLinkPanel.SetSizer(labelSizer)

        frameSizer = wx.BoxSizer(wx.VERTICAL) 
        frameSizer.Add(self.htmlView, 1, wx.EXPAND, 0)
        frameSizer.Add(self._skipLinkPanel, 0, wx.EXPAND, 0)

        self.SetSizer(frameSizer)
        self.Center()
        self.SetMinSize(__splash_min_size__)
       

    def _onTimer(self, event):
        if self.count_down>0 :
            self.count_down = self.count_down - 1
            self._dynamicSkipLabel.SetLabel(bytes(self.count_down))
        else:
            self._close()

    def _quickSkip(self, event):
        self._close()

    def _close(self):
        self.Close()
        self._openMainFrame()
        

    def _onHtmlLoaded(self, event):
        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_NAVIGATED, self._onClickHtmlWindow)
        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_NEWWINDOW, self._onClickHtmlWindow)

    def _onClickHtmlWindow(self, event):
        webbrowser.open_new_tab(__splash_ad_url__)
        self.Close()

    def _onClickHomepage(self, event):
        webbrowser.open_new_tab(__home_page_url__)

    def _openMainFrame(self):
        frame = MainFrame(self.optManager, self.logManager)
        frame.Center()
        frame.Show()

        if self.optManager.options["disable_update"] and not os_path_exists(self.youtubedlPath):
            wx.MessageBox(_("Failed to locate youtube-dl and updates are disabled"), _("Error"), wx.OK | wx.ICON_ERROR)
            frame.close()


