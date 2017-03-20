#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx 
import wx.grid as grid 

class OddEvenTable(grid.PyGridTableBase): 
    def __init__(self): 
        grid.PyGridTableBase.__init__(self) 
        self.odd = grid.GridCellAttr()                  # 获取奇数行
        self.odd.SetBackgroundColour("yellow") 
        self.even = grid.GridCellAttr()                 # 获取偶数行                

    def GetAttr(self, row, col, kind):                  # 对每个单元格进行控制
        attr = [self.even, self.odd][row % 2] 
        attr.IncRef() 
        return attr 
     
    def GetNumberRows(self): 
        return 10

    def GetNumberCols(self): 
        return 10

    def GetValue(self, row, col):                       # Grid类的SetTable()被调用时，此方法被调用
        return str(col) 

    def SetValue(self, row, col, value):                # 当对单元格设置值时，此方法被调用
        print (row, col, value)

class MyFrame(wx.Frame): 
    def __init__(self): 
        wx.Frame.__init__(self, None, -1, u"表格的方法", size=(900,250)) 
        gd = grid.Grid(self) 
        table = OddEvenTable()
        gd.SetTable(table, True) 

if __name__ == '__main__': 
    app = wx.PySimpleApp() 
    frame = MyFrame() 
    frame.Show() 
    app.MainLoop() 



