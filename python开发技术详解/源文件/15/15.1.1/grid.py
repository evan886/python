#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.grid

class MyFrame(wx.Frame):
    def __init__(self):
        rowTitles = [u"第1行", u"第2行", u"第3行", u"第4行"]
        colTitles = [u"第1列", u"第2列", u"第3列", u"第4列"]
        wx.Frame.__init__(self, None, title=u"表格", size=(450,160))
        grid = wx.grid.Grid(self)                           # 定义表格控件
        grid.CreateGrid(4, 4)
        for row in range(4):
            grid.SetRowLabelValue(row, rowTitles[row])      # 设置行标题
            grid.SetColLabelValue(row, colTitles[row])      # 设置列标题
            for col in range(4):
                grid.SetCellValue(row, col, str(col))       # 设置单元格的值

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()



