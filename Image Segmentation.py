import matplotlib.pyplot as plt
import cv2
import operator
import numpy as np

# counting the number of objects
img = cv2.imread('/home/mayank/Downloads/Test_Images/objects.png', 0)
img = np.array(img)
f_image = np.array(img)
s_image = np.array(img)
hist = {}

for i in range(0, len(img)):
    for j in range(0, len(img[i])):
        if img[i][j] in hist.keys():
            hist[img[i][j]] += 1
        else:
            hist[img[i][j]] = 1

sorted_hist = sorted(hist.items(), key=operator.itemgetter(1))
smx = sorted_hist[len(sorted_hist) - 2][0]
for i in range(0, len(img)):
    for j in range(0, len(img[i])):
        if img[i][j] == smx:
            f_image[i][j] = 255
        else:
            f_image[i][j] = 0

for i in range(0, len(img)):
    for j in range(0, len(img[i])):
        if img[i][j] != 255 and img[i][j] != smx:
            s_image[i][j] = 255
        else:
            s_image[i][j] = 0

fig = plt.figure(figsize=(16, 16))
ax = fig.add_subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
ax = fig.add_subplot(2, 2, 3)
plt.imshow(f_image, cmap='gray')
ax = fig.add_subplot(2, 2, 4)
plt.imshow(s_image, cmap='gray')
plt.show()
