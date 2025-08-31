import cv2 as cv
import numpy as np

#? ~~~ this is how to read an image
# dead_pool = cv.imread('dead_pool.jpg')

#? ~~~  the ord function returns the asci value of the specified key
# ASC = ord('B')
# print(ASC)

#? ~~~ if we print the just the image it will be just a matrix
# print(dead_pool)

#? ~~~ this is how to show it on the terminal

# cv.imshow('dead_pool' ,dead_pool )


# while True:
 
#  if cv.waitKey(1) & 0xff == ord('a'):    #* the wait is the time of display of the pic

#   break

# cv.destroyAllWindows()

#? ~~~ this is how to rescale the 

def rescalled(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimentions = (width , height)
    return cv.resize(frame ,dimentions , interpolation= cv.INTER_AREA)

# #? ~~~ this is how to capture videos 
# video =  cv.VideoCapture(0)
 
# while True :
#     flag , frame = video.read()# the first argument is the flag which is a true or false (whether it is working or not) and the other is the video frames itself
    
#     # rescale = rescalled(frame ,scale= 0.25)
#     cv.imshow('me without scalling ',frame)
#     # cv.imshow('me with scale',rescale)
#     #! this is for changing the colors of the pic
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('gray ',gray)

#     # print(flag)
#     if cv.waitKey(1) & 0xff == ord('t'):
#         break

# video.release()

# cv.destroyAllWindows()

#? ~~~this is how to create an image from scratch
#todo basically the image is just a 3d pixle array with each one reprent the color for that pixle 
black = np.zeros((500,500,3) , dtype = 'uint8')
# cv.imshow('black',black)

# black[:] = 255, 0 ,0
# cv.imshow('blue',black)
# cv.waitKey(0)

#? ~~~this is how to draw shapes (rectangle)
# rectangle = cv.rectangle(black.copy() , (30,30) ,(370,370) , ( 120 , 40 , 120) , thickness=-1 )

# #! black - The image/numpy array on which to draw the rectangle

# #! (0,0) - The starting point (top-left corner) of the rectangle

# #! Format: (x-coordinate, y-coordinate)

# #! (0,0) means start at the top-left corner of the image

# #! (blank.shape[1]//2, blank.shape[0]//2) - The ending point (bottom-right corner)

# #! blank.shape[1] gets the width of the image (second element of shape tuple)

# #! blank.shape[0] gets the height of the image (first element of shape tuple)

# #! "//2"  does integer division by 2

# #! This makes the rectangle extend to half the width and half the height

# #! (0,255,0) - The color of the rectangle in BGR format

# #! Blue=0, Green=255, Red=0 → Pure green

# #! In BGR: (Blue, Green, Red)

# #! thickness=-1 - The thickness of the rectangle border

# #! Positive values: Border thickness in pixels

# #! -1: Fills the entire rectangle with the specified color

# cv.imshow('blue',black)
# cv.waitKey(0)

#? ~~~this is how to draw shapes (circle)
# circle = cv.circle(black.copy() , (200,200) , 180 , (60 , 90 , 100), thickness= -1)
# #                          ^ center ^  ^R^
# cv.imshow('blue',black)

# two = cv.bitwise_and(circle, rectangle)
# cv.imshow('two',two)
# cv.waitKey(0)


#?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~?#
#  #! this approach did not work                                                                         
# image1_croco = cv.imread('crocomarine.png') # the shape is (1152, 1152, 3)                                    
# image2_circles = cv.imread('opencv.png') #the shape is  (776, 831, 3)

# circles_rescalled = rescalled(image2_circles , scale= .75) # the shape is 
# blank = np.zeros(image1_croco.shape , dtype='uint8')

# blank[0:circles_rescalled.shape[0] , 0:circles_rescalled.shape[1] ] = circles_rescalled
# two_blendend = cv.bitwise_or(blank,image1_croco)

# cv.imshow('tara', two_blendend)
# cv.waitKey(0) 

#?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~?#

#  #! this approach did not work            
# image1_croco = cv.imread('crocomarine.png') # the shape is (1152, 1152, 3)
# image2_circles = cv.imread('opencv.png') #the shape is  (776, 831, 3)

# circles_rescalled = rescalled(image2_circles , scale= .75) # the shape is 
# blank = np.zeros(image1_croco.shape , dtype='uint8')

# image1_croco[0:circles_rescalled.shape[0] , 0:circles_rescalled.shape[1] ] = circles_rescalled

# cv.imshow('tara', image1_croco )
# cv.waitKey(0) 
#?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~?#
#! this one worked !!!!!!
image1_croco = cv.imread('crocomarine.png') # the shape is (1152, 1152, 3)
image2_circles = cv.imread('opencv.png') #the shape is  (776, 831, 3)
circles_rescalled = rescalled(image2_circles , scale= .75) # the shape is 
blank = np.zeros(image1_croco.shape , dtype='uint8')
blank[0:circles_rescalled.shape[0] , 0:circles_rescalled.shape[1] ] = circles_rescalled
# cv.imshow('asdf',blank)
circles_grayed = cv.cvtColor(blank, cv.COLOR_BGR2GRAY)
thresh_hold , circles_thresh = cv.threshold(circles_grayed , 0 , 255 , cv.THRESH_BINARY)
# cv.imshow('tara', circles_thresh)
not_image = cv.bitwise_not(circles_thresh)
# cv.imshow('tara', not_image)
masked = cv.bitwise_and(image1_croco, image1_croco ,mask= not_image)
# cv.imshow('tara', masked)
add = masked + blank
cv.imshow('tara', add)
cv.waitKey(0)









