from __future__ import division
import matplotlib.pyplot as plt
import scipy as sc
import numpy as np
from scipy import signal

x = np.zeros(40)
x[5] = 1
x[6] = 2
x[7] = 3
x[8] = 2
x[9] = 1

xaxis = np.arange(-5, 35)
y = sc.signal.lfilter([ 1, 0 , 0 , (3/4)] , [1 , 0 , (1/2)] , x )

plt.stem(xaxis , y)
plt.show()