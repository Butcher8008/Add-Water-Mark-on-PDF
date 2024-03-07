from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

# Creating the canvas with text
my_canvas = canvas.Canvas("canvas_image.pdf", pagesize=letter)
my_canvas.saveState()
my_canvas.rotate(270)
my_canvas.drawCentredString(-10, 10, 'osama')
my_canvas.restoreState()
my_canvas.save()

# Read the PDF to which watermark needs to be added
reader = PdfReader('m.pdf')
output_pdf = PdfWriter()

for page in reader.pages:
    # Read watermark PDF
    water_mark = PdfReader('canvas_image.pdf')
    water_mark_page = water_mark.pages[0]
    print(water_mark_page)
    water_mark_page.rotate = (90)

    # Merge watermark with the page from original PDF
    water_mark_page.merge_page(page)
    output_pdf.add_page(water_mark_page)  # Add merged page to the output PDF

# Write the output PDF
with open('output_pdf.pdf', 'wb') as f:
    output_pdf.write(f)
