# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:43:23 2018

@author: oreil
"""

#script designed to curve fit given a certain number of points 
#using np.polyfit
#data taken from: https://www.iasj.net/iasj?func=fulltext&aId=90945
#page 12/219, Figure top right (hip angle for regular subject)

import numpy as np
import matplotlib.pyplot as plt
    
#array containing x and y coordinates to use for fitting
xdata = np.array([0,10,20,30,50,70,85,90,100])
ydata = np.array([20,20,19,10,5,15,25,24,20])

#7th degree polynomial fitting
fitted = np.polyfit(xdata,ydata,7)
p = np.poly1d(fitted)


#setting the step precision for graphing
xp = np.linspace(0,100,1000)

#plotting
#all given data points are points on graph
#interpolated fit is straight line
#higher degree polynomial is dotted line (usually wrong shape)
plot = plt.plot(xdata,ydata,'.',xp,p(xp),'-')
plt.xlim(0,100)
plt.ylim(0,35)
plt.show()