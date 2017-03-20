#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"菜单快捷键", size=(300, 100))
        p = wx.Panel(self)
        menu = wx.Menu()       
        exit = menu.Append(-1, u"&x退出")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        menuBar = wx.MenuBar()
        menuBar.Append(menu, u"&m菜单")  
        self.SetMenuBar(menuBar)

    def OnExit(self, event):
        self.Close()
        

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()





    
