#coding:utf-8
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
#用py3 执行是可以的 100*100像素大小的pdf格式图形中间
d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, 'evan1.pdf', 'A simple PDF file')
