from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

x = [1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4]
h = [1 , 0.5 , 0.25 , 0.125 , 0.0625 ]

y = np.convolve(x , h , mode = 'valid')

plt.stem(y)
plt.show()

