import cv2
import numpy as np
class Window:
    def __init__(self, WIDTH=300, HEIGHT=150, WNAME="Track",pos=None):
        self.WNAME = WNAME
        HEIGHT = int(HEIGHT)
        WIDTH = int(WIDTH)
        self.frame = np.zeros((HEIGHT,WIDTH,3),np.uint8)
        cv2.namedWindow(WNAME)
        cv2.resizeWindow(WNAME, WIDTH, HEIGHT)
        if pos is not None:
            cv2.moveWindow(WNAME,pos[0],pos[1])

    def _nothing(self,x):
        return x
    
    def add_bar(self,name="",start=0,to=255):
        cv2.createTrackbar(name,self.WNAME,start,to,self._nothing)

    def __getitem__(self,name):
        return cv2.getTrackbarPos(name,self.WNAME)

    def show(self):
        cv2.imshow(self.WNAME,self.frame)

    def __setitem__(self,name,value):
        cv2.setTrackbarPos(name, self.WNAME, value)

wind = Window()
rose = cv2.imread('rose1.png')
wind.frame = rose
# wind.show()




lower = np.array([140, 90, 10])
upper = np.array([180, 255, 255])
hsv = cv2.cvtColor(rose, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
mask2 = cv2.inRange(hsv, lower, upper)




gray_one_channel = cv2.cvtColor(rose , cv2.COLOR_BGR2GRAY)
gray_three_channels = cv2.cvtColor(gray_one_channel ,cv2.COLOR_GRAY2BGR)  
bluring  = cv2.blur(gray_three_channels , (wind.frame.shape[1], wind.frame.shape[0]))
blur= cv2.addWeighted(gray_three_channels , alpha= 0.3 , src2= bluring , beta= 0.7 , gamma= 0 )  #todo~~ this is called blending it adds two images together !!!
# cv2.imshow("blur", blur)





#!outliers test 1 !!!
# morph_close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE , kernel ,iterations= 3)
# morph_open = cv2.morphologyEx(morph_close, cv2.MORPH_OPEN , kernel , iterations= 3)
#todo i have to change any mask with morph_open
#!outliers test 1 !!!


#!outliers test 2 !!!
mask = cv2.erode(mask,None , iterations= 3)
mask=cv2.dilate(mask,None , iterations= 19)
mask = cv2.erode(mask,None , iterations= 17 )

cv2.imshow('mask',mask)
#todo i have to change any mask with dilate
#!outliers test 2 !!!





rose_only= cv2.bitwise_and(rose ,rose , mask= mask)
# cv2.imshow("rose_only",rose_only )

image_without_rose_blk_wht = cv2.bitwise_not(mask)
# cv2.imshow("image_without_rose_blk_wht", image_without_rose_blk_wht)

blur_without_rose = cv2.bitwise_and(blur,blur ,mask=image_without_rose_blk_wht)
# cv2.imshow("blur_without_rose", blur_without_rose)

target = blur_without_rose  + rose_only
cv2.imshow("target", target)

# cv2.imshow("erosion", erosion)
# cv2.imshow("dilate", dilate)
# cv2.imshow("morph", morph_open)








cv2.waitKey(0)