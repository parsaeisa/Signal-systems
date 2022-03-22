import matplotlib.pyplot as plt
import numpy
import math

n=[]
x=[]

plt.xlabel('n')
plt.ylabel('x[n]')

for i in range(0 , 101):
    n.append(i-50)
    x.append( 2 * math.exp(0.1 * n[i]) * math.cos( (math.pi/3)*n[i] +(math.pi / 4) ))
    
plt.stem(n,x)
plt.show()