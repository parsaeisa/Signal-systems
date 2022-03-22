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
    plt.show()
    
    plt.stem (xaxis , h)
    plt.show()
    
    convolutionSignal = []
    
    for n in xaxis :
        #print (convolution_elements(x , y1 , y2 , k))
        convolutionSignal.append(convolution_elements( x ,h , n))
        
    plt.stem(xaxis , convolutionSignal)
    plt.show()
    
    return convolutionSignal