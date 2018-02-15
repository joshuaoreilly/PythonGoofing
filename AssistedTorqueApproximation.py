# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:00:54 2018

@author: oreil
"""

# Script designed to curve fit given a certain number of points 
# Using np.polyfit
# Data taken from: Seo et al. - Fully Autonomous Hip Exoskeleton Saved Metabolic Cost of Walking (2016)
# (on the drive under research - mechanical - biomechanical)
# Data taken from pg. 4, assist torque pattern, level ground

import numpy as np
import matplotlib.pyplot as plt
    
# Array containing x and y coordinates to use for fitting
xdata = np.array([0,18,23,30,40,50,66,82,90,100])
ydataPreScale = np.array([0.15,0.55,0.4,0.3,0.02,-0.05,-0.41,-0.05,0,0.17])
# 30Nm/0.55 = 54.54545454545454 (scaling factor for max 30Nm)
ydata = ydataPreScale*54.54545454545454

# 7th degree polynomial fitting
fitted = np.polyfit(xdata,ydata,5)
p = np.poly1d(fitted)


# Setting the step precision for graphing
xp = np.linspace(0,100,1000)


# In order to find average torque, subdivide x into so many values, calculate 
# average torque using absolute torque values for given x
sum = 0
x = 0
while (x<=100):
    y = abs(p(x))
    sum += y
    x += 0.001

# 100/0.01 per subsection = 10000 subsections
average = sum/100000
print(average)

# Plotting
# All given data points are points on graph
# Interpolated fit is straight line
# Higher degree polynomial is dotted line (usually wrong shape)
plot = plt.plot(xdata,ydata,'.',xp,p(xp),'-')
plt.xlim(0,100)
plt.ylim(-40,40)
plt.xlabel('% gait cycle')
plt.ylabel('Nm torque')
plt.title('Assisted torque over gait cycle (approximated)')
plt.show()