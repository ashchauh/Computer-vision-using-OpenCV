
# coding: utf-8

# # Gaussian blur, Dilation and Erosion
# # To remove noise and variance from image (pixel that are closer have high avaerge affect)

import numpy as np
import cv2
image=cv2.imread(r'C:\Users\Ashish\Desktop\Test\Messi.jpg')

cv2.imshow("Original", image)
blur= cv2.GaussianBlur(image,(5,55),0)
cv2.imshow("Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Removed the noise

# # Erosion and Dilation filter
# ##  used to contract or expland the foreground pixels to help remove or accentuate small pixel details (speckles)
# ## dilation--> black pixels into while pixels and erosion--> white into black
kernel= np.ones((5,5),'uint8')
dilate=cv2.dilate(image,kernel, iterations=1)
erode= cv2.erode(image,kernel, iterations=1)
cv2.imshow("Dilate",dilate)
cv2.imshow("Erode", erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
