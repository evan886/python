#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"菜单的事件", size=(300, 200))
        p = wx.Panel(self)
        self.mainMenu = wx.Menu()
        self.mainMenu.Append(1000, u"退出")
        setMenu = wx.Menu()
        subSetMenu = setMenu.Append(1001, u"打开/屏蔽菜单")
        self.Bind(wx.EVT_MENU, self.OnExit, id = 1000)
        self.Bind(wx.EVT_MENU_HIGHLIGHT, self.OnItemSelected, id = 1000)
        self.Bind(wx.EVT_MENU, self.OnEnable, subSetMenu)
        menuBar = wx.MenuBar()
        menuBar.Append(self.mainMenu, u"主菜单")
        menuBar.Append(setMenu, u"设置")
        self.SetMenuBar(menuBar)

    def OnEnable(self, event):
        menubar = self.GetMenuBar()
        enabled = menubar.IsEnabled(1000)                        # 获取菜单的enable属性
        self.mainMenu.Enable(1000, not enabled)                  # 设置菜单的enable选项

    def OnExit(self, event):
        self.Close()
    
    def OnItemSelected(self, event):                             # 当菜单高亮时返回菜单的名称
        item = self.GetMenuBar().FindItemById(event.GetId())     # 获取菜单项   

        wx.MessageBox(u"菜单：%s" % item.GetText())

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()