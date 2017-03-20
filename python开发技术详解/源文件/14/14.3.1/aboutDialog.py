#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"自定义对话框", size=(300, 200))
        MenuHelp = wx.Menu()
        aboutMenu = MenuHelp.Append(-1, u"关于(&A)")
        menuBar = wx.MenuBar()
        menuBar.Append(MenuHelp, u"帮助(&H)")        
        self.Bind(wx.EVT_TOOL, self.ShowAboutDlg, aboutMenu)
        self.SetMenuBar(menuBar)

    def ShowAboutDlg(self, event):
        pos = self.GetPosition()
        dialog = MyDialog(self, -1, u"关于")
        dialog.SetPosition((pos[0] + 100, pos[1] + 60))

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(100,100))        
        self.panel = wx.Panel(self)    
        self.OkBtn = wx.Button(self, 10, u"确定", pos=(8,20),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.CloseDlg, self.OkBtn)
    	self.Show()
        #self.ShowModal()

    def CloseDlg(self, event):
    	self.Close()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()



