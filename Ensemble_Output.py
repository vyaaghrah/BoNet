import os, math
import cv2
import shutil 
import scipy
import sys

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from keras.models import load_model

vgg=load_model('VGG.h5')
vgg.load_weights('VGG19-Attention-best.hdf5')

incep=load_model('Inception.h5')
incep.load_weights('Inception-Attention-best.hdf5')

xcep=load_model('Xception.h5')
xcep.load_weights('Xception-Attention-best.hdf5')

print ("***************************************************************")


img1=cv2.imread(fname)
img1=np.expand_dims(img1, axis=0)
img = img1
t = ""
p = vgg.predict(img)
q = xcep.predict(img)
r = incep.predict(img)

if (math.isnan(p) or math.isnan(q) or math.isnan(r)):
	t = "Unknown Error"
	print (t)
	sys.exit(0)

a = 0 if p < 0.5 else 1
b = 0 if q < 0.5 else 1
c = 0 if r < 0.5 else 1

k = a + b + c

if k >= 2:
	t = "Your input X-ray is Normal."

elif k < 2:
	t = "Your input X-ray is Abnormal."

else:
	t=""

print (t)

print ("***************************************************************")
