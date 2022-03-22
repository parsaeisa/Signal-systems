from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc


def c( k , N , x ):
    a =0 
    for n in range(0,N):
        a = a + (x[n] * np.exp(np.complex(0 , k * 2 * (np.pi/N)* n )) ) 
    a = (1/N) * a
    return a

def f( n , k , N ):
    a = np.complex(np.cos(( k * 2 * (np.pi/N) * n)) , np.sin(( k * 2 * (np.pi/N) * n)) )
    return a

alterntion = [ 1, 1 , 1 , 1 , 1 , 1 , 0 , 0, 0 , 0 , 0 , 0 , 0, 0 , 0 , 1 , 1 , 1 , 1 , 1 ]
# alterntion = [1 , 0.5 , 0.5]
# alterntion = [3 , 1 , 2 , 1]
# alterntion = [1 , 0.5 , 0 , 0 , 0.5 ]

N = len(alterntion)

plt.stem( alterntion )
plt.title("Main Signal Q2")
plt.show()

M = 10000
a = np.zeros( 21 )
#  limited coefficients
for t in range(0,21 ):  
    r=t 
    for k in range(0 , N):        
        a[t] = a[t] + (f(r , k , N) * c(k , N , alterntion))    

plt.stem(a)
plt.title("Estimated Signal Q2");
plt.show()

# infinity M

xM = np.zeros(N)
for t in range(0,N ):  
    for k in range(1, M):        
        xM[t] = xM[t] + (f( t , k, N) * c(k , N , alterntion))
    for k in range(-M, 0):
        xM[t] = xM[t] + (f(t , k , N) * c(k , N , alterntion))

plt.stem(xM)
plt.title("Estimated with formula of question Q2")
plt.show()