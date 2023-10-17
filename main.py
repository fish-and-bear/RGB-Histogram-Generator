# -*- coding: utf-8 -*-
"""
@author: 王安吉

"""

import os
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# Define the folder path
folder_path = 'Pics'  # Update folder_path to your image folder

# Empty list to store histograms
histograms = []

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)
        
        plt.figure()
        plt.imshow(image)
        plt.show()
        image.close()
        
        img = cv2.imread(image_path)
        
        # Histogram for each color channel
        colors = ['b', 'g', 'r']
        num_bins = 256  # Number of bins for the histograms
        
        # Calculate and store histograms
        for idx, channel_color in enumerate(colors):
            histogram = cv2.calcHist([img], [idx], None, [num_bins], [0, num_bins])
            
            plt.style.use('dark_background')
            plt.figure(figsize=(10, 5))
            plt.plot(histogram, color=channel_color)
            plt.xlim([0, num_bins])
        
        # Split the image into color channels (BGR format)
        blue, green, red = cv2.split(img)
        
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 5))
        
        for i, color in enumerate(colors):
            histogram = cv2.calcHist([img], [i], None, [num_bins], [0, num_bins])
            plt.plot(histogram, color=color)
            histograms.append(histogram)  # Append the histogram to the list
            
        plt.show()

# Plot all histograms on a single graph
plt.style.use('dark_background')
plt.figure(figsize=(10, 5))
for histogram in histograms:
    plt.plot(histogram)
    plt.xlim([0, num_bins])
plt.show()
