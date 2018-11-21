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
    __ad_bar_url__,
    __ad_bar_min_size__,
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


class AdBarPanel(wx.Panel):
    def __init__(self, parent, rootFrame):
        wx.Panel.__init__(self, parent, -1, style=0)
        self._parent = parent
        self._rootFrame = rootFrame
        
        # add main show info
        defaultAdBarPage = os.path.join(get_data_dir(), "adBar.html")

        self.htmlView = wx.html2.WebView.New(self, url=defaultAdBarPage, size=__ad_bar_min_size__, 
            backend=wx.html2.WebViewBackendDefault, style=0, 
            name="adBarMainWindow")    
        # self.htmlView.LoadURL(__ad_bar_url__)

        self.htmlView.Bind(wx.html2.EVT_WEBVIEW_LOADED, self._onHtmlLoaded)

        frameSizer = wx.BoxSizer(wx.VERTICAL) 
        frameSizer.Add(self.htmlView, 0, wx.EXPAND, 0)
        self.SetSizer(frameSizer)
        self.SetMinSize(__ad_bar_min_size__)


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
        self._rootFrame._adBarPanel.Close()
        self._rootFrame._mainPanelSizer.Layout()
        
        



