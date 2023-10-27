# you can import sys and pass sys.argv[1] from command line for input and output as well
# command : python3 png_to_jpg.py

from PIL import Image

# input png 
png = Image.open('rmbg_image.png')
jpeg = png.convert('RGB')

# output jpeg
jpeg.save('rmbg_image.jpeg')