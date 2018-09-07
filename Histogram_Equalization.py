# Histogram Equalization

import cv2, math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/mayank/Downloads/Test_Images/Mandrill.tiff', 0)

plt.hist(img.ravel(), 256, [0, 256])  # Image Histogram
plt.show()

img_arr = np.array(img)
pixel_freq = {}
cv2.imshow('Original_Image', img_arr)

for i in range(0, len(img_arr)):
    for j in range(0, len(img_arr[i])):
        if img_arr[i][j] in pixel_freq.keys():
            pixel_freq[img_arr[i][j]] += 1
        else:
            pixel_freq[img_arr[i][j]] = 1

n = img_arr.size
sum = 0
for i in pixel_freq.keys():
    pixel_freq[i] = pixel_freq[i]/n
    sum += pixel_freq[i]
    pixel_freq[i] = math.floor((sum + pixel_freq[i])*len(pixel_freq))

for i in range(0, len(img_arr)):
    for j in range(0, len(img_arr[i])):
        img_arr[i][j] = pixel_freq[img_arr[i][j]]

plt.hist(img_arr.ravel(), 256, [0, 256])  # Image Histogram
plt.show()
cv2.imshow('New_Image', img_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()

