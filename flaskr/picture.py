import cv2 as cv
from PIL import Image
import numpy as np
import io, os
import random

UPLOAD_FOLDER = 'static/image/'
basedir = os.path.abspath(os.path.dirname(__file__))
file_dir = os.path.join(basedir, UPLOAD_FOLDER)

def getpicture(pic1,pic2):
    img1 = cv.imread(file_dir+pic1) #MESSI
    print(file_dir+pic2)
    img = cv.imread(file_dir+pic2) #LOGO
    # img1=cv.resize(img,(300,400))
    # look(img)
    types = 'png'  # 转换后的图片格式
    rows, cols, channels = img.shape
    roi = img1[100:rows+100,100:cols+100]#获得messi的ROI
    img2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)# 颜色空间的转换
    ret, mask = cv.threshold(img2gray, 100, 255, cv.THRESH_BINARY)# 掩码 黑色
    mask_inv = cv.bitwise_not(mask)# 掩码取反 白色
    # #取mask中像素不为的0的值，其余为0
    img1_bg = cv.bitwise_and(img, img, mask=mask)
    img2_fg = cv.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv.add(img1_bg,img2_fg)
    img1[210:(rows+210), 170:(cols+170)] = dst
    cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
    # cv.imshow("image", mask)
    # cv.imshow("mask_inv", mask_inv)
    # cv.imshow("img1_bg", img1_bg)
    # cv.imshow("img2_fg", img2_fg)
    cv.imshow("image", img1)
    new_file_name = str(int(random.random()*10000000000000))+'.png'
    cv.imwrite(file_dir+new_file_name,img1)
    # img1.save()
    cv.waitKey()
    cv.destroyAllWindows()
    return new_file_name

if __name__ == '__main__':
    address = getpicture('beauty_20191020105245.jpg', '1570546506566.jpg')
    print(address)