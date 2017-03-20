#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.gizmos as gizmos

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"树表控件", size=(400, 400))
        # 创建树表控件
        self.tree = gizmos.TreeListCtrl(self, -1, style = wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT)
        self.il = wx.ImageList(16, 16, True)
        # 给树表添加图标
        self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16,16)))
        self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, (16,16)))
        self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16,16)))
        self.tree.SetImageList(self.il)
        # 添加树表的列
        self.tree.AddColumn(u"第1列")
        self.tree.AddColumn(u"第2列")
        self.tree.AddColumn(u"第3列")
        self.tree.SetColumnWidth(0, 186)
        self.root = self.tree.AddRoot("root")
        self.tree.SetItemText(self.root, "", 1)             # 设置第2列第1行单元格的文本
        self.tree.SetItemText(self.root, "", 2)             # 设置第3列第1行单元格的文本
        for x in range(5):                                  # 设置子节点的文本和图标
            child = self.tree.AppendItem(self.root, str(x))
            self.tree.SetItemText(child, str(x), 0)
            self.tree.SetItemText(child, str(x), 1)
            self.tree.SetItemText(child, str(x), 2)
            self.tree.SetItemImage(child, 0, which = wx.TreeItemIcon_Normal)
            self.tree.SetItemImage(child, 1, which = wx.TreeItemIcon_Expanded)
            for y in range(5):
                last = self.tree.AppendItem(child, str(y))
                self.tree.SetItemText(last, str(x) + "-" + str(y), 0)
                self.tree.SetItemText(last, str(x) + "-" + str(y), 1)
                self.tree.SetItemText(last, str(x) + "-" + str(y), 2)
                self.tree.SetItemImage(last, 0, which = wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(last, 1, which = wx.TreeItemIcon_Expanded)
        self.tree.Expand(self.root)       

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()



