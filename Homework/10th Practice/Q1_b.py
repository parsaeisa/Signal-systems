from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.signal as sig

T = 1

I = 1 / (T * (1-np.exp(np.pi * -2 / T)))
II = np.exp(np.pi * -2 / T) / (T * (1-np.exp(np.pi * 2 / T)))

n = np.arange( -6 * np.pi , 6 * np.pi , 0.1)
X = []
for i in n :
    X.append( I + II )

plt.stem(X)
plt.show()
x = np.fft.ifft(X)

plt.stem(x)
plt.show()