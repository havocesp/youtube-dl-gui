import os
import gettext
import wx
import webbrowser
import wx.html
import wx.lib.agw.hyperlink as hyperlink


class Splash(wx.Frame):
    count_down = 5

    def __init__(self):
        print "count down=", Splash.count_down

        wx.Frame.__init__(self, None, title="splash", size=(350,200))

        # Set the Timer
        self._app_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_timer, self._app_timer)
        self._app_timer.Start(1000)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        # bitmap = wx.EmptyBitmap(15,15)
        # self.button = wx.Button(self, -1, "label", size=(30,30), style=wx.NO_BORDER)
        # self.Bind(wx.EVT_BUTTON, self._quick_clost, self.button)
        
        self._skip = wx.StaticText(self, -1, "some txt here")
        # self.Bind(wx.EVT_LEFT_DCLICK, self._quick_clost, self._skip)
        self._skip_link = hyperlink.HyperLinkCtrl(self, -1, "wxPython Main Page", pos=(100, 100), URL="baidu.com")
        self._skip_link.AutoBrowse(False)
        self._skip_link.EnableRollover(True)
        self._skip_link.SetUnderlines(False, False, True)
        self._skip_link.Bind(wx.EVT_LEFT_UP, self._quick_clost)
        

        self.Center()

    def _on_timer(self, event):
        if self.count_down>0 :
            self.count_down = self.count_down - 1

            labelTxt = "cc" + bytes(self.count_down)
            # self.button.SetLabel(labelTxt)
            self._skip.SetLabel(labelTxt)
            print self.count_down
        else:
            # self._close()
            print "done"

    def _quick_clost(self, event):
        self._close()

    def _close(self):
        self.Destroy()


app = wx.App()
frame = Splash()
frame.Show()
app.MainLoop()
