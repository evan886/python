#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.html as html

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"HTML窗口", size=(500, 300))
        self.html = HtmlPanel(self, -1)
        self.html.LoadUrl("contents.html")           # 导入HTML页面

    def OnCloseWindow(self, event):
        self.Destroy()

class HtmlPanel(html.HtmlWindow):
    def __init__(self, parent, id):
        html.HtmlWindow.__init__(self, parent, id, style=wx.NO_FULL_REPAINT_ON_RESIZE)
    
    def LoadUrl(self, url):
	    self.LoadPage(url)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    myFrame = MyFrame()
    myFrame.Show()
    app.MainLoop()