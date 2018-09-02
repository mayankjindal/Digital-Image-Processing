# Histogram Equalization

import cv2, math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/mayank/Downloads/Test_Images/Mandrill.tiff', 0)

plt.hist(img.ravel(), 256, [0, 256])  # Image Histogram
plt.show()

img_arr = np.array(img)
pixel_freq = {}
max_pixel = 0
min_pixel = 255
for i in range(0, len(img_arr)):
    max_pixel = max(max_pixel, img_arr[i].max())
    min_pixel = min(min_pixel, img_arr[i].min())
    for j in range(0, len(img_arr[i])):
        if img_arr[i][j] in pixel_freq.keys():
            pixel_freq[img_arr[i][j]] += 1
        else:
            pixel_freq[img_arr[i][j]] = 1

pixel_range = max_pixel - min_pixel
n = img_arr.size
sum = 0
for i in pixel_freq.keys():
    pixel_freq[i] = pixel_freq[i]/n
    sum += pixel_freq[i]
    pixel_freq[i] = math.floor((sum + pixel_freq[i])*max_pixel)

for i in range(0, len(img_arr)):
    for j in range(0, len(img_arr[i])):
        img_arr[i][j] = pixel_freq[img_arr[i][j]]

plt.hist(img_arr.ravel(), 256, [0, 256])  # Image Histogram
plt.show()


