import numpy as np
import dlib
from skimage import io

def facialPoints(img):
    #USE:
    size=np.shape(img)
    predictor_path="shape_predictor_68_face_landmarks.dat"

    detector=dlib.get_frontal_face_detector()

    predictor=dlib.shape_predictor(predictor_path)

    dets=detector(img,1)
    
    for k, d in enumerate(dets):
        shape=predictor(img,d)
    vec=np.empty([8,2],dtype=int)
    for b in range(68):
        vec[b][0]=shape.part(b).x/(size[0]-1)
        vec[b][1]=shape.part(b).y/(size[1]-1)
    ##/(size[0]-1) IS to Normalize the points to be 
    ##In the range 0. to 1. for all images
    return vec

img=io.imread("example.png")
print (facialPoints(img))