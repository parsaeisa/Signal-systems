from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

def c (k , x = [] ):
    N = len(x)
    a = 0
    for n in range (0 , N):
        a = a +( x[n] * np.exp(np.complex(0 , k * 2 * (np.pi/N)* n )) )#np.complex( np.cos(k * 2 * (np.pi/N)* n) , -1 * np.sin(k * 2 * (np.pi/N) * n) ))
    a = a/N
    return a

ii = [ 1 , 0.5 , 0 , 0 , 0.5 ]
iii = [1 , 0.5 , 0.5]
iv = [ 3 , 2 , 1 , 2 ]

M = 10
Coefficients_ii = []
Coefficients_iii = []
Coefficients_iv = []
# ii
for k in range(0 , len(ii)):
    Coefficients_ii.append( c (k  , ii) )
# iii
for k in range(0 , len(iii)):
    Coefficients_iii.append( c (k  , iii) )
# iv
for k in range(0 , len(iv)):
    Coefficients_iv.append( c (k  , iv))
