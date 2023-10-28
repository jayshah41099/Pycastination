# Requirement : pip install scikit-learn
# command : python3 Image_Color_Extraction.py

from  PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# open the image 
Image.open('color.jpeg')

# read the image file for color extraction
image = mpimg.imread('color.jpeg')
w, h, d = tuple(image.shape)
pixels = np.reshape(image, ( w * h, d))
n_colors = 10 # change this to get more or fewer colors

# Apply KMeans clustering
model = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
palette = np.uint8(model.cluster_centers_)
plt.imshow([palette])
plt.show()

'''
# Create and save the color palette as an image
palette_image = Image.new('RGB', (n_colors, 100))
for i in range(n_colors):
    color = tuple(palette[i])
    palette_image.paste(color, (i, 0, i + 1, 100))

# Save the color palette
palette_image.save('imgclrextract.png')

'''
