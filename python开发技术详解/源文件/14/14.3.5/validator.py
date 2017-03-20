#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"对话框的验证", size=(300, 60))
        panel = wx.Panel(self, -1)
        sizer = wx.BoxSizer(wx.HORIZONTAL)   
        self.addTextCtrl = wx.TextCtrl(panel, -1, "", pos=(10,10))
        addStaticText = wx.StaticText(panel, -1, "+")
        self.addTextCtrl2 = wx.TextCtrl(panel, -1, "")   
        btn = wx.Button(panel, -1, u"计算")
        btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
        sizer.Add(self.addTextCtrl)
        sizer.Add(addStaticText)
        sizer.Add(self.addTextCtrl2)
        sizer.Add(btn)
        panel.SetSizer(sizer)
        panel.Fit()       

    def OnClick(self, event):
        data = {0:self.addTextCtrl.GetValue(), 1:self.addTextCtrl2.GetValue()}
        dlg = MyDialog(data)
        dlg.ShowModal()
        dlg.Destroy()

        
class DataValidator(wx.PyValidator):        # 对话框的验证器
     def __init__(self, data, key):
         wx.PyValidator.__init__(self)
         self.data = data
         self.key = key

     def Clone(self):                       # Clone()方法必须实现
         return DataValidator(self.data, self.key)

     def Validate(self, win):               # 验证数据
         return True

     def TransferToWindow(self):            # 对话框打开时调用
         textCtrl = self.GetWindow()
         textCtrl.SetValue(self.data.get(self.key, ""))
         return True 

     def TransferFromWindow(self):          # 对话框关闭时调用
         return True

class MyDialog(wx.Dialog):
    def __init__(self, data):
        wx.Dialog.__init__(self, None, -1, u"验证器")
        addStaticText  = wx.StaticText(self, -1, u"数字1：")
        addStaticText2 = wx.StaticText(self, -1, u"数字2：")
        self.addTextCtrl  = wx.TextCtrl(self, validator=DataValidator(data, 0))     # 添加验证
        self.addTextCtrl2 = wx.TextCtrl(self, validator=DataValidator(data, 1))        
        btn = wx.Button(self, wx.ID_OK, u"确定")
        btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
        btn.SetDefault()
        sizer = wx.BoxSizer(wx.VERTICAL)       
        gridSizer = wx.FlexGridSizer(2, 2, 5, 5)
        gridSizer.Add(addStaticText, 0, wx.ALIGN_LEFT)
        gridSizer.Add(self.addTextCtrl, 0, wx.EXPAND)
        gridSizer.Add(addStaticText2, 0, wx.ALIGN_LEFT)
        gridSizer.Add(self.addTextCtrl2, 0, wx.EXPAND)
        sizer.Add(gridSizer, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(btn, 0, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def OnClick(self, event):
        result = float(self.addTextCtrl.GetValue()) + float(self.addTextCtrl2.GetValue())
        wx.MessageBox(str(result),u"结果")
        self.Close()
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


