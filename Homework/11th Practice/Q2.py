import matplotlib.pyplot as plt
import numpy as np 
import scipy as sc

M = 20
n = np.arange(0 , M+1)

Rectangular = np.ones(M+1)
balckman = 0.42 - 0.5 * np.cos(2 * np.pi * n/M) + 0.08 * np.cos(4 * np.pi* n/M)
B = np.fft.fft( Rectangular )

def f( window ):
    out = 20 * np.log10(window)
    return out

n = np.arange(0,2 * np.pi , 0.0002 * np.pi)
fig, axs = plt.subplots(2)
fig.suptitle('Rectangular (Top) & Blackman (Bottom)')
axs[0].plot( n , f(np.fft.fft(Rectangular , 10000)) )
axs[1].plot( n , f(np.fft.fft(balckman , 10000)) )

plt.show()