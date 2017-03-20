#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

class App: #第四行，自定义了一个App类
    def __init__(self, master): #定义窗体
        frame = Frame(master)
        frame.pack()

        self.hello = Button(frame, text="Hello",
        		command=self.hello)
        self.hello.pack(side=LEFT) 
        
        self.quit = Button(frame, text="Quit", fg="red", 
        		command=frame.quit)
        self.quit.pack(side=RIGHT)

    def hello(self):
        print "Hello,world!"

root = Tk()
root.wm_title("Hello") #设置标题
root.wm_minsize(200, 200) #设置窗口大小

app = App(root)

root.mainloop()
