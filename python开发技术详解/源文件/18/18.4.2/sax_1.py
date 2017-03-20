#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.sax import *

class MyHandler(ContentHandler):
    def startDocument(self) :#开始处理文档的时候调用
        print "开始处理XML文档"
        print "==============="
        print "name\tquality"
        print "---------------"

    def endDocument(self) :#结束处理文档的时候调用
    	print "==============="
        print "结束处理XML文档"

    def startElement( self, name, attrs) :#处理元素
        if name == "shirt":#打印出所有shirt标签的相关属性
        	print "%s\t%s"%(attrs['name'], attrs['quality'])

parser = make_parser() #生成解析对象
parser.setContentHandler(MyHandler()

#需要分析的XML数据
data = """<goods>
			<shirt name="Helen" quality="A" />
			<shirt name="Fayer" quality="A+" />
			<coat name="Dayie" quality="B+" />
			<shirt name="CaC" quality="A-" />
			</goods>
"""
import StringIO
parser.parse(StringIO.StringIO(data))
