# analyze_glowPlugShot4.py

import numpy as np
from matplotlib import pyplot as plt
from fringeAnalysis.WTP.constants import *
from fringeAnalysis import WTP
from fringeAnalysis.unbias import unbias_image
from fringeAnalysis.mask import get_autolite_template, locate_glowplug, remove_glowplug
from fringeAnalysis.symmetry import center_image_x
from fringeAnalysis.abel import perform_abel_discontinuous

from skimage.restoration import unwrap_phase
from skimage import io, exposure

import sys,os,os.path

## begin parameters
#imageFilename = 'cropped/phi=0.9_frame10_crop.jpg'
wavelet_type= PAUL4		# PAUL4 or MORLET
ridge_alg= MAX 			# MAX or COST
use_FFT = YES
starting_scale = 1		# minimum period of a fringe in the image minus 5.
ending_scale = 20		# maximium period of a fringe in the image plus 5.
Morlet_sigma = 1


d_glowplug = 0.0051 #[m]
measuredWidth = 182
dx = d_glowplug / measuredWidth

templateSlop = 4

imageFileBase = 'phi=0.9_frame'
frameNums = [0, 1, 2, 3, 4, 5, 10]

K_air = 2.274e-4 # merzkirch, p118, T=288K, lam = 509.7 nm
lam = 532e-9
n_air = 1.000293

## end parameters

## determine mask
orig = io.imread('cropped/phi=0.9_frame0_crop.jpg', as_grey=True)
img = exposure.equalize_adapthist(orig)
img = exposure.rescale_intensity(img, out_range=(0,255))
img_h, img_w = img.shape

approxTemplate = get_autolite_template(measuredWidth, img_h/2)
templateX, templateY, templateWidth  = locate_glowplug(img, approxTemplate, debug=False)
template = get_autolite_template(templateWidth+templateSlop, img_h/2)

## perform analysis
if not os.path.exists('results'):
    os.makedirs('results')

frameNums = map(str,frameNums)
for i in frameNums:
    imageFilename = ('cropped/' + imageFileBase + i + '_crop.jpg')

    orig = WTP.imagefile2dat(imageFilename)

    wrapped = WTP.performWTP(wavelet_type = wavelet_type, ridge_alg = ridge_alg, 
                        starting_scale = starting_scale, ending_scale=ending_scale, use_FFT=use_FFT, Morlet_sigma=Morlet_sigma)
    unwrapped = unwrap_phase(wrapped)

    phase = unbias_image(unwrapped)

    masked = remove_glowplug(phase, templateX-templateSlop/2, templateY, template)

    x, y, centered  = center_image_x(masked, templateX + templateWidth/2, templateY, dx)

    r, f_abel, deriv, smoothed  = perform_abel_discontinuous(x, centered)

    delta_n = f_abel*lam / (2*np.pi)
    rho= (n_air - delta_n - 1)/K_air

    fileroot = ('results/' + imageFileBase + i + '_crop')
    np.savetxt(fileroot+"_orig.csv", orig, delimiter=",")
    np.savetxt(fileroot+"_wrapped.csv", wrapped, delimiter=",")
    np.savetxt(fileroot+"_unwrapped.csv", unwrapped, delimiter=",")
    np.savetxt(fileroot+"_phase.csv", phase, delimiter=",")
    np.savetxt(fileroot+"_masked.csv",masked, delimiter=",")
    np.savetxt(fileroot+"_centered.csv",centered, delimiter=",")
    np.savetxt(fileroot+"_rho.csv",rho, delimiter=",")
