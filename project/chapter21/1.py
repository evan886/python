# -*- coding: utf-8 -*-
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

# run with python3
d = Drawing(100, 100)
s = String(50, 50, "my love", textAnchor="middle")

d.add(s)

renderPDF.drawToFile(d, "evan.pdf", "evan simple PDF file")
