import numpy as np
from matplotlib import pyplot as plt
from fringeAnalysis.WTP.constants import *
from fringeAnalysis import WTP
from fringeAnalysis.mask import remove_sphere

from skimage import io, exposure
import sys,os,os.path

orig = io.imread('Centering_088_crop.tif', as_grey=True)
img = exposure.equalize_adapthist(orig)
img = exposure.rescale_intensity(img, out_range=(0,255))

r_min = 90
r_max = 110

masked = remove_sphere(img, img, r_min, r_max, debug = False, outputPlot=False)

plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(orig)
plt.title("Image")

plt.subplot(122)
plt.imshow(masked)
plt.title("Masked")

plt.savefig('sphereResult.png')
plt.show()

