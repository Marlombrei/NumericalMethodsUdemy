from __future__ import division
import numpy as np
import scipy as sp

dy = lambda x, y: x * y
x = 0  # initial value of x
xn = 2  # final value of x
y = 1  # value of y(x0)
h = 0.5  # step size
n = int((xn - x) / h)  # total number of steps
print ('x \t\t y (Euler)')
print ('%f \t %f' % (x, y))
for i in range(n):
    y += dy(x, y) * h
    x += h
    print ('%f \t %f' % (x, y))
