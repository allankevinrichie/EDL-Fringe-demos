import numpy as np
from matplotlib import pyplot as plt
from fringeAnalysis.WTP.constants import *
from fringeAnalysis import WTP
from fringeAnalysis.mask import remove_glowplug

from skimage import io, exposure
import sys,os,os.path

orig = io.imread('phi=0.9_frame0_crop.jpg', as_grey=True)
img = exposure.equalize_adapthist(orig)
img = exposure.rescale_intensity(img, out_range=(0,255))

template = io.imread('autolite_mask180x300.jpg', as_grey=True)

d_glowplug = 0.0051 #[m]
pix_glowplug = 182

masked = remove_glowplug(img, img, template, debug = False, outputPlot=False)

plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(orig)
plt.title("Image")

plt.subplot(122)
plt.imshow(masked)
plt.title("Masked")

plt.show()
plt.savefig('result.png')
