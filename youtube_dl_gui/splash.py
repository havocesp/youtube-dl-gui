import os
import gettext
import wx
import webbrowser
import wx.html
import wx.html2
import wx.lib.agw.hyperlink as hyperlink
import wx.lib.buttons as buttons
import wx.stc as stc


class Splash(wx.Frame):
    count_down = 5

    def __init__(self):
        print "count down=", Splash.count_down
        wx.Frame.__init__(self, None, title="splash", size=(560, 360))
        
        # Set the Timer
        self._app_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_timer, self._app_timer)
        self._app_timer.Start(1000)

        # add main show info
        self.htmlView = wx.html2.WebView.New(self, size=(560, 360), style=0)    # todo: remove the scroll bar
        self.htmlView.LoadURL("http://cn.bing.com")
        
        # add skip link
        self._skipLinkPanel = wx.Panel(self, -1, style=0)
        self._skipLinkPanel.Bind(wx.EVT_LEFT_UP, self._quick_clost)
        self._skipLinkPanel.SetBackgroundColour("white")

        self._staticSkipLabel = wx.StaticText(self._skipLinkPanel, -1, "skip this splash ")
        self._staticSkipLabel.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self._staticSkipLabel.Bind(wx.EVT_LEFT_UP, self._quick_clost)

        self._dynamicSkipLabel = wx.StaticText(self._skipLinkPanel, -1, bytes(self.count_down))
        self._dynamicSkipLabel.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self._dynamicSkipLabel.Bind(wx.EVT_LEFT_UP, self._quick_clost)

        self._homePageLink = hyperlink.HyperLinkCtrl(self._skipLinkPanel, -1, "www.get-more.com")
        self._homePageLink.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self._homePageLink.AutoBrowse(False)
        self._homePageLink.EnableRollover(True)
        self._homePageLink.SetUnderlines(False, False, True)
        self._homePageLink.Bind(wx.EVT_LEFT_UP, self._quick_clost)

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
        self.SetMinSize((560, 360))
       

    def _on_timer(self, event):
        if self.count_down>0 :
            self.count_down = self.count_down - 1

            labelTxt = "cc" + bytes(self.count_down)
            self._dynamicSkipLabel.SetLabel(bytes(self.count_down))
            print self.count_down
        else:
            # self._close()
            print "done"

    def _quick_clost(self, event):
        self._close()

    def _close(self):
        self.Destroy()

    def _onClickHtmlWindow(self, event):
        print "some occur"


app = wx.App()
frame = Splash()
frame.Show()
app.MainLoop()
