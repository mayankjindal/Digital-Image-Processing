# Histogram Equalization

import cv2, math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/mayank/Downloads/Test_Images/Mandrill.tiff', 0)

img_arr = np.array(img)
pixel_freq = {}
fig = plt.figure(figsize=(16, 16))
ax = fig.add_subplot(2, 2, 1)
plt.imshow(img_arr, cmap='gray')
ax = fig.add_subplot(2, 2, 2)
plt.hist(img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')


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

ax = fig.add_subplot(2, 2, 3)
plt.imshow(img_arr, cmap='gray')
ax = fig.add_subplot(2, 2, 4)
plt.hist(img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
plt.show()