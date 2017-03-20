#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

data = ["1",
       ["2", ["2-1", "2-2", ["2-3", ["2-3-1", "2-3-2"]]]],
       ["3", ["3-1", "3-2"]],
       ["4", ["4-1", "4-2", "4-3"]],
        "5"]

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"树型控件", size=(200, 300))
        self.tree = wx.TreeCtrl(self)                   # 创建树型控件  
        root = self.tree.AddRoot("root")                # 添加根节点 
        self.AddTreeNodes(root, data)                   # 添加子节点     
        self.tree.Expand(root)                          # 展开根节点              

    def AddTreeNodes(self, parent, tree):
        for node in tree:
            if type(node) == str:                       # 当前节点为子节点时直接添加
                self.tree.AppendItem(parent, node)
            else:
                item = self.tree.AppendItem(parent, node[0])
                self.AddTreeNodes(item, node[1])        # 递归添加子节点
              
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()




