from __future__ import division
import numpy as np
import scipy as sp

def derivatives_central(f,x,h):
    deriv_1 = (f(x+h) - f(x-h)) / (2*h)
    deriv_2 = (f(x+h) - 2*f(x) + f(x-h)) / h**2
    return deriv_1, deriv_2

def second_fwd_derivative(f,x,h):
    deriv_1 = (-f(x+2*h) + 4*f(x+h) - 3*f(x)) / (2*h)
    deriv_2 = (-f(x+3*h) + 4*f(x+2*h) - 5*f(x+h) + 2*f(x)) / h**2
    return deriv_1, deriv_2

def dxdf(x,y,h=0.01):
    df1 = []
    for i in range(0,len(x)-1):
        d = (y[i+1]-y[i]) /(x[i+1]-x[i])
        df1.append(d)
    return df1

def dxdf2(x,df1,h=0.01):
    df2 = []
    for i in range(0,len(x)-1):
        d = (df1[i+1]-df1[i]) /(x[i+1]-x[i])
        df2.append(d)
    return df2

def Richardson_Extrapolation(x,y,h=0.01):
    df1 = []
    for i in range(0,len(x)-2):
        #print i
        d = (-3*y[i] + 4*y[i+1] - y[i+2]) / 2.0
        df1.append(d)
    return df1










































































