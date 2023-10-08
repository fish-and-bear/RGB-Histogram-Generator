# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 20:39:51 2023

@author: 王安吉
"""

import os
from PIL import Image
import matplotlib.pyplot as plt
import cv2

folder_path = 'Pics'  # Update folder_path to your image folder

# Empty list to store histograms
histograms = []

i = 0
for filename in os.listdir(folder_path):  
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        plt.figure()
        plt.imshow(image)
        plt.show()
        image.close()
        
        i += 1
        img = cv2.imread(image_path)
        # cv2.imshow("Img "+str(i),img)
        cv2.waitKey()
        
        # histogram
        color = ('b','g','r')
        plt.style.use('dark_background')
        plt.figure(figsize=(10,5))
        for idx, color in enumerate(color):
            histogram = cv2.calcHist([img],[idx],None,[256],[0, 256])
            plt.plot(histogram, color = color)
            plt.xlim([0, 256])
            histograms.append(histogram)  # Append the histogram to the list
            
        plt.show()
cv2.destroyAllWindows()

# Plot all histograms on a single graph
plt.style.use('dark_background')
plt.figure(figsize=(10,5))
for histogram in histograms:
    plt.plot(histogram)
    plt.xlim([0, 256])
plt.show()
