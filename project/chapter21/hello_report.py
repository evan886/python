from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s  = String(50, 50, "Hello, World!",textAnchor='middle')

d.add(s)
ss=drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
renderPDF.drawToFile(d, "hello_report.pdf", "Hello Report")

renderPDF.drawToFile(d, "hello_report.pdf", "Hello Report")