import cv2

### To find bounding rectangle of image/define grid limits
### Issues- Stops if it doesn't detect any boundaries/Test with camera impending

vid = cv2.VideoCapture(0)

while (True):


    ret, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,127,255,0)

    contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    x,y,w,h = cv2.boundingRect(cnt)

    img = cv2.drawContours(img,[cnt],0,(0,255,255),2)

    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Bounding Rectangle", img)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
       break



#cv2.waitKey(0)
cv2.destroyAllWindows()