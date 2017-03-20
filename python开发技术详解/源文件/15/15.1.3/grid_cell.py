#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx 
import wx.grid as grid 

class SimpleGrid(grid.Grid):
    def __init__(self, parent): 
        grid.Grid.__init__(self, parent, -1) 
        self.CreateGrid(8, 4)
        self.EnableEditing(True) 

        self.SetColLabelValue(0, u"第1列")                                   # 设置行标题
        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)            
        self.SetRowLabelValue(0, u"第1行")                                   # 设置列标题
        self.SetRowLabelAlignment(wx.ALIGN_RIGHT, wx.ALIGN_BOTTOM) 

        self.SetCellValue(0, 0, "Hello")                                     
        self.SetCellTextColour(0, 0, wx.RED) 
        self.SetCellFont(0, 0, wx.Font(10, wx.ROMAN, wx.ITALIC, wx.NORMAL))  # 设置单元格的字体

        self.SetCellValue(1, 0, "Read Only") 
        self.SetReadOnly(1, 0, True)                                         # 设置只读单元格
        self.SetCellBackgroundColour(1, 0, wx.RED)                           # 设置单元格的背景颜色

        self.SetCellEditor(2, 0, grid.GridCellNumberEditor(1, 10))           # 嵌入数字选择控件
        self.SetCellValue(2, 0, "1") 
        self.SetCellEditor(2, 1, grid.GridCellFloatEditor(0, 1))             # 嵌入浮点数编辑控件
        self.SetCellValue(2, 1, "10.19") 

        attr = grid.GridCellAttr()                          
        attr.SetTextColour(wx.BLUE) 
        self.SetColAttr(1, attr)                                             # 设置一列的单元格属性

        self.SetCellAlignment(5, 1, wx.ALIGN_CENTRE, wx.ALIGN_BOTTOM)        
        self.SetCellValue(5, 1, u"跨行、列的单元格")
        self.SetCellSize(5, 1, 2, 2)                                         # 设置跨行、列的单元格

        self.SetCellEditor(6, 0, grid.GridCellChoiceEditor(["one", "two", "three"])) # 嵌入下拉列表
        self.SetCellValue(6, 0, "one")

        self.SetCellEditor(7, 0, grid.GridCellBoolEditor()) # 嵌入下拉列表
        self.SetCellValue(7, 0, "True")

class MyFrame(wx.Frame): 
    def __init__(self): 
        wx.Frame.__init__(self, None, -1, u"单元格的设置", size=(450,250)) 
        self.grid = SimpleGrid(self) 

if __name__ == '__main__': 
    app = wx.PySimpleApp()
    frame = MyFrame() 
    frame.Show() 
    app.MainLoop() 



