from __future__ import division
import numpy as np
import scipy as sp
import Integration

def for_interation(x,n):
    """x is a initial guess number
       n is the number of iterations"""

    for i in range(1,n):
        print i,x
        xnew = sp.sqrt((5*x - 3)/2)
        if x == xnew:
            break
        x = xnew

def bisection(f,x1,x2):
    y1 = f(x1)
    y2 = f(x2)
    if y1*y2>0:
        print 'No roots exist within the given interval'
        exit
    for i in range(1,101):
        xh = (x1+x2)/2
        yh = f(xh)
        y1 = f(x1)
        if abs(y1) < 1E-6:
            break
        elif y1*yh < 0:
            x2 = xh
        else:
            x1 = xh
    print 'The root: %.5f'% x1
    print 'Number of bisections: %d'%i