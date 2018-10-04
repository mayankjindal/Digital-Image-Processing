# Histogram Matching

import cv2, math
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('/home/mayank/Downloads/Test_Images/House.tiff', 0)
img2 = cv2.imread('/home/mayank/Downloads/Test_Images/Lena.tiff', 0)

img_arr1 = np.array(img1)
img_arr2 = np.array(img2)
pixel_freq1 = {}
pixel_freq1_arr = []
pixel_freq2 = {}
pixel_freq2_arr = []

fig = plt.figure(figsize=(16, 16))
ax = fig.add_subplot(3, 2, 1)
plt.imshow(img_arr1, cmap='gray')
ax = fig.add_subplot(3, 2, 2)
plt.hist(img_arr1.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

ax = fig.add_subplot(3, 2, 3)
plt.imshow(img_arr2, cmap='gray')
ax = fig.add_subplot(3, 2, 4)
plt.hist(img_arr2.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')


# For the First Image
for i in range(0, len(img_arr1)):
    for j in range(0, len(img_arr1[i])):
        if img_arr1[i][j] in pixel_freq1.keys():
            pixel_freq1[img_arr1[i][j]] += 1
        else:
            pixel_freq1[img_arr1[i][j]] = 1

n = img_arr1.size
prob_sum = 0
for i in pixel_freq1.keys():
    pixel_freq1[i] = pixel_freq1[i]/n
    prob_sum += pixel_freq1[i]
    pixel_freq1[i] = math.floor((prob_sum + pixel_freq1[i])*255)
    pixel_freq1_arr.append(pixel_freq1[i])

# Now for the second image
for i in range(0, len(img_arr2)):
    for j in range(0, len(img_arr2[i])):
        if img_arr2[i][j] in pixel_freq2.keys():
            pixel_freq2[img_arr2[i][j]] += 1
        else:
            pixel_freq2[img_arr2[i][j]] = 1

n = img_arr2.size
prob_sum = 0
for i in pixel_freq2.keys():
    pixel_freq2[i] = pixel_freq2[i]/n
    prob_sum += pixel_freq2[i]
    pixel_freq2[i] = math.floor((prob_sum + pixel_freq2[i])*255)
    pixel_freq2_arr.append(pixel_freq2[i])

new_img_arr = []
for i in range(0, len(pixel_freq1_arr)):

    for j in range(0, len(pixel_freq2_arr)):
        if pixel_freq1_arr[i] <= pixel_freq2_arr[j]:
            new_img_arr.append(j)

k = 0
for i in pixel_freq1.keys():
    pixel_freq1[i] = new_img_arr[k]
    k += 1

for i in range(0, len(img_arr1)):
    for j in range(0, len(img_arr1[i])):
        img_arr1[i][j] = pixel_freq1[img_arr1[i][j]]

ax = fig.add_subplot(3, 2, 5)
plt.imshow(img_arr1, cmap='gray')
ax = fig.add_subplot(3, 2, 6)
plt.hist(img_arr1.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
plt.show()