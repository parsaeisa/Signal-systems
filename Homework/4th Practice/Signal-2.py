import matplotlib.pyplot as plt
import scipy as sc 
import scipy.signal
import numpy as np 

x1 = [1 , 2 , 1 , 0 ]
y1 = [0 , 1 , 1 , 0 ]
A = [0 , 0 , 2 , -1 ]
X = [-1 , 0 , 1 , 2 , 3 ]
x2 = sc.convolve(x1 , A)

plt.stem( x1 )
plt.show()

plt.stem( A )
plt.show()

plt.stem( x2 )
plt.show()

y2 = sc.convolve(A , y1)

plt.stem(y2)
plt.show()
