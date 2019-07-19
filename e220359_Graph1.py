# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:26:00 2019

@author: Zohra
"""

# CAREFULLY READ THE COMMENTS MARKED WITH THE SIGN "#"
# AND FOLLOW THE INSTRUCTIONS WRITTEN THERE

# IMPORT NECESSARY MODULES
import numpy as np
import matplotlib.pyplot as plt


v1=[-1.314, -2.0, -1.5, -1.0, 0.0, 5.0, 10.0, 20.0, 30.0 ]
v2=[-1.301, -2.0, -1.5, -1.0, 0.0, 5.0, 10.0, 20.0, 30.0 ]
v3=[-1.357, -2.0, -1.5, -1.0, 0.0, 5.0, 10.0, 20.0, 30.0 ]


i1=[0, -3.5, -2.2, 19.4, 101.0, 587.0, 978.0, 1535.0, 1934.0]
i2=[0, -12.3, -8.7, 71.3, 375.0, 2150.0, 3630.0, 5760.0, 7190.0]
i3=[0, -27.2, -16.1, 383.0, 1702.0, 8620.0, 14810.0, 23400.0, 28800.0]

plt.plot(v1, i1, color='blue', marker='v', linestyle='solid', label='2mm aperture')
plt.plot(v2, i2, color='red', marker='D', linestyle='solid', label='4mm aperture')
plt.plot(v3, i3, color='green', marker='p', linestyle='solid', label='8mm aperture')

plt.title('Voltage vs Current for 3 aperture sizes')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (e-13 A)')
plt.legend(loc='upper left')
plt.grid(linestyle='-')
# PLOT THE DATASET, PUT LABELS, 2TLE, LEGEND AND GRID
# (1) use plt.plot command 3 times for all three optical apertures
# (2) inside plt.plot use x-axis as voltage data and y-axis as current data
# (3) inside plt.plot use different "color", "marker", "linestyle" and "label" for every optical aperture
# (4) use plt.title command to put a clear title on your graph
# (5) use plt.xlabel command to put x-axis label with correct units
# (6) use plt.ylabel command to put y-axis label with correct units
# (7) use plt.legend command to put a legend to the "best location" on your graph
# (8) use plt.grid command with a "linestyle" option to place a grid

plt.savefig('Graph1.jpg')   # save your plot with your favourite format: pdf, jpg, etc...
plt.show()                  # show your plot on the screen