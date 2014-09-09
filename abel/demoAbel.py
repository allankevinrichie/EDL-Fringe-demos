import numpy as np
from matplotlib import pyplot as plt

from fringeAnalysis.symmetry import center_image_x
from fringeAnalysis.abel import perform_abel_discontinuous

import sys,os,os.path

d_glowplug = 0.0051 #[m]
measuredWidth = 182
dx = d_glowplug / measuredWidth

bestWidth = 179 # output from glowplug.py
bestX = 185
bestY = 205

centerX = bestX + bestWidth/2

image = np.loadtxt('phi=0.9_frame0_crop_masked.csv', delimiter=",")
x, y, centered = center_image_x(image, centerX, bestY, dx)

r, f_abel, deriv, smoothed = perform_abel_discontinuous(x,centered)

for row in [100, 300]:

    plt.figure(figsize=(20, 6))
    plt.suptitle('phi=0.9_frame0_crop_masked.csv, row '+str(row))

    plt.subplot(141)
    plt.plot(1000*x, centered[row])
    plt.title('Signal F[y]')
    plt.xlabel('x [mm]')

    plt.subplot(142)
    plt.plot(1000*x, smoothed[row])
    plt.title('Smoothed')
    plt.xlabel('x [mm]')

    plt.subplot(143)
    plt.plot(1000*x, deriv[row])
    plt.ylim( [-10000, 10000])
    plt.title('Derviative')
    plt.xlabel('x [mm]')

    plt.subplot(144)
    plt.plot(1000*r, f_abel[row])
    plt.title('Signal f(r)')
    plt.xlabel('r [mm]')

    plt.savefig('result_row'+str(row)+'.png')

plt.show()

