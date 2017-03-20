#!/bin/python
#encoding=utf-8

class PythonUtilities(object):
    _public_methods_ = [ 'SplitString' ] #提供的接口名
    
    _reg_progid_ = "Python.Utilities" #注册的ProgID
    
    _reg_clsid_ = "{41E24E95-D45A-11D2-852C-204C4F4F5020}"#注册的CLSID
    
    def SplitString(self, val, item=None):
        import string
        if item != None: item = str(item)
        return string.split(str(val), item)

if __name__=='__main__':
	#注册COM服务组件
    print "Registering COM server..."
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonUtilities)
