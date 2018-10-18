import matplotlib.pyplot as plt
import cv2


class ObjectCount:

    def __init__(self, loc):
        self.img = cv2.imread(loc, 0)

    def count_objects(self):
        objects = [[0 for i in range(0, len(self.img[0]))] for j in range(0, len(self.img))]
        object_count = 0
        for i in range(0, len(self.img)):
            for j in range(0, len(self.img[i])):
                flag = 0
                if i == 0:
                    objects[i][j] = 1
                    flag = 1
                else:
                    if self.img[i][j] <= self.img[i-1][j]+10 and self.img[i][j]+10 >= self.img[i-1][j]:
                        objects[i][j] = objects[i - 1][j]
                        flag = 1
                    elif j != 0 and self.img[i][j] <= self.img[i-1][j-1]+10 and self.img[i][j]+10 >= self.img[i-1][j-1]:
                        objects[i][j] = objects[i - 1][j-1]
                        flag = 1
                    elif j != 0 and self.img[i][j] <= self.img[i][j-1]+10 and self.img[i][j]+10 >= self.img[i][j-1]:
                        objects[i][j] = objects[i][j-1]
                        flag = 1
                    elif j != len(self.img[i])-1 and self.img[i][j] <= self.img[i-1][j+1]+10 and self.img[i][j]+10 >= self.img[i-1][j+1]:
                        objects[i][j] = objects[i - 1][j+1]
                        flag = 1
                if flag == 0:
                    object_count += 1
                    objects[i][j] = object_count

        for i in range(len(self.img)-1, -1, -1):
            for j in range(len(self.img[i])-1, -1, -1):
                if i != len(self.img)-1 and j != 0 and self.img[i][j] <= self.img[i+1][j-1]+10 and self.img[i][j]+10 >= self.img[i+1][j-1]:
                    objects[i][j] = objects[i+1][j-1]
                elif i != len(self.img)-1 and self.img[i][j] <= self.img[i+1][j]+10 and self.img[i][j]+10 >= self.img[i+1][j]:
                    objects[i][j] = objects[i+1][j]
                elif j != len(self.img[i])-1 and i != len(self.img)-1 and self.img[i][j] <= self.img[i+1][j+1]+10 and self.img[i][j]+10 >= self.img[i+1][j+1]:
                    objects[i][j] = objects[i+1][j+1]
                elif j != len(self.img[i])-1 and self.img[i][j] <= self.img[i][j+1]+10 and self.img[i][j]+10 >= self.img[i][j+1]:
                    objects[i][j] = objects[i][j+1]
        print(objects)
        b = []
        for i in range(0, len(objects)):
            b = set(list(b) + objects[i])
        print(b, len(b))


obj = ObjectCount('/home/mayank/Downloads/Test_Images/TestIMage.png')
obj.count_objects()
