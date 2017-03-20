#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text', size = (100, 75))
        panel = wx.Panel(self, -1)
        text = wx.StaticText(panel, -1, "Hello world!", (10, 10), (80, 15))   
        font = wx.Font(12, wx.DEFAULT, wx.ITALIC, wx.NORMAL, True)      # 创建字体类型
        text.SetFont(font)                                              # 设置字体

if __name__ == '__main__': 
    app = wx.PySimpleApp() 
    frame = TextFrame() 
    frame.Show() 
    app.MainLoop() 