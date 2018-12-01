#该程序目的将眼球图片中的瞳孔圆心位置提取出来
# -- coding: UTF-8 --
import numpy as np
from PIL import Image
import skimage.io
import matplotlib.pyplot as plt
import cv2
from skimage import measure

def own_threshold(img): #自己设置阈值100            全局
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)  #首先变为灰度图
    ret , binary = cv2.threshold( gray , 45, 255 , cv2.THRESH_BINARY )#cv.THRESH_BINARY |cv.THRESH_OTSU 根据THRESH_OTSU阈值进行二值化
    print("阈值：", ret)
    cv2.imshow('binary', binary)
    cv2.waitKey(100)
    return  binary

def close_image(gray):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    return binary

img = cv2.imread('E:/cropped/12.bmp')

cv2.imshow('img',img)
im = own_threshold(img)

im = ~im

gray = ~close_image(im)


circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                            50, param1=20, param2=10, minRadius=20, maxRadius=40)

circles = circles1[0, :, :]
circles = np.uint16(np.around(circles))
for i in circles[:]:
    cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)
    cv2.rectangle(img, (i[0] - i[2], i[1] + i[2]), (i[0] + i[2], i[1] - i[2]), (255, 255, 0), 5)

print"Center-coordinates_x: " + str(i[0]) + ' Center-coordinates_y: ' + str(i[1])
cv2.imshow('gray',gray)
cv2.waitKey(100)
cv2.imshow('img',img)
cv2.waitKey(100)
# plt.figure(img)
# plt.subplot(121), plt.imshow(gray, 'gray')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img)
# plt.xticks([]), plt.yticks([])



