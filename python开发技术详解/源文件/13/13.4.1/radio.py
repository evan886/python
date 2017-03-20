#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class RadioFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'单选框', size=(200, 150))
        panel = wx.Panel(self, -1)
        radioRed = wx.RadioButton(panel, -1, u"红", pos=(10, 10))
        radioBlue = wx.RadioButton(panel, -1, u"蓝", pos=(10, 40))
        radioGreen = wx.RadioButton(panel, -1, u"绿", pos=(10, 70))
        # 建立颜色和wx常量的对应关系
        self.colors = {"红": wx.RED, "蓝": wx.BLUE, "绿": wx.GREEN}
        self.textColor = wx.TextCtrl(panel, -1, "", pos=(80, 10))

        for eachRadio in [radioRed, radioBlue, radioGreen]:          # 注册Radio事件
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)

    def OnRadio(self, event):
        radioSelected = event.GetEventObject()                       # 返回选中的Radio
        str = radioSelected.GetLabel()
        # 选择Radio的背景颜色
        self.textColor.SetBackgroundColour(self.colors[str.encode("UTF-8")])
        self.textColor.SetFocus()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    RadioFrame().Show()
    app.MainLoop()