#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'自定义窗口', size=(300, 200))
        png_save = wx.Image('./icons/save_page.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        png_home = wx.Image('./icons/go_home.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        png_cfg = wx.Image('./icons/settings.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        png_forward = wx.Image('./icons/go_forward.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        png_back = wx.Image('./icons/go_back.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()        
        toolbar = self.CreateToolBar(wx.TB_HORIZONTAL | wx.TB_TEXT)     # 创建工具栏   
        toolbar.AddSimpleTool(100, png_save, "Save page")
        toolbar.AddSimpleTool(200, png_home, "Go home")
        toolbar.AddSimpleTool(220, png_back, "Go back")
        toolbar.AddSimpleTool(230, png_forward, "Go Forward")
        toolbar.AddSimpleTool(400, png_cfg, "Settings")
        toolbar.Realize()
        self.CreateStatusBar()                                          # 创建状态栏

if __name__ == '__main__':
    app = wx.PySimpleApp()
    myFrame = MyFrame()
    myFrame.Show()
    app.MainLoop()