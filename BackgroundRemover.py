# requirement: pip install rembg
# sys arguments take the file path or the image
#terminal command: python3 BackgroundRemover.py image.jpeg

from rembg import remove
from PIL import Image
import sys

Image_Path = sys.argv[1]
Output_Image = 'rmbg_image.png'

input = Image.open(Image_Path)
output = remove(input)

output.save(Output_Image)