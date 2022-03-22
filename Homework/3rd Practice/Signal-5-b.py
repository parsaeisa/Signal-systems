import matplotlib.pyplot as plt
import scipy as sc 
import numpy as np 
import array as arr

x = np.cos(np.linspace(0,4.*np.pi,100))

y1 = sc.convolve(np.ones(5), x)
y2 = sc.convolve([1, -1, -1, -1, 1], x) 
firsty = sc.convolve(np.ones(3), y1+y2)
plt.stem (firsty)
plt.show()

H = sc.convolve(np.ones(3) ,[2 , 0 , 0 , 0 , 2] )
secondy = sc.convolve(H , x)

plt.stem(secondy)
plt.show()