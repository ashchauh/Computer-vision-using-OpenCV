
# coding: utf-8
import cv2
import numpy as np
img=cv2.imread(r'C:\Users\Ashish\Desktop\Test\download.png')
cv2.imshow("Image", img)
cv2.waitKey(0)

img1=cv2.imread(r'C:\Users\Ashish\Desktop\Test\download.png',1)
cv2.imshow("Image", img1)
cv2.waitKey(0)
img
type(img)
img.dtype
img.shape
img.size


# In[6]:


black= np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)
print (black)
cv2.waitKey(0)
cv2.destroyAllWindows()
ones= np.ones([150,200,3], 'uint8')
cv2.imshow("Ones", ones)
print (ones)
cv2.waitKey(0)
cv2.destroyAllWindows()

white= np.ones([150,200,3], 'uint16')
white*=(2**16-1)
cv2.imshow("White", white)
print (white[0,0,:])
cv2.waitKey(0)
cv2.destroyAllWindows()
blue=ones.copy()
blue[:,:,0]= 255
cv2.imshow("Blue", blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image types and conversions:
color=cv2.imread(r'C:\Users\Ashish\Desktop\Test\Messi.jpg')
cv2.imshow("Image", color)

cv2.moveWindow("Image",0,0)
b,g,r=cv2.split(color)
height,width,length= color.shape
cv2.waitKey(0)
cv2.destroyAllWindows()

#Splitting image into RGB images:
rgb_split= np.empty([height,width*3, 3], 'uint8')
rgb_split[:,0:width]=cv2.merge([g,g,g])
rgb_split[:,width:width*2]=cv2.merge([b,b,b])
rgb_split[:,width*2:width*3]=cv2.merge([r,r,r])
cv2.moveWindow("rgb_split",0,height)
cv2.imshow("Split", rgb_split)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Hue Saturation and value space:
hsv=cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v=cv2.cv2.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow("HSVSplit", hsv_split)
cv2.waitKey(0)
cv2.destroyAllWindows()

