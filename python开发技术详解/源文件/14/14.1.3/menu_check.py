#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx

class MyFrame(wx.Frame):
     def __init__(self):
         wx.Frame.__init__(self, None, -1, u"多级菜单", size=(300, 100))
         p = wx.Panel(self)
         menu = wx.Menu()
         submenu = wx.Menu()
         submenu.AppendCheckItem(-1, u"菜单1")             # 多选标记
         submenu.AppendRadioItem(-1, u"菜单2")             # 单选标记
         menu.AppendMenu(-1, u"子菜单", submenu)           # 添加子菜单
         menuBar = wx.MenuBar()
         menuBar.Append(menu, u"菜单")
         self.SetMenuBar(menuBar)
  
if __name__ == "__main__":
     app = wx.PySimpleApp()
     frame = MyFrame()
     frame.Show()
     app.MainLoop()


