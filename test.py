from PIL import Image, ImageDraw, ImageFont

draw = ImageDraw.Draw()
font = ImageFont.truetype("arial.ttf", 20)
draw.text((20,20), "Hello World", font=font, fill=(0, 0, 0))