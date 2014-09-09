import numpy as np
from matplotlib import pyplot as plt
from skimage import io

import sys,os,os.path

imageFileBase = 'phi=0.9_frame'
frameNums = [0, 1, 2, 3, 4, 5, 10]
h = 500
w = 550
x_off = 100
y_off = 25

if not os.path.exists('cropped'):
    os.makedirs('cropped')

frameNums = map(str,frameNums)
for i in frameNums:
    imageFilename = ('images/' + imageFileBase + i + '.jpg')
    cropFilename = ('cropped/' + imageFileBase + i + '_crop.jpg')
    img = io.imread(imageFilename, as_grey=True)
    crop = img[ y_off:y_off+h, x_off:x_off+w]
    io.imsave(cropFilename, crop)

plt.figure()
plt.gray()
plt.title(cropFilename)
plt.imshow(crop)
plt.show()
