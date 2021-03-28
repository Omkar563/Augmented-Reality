# Augmented-Reality
This a Computer Vision project where I implement certain algorithms  to detect features of a certain image, Match the features and Augment a certain image onto  the 3D Object

## Feature Detection
In this program we detect all the features of a certain image.
* It explains the concept of Feature Detection and Description.
* Oriented FAST and Rotated BRIEF (ORB) is used as its Open Source.
* Feature detected and marked as green points in the image (red.jpg)


![Detect_Features](https://user-images.githubusercontent.com/74735039/112752648-a26ee900-8ff1-11eb-9fea-d1fdbb09d37b.png)

## Feature Matching
In this program we match the features that we detected to the real object.
* Feature Matching Attained with FLANN Based Matcher
* Draws matching lines while feauture matching accurately

### This Image shows almost no feature matching as its not the same as the data fed to the program:

![1](https://user-images.githubusercontent.com/74735039/112753092-dba85880-8ff3-11eb-8baf-ccaf60047fab.png)



### This Image shows the feature matching when the object is upright:

![Feature_Matching_Direct](https://user-images.githubusercontent.com/74735039/112752860-af400c80-8ff2-11eb-8196-1ea86a67cd35.png)


### This image shows the feature matching when the object is inverted:

![Feature Matching Inverted](https://user-images.githubusercontent.com/74735039/112752996-748aa400-8ff3-11eb-93a3-36f46363dad9.png)

## Image Augmentation
In this we use the features of the image and map them to a 'mask' image that has to be augmented on the real object.
* Uses the Homography Matrix to map all the features.
* Augments Image on realtime frame.


### This a demonstration of how this works:

This is when its held Upright


![Screenshot (292)](https://user-images.githubusercontent.com/74735039/112753228-596c6400-8ff4-11eb-8da0-07ecd36c494e.png)



This is when the object is held inverted



![Screenshot (293)](https://user-images.githubusercontent.com/74735039/112753301-b10acf80-8ff4-11eb-969e-9ec5dc54a104.png)
