import matplotlib.pyplot as plt
from skimage import io
import matplotlib.image as mp
from PIL import Image
import numpy as np

# counting the number of objects
Image_obj_count = io.imread('/home/mayank/Downloads/Test_Images/TestIMage.png', as_gray=True)
print(len(Image_obj_count), len(Image_obj_count[0]))

Image_obj_count = Image_obj_count*255
plt.hist(Image_obj_count.ravel(), 256, [0, 256])
plt.show()


def count_objects(img):
    objects = [[0 for i in range(0, len(img[0]))] for j in range(0, len(img))]
    object_count = 0
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            flag = 0
            if i == 0:
                objects[i][j] = 1
                flag = 1
            else:
                if img[i][j] <= img[i-1][j]+10 and img[i][j]+10 >= img[i-1][j]:
                    objects[i][j] = objects[i - 1][j]
                    flag = 1
                elif j != 0 and img[i][j] <= img[i-1][j-1]+10 and img[i][j]+10 >= img[i-1][j-1]:
                    objects[i][j] = objects[i - 1][j-1]
                    flag = 1
                elif j != 0 and img[i][j] <= img[i][j-1]+10 and img[i][j]+10 >= img[i][j-1]:
                    objects[i][j] = objects[i][j-1]
                    flag = 1
                elif j != len(img[i])-1 and img[i][j] <= img[i-1][j+1]+10 and img[i][j]+10 >= img[i-1][j+1]:
                    objects[i][j] = objects[i - 1][j+1]
                    flag = 1
            if flag == 0:
                object_count += 1
                objects[i][j] = object_count

    for i in range(len(img)-1, -1, -1):
        for j in range(len(img[i])-1, -1, -1):
            if i != len(img)-1 and j != 0 and img[i][j] <= img[i+1][j-1]+10 and img[i][j]+10 >= img[i+1][j-1]:
                objects[i][j] = objects[i+1][j-1]
            elif i != len(img)-1 and img[i][j] <= img[i+1][j]+10 and img[i][j]+10 >= img[i+1][j]:
                objects[i][j] = objects[i+1][j]
            elif j != len(img[i])-1 and i != len(img)-1 and img[i][j] <= img[i+1][j+1]+10 and img[i][j]+10 >= img[i+1][j+1]:
                objects[i][j] = objects[i+1][j+1]
            elif j != len(img[i])-1 and img[i][j] <= img[i][j+1]+10 and img[i][j]+10 >= img[i][j+1]:
                objects[i][j] = objects[i][j+1]
    print(objects)
    b = []
    for i in range(0, len(objects)):
        for j in range(0, len(objects[i])):
            if objects[i][j] not in b:
                b.append(objects[i][j])
    print(len(b))


count_objects(Image_obj_count)
