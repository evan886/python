#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
    def hello(self, widget, data=None): #自定义的回调函数
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        print "delete event"
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self): #构建特定的窗口部件
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.connect("delete_event", self.delete_event)

        self.window.connect("destroy", self.destroy)

        self.window.set_border_width(10)

        self.button = gtk.Button("Hello World")

        self.button.connect("clicked", self.hello, None)

        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        self.window.add(self.button)

        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()

