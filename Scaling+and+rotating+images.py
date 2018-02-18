
# coding: utf-8

# # Scaling and rotating images

# In[1]:


import numpy as np
import cv2


# In[4]:


img= cv2.imread(r'C:\Users\Ashish\Desktop\Test\Messi.jpg')


# In[5]:


img_hlf= cv2.resize(img, (0,0), fx=0.5,fy=0.5)


# In[6]:


img_strch=cv2.resize(img, (600,600), fx=600,fy=600)


# In[7]:


img_strch_near=cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)


# In[10]:


cv2.imshow("Image Half",img_hlf)
cv2.imshow("Image Stretch",img_strch)
cv2.imshow("Image Strech Near", img_strch_near)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Rotation of image (using matrix transformation)

# In[12]:


M=cv2.getRotationMatrix2D((0,0),-30,1)
rotated=cv2.warpAffine(img,M, (img.shape[1],img.shape[0]))


# In[13]:


cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

