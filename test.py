from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import Integration
import Roots_High_Degree_Equations as roots
from Interpolation_CurveFitting import Newton_method
from Differentiation import derivatives_central, second_fwd_derivative
from scipy.misc import derivative

def test():
    f = lambda x: np.exp(-x)
    h = 0.1
    x = np.array([0.,0.1,0.2,0.3,0.4])
    #x = 0.0
    y = np.array([0.,0.0819,0.1341,0.1646,0.1797])
#     dev1, dev2 = second_fwd_derivative(f, x, h)
#     print 'dev1:%f'%dev1
#     print 'dev2:%f'%dev2
    scipy_dev1 = derivative(f,x,h)
    scipy_dev2 = derivative(f,x,h,2)
    print 'scipy_dev1:%f'%scipy_dev1
    print 'scipy_dev2:%f'%scipy_dev2


test()























































































