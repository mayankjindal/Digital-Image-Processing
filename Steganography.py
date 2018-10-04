# Steganography
# Encoding-Decoding text in an image as well as a smaller image in a larger image.

import cv2
import numpy as np


def encode_text_in_image(text):
    n = len(text)
    c = img_arr.shape[0]*img_arr.shape[1]

    if (c/8 - 16) < n:
        return "N"
    ascii_text = []
    for i in text:
        ascii_text.append(bin(ord(i))[2:].zfill(8))

    # Encoding Text Length
    len_ = bin(n)[2:].zfill(16)
    for i in range(0, 16):
        temp = list(bin(img_arr[0][i])[2:])
        temp[-1] = len_[i]
        img_arr[0][i] = int("".join(temp), 2)

    # Encoding Main Text
    i, j = 0, 16
    for c in ascii_text:
        for l in range(0, len(c)):
            if j >= len(img_arr[i]):
                j = 0
                i += 1
            temp = list(bin(img_arr[i][j])[2:])

            temp[-1] = c[l]
            img_arr[i][j] = int("".join(temp), 2)
            j += 1

    cv2.imwrite('/home/mayank/Downloads/StegoDataset/Text_In_Lena.tiff', img_arr)
    return "Y"


def decode_text_in_image(arr):
    # Decoding Text Length
    lim = []
    for i in range(0, 16):
        lim.append(bin(arr[0][i])[2:][-1])
    lim = int("".join(lim), 2)
    print("Length of the text: ", lim)

    # Decoding Text
    decoded_text = []
    i, j = 0, 16
    for c in range(0, lim):
        temp = []

        for l in range(0, 8):
            if j >= len(arr[i]):
                j = 0
                i += 1
            temp.append(bin(arr[i][j])[2:][-1])
            j += 1
        decoded_text.append(chr(int("".join(temp), 2)))

    decoded_text = "".join(decoded_text)
    print("The decoded text is: ", decoded_text)


def encode_image_in_image(arr):
    pixel_bin = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            pixel_bin.append(bin(arr[i][j])[2:].zfill(8))

    m = arr.shape[0]*arr.shape[1]
    c = img_arr.shape[0]*img_arr.shape[1]

    if (c/8 - 32) < m:
        return "N"

    print("\nDimensions of the Encoded Image: ", arr.shape[0], arr.shape[1])
    # Encoding Image Dimensions
    rows = bin(arr.shape[0])[2:].zfill(16)
    cols = bin(arr.shape[1])[2:].zfill(16)
    for i in range(0, 16):
        temp = list(bin(img_arr[0][i])[2:])
        temp[-1] = rows[i]
        img_arr[0][i] = int("".join(temp), 2)
    for i in range(16, 32):
        temp = list(bin(img_arr[0][i])[2:])
        temp[-1] = cols[i-16]
        img_arr[0][i] = int("".join(temp), 2)

    # Encoding image
    i, j = 0, 32
    for c in pixel_bin:
        for l in range(0, len(c)):
            if j >= len(img_arr[i]):
                j = 0
                i += 1
            temp = list(bin(img_arr[i][j])[2:])

            temp[-1] = c[l]
            img_arr[i][j] = int("".join(temp), 2)
            j += 1

    cv2.imwrite('/home/mayank/Downloads/StegoDataset/Image_In_Lena.tiff', img_arr)
    return "Y"


def decode_image_in_image(arr):
    # Decoding Dimensions
    row, col = [], []
    for i in range(0, 16):
        row.append(bin(arr[0][i])[2:][-1])
    row = int("".join(row), 2)
    for i in range(16, 32):
        col.append(bin(arr[0][i])[2:][-1])
    col = int("".join(col), 2)
    print("Dimensions of the Decoded Image: ", row, col)

    # Decoding Image
    decoded_arr = []
    i, j = 0, 32
    for c in range(0, row):
        temp1 = []
        for d in range(0, col):
            temp = []
            for l in range(0, 8):
                if j >= len(arr[i]):
                    j = 0
                    i += 1
                temp.append(bin(arr[i][j])[2:][-1])
                j += 1
            temp1.append(int("".join(temp), 2))
        decoded_arr.append(temp1)

    final_arr = np.array(decoded_arr, np.uint8)
    cv2.imwrite('/home/mayank/Downloads/StegoDataset/Decoded_Image.tiff', final_arr)
    cv2.imshow('Decoded_Image', final_arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main Image
img = cv2.imread('/home/mayank/Downloads/StegoDataset/Lena.tiff', 0)
img_arr = np.array(img)

# Text For Encryption
original_text = 'Exploring Image Binarization Techniques - The book focuses on an image processing technique known as binarization. It provides a comprehensive survey over existing binarization techniques for both document and graphic images. A number of evaluation techniques have been presented for quantitative comparison of different binarization methods. The book provides results obtained comparing a number of standard and widely used binarization algorithms using some standard evaluation metrics. The comparative results presented in tables and charts facilitates understanding the process. In addition to this, the book presents techniques for preparing a reference image which is very much important for quantitative evaluation of the binarization techniques. The results are produced taking image samples from standard image databases.'
ans = encode_text_in_image(original_text)
if ans == "Y":
    # Reading Text Encoded Image
    img = cv2.imread('/home/mayank/Downloads/StegoDataset/Text_In_Lena.tiff', 0)
    img_arr_2 = np.array(img)
    decode_text_in_image(img_arr_2)
else:
    print("Text cannot be encoded. Size is too big!")

# Image For Encryption
small_img = cv2.imread('/home/mayank/Downloads/StegoDataset/F16.tiff', 0)
small_img_arr = np.array(small_img)
ans = encode_image_in_image(small_img_arr)
if ans == "Y":
    # Reading Image Encoded Image
    img = cv2.imread('/home/mayank/Downloads/StegoDataset/Image_In_Lena.tiff', 0)
    img_arr_2 = np.array(img)
    decode_image_in_image(img_arr_2)
else:
    print("Image cannot be encoded. Size is too big!")
