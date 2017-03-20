#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.html as html

page = u'<html><body bgcolor="#8e8e95"><table cellspacing="5" border="0" width="250"> \
<tr width="200" align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;特征量</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>数值</b></td> \
</tr> \
<tr width="200" align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;最大值</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>9000</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;最小值</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>3000</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;中间值</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>5000</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;平均值</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>5666</b></td> \
</tr> \
</body></table></html>'

class MyFrame(wx.Frame):
    def __init__(self, parent): #生成窗口
        wx.Frame.__init__(self, parent, -1, u"统计窗口", size=(300, 300)) 
        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        htmlwin = html.HtmlWindow(panel, -1, style=wx.NO_BORDER)
        htmlwin.SetPage(page)

        vbox.Add((-1, 10), 0)
        vbox.Add(htmlwin, 1, wx.EXPAND | wx.ALL, 9)
        bitmap = wx.StaticBitmap(panel, -1, wx.Bitmap('./wxPython.jpg'))
        hbox.Add(bitmap, 1, wx.LEFT | wx.BOTTOM | wx.TOP, 10)
        buttonOk = wx.Button(panel, wx.ID_CLOSE, u'确定')
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=wx.ID_CLOSE)
        hbox.Add((100, -1), 1, wx.EXPAND | wx.ALIGN_RIGHT)
        hbox.Add(buttonOk, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)
        panel.SetSizer(vbox)
        self.Centre()

    def OnClose(self, event):
        self.Close()

app = wx.App()
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()