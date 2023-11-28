from PIL import Image, ImageDraw, ImageFont
import sys

img = Image.open('gif.jpeg')
draw = ImageDraw.Draw(img)
text = sys.argv[1]

# You can specify a different font path or use a default PIL font
try:
    font = ImageFont.truetype('arial.ttf', 28)
except IOError:
    font = ImageFont.load_default()

textwidth, textheight = draw.textsize(text, font)
width, height = img.size
x = width/2 - textwidth/2
y = height - textheight - 28
draw.text((x, y), text, font=font)
img.save('gif.jpeg')
