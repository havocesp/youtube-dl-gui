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


class AdBarPanel(wx.Panel):
    def __init__(self, parent, rootFrame, opt_manager):
        wx.Panel.__init__(self, parent, -1, style=0)
        self._parent = parent
        self._rootFrame = rootFrame
        self._optManager = opt_manager
        
        # add main show info
        defaultAdBarPage = os.path.join(get_data_dir(), "adBar.html")

        self.htmlView = wx.html2.WebView.New(self, url=defaultAdBarPage, size=self._optManager.options["ad_bar_min_size"], 
            backend=wx.html2.WebViewBackendDefault, style=0, 
            name="adBarMainWindow")    
        # self.htmlView.LoadURL(self._optManager.options["ad_bar_url"])

        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_LOADED, self._onHtmlLoaded)

        frameSizer = wx.BoxSizer(wx.VERTICAL) 
        frameSizer.Add(self.htmlView, 0, wx.EXPAND, 0)
        self._frameSizer = frameSizer
        self.SetSizer(frameSizer)
        self.SetMinSize(self._optManager.options["ad_bar_min_size"])


    def _close(self):
        self.Close()

    def _onHtmlLoaded(self, event):
        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_NAVIGATED, self._onClickHtmlWindow)
        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_NEWWINDOW, self._onClickHtmlWindow)

    def _onClickHtmlWindow(self, event):
        url = event.GetURL()
        webbrowser.open_new_tab(url)
        self._removeAdBar()

    def _removeAdBar(self):
        # the adBar always is the lastest item
        adBarIndex = self._rootFrame._mainPanelSizer.GetItemCount() - 1
        self._rootFrame._mainPanelSizer.Remove(adBarIndex)
        self._rootFrame._mainPanelSizer.Layout()
        self._close()
        
        
        



