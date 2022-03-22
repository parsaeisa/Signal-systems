from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import math

def c (k):
    a=(( ( np.cos ((1/3)*(np.pi)*k)  - np.cos ((2/3)*(np.pi)*k) )  *(-1)) / np.pi )/k
    return a

def f (k , t):
    a =np.sin(k * (np.pi/3) * t)
    return a

M = 50
a = np.zeros(201 )
x = np.linspace(-10 , 10 , 201)

for t in range(0,201 ):  
    r = (t-100)/10  
    for k in range(1, M):        
        a[t] = a[t] + (f(k,r) * c(k))
    for k in range(-M, 0):
        a[t] = a[t] + (f(k,r) * c(k))

plt.plot(x , a)
plt.show()

