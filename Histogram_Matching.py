# Histogram Matching

from Histogram_Equalization import HistogramEqualization as HE
import matplotlib.pyplot as plt


class HistogramMatching:

    def __init__(self, loc1, loc2):
        # Calling class for Histogram Equalization
        self.img1 = HE(loc1)
        self.img1.compute()

        self.img2 = HE(loc2)
        self.img2.compute()

        self.map = {}
        self.matched = {}

    def display_initial(self):
        self.fig = plt.figure(figsize=(16, 16))
        ax = self.fig.add_subplot(3, 2, 1)
        plt.imshow(self.img1.new_img_arr, cmap='gray')
        ax = self.fig.add_subplot(3, 2, 2)
        plt.hist(self.img1.img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

        ax = self.fig.add_subplot(3, 2, 3)
        plt.imshow(self.img2.new_img_arr, cmap='gray')
        ax = self.fig.add_subplot(3, 2, 4)
        plt.hist(self.img2.img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')

    def match(self):
        for i in self.img1.final_val.keys():
            self.map[i] = 0
            self.matched[i] = 0
        for i in self.img1.final_val.keys():
            for j in self.img2.final_val.keys():
                if self.img1.final_val[i] >= self.img2.final_val[j]:
                    self.map[i] = j
                    break

        for i in self.map.keys():
            self.matched[i] += self.img1.cum_dis[i]

        for i in range(0, len(self.img1.new_img_arr)):
            for j in range(0, len(self.img1.new_img_arr[i])):
                self.img1.new_img_arr[i][j] = self.img1.final_val[self.img1.img_arr[i][j]]

    def display_final(self):
        ax = self.fig.add_subplot(3, 2, 5)
        plt.imshow(self.img1.new_img_arr, cmap='gray')
        ax = self.fig.add_subplot(3, 2, 6)
        plt.hist(self.img1.new_img_arr.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
        plt.show()


if __name__ == '__main__':
    location1 = '/home/mayank/Downloads/Test_Images/image2.jpg'
    location2 = '/home/mayank/Downloads/Test_Images/image1.jpg'
    obj = HistogramMatching(location1, location2)
    obj.display_initial()
    obj.match()
    obj.display_final()
