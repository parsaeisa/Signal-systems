import matplotlib.pyplot as plt
import numpy as np
import math
import array as arr
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

x = arr.array('d',[])
h = arr.array('d',[])

for i in range (-50 , 51):
    #y1
    if  i >= -1 and i < 3 :
        x.append (-1)
    else:
        x.append(0)
    #y2
    if i >= 0 and i < 5 :
        h.append (-2)
    elif i >= 5 :
        h.append (-1)
    else:
        h.append(0)
        
y3 = convolution ( x ,h )