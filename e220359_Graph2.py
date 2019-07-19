# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:40:02 2019

@author: Zohra
"""

v4=[-1.923, -2.0, -1.5, -1.0, 0.0, 5.0, 10.0, 20.0, 30.0 ]
v5=[-1.462, -2.0, -1.5, -1.0, 0.0, 5.0, 10.0, 20.0, 30.0 ]
v6=[-0.785, -2.0, -1.5, -1.0, 0.0, 5.0, 10.0, 20.0, 30.0 ]

i4=[0, -12.5, 161.0, 512.0, 1256.0, 6500.0, 11320.0, 18430.0, 23100.0]
i5=[0, -9.0, -2.1, 70.6, 280.0, 1505.0, 2590.0, 4170.0, 5220.0]
i6=[0, -6.9, -6.7, -6.0, 250.0, 1410.0, 2220.0, 3200.0, 3670.0]


# IMPORT NECESSARY MODULES
import numpy as np
import matplotlib.pyplot as plt

# DEFINE YOUR DATASET
# (1) create the "frequency" array
# (2) create the "stopping potential" array
x=[5.490, 6.879, 7.408, 8.214]
y=[0.785, 1.324, 1.462, 1.923]


plt.errorbar(x, y, yerr=0.1, color='red', marker='|', label='error in potential', linestyle='none') 
a=np.polyfit(x,y,1,)
plt.plot(x, np.polyval(a,x), linestyle='dashed', label='fit')
print(a[0],a[1])

plt.title('Frequency vs Stopping Potential')
plt.xlabel('Frequency (e+14 Hz)')
plt.ylabel('Voltage (V)')
plt.legend(loc='upper left')
plt.grid(linestyle='-')

plt.savefig('Graph3.jpg')   # save your plot with your favourite format: pdf, jpg, etc...
plt.show()                  # show your plot on the screen


# PLOT THE DATASET WITH ERRORBAR (ERROR IN V IS 0.1)
# (1) use plt.errorbar command with frequency on the x-axis and stopping potential on the y-axis
# (2) inside plt.errorbar use yerr=0.1 which places a 0.1 errorbar on y values
# (3) inside plt.errorbar use "color", "marker" and "label" commands
# (4) inside plt.errorbar use linestyle='none'
# (5) execute your program to see the graph, check whether everyhing is OK or not

# FIT YOUR DATA AND PLOT THE FITTED DATA (or BEST LINE)
# (1) use np.polyfit to fit your data in the first order and give it a name
# (2) use plt.plot with frequecy on the x-axis and fitted data on the y-axis
# (3) inside plt.plot use np.polyval(fitted data, frequeny) as your y-axis data. Why?
# (4) use "color", "linestyle" and "label". Do not use "marker" option.

# PRINT THE SLOPE AND THE X-INTERCEPT OF THE BEST LINE
# (1) print the 0th and 1st values of the fitted data
# These will correspond to Planck's constant and work function respectively 
