import cv2
import numpy as np

#Getting the Image ready for feature detection
img_path=r'C:\Users\ojask\Desktop\red.jpg'
image = cv2.imread(img_path)
#Resizing the image to our liking.
image = cv2.resize(image, (400,550),interpolation=cv2.INTER_AREA)
#Conversion to gray scale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Initiate ORB object
orb = cv2.ORB_create(nfeatures=1000)

# find the keypoints and descriptors with ORB
keypoints, descriptors = orb.detectAndCompute(gray_image, None)

# draw only the location of the keypoints.
final_keypoints = cv2.drawKeypoints(gray_image, keypoints,image,(0,255,0))
#Show the final output
cv2.imshow('ORB keypoints', final_keypoints)
cv2.waitKey()