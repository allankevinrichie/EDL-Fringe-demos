# uses method from takeda to analyze an interferogram

import numpy as np
from skimage import data, io, filter, exposure
from matplotlib import pyplot as plt
from skimage.restoration import unwrap_phase

from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')

filename = 'dimpleRot.bmp'

img = io.imread(filename, as_grey=True)
img = exposure.rescale_intensity(img)

w = len(img[0,:])
h = len(img[:,0])

# reference row
row_ref = img[10,:]
row_ref_window = row_ref * np.hanning(w)
fft_ref = np.fft.fft(row_ref_window)
fftfreq_ref = np.fft.fftfreq(w)

# determine carrier frequency
ind = np.argmax(abs(fft_ref[3:w/2].real))+3

phi = np.zeros((h,w))
for i in range(0, h):
	row = img[i,:]
	#row_window = row * np.hanning(w)
        row_window = row	
        fft = np.fft.fft(row_window)

        #if i == h/2:	
        #    plt.figure()
	#    plt.plot(fft)	
        
	# do shifting
	fft_shift = fft
	# clear duplicates and DC
	fft_shift[0:w/2]=0
	fft_shift[w-1:len(row)]=0	
	# shift
	fft_shift = np.roll(fft_shift,ind)
	c = np.fft.ifft(fft_shift)
	phi[i,:] = np.log(c).imag

unwrapped = unwrap_phase(phi)

plt.figure(figsize = (12,6) )
plt.gray()

plt.subplot(131)
plt.imshow(img)
plt.title("Image")

plt.subplot(132)
plt.imshow(phi)
plt.title("Wrapped Phase")

plt.subplot(133)
plt.imshow(unwrapped)
plt.title("Unwrapped Phase")

plt.show()
plt.savefig('result.png')
