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

plt.hist(img.ravel(), 256, [0, 256])  # Image Histogram
plt.show()
cv2.imshow('image', img_arr)

f_max = 0
f_min = 255
# Increasing brightness
for i in range(0, len(img_arr)):
    f_max = max(img_arr.max(), f_max)
    f_min = min(img_arr.min(), f_min)
    for j in range(0, len(img_arr[0])):
        img_arr[i, j] = img_arr[i, j]+40

plt.hist(img_arr.ravel(), 256, [0, 256])  # Image Histogram
plt.show()
cv2.imshow('b_image', img_arr)

# Changing contrast
f = f_max - f_min
for i in range(0, len(img_arr)):
    f_max = max(img_arr[i].max(), f_max)
    f_min = min(img_arr[j].min(), f_min)
    for j in range(0, len(img_arr[0])):
        img_arr[i, j] = (img_arr[i, j] - f_min)*512/f

plt.hist(img_arr.ravel(), 256, [0, 256])  # Image Histogram
plt.show()
cv2.imshow('c_image', img_arr)

# Reducing size of the image to half
img_arr = np.array(img)
new_img = []
for i in range(0, len(img_arr)):
    if i%2 == 0:
        temp = []
        for j in range(0, len(img_arr[0])):
            if j%2 == 0:
                temp.append(img_arr[i, j])
        new_img.append(temp)

new_img = np.array(new_img)
print("Original Size: ", img_arr.shape)
print("Size of reduced image: ", new_img.shape)
cv2.imshow('new_image', new_img)

# Zooming in the image
new_img = []
for i in range(0, len(img_arr)):
    temp = []
    for j in range(0, len(img_arr[0])):
        temp.append(img_arr[i, j])
        temp.append(img_arr[i, j])
    new_img.append(temp)
    new_img.append(temp)

new_img = np.array(new_img[:len(new_img)//2][:len(new_img)//2])  # Only half of the image will be shown
print("Original Size: ", img_arr.shape)
print("Size of reduced image: ", new_img.shape)
cv2.imshow('zoom_image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
