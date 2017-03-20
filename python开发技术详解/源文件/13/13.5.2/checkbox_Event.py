#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'多选框', size=(120, 200))
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, u"你喜欢的水果：", (10, 10), (100, 20))
        self.checkBox1 = wx.CheckBox(panel, -1, u"苹果", (10, 30), (100, 20))
        self.checkBox2 = wx.CheckBox(panel, -1, u"香蕉", (10, 50), (100, 20))
        self.checkBox3 = wx.CheckBox(panel, -1, u"西瓜", (10, 70), (100, 20))
        self.checkBox4 = wx.CheckBox(panel, -1, u"桔子", (10, 90), (100, 20))
        self.allCheckBox = wx.CheckBox(panel, -1, u"全选", (10, 110), (100, 20))
        self.selectFlag = True                                         # 判断全选是否选中
        self.fruit = []                                                # 存放选中的水果
        self.button = wx.Button(panel, -1, u"查看", (10, 140), (100, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)            # 注册checkbox的选择事件
        for checkBox in [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4]:
            self.Bind(wx.EVT_CHECKBOX, self.OnSelectSingle, checkBox)
        self.Bind(wx.EVT_CHECKBOX, self.OnSelect, self.allCheckBox)

    def OnSelectSingle(self, event):
        checkBoxSelected = event.GetEventObject()
        if checkBoxSelected.IsChecked():
            self.fruit.append(checkBoxSelected.GetLabelText())
        else:
            self.fruit.remove(checkBoxSelected.GetLabelText())
            self.selectFlag = not self.selectFlag

    def OnSelect(self, event):
        self.fruit = []
        for checkBox in [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4]:
            checkBox.SetValue(self.selectFlag)
        if self.allCheckBox.IsChecked():
            for checkBox in [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4]:
                self.fruit.append(checkBox.GetLabelText())
                checkBox.Disable()
        else:
            for checkBox in [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4]:
                checkBox.Enable()
        self.selectFlag = not self.selectFlag

    def OnClick(self, event):
        str = "".join(self.fruit)                                 # 获取checkbox的文本值
        wx.MessageBox(str.encode("cp936"), u"提示")                # 输出中文对话框

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CheckBoxFrame().Show()
    app.MainLoop()

