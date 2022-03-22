import matplotlib.pyplot as plt
import scipy as sc
import numpy as np
from scipy import signal

xaxis = np.arange(-5,20)
step = np.zeros(25)
for i in range(5,25):
    step[i] = 1 ;

# step response

y = sc.signal.lfilter([1 , 0.8 , 0.64] , [1] , step )

plt.stem(xaxis , y)
plt.ylabel("step response")
plt.show()

# impulse response

impulse = np.zeros(25)
impulse[5] = 1

y1 = sc.signal.lfilter([1 , 0.8 , 0.64] , [1] , impulse)

plt.stem(xaxis , y1)
plt.ylabel("impulse response")
plt.show()