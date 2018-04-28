# ML2018_410321170
# Get image height and width

from PIL import Image
with Image.open('C:\Python36-32\8f0.png') as img:
	width,height = img.size
print ("Width  is ",width)
print ("Height is ",height)
