#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from wx import xrc

class MyApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource('clipboard.xrc') #从XRC文件中读取界面描述
        self.init_frame()
        return True

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'MyFrame2')
        self.panel = xrc.XRCCTRL(self.frame, 'm_Panel1')
        self.text1 = xrc.XRCCTRL(self.panel, 'm_textCtrl4')
        self.text2 = xrc.XRCCTRL(self.panel, 'm_textCtrl5')
        self.frame.Bind(wx.EVT_BUTTON, self.OnCopy, id=xrc.XRCID('m_button6')) #绑定事件
        self.frame.Bind(wx.EVT_BUTTON, self.OnPaste, id=xrc.XRCID('m_button7')) #绑定事件
        self.frame.Bind(wx.EVT_BUTTON, self.OnQuit, id=xrc.XRCID('m_button8')) #绑定事件
        self.frame.Show()

    def OnQuit(self, event):
        self.frame.Close(True)

    def OnCopy(self, event): #复制数据到剪贴板中
        data = wx.TextDataObject()
        data.SetText(self.text1.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(data) 
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("不能打开剪贴板", "错误")

    def OnPaste(self, event): #从剪贴板中读取数据
        data = wx.TextDataObject()
        success = False
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(data) 
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("不能打开剪贴板", "错误")

        if success:
            self.text2.SetValue(data.GetText())
        else:
            wx.MessageBox("格式不匹配", "错误")

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
