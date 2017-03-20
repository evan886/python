#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
 
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"位图菜单", size=(300, 100))
        p = wx.Panel(self)
        menu = wx.Menu()
        bmp = wx.Bitmap("previous.png", wx.BITMAP_TYPE_PNG)
        item = wx.MenuItem(menu, -1, u"位图1")
        item.SetBitmap(bmp)                     # 给菜单增加位图
        menu.AppendItem(item)
        bmp = wx.Bitmap("next.png", wx.BITMAP_TYPE_PNG)
        item = wx.MenuItem(menu, -1, u"位图2")
        item.SetBitmap(bmp)                     # 给菜单增加位图        
        menu.AppendItem(item)
        menuBar = wx.MenuBar()
        menuBar.Append(menu, u"菜单")
        self.SetMenuBar(menuBar)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()