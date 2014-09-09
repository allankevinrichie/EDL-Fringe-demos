import numpy as np
from matplotlib import pyplot as plt
from skimage import io
import sys,os,os.path
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')
imageFileBase = 'phi=0.9_frame'
frameNums = [0, 1, 2, 3, 4, 5, 10]
fps = 6000

d_glowplug = 0.0051 #[m]
pix_glowplug = 182
dx = d_glowplug / pix_glowplug

fig, axs = plt.subplots(2,4, figsize=(20,12) )
plt.suptitle(r'Density [kg/m$^3$], $\phi$ = 0.9', fontsize=24)
plt.jet()
axs = axs.ravel()
#
for idx, frame in enumerate(frameNums):
    #frameStr = map(str, frame)
    filename = 'results/' + imageFileBase + str(frame) +"_crop_rho.csv"
    rho = np.loadtxt(filename, delimiter=",")
    h, w =  rho.shape
    x_extent = w * dx*1000
    y_extent = h * dx*1000
    
    plt.axes(axs[idx]) 
    plt.imshow(rho,interpolation='none',extent=(0,x_extent, 0, y_extent) ) 
    
    plt.colorbar()
    plt.clim(0,1.4)
    t = 1.0* frame/fps
    plt.title('t = ' + "{:10.4f}".format(t*1000) + ' ms')
    plt.xlabel('r [mm]',fontsize=12)
    plt.ylabel('z [mm]')

plt.savefig('result.png')
plt.show()

