import numpy as np
import matplotlib.pyplot as plt
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

# Load image using the ImageProcessor
imp = ImageProcessor()
arr = imp.load("../attachments/42AI.png")
print(f"Loading image of dimensions {arr.shape[0]} x {arr.shape[1]}")

# Create a ColorFilter object and apply the filters
cf = ColorFilter()

# Apply the filters (you can apply any one of these based on your preference)
inverted_image = cf.invert(arr)
green_image = cf.to_green(arr)
red_image = cf.to_red(arr)
blue_image = cf.to_blue(arr)
celluloid_image = cf.to_celluloid(arr)
grayscale_mean = cf.to_grayscale(arr, 'm')
grayscale_weighted = cf.to_grayscale(arr, 'weight', r_weight=0.2, g_weight=0.3, b_weight=0.5)

# Display the images using matplotlib
fig, ax = plt.subplots(2, 3, figsize=(10, 6))

# List of images to display
images = [inverted_image, green_image, red_image, blue_image, celluloid_image, grayscale_mean]
titles = ['Inverted', 'Green Filter', 'Red Filter', 'Blue Filter', 'Celluloid', 'Grayscale (Mean)']

for i, ax in enumerate(ax.flat):
    ax.imshow(images[i])
    ax.set_title(titles[i])
    ax.axis('off')

# Display all images
plt.tight_layout()
plt.show()
