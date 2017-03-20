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

    def OnCopy(self, event):
        pass

    def OnPaste(self, event):
        pass

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
