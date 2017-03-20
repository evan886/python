#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'按钮', size=(300, 75))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, u"确定", pos=(10, 10))                          # 创建按钮
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()                                                          # 设置缺省按钮
        self.inputText = wx.TextCtrl(panel, -1, "", pos = (100,10), size=(150, -1), style=wx.TE_READONLY)

    def OnClick(self, event):
        self.inputText.Value = "Hello world!"

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()