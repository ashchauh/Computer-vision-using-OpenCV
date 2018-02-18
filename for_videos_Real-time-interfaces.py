
# coding: utf-8

# # Real time interface

# In[5]:


import numpy as np
import cv2


# In[8]:


cap=cv2.VideoCapture(0)
color= (0,255,0)
line_width=3
radius=100
point=(0,0)
def click(event,x,y,flags,param):
    global point,pressed #this is a callback everytime we click the mouse on video feed
    if event==cv2.EVENT_LBUTTONDOWN:
        print ("Pressed", x,y)
## register this stuff to opencv handler
cv2.namedWindow("FRAME")
cv2.setMouseCallback("FRAME", click)
while (True):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(0,0), fx=0.5,fy=0.5)
    cv2.circle(frame,point,radius,color,line_width)
    cv2.imshow("Frame", frame)
    ch=cv2.waitKey(1)
    if ch & 0xFF==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
