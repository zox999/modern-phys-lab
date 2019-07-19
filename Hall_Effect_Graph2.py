# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:21:42 2019

@author: Zohra
"""


import numpy as np
import matplotlib.pyplot as plt

x=[300,250,200,150,100,50,0.21]
y=[58.0,50.1,41.5,32.0,22.0,11.5,1.1]


#plt.errorbar(x, y, yerr=0.1, color='red', marker='|', label='error in potential', linestyle='none') 
a=np.polyfit(x,y,1,)
plt.plot(x, np.polyval(a,x), linestyle='dashed', label='fit, y=0.19x-2.21', marker='D')
print(a[0],a[1])
plt.plot(x,y, linestyle='none', marker='o', label='data')
plt.title('Hall Voltage vs Flux Density')
plt.xlabel('Flux density (mT)')
plt.ylabel('Hall voltage (mV)')
plt.legend(loc='upper left')
plt.grid(linestyle='-')

plt.savefig('x.jpg')   # save your plot with your favourite format: pdf, jpg, etc...
plt.show()   