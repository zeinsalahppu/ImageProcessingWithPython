"""
Image Processing Example with openCV

"""

import cv2 as cv
import numpy as np

img = cv.imread('d:/develope/ocvtest/f2_new.JPG', cv.IMREAD_COLOR)

size = img.shape
print(size)

neg_img1 = np.zeros(size, np.uint8)

for i in range(size[0]):
    for j in range(size[1]):
        in_pixel = img[i, j]
        out_pixel = [255 - in_pixel[0], 255 - in_pixel[1], 255 - in_pixel[2]]
        neg_img1[i, j] = out_pixel


cv.imshow('image', img)
cv.imshow('negated image', neg_img1)

cv.imwrite('d:/develope/ocvtest/f1_new_neg1_ocv.JPG', neg_img1)

cv.waitKey(0)

