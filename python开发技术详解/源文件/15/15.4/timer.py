#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  wx
import  time

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, size=(320, 100))        
        panel = wx.Panel(self, -1)
        sb = self.CreateStatusBar(2) 
        sb.SetStatusWidths([100, 220])
        self.count = 0
        self.timer = wx.PyTimer(self.Notify)                # 创建定时器
        self.timer.Start(1000)                              # 设置间隔时间                             
        self.inputText = wx.TextCtrl(panel, -1, "", pos = (10,10), size=(50, -1))
        self.inputText2 = wx.TextCtrl(panel, -1, "", pos = (10,10), size=(50, -1))
        btn = wx.Button(panel, -1, u"带参数的定时器")
        btn2 = wx.Button(panel, -1, u"停止")
        self.Bind(wx.EVT_BUTTON, self.OnStart, btn)
        self.Bind(wx.EVT_BUTTON, self.OnStop, btn2)
        sizer = wx.FlexGridSizer(cols=4, hgap=10, vgap=10)
        sizer.Add(self.inputText)
        sizer.Add(self.inputText2)
        sizer.Add(btn)    
        sizer.Add(btn2)
        panel.SetSizer(sizer)
        panel.Fit()
        
    def OnStart(self, evt):
        self.timer2 = wx.CallLater(1000, self.OnCallTimer, 1, 2, 3)  # 带参数的定时器
        
    def OnStop(self, evt):
        self.timer2.Stop()                                  # 停止定时器
        self.inputText2.Value = str(self.timer2.GetResult())# 返回参数的计算结果
        del self.timer2
           
    def OnCallTimer(self, *args, **kw):
        self.count = self.count + 1
        self.inputText.Value = str(self.count)       
        tup = args
        total = 0
        for x in tup:
            total = total + int(x)
        self.timer2.Restart(1000, total)                    # 重新启动定时器
        return total

    def Notify(self):
        t = time.localtime(time.time())
        self.SetStatusText(u"定时器", 0) 
        self.SetStatusText(time.strftime("%d-%B-%Y %I:%M:%S", t), 1) 

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()



