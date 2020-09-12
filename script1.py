import cv2

s=input("Enter The Name of the File: ")
#print(s)
a=int(input("Enter the Desired Breadth: "))
b=int(input("Enter the Desired Height: "))
t=input("Enter the Name of the New Resized File: ")
t="Files/"+t
s="Files/"+s
img=cv2.imread(s,1)
#cv2.imshow("Picture Box",img)
#cv2.waitKey(0)
resized_image=cv2.resize(img,(a,b))
cv2.imwrite(t,resized_image)
