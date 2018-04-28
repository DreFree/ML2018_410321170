# ML2018_410321170
# Gets the grayscale values for each picture as integers

from PIL import Image
with Image.open('C:\Python36-32\key1.png').convert('L') as img1:
	print(list(img1.getdata()))
with Image.open('C:\Python36-32\key2.png').convert('L') as img2:
	print(list(img2.getdata()))
with Image.open('C:\Python36-32\I.png').convert('L') as img3:
	print(list(img3.getdata()))
