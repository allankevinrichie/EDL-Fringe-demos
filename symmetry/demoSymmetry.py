import numpy as np
from matplotlib import pyplot as plt

from fringeAnalysis.symmetry import center_image_x, symmetry_error_x

import sys,os,os.path

d_glowplug = 0.0051 #[m]
measuredWidth = 182

bestWidth = 179 # output from glowplug.py
bestX = 185
bestY = 205

offset = 350

centerX = bestX + bestWidth/2

image = np.loadtxt('phi=0.9_frame0_crop_masked.csv', delimiter=",")
h, w = image.shape

dx = d_glowplug / measuredWidth

zeros = np.zeros( (h, offset) )

image = np.append(image, zeros , 1)
x, y, centered = center_image_x(image, centerX, bestY, dx)
error = symmetry_error_x(centered)

plt.figure(figsize=(20,6))
plt.subplot(131)
plt.imshow(image)
plt.title('Uncentered Image')

plt.subplot(132)
plt.imshow(centered)
plt.title('Centered Image')

plt.subplot(133)
plt.imshow(error, interpolation='none')
plt.title('Symmetry error')
plt.colorbar()
plt.clim(0,.25)

plt.savefig('result.png')

plt.show()
