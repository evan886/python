#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"对话框", size=(300, 100))
        button = wx.Button(self, wx.ID_OK, u"退出", pos=(10, 10))
        button.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)

    def OnClick(self, event):
        # 创建选择对话框
        dlg = wx.MessageDialog(None, u"是否退出？", u"退出", wx.YES_NO | wx.ICON_QUESTION)
        # 判断用户选择的返回值
        if (dlg.ShowModal() == wx.ID_YES):
            frame.Close()
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


