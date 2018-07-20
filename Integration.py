from __future__ import division
import numpy as np
import scipy as sp


def simpson_one_third(f, a, b, n):
    assert n % 2 == 0, 'Error: n must be an even number'
    assert b > a, 'Error: b must be greater than a'
    h = (b - a) / n
    sum_odd = 0
    for i in range(1, n, 2):  # note: range(1,n,2) is from 1 to n-1
        sum_odd += 4 * f(a + i * h)
    sum_even = 0
    for i in range(2, n, 2):  # note: range(2,n,2) is from 2 to n-2
        sum_even += 2 * f(a + i * h)
    return (1 / 3) * h * (f(a) + f(b) + sum_odd + sum_even)


def simpson_three_eights(f, a, b, n):
    assert n % 3 == 0, 'Error: n must be multiple of 3'
    assert b > a, 'Error: b must be greater than a'
    h = (b - a) / n
    sum_odd = 0
    for i in range(1, n + 1, 3):  # note: range(1,n,3) is from 1 to n-2
        sum_odd += 3 * (f(a + i * h) + f(a + h + i * h))
    sum_even = 0
    for i in range(3, n, 3):  # note: range(3,n,3) is from 3 to n-3
        sum_even += 2 * f(a + i * h)
    return (3 / 8) * h * (f(a) + f(b) + sum_odd + sum_even)


""" *** Newton Method is done at work, just need to send the file"""


def Newton_method(x, y):
    row_i = len(x)
    for j in range(len(y)):
        print (y[j])
        for i in range(row_i):
            print ('#', x[i])
        row_i -= 1


def Polynomial_fitting(x, y, n=2):
    """n is the degree of the polynomial and does not depend on the number of data-points in the way it is done in Interpolation"""
    assert n >= 1, 'Error: n must be greater or equal to 1'
    m = len(x)  # number of data-points
    A = np.zeros((n + 1, n + 1))  # matrix that will allocate all x-values
    B = np.zeros(n + 1)  # vector that will allocate all y-values           
    for row in range(n + 1):
        for col in range(n + 1):
            if row == 0 and col == 0:
                A[row, col] = m
                continue
            A[row, col] = np.sum(x ** (row + col))
        B[row] = np.sum(x ** row * y)
    a = np.linalg.solve(A, B)  # solution of the linear system [A]{a}={B} #vector to be solved and it will return all 'a' values
    print ('***The Polynomial***\n')
    print ('f(x) =\t %f \t' % a[0])
    for i in range(1, n + 1):
        print ('\t %+f x^%d' % (a[i], i))

