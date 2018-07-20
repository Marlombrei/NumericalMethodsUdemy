from __future__ import division
import numpy as np
import scipy as sp
import Integration


def Newton_method(xp,x,y):
    """Interpolation using Newton's Method"""
    """
    def test():
    x = np.array([3,4,5,6,7,8])
    y = np.array([0,7,17,26,35,45])
    xp = np.arange(0,8.1,0.1,)
    yp = []
    for i in range(len(xp)):
        yy = Newton_method(xp[i], x, y)
        yp.append(yy)
    plt.plot(x,y,'o')
    plt.plot(xp,yp,'--')
    plt.show()
    """
    #1st step --> constructs y-differences table
    n = len(x) - 1
    Dy = np.zeros((n+1,n+1))
    Dy[:,0] = y # assigns values of y to first column of Dy
    for j in range(n): #from 1 to n
        for i in range(j+1,n+1): #from j+1 to n+1
            Dy[i,j+1] = (Dy[i,j] - Dy[j,j])/(x[i] - x[j])
    
    #2nd step --> calculate the polynomial for a given x-value
    yp = Dy[0,0]                  #the term of a0
    for i in range(n):            # loop form the term of a1 to an 
        xprod = 1                 # xprod initialized for current term
        for j in range(i+1):      # one is added since i starts from 0
            xprod *= xp - x[j]    # product of x differences
        yp += xprod * Dy[i+1,i+1] # summation of terms
    
    return yp

def Linear_regression(x,y):
    """Fitting with a straight line"""
    n = len(x)
    a = (np.mean(y)*np.sum(x**2) - np.mean(x)*np.sum(x*y)) / (np.sum(x**2) - n*np.mean(x)**2)
    b = (np.sum(x*y) - np.mean(x)*np.sum(y)) / (np.sum(x**2) - n*np.mean(x)**2)   
    return a,b
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    