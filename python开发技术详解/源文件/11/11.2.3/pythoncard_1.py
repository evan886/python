#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PythonCard import model

class Minimal(model.Background):
    pass

if __name__ == '__main__':
    app = model.Application(Minimal)
    app.MainLoop()
