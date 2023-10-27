# requirement : pip install PIL - for first set of commented code
    # choice of images to create gif, it has to be in same directory as this script
# command : python3 Gif.py

'''
# if you require the images to be resized than use the following code

from PIL import Image
import imageio

# List of image file names
gifs = ["gif0.jpeg", "gif1.jpeg", "gif2.jpeg", "gif3.jpeg"]

# Open the first image to get its dimensions
with Image.open(gifs[0]) as img:
    width, height = img.size

# Create a list to store resized images
resized_images = []

# Loop through the images, open and resize if needed
for gif in gifs:
    with Image.open(gif) as img:
        img = img.resize((width, height))
        # Save the resized image with a unique name
        resized_path = gif.replace('.jpeg', '_resized.jpeg')
        img.save(resized_path)
        resized_images.append(resized_path)

# Load the resized images and save as a GIF
images = [imageio.imread(img) for img in resized_images]

# Save the resized images as a GIF
imageio.mimsave('Final.gif', images, 'GIF', duration=0.1)

'''

# if you don't require the images to be resized than use the following code

import imageio

# add your choice of image can be jpeg or png
gifs = ["gif0.jpeg", "gif1.jpeg", "gif2.jpeg", "gif3.jpeg"]

images = []
for gif in gifs:
    images.append(imageio.imread(gif))

imageio.mimsave('Final.gif', images, 'GIF', duration=1)



