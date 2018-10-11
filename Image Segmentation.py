import matplotlib.pyplot as plt
import cv2
import numpy as np

# counting the number of objects
objects = cv2.imread('/home/mayank/Downloads/Test_Images/objects.png', 0)

obj = {}
for i in range(0, len(objects)):
    for j in range(0, len(objects[i])):
        if objects[i][j] in obj.keys():
            obj[objects[i][j]] += 1
        else:
            obj[objects[i][j]] = 1
print(obj)
s = min(obj, key=obj.get)
m = max(obj, key=obj.get)
for i in range(0, len(objects)):
    for j in range(0, len(objects[i])):
        if objects[i][j] == s or objects[i][j] == m:
            objects[i][j] = 255
        else:
            objects[i][j] = 1
plt.imshow(objects, cmap='gray')
plt.show()
