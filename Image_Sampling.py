# Converting Image to grayscale, changing brightness and contrast, reducing and increasing image size

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/mayank/Downloads/Test_Images/Mandrill.tiff')

# Converting image to gray scale
img_arr = np.array(img)
for i in range(0, len(img_arr)):
    for j in range(0, len(img_arr[0])):
        img_arr[i, j] = img_arr[i, j, 0]*0.11 + img_arr[i, j, 1]*0.59 + img_arr[i, j, 2]*0.30

fig = plt.figure(figsize=(16, 16))
ax = fig.add_subplot(3, 2, 1)
plt.imshow(img_arr, cmap='gray')
ax = fig.add_subplot(3, 2, 2)
plt.hist(img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')


f_max = 0
f_min = 255
# Increasing brightness
for i in range(0, len(img_arr)):
    f_max = max(img_arr.max(), f_max)
    f_min = min(img_arr.min(), f_min)
    for j in range(0, len(img_arr[0])):
        img_arr[i, j] = img_arr[i, j]+40

ax = fig.add_subplot(3, 2, 3)
plt.imshow(img_arr, cmap='gray')
ax = fig.add_subplot(3, 2, 4)
plt.hist(img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

# Changing contrast
f = f_max - f_min
for i in range(0, len(img_arr)):
    f_max = max(img_arr[i].max(), f_max)
    f_min = min(img_arr[j].min(), f_min)
    for j in range(0, len(img_arr[0])):
        img_arr[i, j] = (img_arr[i, j] - f_min)*512/f

ax = fig.add_subplot(3, 2, 5)
plt.imshow(img_arr, cmap='gray')
ax = fig.add_subplot(3, 2, 6)
plt.hist(img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
plt.show()

# Reducing size of the image to half
img_arr = np.array(img)
new_img_arr = []
for i in range(0, len(img_arr)):
    if i%2 == 0:
        temp = []
        for j in range(0, len(img_arr[0])):
            if j%2 == 0:
                temp.append(img_arr[i, j])
        new_img_arr.append(temp)

new_img_arr = np.array(new_img_arr)
print("Input image Size: ", img_arr.shape)
print("Size of reduced image: ", new_img_arr.shape)
cv2.imshow('reduced_image', new_img_arr)

# Using the reduced image to restore the original image
new_img = []
for i in range(0, len(new_img_arr)):
    temp = []
    for j in range(0, len(new_img_arr[0])):
        temp.append(new_img_arr[i, j])
        temp.append(new_img_arr[i, j])
    new_img.append(temp)
    new_img.append(temp)

new_img = np.array(new_img[:len(new_img)][:len(new_img)])
print("Input image Size: ", new_img_arr.shape)
print("Size of enlarged image: ", new_img.shape)
cv2.imshow('Original Image', img_arr)
cv2.imshow('enlarged_image', new_img)
cv2.waitKey()
cv2.destroyAllWindows()
