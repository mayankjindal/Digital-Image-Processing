import cv2
import matplotlib.pyplot as plt
import numpy as np

class Dither:

    def __init__(self, img_arr):
        self.img_arr = np.array(img_arr)

    def thresholding(self):
        th = 200
        for i in range(0, len(self.img_arr)):
            for j in range(0, len(self.img_arr[i])):
                if self.img_arr[i][j] > th:
                    self.img_arr[i][j] = 255
                else:
                    self.img_arr[i][j] = 0

        plt.imshow(self.img_arr, cmap='gray')
        plt.show()




img = cv2.imread("/home/mayank/Downloads/Test_Images/greek.png", 0)
obj = Dither(img)
obj.thresholding()