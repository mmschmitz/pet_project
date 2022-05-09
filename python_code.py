# %%
""" Writing a code to try to convert image (binary) files into edges.
Unfortunately, it's been a few years since I've written a lot of Python, so... 
I've got a lot of links here. :)
 """
#https://pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/
#https://pyimagesearch.com/2018/09/19/pip-install-opencv/

# %%
#import new modules
import os, sys
#below modules are specifically for cv
import imageio as iio
#import opencv-contrib-python as cv2 #opencv
import cv2
import argparse
# %%
#get directories
photo_directory = "C:/Users/mmsch/OneDrive/Desktop/pet_project/cute_photos"
os.chdir(photo_directory)
print("Current working dir : %s" % os.getcwd())
#print(photo_directory)
# %%
# We see here that there are a lot of JPGs available :)
photo_list = os.listdir(photo_directory)
# %%
# Use one of these elements to try to iterate and do a single test
data_file = open(photo_list[0],"r+") #confirmed it opened
img_test = cv2.imread(photo_list[0])
# %%
img_test
# %%
cv2.imshow("image_test1",img_test)
# %%
#usage: ipykernel_launcher.py [-h] -i IMAGE
#ipykernel_launcher.py: error: the following arguments are required: -i/--image
#An exception has occurred, use %tb to see the full traceback.
#
# SystemExit: 2

# # construct an argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,help="path to input image")
args = vars(ap.parse_args())

# %%
# %%


""" Writing a code to try to convert image (binary) files into edges.
Unfortunately, it's been a few years since I've written a lot of Python, so... 
I've got a lot of links here. :)
 """
#https://pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/
#https://pyimagesearch.com/2018/09/19/pip-install-opencv/

#import new modules
import os, sys
#below modules are specifically for cv
import imageio as iio
#import opencv-contrib-python as cv2 #opencv
import cv2
import argparse

#get directories
photo_directory = "C:/Users/mmsch/OneDrive/Desktop/pet_project/cute_photos"
os.chdir(photo_directory)
#print("Current working dir : %s" % os.getcwd())
#print(photo_directory)

os.listdir(photo_directory)
#https://stackoverflow.com/questions/1724693/find-a-file-in-python
########----

#initial test with a single image (will make a pipeline for the photo directory later)
data_file = open('20200516_184555.jpg',"r+")
img_test = cv2.imread("20200516_184555.jpg")
cv2.imshow("image_test1",img_test)

# # # construct an argument parser and parse the arguments (this needs to be fixed)
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, required=True,help="path to input image")
# args = vars(ap.parse_args())

# # load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)