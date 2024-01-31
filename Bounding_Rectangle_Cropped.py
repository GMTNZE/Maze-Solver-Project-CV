import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

### To crop bounding rectabgle and remove other parts---does not stop once corner is not detected so issue in bounding_rectangle can be solved
### Issue- Test if it would work on the maze is impending



def scan_to_frame(img):


    img1 = cv.imread(img, 0)
    cv.imshow('image', img1)
    corners = cv.goodFeaturesToTrack(img1, 50, 0.01, 5) 
    corners = np.int0(corners)
    print (corners)

    ret, thresh = cv.threshold(img1,140,255,0)
    contours,hierarchy = cv.findContours(thresh, 1, 2)
    cnt = contours[0]

    x,y,w,h = cv.boundingRect(cnt)
    thresh = cv.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
    thresh = thresh[y:y+h,x:x+h]
    
    cv.imshow('binary image', thresh)

    cv.imwrite(f'imagee{count}.jpg', thresh)
    cv.waitKey(2000)

cap = cv.VideoCapture(0)

while (True):
    count = 0
    count = count + 1

    ret, frame = cap.read()

    cv.imwrite(f"frame{count}.jpg", frame)
    scan_to_frame(f'frame{count}.jpg')

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows










