
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import cv2


# In[5]:


color= cv2.imread(r'C:\Users\Ashish\Desktop\Test\Messi.jpg')


# In[6]:


gray=cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)


# In[8]:


cv2.imwrite("Gray.jpg", gray)


# In[10]:


cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


b= color[:,:,0]


# In[13]:


g=color[:,:,1]


# In[14]:


r=color[:,:,2]


# # converting the image to gray and adding alpha channel

# In[15]:


cv2.imshow("Blue", b)
cv2.moveWindow("Blue",0,0)
cv2.imshow("Green", g)
cv2.moveWindow("Green",0,50)
cv2.imshow("Red", r)
cv2.moveWindow("Red",0,100)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[16]:


rgba=cv2.merge((r,g,b,g))
cv2.imshow("RGBA",rgba)
cv2.waitKey(0)
cv2.destroyAllWindows()

