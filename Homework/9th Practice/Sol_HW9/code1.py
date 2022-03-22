import numpy as np
import matplotlib.pyplot as plt

w = np.arange(-np.pi,np.pi,0.001)
b = 1/(np.absolute(1-0.8*np.exp(-1j*w)+0.81*np.exp(-1j*2*w))5)
b = b/max(b)
plt.plot(w,b)
plt.show()
