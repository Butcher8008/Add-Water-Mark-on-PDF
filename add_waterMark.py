from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter

def makeWatermark(position, user_choice, x_coordinates, y_coordinates):
    text = input("Enter the watermark text here:")
    fontType = input("Enter the font family you want to have the watermark: ")
    fontSize = int(input("Enter the font size of the watermark: "))
    rotation_degree = int(input("Enter the rotation angle of the watermark: "))
    
    pdf = canvas.Canvas("watermark.pdf", trimBox=1000)
    pdf.translate(dx=inch, dy=inch)
    
    if user_choice == 1:
        if position == "topleft":
            x = inch
            y = A4[1] - 200
        elif position == "topright":
            x = A4[0] - 200
            y = A4[1] - 200 
        elif position == "bottomleft":
            x = inch
            y = inch
        elif position == "bottomright":
            x = A4[0] - 200
            y = inch
        else:
            print("Invalid position. Please enter 'topleft', 'topright', 'bottomleft', or 'bottomright'.")
            return
    elif user_choice == 2:
        x = x_coordinates
        y = y_coordinates
    else:
        print("Invalid choice. Please enter 1 for default option or 2 for custom coordinates.")
        return
    
    pdf.setFillColor(colors.grey, alpha=0.6)
    pdf.setFont(psfontname=fontType, size=fontSize)
    pdf.rotate(rotation_degree)
    pdf.drawCentredString(x, y, text)
    pdf.save()

def merge():
    pdf_file = input("Enter PDF Name: ")
    reader = PdfReader(pdf_file)
    water_mark = PdfReader('watermark.pdf')
    output = PdfWriter()
    
    for page in reader.pages:
        page.merge_page(water_mark.pages[0])  
        output.add_page(page)
    
    with open('waterMarked_pdf.pdf', 'wb') as file:
        output.write(file)

user_choice = int(input("Enter 1 for default option or 2 for custom coordinates: "))
position = ""
x_coordinates=0
y_coordinates=0
if user_choice == 1:
    position = input("Enter the position for the watermark (topleft, topright, bottomleft, bottomright): ")
elif user_choice == 2:
    x_coordinates = int(input("Enter x-coordinate: "))
    y_coordinates = int(input("Enter y-coordinate: "))
else:
    print("Invalid choice. Please enter 1 for default option or 2 for custom coordinates.")
    exit()

makeWatermark(position, user_choice, x_coordinates, y_coordinates)
merge()
