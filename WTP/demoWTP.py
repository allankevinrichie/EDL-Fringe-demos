import numpy as np
from matplotlib import pyplot as plt
import sys,os,os.path
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')

from fringeAnalysis.WTP.constants import *
from fringeAnalysis import WTP
from fringeAnalysis.unbias import unbias_image
from skimage.restoration import unwrap_phase

## begin parameters
imageFilename = 'dimple.bmp'    # image from http://www.ljmu.ac.uk/GERI/98301.htm
wavelet_type=MORLET		# PAUL4 or MORLET
ridge_alg= MAX 			# MAX or COST
use_FFT = YES
starting_scale = 1		# minimum period of a fringe in the image minus 5.
ending_scale = 50		# maximium period of a fringe in the image plus 5.
Morlet_sigma = 1
output_csv = True
## end parameters

orig = WTP.imagefile2dat(imageFilename)
wrapped = WTP.performWTP(wavelet_type = wavelet_type, ridge_alg = ridge_alg, 
	starting_scale = starting_scale, ending_scale=ending_scale, use_FFT=use_FFT, Morlet_sigma=Morlet_sigma)
unwrapped = unwrap_phase(wrapped)
signal = unbias_image(unwrapped)

plt.figure()
plt.gray()

plt.subplot(221)
plt.imshow(orig)
plt.title("Image")

plt.subplot(222)
plt.imshow(wrapped)
plt.title("Wrapped Phase")

plt.subplot(223)
plt.imshow(unwrapped)
plt.title("Unwrapped Phase")

plt.subplot(224)
plt.imshow(signal)
plt.title("Signal")

plt.show()
plt.savefig('result.png')

if output_csv :
	np.savetxt("image.csv", orig, delimiter=",")
	np.savetxt("wrapped.csv", wrapped, delimiter=",")
	np.savetxt("unwrapped.csv", unwrapped, delimiter=",")
       	np.savetxt("signal.csv", signal, delimiter=",")
