'''
What is opencv?
    -> open source computer vision
    -> used mainly for image processing and computer vision
 
Steps:
1. we need to install the opencv in our project
    pip install opencv-python
 
2. create a sample.py file and import cv2 package
3. write a code print(cv2.__version__)
 
Predefined functions available:
1. how to read an image to our program
    -> imread()
        -> used to get the image from the specified location
    syntax:
    cv2.imread(filename,flag)
 
    filename = the path to the image. it shouldn't be a direct link
    flag = how the image should be read(with color or without color)
 
    if you want the image in color, we need to give that as cv2.IMREAD_COLOR
    if you want the image in grayscale, we need to give that as cv2.IMREAD_GRAYSCALE
 
    we need to store this image in a variable
 
2. how we need to display the image
    -> imshow()
        -> used to display the image as a dialogue box
 
    syntax:
    cv2.imshow(window_name,image_variable)
 
3. To keep the image output steady.
    -> waitKey()
        -> used to hold the output window for certain seconds until user enter/press any key
    syntax:
    cv2.waitKey(0)
 
4. how to close the output window without using close icon
    ->destoryAllWindows()
        -> used to close all the output windows
    syntax:
        cv2.destoryAllWindows()
'''
# 5. How to get multiple image loaded to multiple output screen
# import cv2
 
# img1 = cv2.imread("blood cell.jpg",cv2.IMREAD_COLOR)
# img2 = cv2.imread("blood cell.jpg",cv2.IMREAD_GRAYSCALE)
 
# cv2.imshow("Input Image1",img1)
# cv2.imshow("Input image2",img2)
 
# cv2.waitKey(0)
 
# cv2.destroyAllWindows()
 
# 6. How to get multiple image loaded to single output window
#     -> concatenate()
#         -> this concatenate function is available only in out numpy package not in opencv package
#         -> image needs to be same as input don't change the color frames.
#     syntax:
#     numpy.concatenate((filenames...),axis=val)
 
#     val = 0 or 1
#     0 -> combine the files into vertical axis
#     1 -> combine the files into horizontal axis
 
#     1. we need to import the numpy package
#         import numpy
 
#         used to have lot of advance mathematical formulas, implementation, inside that package with predefined executions
 
# import cv2
# import numpy
 
# img1 = cv2.imread("sample2/blood cell.jpeg")
# img2 = cv2.imread("sample2/blood cell.jpeg")
 
# img = numpy.concatenate((img1,img2),axis=0)
 
# cv2.imshow("Concatenated Images",img)
 
# cv2.waitKey(0)
 
# cv2.destroyAllWindows()
 
#  7. How to save an image using opencv
#     -> imwrite()
#         -> used to store the images used in our project with different names for future purpose.
 
#     syntax:
#     cv2.imwrite(imagename,image_source)
 
# import cv2
 
# img = cv2.imread('blood cell.jpg',cv2.IMREAD_GRAYSCALE)
 
# imagename = 'grayscale_converted_image.jpg'
 
# cv2.imwrite(imagename,img)
 
# # img = cv2.imread('grayscale_converted_image.jpg')
# # cv2.imshow('output',img)
 
# cv2.waitKey(0)
 
# cv2.destroyAllWindows()
 
# 8. How to resize the images which we read.
#     -> most of the time, we will not get the perfect size of the image, sometimes it will be large or too small. So, we need to
#     re-size the image to common size.
#     -> resize()
#         -> used to re-size the images to a common size.
   
#     syntax:
#     cv2.resize(source,dsize,destination,fx,fy,interpolation)
 
#     source -> image which we have read
#     dsize -> size of the output iamge
#     destination -> the output image to be saved once again (work like imwrite())
#                 -> optional
#     fx - scale factor on horizontal axis
#     fy - scale factor on vertical axis
#     interpolation - automated sizing
#         -> INTER_AREA
#             -> when we are going to use a image as shrinked one
#         -> INTER_CUBIC
#             -> slowest resizing option
#         -> INTER_LINEAR
#             -> when we are going to use a image as zoomed one
#         -> optional
   
#     1. half image condition
#         -> dsize = (0,0)
#         -> fx > 0
#         -> fy > 0
 
# 
# 9. Edge detection
#     -> is a process that involves detecting sharp edges in the image.
#     -> canny() function
#         -> canny edge detection algorithm
#             -> John F. Canny
#     -> use of this algorithm:
#         -> Noise reduction using filters
#         -> maximum supression (we need to have only the shapes of the images)
 
#     syntax:
#     cv2.Canny(source,min value, max value, size,L2gradient)
#         source = image
#         minvalue = minimum gradient
#         maxvalue = maximum gradient
#         size = optional
#         L2gradient = used to provide the accurate gradient calculation
#                   -> two values possible
#                   ->0 -> false
#                   ->1 -> true
 
#     min = 0 -> with inner circle and all possible edges of the images
#     min = 100 -> with few inner circles are possible
 
# import cv2
 
# img = cv2.imread('sample2/blood cell.jpeg')
 
# # edge1 = cv2.Canny(img,0,300)
# # edge2 = cv2.Canny(img,100,300)
# # edge3 = cv2.Canny(img,200,300)
# edge4 = cv2.Canny(img,0,1000)
# # cv2.imshow("Edge1 Output",edge1)
# # cv2.imshow("Edge2 Output",edge2)
# # cv2.imshow("Edge3 Output",edge3)
# cv2.imshow("Edge4 Output",edge4)
 
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''For converting from color to grayscale
    -> cvtColor()
        -> used to convert the given image into any color for image as you wish
        -> grayscale = cv2.COLOR_BGR3GRAY
For blurring the images
    -> GaussianBlur()
    syntax:
    cv2.GaussianBlur(image,(sigmaX,sigmaY),kernal_size)
For the theshold image
    -> threshold()
for the contour image
    -> whether we have curved edges in our given image
    -> findContour()
 
Contour Types:
RETR_LINK -> including all outer and inner curves
RETR_EXTERNAL -> include only the outer curves
RETR_TREE -> grandparents,parents,child
RETR_CCOMP ->
'''
import cv2
 
abo_image = cv2.imread('blood cell.jpeg')
# cv2.imshow('Original Image',abo_image)
 
# convert the image from color to grayscale
gray = cv2.cvtColor(abo_image,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale Image',gray)
# we need to blur the image for more accurate blood cell conditions
# blurring the image means -> smoothening the image
blur = cv2.GaussianBlur(gray,(5,5),0)
# cv2.imshow('Blurred Image',blur)
# blurred to threshold
# threshold
# syntax: threshold(image,dest,thresholdValue,maxValue,thresholdType)
# calculate the threshold values for the images your have given and it will return the image as well as the val
val1,threshold = cv2.threshold(blur,120,255,cv2.THRESH_BINARY)
# cv2.imshow('Threshold Image',threshold)
# find the contours
# used to find the curved edges of the images
# findContours(image,contourType,contourValue)
contour,val2 = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# count the number of contours we found in the image
# print(contour)
contour_length = len(contour)
# print(contour_length)
if(contour_length<50):
    print('O')
elif(50 <= contour_length < 100):
    print('A')
elif(100 <= contour_length < 150):
    print('B')
else:
    print('AB')
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 