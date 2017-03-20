#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import os

def ShowFileDialog():
    filterFile = "Python source (*.py)|*.py| All files (*.*)|*.*"         # 过滤文件
    dialog = wx.FileDialog(None, u"选择文件", os.getcwd(), "", filterFile, wx.OPEN)
    dialog.ShowModal()
    dialog.Destroy()           

if __name__ == "__main__":
    app = wx.PySimpleApp()
    ShowFileDialog()


