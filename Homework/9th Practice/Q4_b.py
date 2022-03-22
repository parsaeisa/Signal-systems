from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

x = [1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4]

X = np.fft.fft(x)

y = np.fft.ifft( X * 5 * np.exp(np.complex(0,np.pi /4)) )

plt.stem(y)
plt.show()