# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:43:23 2018

@author: oreil
"""

#script designed to curve fit given a certain number of points 
#using scipy.optimize.curve_fit

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#order 5 polynomial for curve fitting
def fit_fun(x,a,b,c,d,e,f):
    return (a*(x^5))+(b+(x^4))+(c*(x^3))+(d*(x^2))+(e*(x))+f

#array containing x and y coordinates to use for fitting
x = []
y = []

coord = curve_fit(fit_fun,x,y)

print(coord)

