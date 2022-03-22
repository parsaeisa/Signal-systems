import matplotlib.pyplot as plt
import numpy as np
import math

def convolution_elements ( x , h , n) :#calculating y[n]
    ans = 0  
    for k in range(-50 , 51) :
        ans += x[k] * h[n-k]
    return ans

def convolution ( x , h ):# calculate and display y signal
    xaxis = []
    for i in range (-50 , 51):
        xaxis.append(i)

    plt.stem (xaxis , x)
    plt.xlabel('n')
    plt.ylabel('x[n] = u[n]')
    plt.show()
    
    plt.stem (xaxis , h)
    plt.xlabel('n')
    plt.ylabel('h[n] = = (-0.5)^n * u[n]')
    plt.show()
    
    convolutionSignal = []
    
    for n in xaxis :
        #print (convolution_elements(x , y1 , y2 , k))
        convolutionSignal.append(convolution_elements( x ,h , n))
        
    plt.stem(xaxis , convolutionSignal)
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.show()
    
    return convolutionSignal
    
x = []
h = []

for i in range (-50 , 51):
    #y1
    if  i >= 0  :
        x.append (1)
    else:
        x.append(0)
    #y2
    if i >= 0  :
        h.append ( math.pow(0.5 , i))
    else :
        h.append (0)

y3 = convolution ( x , h )        

