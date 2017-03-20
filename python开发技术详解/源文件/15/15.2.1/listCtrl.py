#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import wx
import wx.lib.mixins.listctrl as listmix

data = {1 : ("1", "listctrl", u"列表控件"),
        2 : ("2", "grid", u"表格控件"),
        3 : ("3", "tree", u"树控件"),
        4 : ("4", "timer", u"定时器控件")
       }


class MyListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)           # 使列的宽度与ListCtrl的宽度自动对齐
        self.setColumns()

    def setColumns(self):
        # 定义列头
        self.InsertColumn(0, u"第1列")
        self.InsertColumn(1, u"第2列")
        self.InsertColumn(2, u"第3列")
        # 设置各列中的值
        items = data.items()
        for key, values in items:            
            #    InsertStringItem(self, long index, String label, int imageIndex=-1) -> long
            index = self.InsertStringItem(sys.maxint, values[0])
            for i in range(len(values)):
                self.SetStringItem(index, i, values[i])
        # 设置列的宽度
        self.SetColumnWidth(0, 100)
        self.SetColumnWidth(1, 100)
        # 第3列的宽度自动对齐
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"列表控件", size=(400, 200))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.list = MyListCtrl(self, -1, style=wx.LC_REPORT)
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
