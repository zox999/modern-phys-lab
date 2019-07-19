# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:33:03 2019

@author: Zohra
"""


import numpy as np

import matplotlib.pyplot as plt



B_field = np.sort(np.array([0.494,0.445,0.421,0.336,0.279])) 

sigma_delta = np.sort(np.array([0.23,0.19,0.15,0.15,0.115]))

fitted_data = np.polyfit(B_field, sigma_delta, 1)

plt.plot(B_field, np.polyval(fitted_data, B_field),label='Fitted data', marker='D')
plt.plot(B_field,sigma_delta, label='Experimental data', marker='o')

print(fitted_data[0])


print(fitted_data[1])



plt.title('Distance ratio vs. Magnetic field')

plt.xlabel('B field (T)')

plt.ylabel('sigma_a/delta_a')

plt.legend()

plt.grid()

plt.savefig('Graph3.jpg')