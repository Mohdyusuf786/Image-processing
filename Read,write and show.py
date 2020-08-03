import cv2

img=cv2.imread('apple.jpg') #to read a image
var=cv2.imwrite('orange.jpg',img) #to overwrite on existing image

cv2.imshow("org",img)#to show the image

cv2.waitKey(0)
cv2.destroyAllWindows() #to destroy the windows
