#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET

try:
    ET.parse("xml_1.xml")
    print u"这是一个良构的XML文档"
except Exception, e:
    print u"这可能是一个非良构文档"
    print u"出错信息: ",e
