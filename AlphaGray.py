import numpy as np
import cv2
color= cv2.imread(r'C:\Users\Ashish\Desktop\Test\Messi.jpg')
gray=cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)


cv2.imwrite("Gray.jpg", gray)

cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
b= color[:,:,0]
g=color[:,:,1]
r=color[:,:,2]


# # converting the image to gray and adding alpha channel

cv2.imshow("Blue", b)
cv2.moveWindow("Blue",0,0)
cv2.imshow("Green", g)
cv2.moveWindow("Green",0,50)
cv2.imshow("Red", r)
cv2.moveWindow("Red",0,100)
cv2.waitKey(0)
cv2.destroyAllWindows()
rgba=cv2.merge((r,g,b,g))
cv2.imshow("RGBA",rgba)
cv2.waitKey(0)
cv2.destroyAllWindows()
