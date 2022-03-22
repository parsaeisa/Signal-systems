from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import numpy.fft as fft
# a
n = np.linspace(-5000 , 5000 , 10001)
x = np.zeros(10001)
i =0 
for N in n :
    i = i+ 1
    if ( N >= 0 and N<=5 ):
        x[i] = N
    elif (N>5 and N <= 10):
        x[i] = 10 - N

y = fft.fft ( x )

y_angle = np.angle(y)
y_magnitude = np.abs(y)

plt.stem(n , y_angle)
plt.title("Angle")
plt.show()

plt.stem(n , y_magnitude)
plt.title("Magnitude")
plt.show()
# b
x = [ 0 , 1 , 2 , 3 , 4 , 5 , 4 , 3 , 2 , 1 , 0 ]
N = len(x)
Coefficient = fft.fft(x)/N