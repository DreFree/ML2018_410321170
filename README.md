#Retrieval of Pixel information
import random 
import numpy as np
from PIL import Image # image library
with Image.open('C:\Python36-32\key1.png').convert('L') as imgk1: #.open opens file, .convert('L') changes it to grayscale image
	width, height = imgk1.size
	k1=(list(imgk1.getdata())) #list makes it a continuos list. getdata gets each pixel info. Since it is grayscale image now, it will all be integers
with Image.open('C:\Python36-32\key2.png').convert('L') as imgk2:
	k2=(list(imgk2.getdata()))
with Image.open('C:\Python36-32\I.png').convert('L') as imgI:
	I=(list(imgI.getdata()))
with Image.open('C:\Python36-32\E.png').convert('L') as imgE:
	E=(list(imgE.getdata()))	

#############################################################
print (k1[(width*height)-2])
print ("width: ", width, "height: ", height)


#############################################################
maxiterlimit = 30
E = 2
alpha = 0.00001
epoch = 1
w = np.random.rand(1,3)
x = np.random.rand(width*height, 3)

for i in range(width*height):
	print(i)
	if i == 119999:
		x[i] = [0,0,0]

print (x)
#while epoch==1
#for i in range(width*height)
