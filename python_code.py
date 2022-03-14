#https://pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/
#https://pyimagesearch.com/2018/09/19/pip-install-opencv/

#import new packages
import sys
import os
#import imageio as iio
#import opencv-contrib-python as cv2 #opencv
import cv2
import argparse

os.chdir("C:\Users\mmsch\OneDrive\Desktop\pet_project\cute_photos")
photo_directory = os.getcwd()
#print(photo_directory)

#initial test with a single image (will make a pipeline for the photo directory later)
img_test = cv2.imread("20200516_184555.jpg")
cv2.imshow("image_test1",img_test)