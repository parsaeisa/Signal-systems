import numpy as np
import matplotlib.pyplot as plt


n = np.arange(0,61)
c = np.zeros(8,dtype='complex')
### A
"""
c[0] = 32
c[1] = 6.54*np.exp(-1j*np.pi/4)
c[2] = 0
c[3] = 0.54*np.exp(1j*np.pi/4)
c[4] = 0
c[5] = 0.54*np.exp(-1j*np.pi/4)
c[6] = 0
c[7] = 6.54*np.exp(1j*np.pi/4)
"""
### B

c[0] = 10*np.exp(1j*np.pi/4)
c[1] = 4.27*np.exp(1j*np.pi)
c[2] = 0
c[3] = 0.73*np.exp(1j*np.pi/2)
c[4] = 0
c[5] = 0.73
c[6] = 0
c[7] = 4.27*np.exp(-1j*np.pi/2)


### C
"""
c[0] = 1.4375
c[1] = 0.51*np.exp(1j*0.65*np.pi)
c[2] = 0
c[3] = 0.21*np.exp(1j*0.15*np.pi)
c[4] = 0
c[5] = 0.21*np.exp(-1j*0.15*np.pi)
c[6] = 0
c[7] = 0.51*np.exp(-1j*0.65*np.pi)
"""
yssn = np.zeros(n.shape[0],dtype = 'complex')
for k in range(8):
    yssn += c[k]*np.exp(1j*(2*np.pi/8)*k*n)

#print(yssn) #to make sure thay're all real

# for part B comment the code below ==> it is not real!
"""
yssn = np.real(yssn)
plt.stem(n,yssn)
plt.show()
"""
#for part B uncomment the code below
absYssn = np.abs(yssn)
angYssn = np.angle(yssn)
# Qusetion: Why the angle is not constant when you plot it???

plt.stem(n,absYssn)
plt.figure()
plt.stem(n,angYssn)
plt.show()
