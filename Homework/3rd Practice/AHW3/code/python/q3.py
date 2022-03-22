#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def u(n):
	u = np.heaviside(n, 1)
	return u

def conv(x, h):
	rngy = int((x.shape[0] - 1) / 2)
	ny = np.linspace(-rngy, rngy, 2 * rngy + 1)
	y = np.zeros(ny.shape[0])
	fh = np.flip(h)
	for i in ny:
		y[int(i + rngy)] = np.dot(x, fh[int(i + rngy) : int(i + rngy + x.shape[0])])
	y = np.flip(y)
	fig, axs = plt.subplots(3, 1, constrained_layout = True)
	axs[0].stem(ny, x, use_line_collection = True)
	axs[0].set_title('x[n]')
	axs[1].stem(ny, h[rngy : 3 * rngy + 1], use_line_collection = True)
	axs[1].set_title('h[n]')
	axs[2].stem(ny, y, use_line_collection = True)
	axs[2].set_title('y[n] = x[n] * h[n]')
	plt.show()

rngx = 50
rngh = 100
n = np.linspace(-rngx, rngx, 2 * rngx + 1)
nh = np.linspace(-rngh, rngh, 2 * rngh + 1)
# a
x = u(n)
a = 0.5
h = a ** nh * u(nh)
conv(x, h)
# b
x = u(n) - u(n - 3)
h = u(nh) - u(nh - 2)
conv(x, h)
# c
x = u(n - 5) - 2 * u(n)
h = u(nh - 3) - u(nh + 1)
conv(x, h)
# d
x = u(n - 3) - 2 * u(n + 2)
h = u(nh - 3) - u(nh + 1)
conv(x, h)