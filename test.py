from PyPDF2 import PdfReader 
from PyPDF2 import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
reader = PdfReader('m.pdf')
for page in range(len(reader.pages)):
    text= reader.pages[page].extract_text()
c=canvas.Canvas('try.pdf', pagesize=A4, )
c.drawCentredString(inch,inch, text)
c.save()