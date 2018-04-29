####################################
#                                  #
#       ML_2018 410321170          #
#         TuWorld Slader           #
#                                  #
####################################



##################################
# Retrieval of Pixel information #
##################################

import random  #for the random number generator
import numpy as np
from PIL import Image # image library
with Image.open('C:\Python36-32\key1.png').convert('L') as imgk1: #'.open' opens file, '.convert('L')' changes it to grayscale image
	width, height = imgk1.size #gets the pixel dimensions of the image
	k1=(list(imgk1.getdata())) #list makes it a continuos list. getdata gets each pixel info. Since it is grayscale image now, it will all be integers
with Image.open('C:\Python36-32\key2.png').convert('L') as imgk2:
	k2=(list(imgk2.getdata()))
with Image.open('C:\Python36-32\I.png').convert('L') as imgI:
	I=(list(imgI.getdata()))
with Image.open('C:\Python36-32\E.png').convert('L') as imgE:
	E=(list(imgE.getdata()))	


####################################
# Declarations and initializations #
# of the variables				   #
####################################

maxiterlimit = 20
Ep = np.full((width*height+1,3), 0.00001) # the vigilance level for checking the convergence of weight vectors
alpha = 0.00001 #learning rate
epoch = 1
w_curr_epoch = np.zeros((width*height+1,3)) 
w_curr_epoch[0] = np.random.rand(1,3) #Generates random values for w(0) from 0-1
w_last_epoch = np.zeros((width*height+1, 3))
x = np.zeros((width*height+1, 3))
a = np.zeros((width*height, 1))
e = np.zeros((width*height, 1))

#################################
# Set x(k) = [K1(k),K2(k),I(k)] #
#################################
for i in range(width*height):
	x[i] = np.array([k1[i], k2[i], I[i]])


################################
#    Finding w=[w1, w2, w3]    #
################################

while (epoch==1) or (epoch < maxiterlimit) and (np.any((np.absolute(np.array(w_curr_epoch) - np.array(w_last_epoch))) > Ep)):
	for k in range(width*height):
		a[k] = w_curr_epoch[k].dot(x[k])
		e[k] = E[k] - a[k]
		w_last_epoch[k] = w_curr_epoch[k]
		temp = alpha*(e[k])
		w_curr_epoch[k+1] = w_curr_epoch[k] + temp*(x[k])
	
	print(epoch)
	epoch = epoch+1
print (w_curr_epoch) #Prints the [w1,w2,w3] for each pixel


##################################
#      Decryption test           #
##################################

with Image.open('C:\Python36-32\Eprime.png').convert('L') as imgEprime:
	Eprime=(list(imgEprime.getdata()))

tempIprime = np.full((width*height, 1), 0)
for i in range(width*height):
	tempIprime[i] = (Eprime[i] - w_curr_epoch[i+1][0]*k1[i] - w_curr_epoch[i+1][1]*k2[i]) / w_curr_epoch[i+1][2] #Decryption formula
	#Ensuring that tempIprime is within 0 - 255
	if tempIprime[i] < 1: 
		tempIprime[i] = 0
	elif tempIprime[i] > 255:
		tempIprime[i] = 255

#Saves and displays the decrypted image
tempIprime = np.asarray(tempIprime, dtype=np.uint8) #converts the values back to int
tempIprime.resize((height,width)) #resize the array to the dimensions of the picture
Iprime = Image.fromarray(tempIprime, mode='L') #Converts the array into a grayscale image
Iprime.save('C:\Python36-32\Iprime.png') #Saves the image
Iprime.show() #display image
