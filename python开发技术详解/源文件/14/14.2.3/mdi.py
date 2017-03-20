#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MDIFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, u"MDI窗口", size=(300,200))
        menubar = wx.MenuBar()                               # 添加菜单栏
        menu = wx.Menu()                                     # 添加菜单
        menu.Append(5000, u"新建(&N)")                        # 添加子菜单
        menu.Append(5001, u"退出(&X)")
        menubar.Append(menu, u"文件(&F)")
        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=5000)    # 绑定菜单项的事件
        self.Bind(wx.EVT_MENU, self.OnExit, id=5001)
        self.SetMenuBar(menubar)

    def OnExit(self, evt):
        self.Close(True)

    def OnNewWindow(self, evt):
        win = wx.MDIChildFrame(self, -1, u"子窗口")           # 新建子窗口
        win.Show(True)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MDIFrame()
    frame.Show()
    app.MainLoop()