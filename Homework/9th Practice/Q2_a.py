from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import math

# magnitude = b / ( 1 + 0.81 * np.exp(np.complex(0 , -2 * w) )+ 0.8 * np.exp(np.complex(0 , -1 * w) ) )
Magnitude = []
# for w in range(0 , 2* np.pi , 0.01):
    # Magnitude.append ( 5 / ( 1 + 0.81 * np.exp(np.complex(0 , -2 * w) )+ 0.8 * np.exp(np.complex(0 , -1 * w) ) ))

x = []
for i in range(0 ,200):
    x.append( math.pow( 0.25 , i ) + math.pow(0.2 , i) )

H = []
for i in range(0 , 200 ):
    a = 2 - 0.45 * np.exp(np.complex(0 , -2 * np.pi * (i/200) ) )
    b = 1 - 0.1 * np.exp(np.complex(0 , -2 * np.pi * (i/200) ) )
    c = 1 - 0.2 * np.exp(np.complex(0 , -2 * np.pi * (i/200) ) )
    d = 1 - 0.25 * np.exp(np.complex(0 , -2 * np.pi * (i/200) ) )

    H.append( (d*c) / (a*b) )

X = np.fft.fft(x)

Y = []

for i in range(0,200):
    Y.append ( H[i] * X[i] )

y = np.fft.ifft(Y)

for i in range(0 , 20):
    print y[i].imag
