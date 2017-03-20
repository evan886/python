#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MDIFrame(wx.MDIParentFrame):                              # 创建MDI窗口
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, u"MDI窗口", size=(600,400))
        menubar = wx.MenuBar()                                  # 添加菜单栏
        self.SetMenuBar(menubar)                                # 提供带有windows的缺省菜单
        help(wx.MDIParentFrame.__init__)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MDIFrame()
    frame.Show()
    app.MainLoop()