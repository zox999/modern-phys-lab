# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:53:35 2019

@author: Zohra
"""
import numpy as np
import matplotlib.pyplot as plt

x=[-30,-20,-10,0,10,20,30]
y=[-62.5,-41.8,-22.0,-0.3,20.6,38.9,58.2]


#plt.errorbar(x, y, yerr=0.1, color='red', marker='|', label='error in potential', linestyle='none') 
a=np.polyfit(x,y,1,)
plt.plot(x, np.polyval(a,x), linestyle='dashed', label='fit, y=2.02x-1.27', marker='D')
print(a[0],a[1])
plt.plot(x,y, linestyle='none', marker='o', label='data')
plt.title('Hall Voltage vs Sample Current')
plt.xlabel('Sample current (mA)')
plt.ylabel('Hall voltage (mV)')
plt.legend(loc='upper left')
plt.grid(linestyle='-')

plt.savefig('Graph1.jpg')   # save your plot with your favourite format: pdf, jpg, etc...
plt.show()   