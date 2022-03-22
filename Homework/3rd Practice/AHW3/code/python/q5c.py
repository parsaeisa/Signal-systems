#!/usr/bin/env python3
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def u(n):
	u = np.heaviside(n, 1)
	return u

n = np.linspace(0, 99, 100) 
x = u(n)
y1 = sc.convolve(np.ones(5), x)
y2 = sc.convolve([1, -1, -1, -1, 1], x)
y = sc.convolve(np.ones(3), y1 + y2)
h = np.array([2, 2, 2, 0, 2, 2, 2])
yp = sc.convolve(h, x)
fig, axs = plt.subplots(2, 1, constrained_layout = True)
axs[0].stem(y, use_line_collection = True)
axs[0].set_title('y[n] from question')
axs[1].stem(yp, use_line_collection = True)
axs[1].set_title('y[n] from solution a')
plt.show()