#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"菜单", size=(300, 200))
        p = wx.Panel(self)
        menuBar = wx.MenuBar()                                # 添加菜单栏
        menu = wx.Menu()
        menuBar.Append(menu, u"文件")                         # 添加菜单
        menu.Append(1000, u"消息框")                          # 添加子菜单
        menu.AppendSeparator()
        menu.Append(1001, u"退出")
        self.Bind(wx.EVT_MENU, self.OnHello, id=1000)         # 添加菜单事件
        self.Bind(wx.EVT_MENU, self.OnExit, id=1001)
        self.SetMenuBar(menuBar)
        help(wx.TextEntryDialog.__init__)
    def OnHello(self, event):
        wx.MessageBox(u"你好!", u"提示")

    def OnExit(self, event):
        self.Close(True)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()