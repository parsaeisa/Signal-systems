import matplotlib.pyplot as plt
import numpy as np 
import scipy as sc
import scipy.io.wavfile as wav

# n is array like ##########################################################################

#Rectangular
def RactangularWindow(dw):
    M = (1.8 * np.pi / dw) 
    M = int(M)
    return (np.ones( M+1 ) , M )

# Triangle
def TriangleWindow (dw):
    M = (6.1 * np.pi / dw) 
    M = int(M)
    out = []
    for i in range(0,M/2):
        out.append(2*i / M)
    for i in range(M/2 , M+1):
        out.append( 2 - (2*i/M) )
    return (out , M)

# Hann 
def HannWindow (dw):
    M = (6.2 * np.pi / dw) 
    M = int(M)
    n = np.arange(M+1)
    return ( 0.5*( 1 - np.cos(2*np.pi * n / M) ) , M )

#Hamming 
def HaammingWindow(dw):
    M = (6.6 * np.pi / dw)    
    M = int(M)
    n = np.arange(M+1)
    return (0.54 - 0.46 * np.cos( 2 * np.pi * n / M ) , M)    

# Blackman
def BlackmanWinddow (dw):
    M = (11 * np.pi / dw) 
    M = int(M)
    n = np.arange(M+1)
    return (0.42 - 0.5 * np.cos(2 * np.pi * n / M) + 0.08 * np.cos(4 * np.pi * n / M) , M)        