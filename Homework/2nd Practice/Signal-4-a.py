import matplotlib.pyplot as plt
import numpy
import math
# y = math.cos ( (math.pi/3)*n +(math.pi / 4) )
plt.xlabel ('n')
plt.ylabel ('x[n]')
n= []
x= []
for i in range (0 , 101):
    n.append (i - 50 )
    x.append( math.cos( (math.pi/3)*n[i] +(math.pi / 4) ) )

plt.stem ( n , x )
plt.show()
