# Histogram Equalization

import cv2, math
import numpy as np
import matplotlib.pyplot as plt


class HistogramEqualization:

    def __init__(self, loc):
        self.img = cv2.imread(loc, 0)
        self.img_arr = np.array(self.img)
        self.new_img_arr = np.array(self.img)
        self.cum_dis = {}
        self.final_val = {}

    def display_initial(self):
        self.fig = plt.figure(figsize=(16, 16))
        ax = self.fig.add_subplot(2, 2, 1)
        plt.imshow(self.img_arr, cmap='gray')
        ax = self.fig.add_subplot(2, 2, 2)
        plt.hist(self.img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

    def compute(self):
        for i in range(0, len(self.img_arr)):
            for j in range(0, len(self.img_arr[i])):
                if self.img_arr[i][j] in self.cum_dis.keys():
                    self.cum_dis[self.img_arr[i][j]] += 1
                else:
                    self.cum_dis[self.img_arr[i][j]] = 1
                    self.final_val[self.img_arr[i][j]] = 0

        sum = 0
        for i in self.cum_dis.keys():
            sum += self.cum_dis[i]
            self.cum_dis[i] = sum + self.cum_dis[i]
        m = max(self.cum_dis.values())
        for i in self.final_val.keys():
            self.final_val[i] = math.floor(self.cum_dis[i]*255/m)

        for i in range(0, len(self.new_img_arr)):
            for j in range(0, len(self.new_img_arr[i])):
                self.new_img_arr[i][j] = self.final_val[self.img_arr[i][j]]

    def display_final(self):
        ax = self.fig.add_subplot(2, 2, 3)
        plt.imshow(self.new_img_arr, cmap='gray')
        ax = self.fig.add_subplot(2, 2, 4)
        plt.hist(self.new_img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
        plt.show()


if __name__ == '__main__':
    obj = HistogramEqualization('/home/mayank/Downloads/Test_Images/Mandrill.tiff')
    obj.display_initial()
    obj.compute()
    obj.display_final()
