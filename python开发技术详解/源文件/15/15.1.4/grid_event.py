#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.grid as grid
import pprint

class MyGrid(grid.Grid):
    def __init__(self, parent):
        grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(5, 5)
        # 表格的事件
        self.Bind(grid.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)   # 当单击鼠标左键时触发
        self.Bind(grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick) # 当单击鼠标右键时触发
        self.Bind(grid.EVT_GRID_SELECT_CELL, self.OnSelectCell)          # 当选择单元格时触发
        self.Bind(grid.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)        # 当选择多个单元格时触发
        self.Bind(grid.EVT_GRID_CELL_CHANGE, self.OnCellChange)          # 当单元格的内容改变时触发
        # 当编辑单元格时触发的事件
        self.Bind(grid.EVT_GRID_EDITOR_SHOWN, self.OnEditorShown)        
        self.Bind(grid.EVT_GRID_EDITOR_HIDDEN, self.OnEditorHidden)
        self.Bind(grid.EVT_GRID_EDITOR_CREATED, self.OnEditorCreated)
        # 响应键盘输入
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def OnCellLeftClick(self, evt):
        print "(%d, %d)"%(evt.GetRow(), evt.GetCol())
        evt.Skip()

    def OnCellRightClick(self, evt):
        wx.MessageBox("%s"%(evt.GetPosition()), u"提示")
        evt.Skip()

    def OnRangeSelect(self, evt):
        if evt.Selecting():
            print "(%s, %s)"%(evt.GetTopLeftCoords(), evt.GetBottomRightCoords())
        evt.Skip()

    def OnCellChange(self, evt):
        value = self.GetCellValue(evt.GetRow(), evt.GetCol())
        print value

    def OnSelectCell(self, evt):
        self.SetCellBackgroundColour(evt.GetRow(), evt.GetCol(), wx.RED) 
        evt.Skip()

    def OnEditorShown(self, evt):
        print "show"
        evt.Skip()

    def OnEditorHidden(self, evt):
        print "hidden"
        evt.Skip()

    def OnEditorCreated(self, evt):
        print evt.GetControl()
        evt.Skip()

    def OnKeyDown(self, evt):
        value = evt.GetPosition()
        pp = pprint.PrettyPrinter()
        pp.pprint(value)
        print "KeyCode:" + str(evt.GetKeyCode())
        evt.Skip()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"表格的事件", size=(500,180))
        self.grid = MyGrid(self)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()



