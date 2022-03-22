import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-200,201)

hn = (1/(2*np.pi))*((1/(3*1j*n))*(np.exp(1j*np.pi*n) - np.exp(-1j*np.pi*n))
                    - (1/(3*1j*n))*(np.exp(1j*7*(np.pi/8)*n) - np.exp(-1j*7*(np.pi/8)*n))
                    + (2/(3*1j*n))*(np.exp(1j*5*(np.pi/8)*n) - np.exp(-1j*5*(np.pi/8)*n))
                    - (2/(3*1j*n))*(np.exp(1j*3*(np.pi/8)*n) - np.exp(-1j*3*(np.pi/8)*n))
                    + (1/(1j*n))*(np.exp(1j*(np.pi/8)*n) - np.exp(-1j*(np.pi/8)*n)))

hn[n==0] = np.inf #It can't be plotted, but we know that its dirac function
hn = np.real(hn)
plt.stem(n,hn)
plt.show()
