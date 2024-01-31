import numpy as np
import cv2 
from skimage import util

### To take input image, blur it to reduce noise and then grayscale it (also save it)
### Issues- Noise from shadows not completely removed/dependent on light. (Threshhold changes were useful so may be fixed after IRL Test)
def grayscale (pic):
    imgray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    ret, pic = cv2.threshold(imgray, 150, 255, 0, cv2.THRESH_BINARY)
    cv2.imshow('grayscale', pic)
  
    return(pic)

    '''corners = cv2.goodFeaturesToTrack(pic, 50, 0.01, 5) 
    corners = np.int0(corners)

    set_z = np.ravel(corners)

    min_x=max_x=set_z[0]
    min_y=max_y=set_z[1]


    for i in corners: 
       x, y = i.ravel() 
       cv2.circle(pic, (x, y), 3, 255, -1)
       if x < min_x:
           min_x = x
       if x > max_x:
           max_x = x
       if y < min_y:
           min_y = y
       if y > max_y:
           max_y = y

    print (min_x,min_y,max_x,max_y)

##site for direct code/attribute for bounding rectangle
#https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html 

    crop_img = pic[min_x:max_x,min_y:max_y]

    cv2.imshow('crop_image',crop_img)'''
i = 1
vid = cv2.VideoCapture(0)
while (True):
      
    
    i = i+2
    ret, frame = vid.read() 
  
   
    cv2.imshow('frame', frame) 
    cv2.imwrite('xyz'+str(i)+'.jpg', frame)

    #lower_red = np.array([0, 0, 200], dtype = "uint8")
    #upper_red= np.array([0, 0, 255], dtype = "uint8")
    #hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #mask = cv2.inRange(frame, lower_red, upper_red)

    #robot_mark = cv2.bitwise_and(frame, frame, mask = mask)

    #cv2.imshow('robot location', robot_mark)

    #cv2.imwrite('xyz'+str(i+1)+'.jpg', robot_mark)
    Gaussian = cv2.GaussianBlur(frame, (7, 7), 0) 
    cv2.imshow('Gaussian Blurring', Gaussian)


    frame = grayscale(Gaussian)
    cv2.imwrite('xyz'+str(i)+str(i)+'.jpg', frame)
    
    cv2.waitKey(2000)

    

 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
       break








vid.release() 
cv2.destroyAllWindows() 
''' Gaussian = cv2.GaussianBlur(frame, (7, 7), 0) 
    cv2.imshow('Gaussian Blurring', Gaussian)


    frame = grayscale(Gaussian)
    cv2.imwrite('xyz'+str(i)+str(i)+'.jpg', frame)
    
    cv2.waitKey(2000)
    
'''

'''
    cv2.imwrite("xyz.jpg", frame) 
    img = cv2.imread("xyz.jpg",0)
      

    ret, thresh = cv2.threshold("xyz",140,255,0)

    cv2.imwrite('xyz', thresh)'''






'''img = cv2.imread('frame65.jpg')

# Gaussian Blur 
Gaussian = cv2.GaussianBlur(img, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', Gaussian) 
grayscale(Gaussian)





cv2.waitKey(0) 
  
# Median Blur 
median = cv2.medianBlur(img, 5) 
cv2.imshow('Median Blurring', median) 
grayscale(median)
cv2.waitKey(0) 
  
  
# Bilateral Blur 
bilateral = cv2.bilateralFilter(img, 9, 75, 75) 
cv2.imshow('Bilateral Blurring', bilateral) 
grayscale(bilateral)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

cv2.waitKey()
cv2.destroyAllWindows()'''