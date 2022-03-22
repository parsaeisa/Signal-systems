import matplotlib.pyplot as plt
import math
n=[]
x=[]

plt.xlabel('n')
plt.ylabel('x')

for i in range (0,101):
        n.append(i-50)
        x.append(2 * math.exp(0.1 * n[i]))
        
plt.stem(n, x)
plt.show()