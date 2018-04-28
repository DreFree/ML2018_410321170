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
#print (k1[(width*height)-2])
#print ("width: ", width, "height: ", height)

################
#Declarations
################
maxiterlimit = 30
Ep = np.ones((width*height,3))
alpha = 0.00001
epoch = 1
w_curr_epoch = np.random.rand(width*height,3)
w_last_epoch = np.zeros((width*height, 3))
x = np.zeros((width*height, 3))
a = np.zeros((width*height, 1))
e = np.zeros((width*height, 1))

#Set x(k) = [K1(k),K2(k),I(k)]
for i in range(width*height):
	x[i] = np.array([k1[i], k2[i], I[i]])

while (epoch==1 or (epoch < maxiterlimit) and (np.all((np.absolute(np.array(w_curr_epoch) - np.array(w_last_epoch))) > Ep))):
	for k in range(width*height):
		a[k] = w_curr_epoch[k].T.dot(x[k])
		e[k] = E[k] - a[k]
		w_last_epoch[k] = w_curr_epoch[k]
		temp = a[k].dot(e[k])
		w_curr_epoch[k] = w_curr_epoch[k] + temp*x[k]
	epoch = epoch+1

print (w_curr_epoch)

sum0=sum1=sum2=0
for i in range(width*height):
	sum0 = sum0 + w_curr_epoch[i][0]
	sum1 = sum1 + w_curr_epoch[i][1]
	sum2 = sum2 + w_curr_epoch[i][2]
w = [(sum0, sum1, sum2)]
print()
print(w)
#print (x)
#print ()
#print (w)
#print ()
#print (x[119999].dot(x[119998].T))
#while epoch==1
#for i in range(width*height)
