# Converting Image to grayscale, changing brightness and contrast, reducing and increasing image size

import cv2
import numpy as np
import matplotlib.pyplot as plt


class ImageSampling:

    def __init__(self, loc):
        self.location = loc
        self.img = cv2.imread(self.location)
        self.img_arr = np.array(self.img)

    def gray_scale(self):
        # Converting image to gray scale
        for i in range(0, len(self.img_arr)):
            for j in range(0, len(self.img_arr[0])):
                self.img_arr[i, j] = self.img_arr[i, j, 0]*0.11 + self.img_arr[i, j, 1]*0.59 + self.img_arr[i, j, 2]*0.30

        self.fig = plt.figure(figsize=(16, 16))
        ax = self.fig.add_subplot(3, 2, 1)
        plt.imshow(self.img_arr, cmap='gray')
        ax = self.fig.add_subplot(3, 2, 2)
        plt.hist(self.img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

    def change_brightness(self, b):
        # Increasing brightness
        self.f_max = 0
        self.f_min = 255
        for i in range(0, len(self.img_arr)):
            self.f_max = max(self.img_arr.max(), self.f_max)
            self.f_min = min(self.img_arr.min(), self.f_min)
            for j in range(0, len(self.img_arr[0])):
                self.img_arr[i, j] = self.img_arr[i, j]+b

        ax = self.fig.add_subplot(3, 2, 3)
        plt.imshow(self.img_arr, cmap='gray')
        ax = self.fig.add_subplot(3, 2, 4)
        plt.hist(self.img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

    def change_contrast(self):
        # Changing contrast
        f = self.f_max - self.f_min
        for i in range(0, len(self.img_arr)):
            self.f_min = min(self.img_arr[i].min(), self.f_min)
            for j in range(0, len(self.img_arr[0])):
                self.img_arr[i, j] = (self.img_arr[i, j] - self.f_min)*512/f

        ax = self.fig.add_subplot(3, 2, 5)
        plt.imshow(self.img_arr, cmap='gray')
        ax = self.fig.add_subplot(3, 2, 6)
        plt.hist(self.img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
        plt.show()

    def reduce_size(self):
        # Reducing size of the image to half
        self.img_arr = np.array(cv2.imread(self.location, 0))
        self.new_img_arr = []
        for i in range(0, len(self.img_arr)):
            if i%2 == 0:
                temp = []
                for j in range(0, len(self.img_arr[0])):
                    if j%2 == 0:
                        temp.append(self.img_arr[i, j])
                self.new_img_arr.append(temp)

        self.new_img_arr = np.array(self.new_img_arr)
        print("Input image Size: ", self.img_arr.shape)
        print("Size of reduced image: ", self.new_img_arr.shape)
        cv2.imshow('reduced_image', self.new_img_arr)

    def increase_size(self):
        # Using the reduced image to restore the original image
        self.new_img = []
        for i in range(0, len(self.new_img_arr)):
            temp = []
            for j in range(0, len(self.new_img_arr[0])):
                temp.append(self.new_img_arr[i, j])
                temp.append(self.new_img_arr[i, j])
            self.new_img.append(temp)
            self.new_img.append(temp)

        self.new_img = np.array(self.new_img[:len(self.new_img)][:len(self.new_img)])
        print("Input image Size: ", self.new_img_arr.shape)
        print("Size of enlarged image: ", self.new_img.shape)
        cv2.imshow('Original Image', self.img_arr)
        cv2.imshow('enlarged_image', self.new_img)
        cv2.waitKey()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    obj = ImageSampling('/home/mayank/Downloads/Test_Images/Mandrill.tiff')
    obj.gray_scale()
    obj.change_brightness(40)
    obj.change_contrast()
    obj.reduce_size()
    obj.increase_size()
