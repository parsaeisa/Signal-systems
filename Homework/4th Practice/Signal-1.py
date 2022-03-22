import matplotlib.pyplot as plt
import scipy as sc 
import numpy as np 
import array as arr

h = [0,1,1,1,1,1,1,1,1,1,1,1,1,1]
a = [0,1,1,1,-1,-1,-1]
b = np.sin(np.linspace(0 , (11/6)*np.pi , 12))

plt.stem(a)
plt.xlabel('n')
plt.ylabel('a[n]')
plt.show()

y = np.convolve(a , h , mode="full")

plt.stem(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()
################################################
plt.stem(b)
plt.xlabel('n')
plt.ylabel('b[n]')
plt.show()

y = np.convolve(b , h , mode="full")

plt.stem(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()