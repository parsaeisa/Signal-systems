import matplotlib.pyplot as plt
import math

x=[]
n=[]

plt.xlabel('n')
plt.ylabel('x[n]')

for i in range(0 , 11):
    n.append(i-5)
    m = (3*math.sin(math.pi*n[i])) + ( 3*math.fabs( math.cos( 7*n[i] ) ) )
    x.append( m )

plt.stem(n , x)
plt.show()

y=[]

plt.xlabel('n')
plt.ylabel('y[n]')

for i in range(0,11):
    if( x[i]>5 ):
        y.append(5)
    elif( x[i]<0 ):
        y.append(0)
    else:
        y.append(x[i])
plt.stem(n,y)    
plt.show();