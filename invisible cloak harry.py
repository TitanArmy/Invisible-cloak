
import numpy as np
import cv2
import time


cap=cv2.VideoCapture(0)

time.sleep(3) 
for i in range(30):
    retval,back=cap.read()
back=np.flip(back,axis=1)
cap=cv2.VideoCapture(0)  



while (cap.isOpened()): 
    ret,img=cap.read()
    if ret:
        img=np.flip(img,axis=1)
        
        
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
       
        lower_blue = np.array([0,120,70])
        upper_blue = np.array([10,255,255])
        mask1 = cv2.inRange(hsv,lower_blue,upper_blue)
        
        lower_blue = np.array([170,120,70])
        upper_blue = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_blue,upper_blue)
        mask1+=mask2
        
       

        mask = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        img[np.where(mask==255)]=back[np.where(mask==255)]
        

        cv2.imshow("Harry Potter's invisible secret revealed",img)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()