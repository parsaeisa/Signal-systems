from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

x = [1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4]
h = [2.-1,1,3,6,3,1,-1,2]

y = np.convolve(x , h , mode = 'valid')

plt.stem(y)
plt.show()

