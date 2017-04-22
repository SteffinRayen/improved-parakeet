# Image Processing Assignment

## 1 Problem statement on OpenCV

You have to design a program which accepts coordinate arguments as A,B,C,D and image path. The output will distorted image according to given coordinates. 
Please use below representation as reference. You need to use libraries in Python (compulsory for this problem) to implement it. 
![Sample](https://www.flickr.com/photos/149397301@N04/shares/M75TgJ)

### Solution:
> python ImageDistortionUsingCoordinates.py 00.jpg 0 0 1600 0 1600 1600 0 1600 1600 0 1600 1600 0 1600 0 0

![Original Image](https://raw.githubusercontent.com/SteffinRayen/improved-parakeet/master/00.jpg)

![Distorted Image](https://raw.githubusercontent.com/SteffinRayen/improved-parakeet/master/distorted_picture.png)

## 2 Problem statement on python without library

1. Take any image as input and give a zoomed image as output. 
2. Width and height needs to be same of input and output image. 
3. Take pivot point (where to zoom) and scale as parameters. 
4. You can only use image libraries for loading and saving images, NOT for the function part.

### Solution:
> python ImageZoomingAndCropping.py 00.jpg 1.2 800 800

![Original Image](https://raw.githubusercontent.com/SteffinRayen/improved-parakeet/master/00.jpg)

![Zoomed Image](https://raw.githubusercontent.com/SteffinRayen/improved-parakeet/master/zoomed_picture.png)
