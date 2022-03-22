from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

n = np.arange(-200 , 201)
H = []
w = np.linspace(-1 * np.pi , np.pi , 401 )

for W in w:
    if( np.abs(W) < np.pi / 8):
        H.append(1)
    elif( np.abs(W) > np.pi * 0.125 and np.abs(W) < np.pi * 0.625 ):
        H.append(2/3)
    elif( np.abs(W) > np.pi * 0.875 and np.abs(W) < np.pi ):
        H.append(1/3)
    else:
        H.append(0)

h = np.fft.ifft(H)

plt.plot(h)
plt.show()