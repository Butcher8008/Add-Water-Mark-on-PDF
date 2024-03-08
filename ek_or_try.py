from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os
import PyPDF2 

Choice=input("Enter your choice: ")
position=input("Enter position: (tl, tp, bl, br, tc, bc, lc, rc): ")
angle= int(input('Enter the angle : '))


image = Image.new("RGBA", (200, 80), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 20)

draw.text((20,20), "Hello World", font=font, fill=(0, 0, 0))

rotated_image = image.rotate(angle, expand=True, fillcolor=(255, 255, 255, 0))
image_path = "temp_image.png"
rotated_image.save(image_path)
pdf_path = "output.pdf"

c = canvas.Canvas(pdf_path, pagesize=LETTER)
if Choice == "all":        
    c.setFillColor(colors.grey,alpha=0.4)
    c.drawImage(image_path, 10,700,)
    c.drawImage(image_path, 10,300,)
    c.drawImage(image_path, 400,700)
    c.drawImage(image_path, 200,700)
    c.drawImage(image_path, 200,300)
    c.drawImage(image_path, 400,300)
    c.drawImage(image_path, 400, 10) 
    c.drawImage(image_path, 200, 10) 
    c.drawImage(image_path, 10, 10) 
elif Choice == "by choice":
    if position=='tl':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 10,700)
    elif position=='tr':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 400,700)
    elif position=='bl':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 10,10)
    elif position=='br':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 400,10)
    elif position=='tc':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 200,700)
    elif position=='bc':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 200,10)
    elif position=='lc':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 10,300)
    elif position=='bc':
        c.setFillColor(colors.grey,alpha=0.4)
        c.drawImage(image_path, 400,300)
elif Choice=='top':
    c.setFillColor(colors.grey, alpha=0.4)
    c.drawImage(image_path, 10,700)
    c.drawImage(image_path, 10,300)
    c.drawImage(image_path, 10,10)
elif Choice=='center':
    c.setFillColor(colors.grey, alpha=0.4)
    c.drawImage(image_path, 200,700)    
    c.drawImage(image_path, 200,300)    
    c.drawImage(image_path, 200,10)
elif Choice == 'bottom':
    c.setFillColor(colors.grey , alpha=0.4)
    c.drawImage(image_path, 400,10)    
    c.drawImage(image_path, 400,300)    
    c.drawImage(image_path, 400,700)   
elif Choice=='mid':
    c.setFillColor(colors.grey, alpha=0.6)
    c.setFont(psfontname="Helvetica", size=70)
    c.rotate(angle)
    c.drawCentredString(600, 100, "Hello world")

c.save()
os.remove(image_path)

print("PDF saved successfully.")

pdf_file = input("Enter PDF Name: ")
reader = PyPDF2.PdfReader(pdf_file)
water_mark = PyPDF2.PdfReader('output.pdf')
output = PyPDF2.PdfWriter()
    
for page in range(len(reader.pages)):
        main_page = reader.pages[page]
        watermark_page = water_mark.pages[page % len(water_mark.pages)]
        
        # Create a new page object
        merged_page = PyPDF2.PageObject.create_blank_page(width=main_page.mediabox.width ,height=main_page.mediabox.height)
        # Overlay the main page onto the new page
        merged_page.merge_page(main_page)
        
        # Overlay the watermark page behind the main page
        merged_page.merge_page(watermark_page)
        
        # Add the merged page to the output PDF
        output.add_page(merged_page)
with open('waterMarked_pdf.pdf', 'wb') as file:
    output.write(file)
