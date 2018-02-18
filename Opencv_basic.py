
# coding: utf-8

# In[4]:


import cv2
import numpy as np
img=cv2.imread(r'C:\Users\Ashish\Desktop\Test\download.png')
cv2.imshow("Image", img)
cv2.waitKey(0)


# In[4]:


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


# In[7]:


ones= np.ones([150,200,3], 'uint8')
cv2.imshow("Ones", ones)
print (ones)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


white= np.ones([150,200,3], 'uint16')
white*=(2**16-1)
cv2.imshow("White", white)
print (white[0,0,:])
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


blue=ones.copy()
blue[:,:,0]= 255


# In[10]:


cv2.imshow("Blue", blue)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


Image types and conversions:


# In[11]:


color=cv2.imread(r'C:\Users\Ashish\Desktop\Test\Messi.jpg')
cv2.imshow("Image", color)

cv2.moveWindow("Image",0,0)
b,g,r=cv2.split(color)
height,width,length= color.shape
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


Splitting image into RGB images:


# In[12]:


rgb_split= np.empty([height,width*3, 3], 'uint8')
rgb_split[:,0:width]=cv2.merge([g,g,g])
rgb_split[:,width:width*2]=cv2.merge([b,b,b])
rgb_split[:,width*2:width*3]=cv2.merge([r,r,r])
cv2.moveWindow("rgb_split",0,height)
cv2.imshow("Split", rgb_split)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


Hue Saturation and value space:


# In[13]:


hsv=cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v=cv2.cv2.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow("HSVSplit", hsv_split)
cv2.waitKey(0)
cv2.destroyAllWindows()

