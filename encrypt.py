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
	

w = []
file = open('C:\Python36-32\w.txt', 'r')
for x in file.readlines():
	w.append(float(x))

	
################################
#    Encryption	               #
################################

with Image.open('C:\Python36-32\I4.png').convert('L') as imgItest:
	Itest=(list(imgItest.getdata()))
	
tempE2 = np.full((width*height, 1), 0)
for i in range(width*height):
	tempE2[i] = w[0]*k1[i] + w[1]*k2[i] + w[2]*Itest[i] #Encryption formula
	#Ensuring that tempIprime is within 0 - 255
	if tempE2[i] < 1: 
		tempE2[i] = 0
	elif tempE2[i] > 255:
		tempE2[i] = 255

#Saves and displays the decrypted image
tempE2 = np.asarray(tempE2, dtype=np.uint8) #converts the values back to int
tempE2.resize((height,width)) #resize the array to the dimensions of the picture
E2 = Image.fromarray(tempE2, mode='L') #Converts the array into a grayscale image
E2.save('C:\Python36-32\E4prime.png') #Saves the image
E2.show() #display image