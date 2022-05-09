""" Writing a code to try to convert image (binary) files into edges.
Unfortunately, it's been a few years since I've written a lot of Python, so... 
I've got a lot of links here. :)
 """
#https://pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/
#https://pyimagesearch.com/2018/09/19/pip-install-opencv/

#import new modules
import sys
import os
#below modules are specifically for cv
import imageio as iio
#import opencv-contrib-python as cv2 #opencv
import cv2
import argparse

#get directories
os.chdir("C:/Users/mmsch/OneDrive/Desktop/pet_project/cute_photos")
photo_directory = os.getcwd()
#print(photo_directory)

os.listdir(photo_directory)
#https://stackoverflow.com/questions/1724693/find-a-file-in-python
########----

#initial test with a single image (will make a pipeline for the photo directory later)
data_file = open('20200516_184555.jpg',"r+")
img_test = cv2.imread("20200516_184555.jpg")
cv2.imshow("image_test1",img_test)

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, required=True,help="path to input image")
# args = vars(ap.parse_args())

# # load the image, convert it to grayscale, and blur it slightly
# image = cv2.imread(args["image"])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# # show the original and blurred images
# cv2.imshow("Original", image)
# cv2.imshow("Blurred", blurred)