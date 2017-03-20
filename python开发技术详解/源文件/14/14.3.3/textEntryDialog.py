#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "TextEntryDialog", size=(300, 100))
        panel = wx.Panel(self, -1)
        self.textCtrl = wx.TextCtrl(panel, -1, "", pos=(10,10), style=wx.TE_PROCESS_ENTER)
        self.textCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnClick, self.textCtrl)

    def OnClick(self, evt):
        # 创建文本对话框      
        self.dialog = wx.TextEntryDialog(None, u"输入文本", u"文本对话框", "", style=wx.OK|wx.CANCEL)
        if self.dialog.ShowModal() == wx.ID_OK:
            self.textCtrl.SetLabel(self.dialog.GetValue())        # 获取输入文本的内容

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
