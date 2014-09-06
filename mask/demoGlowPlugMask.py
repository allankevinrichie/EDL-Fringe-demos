import numpy as np
from matplotlib import pyplot as plt
from fringeAnalysis.WTP.constants import *
from fringeAnalysis import WTP
from fringeAnalysis.mask import get_autolite_template, locate_glowplug, remove_glowplug
from skimage import io, exposure
import sys,os,os.path

measuredWidth = 182
templateSlop = 4

orig = io.imread('phi=0.9_frame0_crop.jpg', as_grey=True)
img = exposure.equalize_adapthist(orig)
img = exposure.rescale_intensity(img, out_range=(0,255))

img_h, img_w = img.shape
approxTemplate = get_autolite_template(measuredWidth, img_h/2)

templateX, templateY, templateWidth  = locate_glowplug(img, approxTemplate, debug=False)

template = get_autolite_template(templateWidth+templateSlop, img_h/2)
masked = remove_glowplug(img, templateX-templateSlop/2, templateY, template)

plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(orig, interpolation='none')
plt.title("Image")

plt.subplot(122)
plt.imshow(masked, interpolation='none')
plt.title("Masked")

plt.savefig('glowplugResult.png')
plt.show()

