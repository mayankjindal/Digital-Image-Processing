# Steganography
# Encoding text in an image

import cv2
import numpy as np

img = cv2.imread('/home/mayank/Downloads/Test_Images/Lena.tiff', 0)
img_arr = np.array(img)

text = 'Everyday Jiu-Jitsu'
ascii_text = []
for i in text:
    ascii_text.append(bin(ord(i))[2:].zfill(7))


# Encoding length of the text
text_len = bin(len(text))[2:].zfill(7)
for i in range(0, 7):
    temp = list(bin(img_arr[0][i])[2:])
    temp[-1] = text_len[i]
    img_arr[0][i] = int("".join(temp), 2)

# Encoding main text
i, j = 0, 7
for c in ascii_text:
    for l in range(0, len(c)):
        if j >= len(img_arr[i]):
            j = 0
            i += 1
        temp = list(bin(img_arr[i][j])[2:])

        temp[-1] = c[l]
        img_arr[i][j] = int("".join(temp), 2)
        j += 1

# Decoding length of the text
lim = []
for i in range(0, 7):
    lim.append(bin(img_arr[0][i])[2:][-1])
lim = int("".join(lim), 2)
print("Length of the text: ", lim)

# Decoding main text
decoded_text = []
i, j = 0, 7
for c in range(0, lim):
    temp = []

    for l in range(0, 7):
        if j >= len(img_arr[i]):
            j = 0
            i += 1
        temp.append(bin(img_arr[i][j])[2:][-1])
        j += 1
    decoded_text.append(chr(int("".join(temp), 2)))

decoded_text = "".join(decoded_text)
print("The decoded text is: ", decoded_text)
