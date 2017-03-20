#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class PopupFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"弹出式菜单", size=(200, 75))
        self.panel = wx.Panel(self)
        self.textCtrl = wx.TextCtrl(self.panel, -1, pos=(10, 10))
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        self.popupmenu = wx.Menu()
        menuList = [u"菜单1", u"菜单2", u"菜单3"]
        for menuitem in menuList:
            item = self.popupmenu.Append(-1, menuitem)
            self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)      # 菜单项选择事件
            self.textCtrl.Bind(wx.EVT_CONTEXT_MENU, self.OnPopup)       # 在文本框中绑定弹出式菜单

    def OnPopup(self, event):
        pos = self.panel.ScreenToClient(event.GetPosition())            # 获取鼠标的坐标
        self.panel.PopupMenu(self.popupmenu, pos)

    def OnPopupItemSelected(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        self.textCtrl.SetLabel(item.GetText())

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = PopupFrame()
    frame.Show()
    app.MainLoop()
