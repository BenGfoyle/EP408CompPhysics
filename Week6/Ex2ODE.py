# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:47:39 2019

@author: bguilfoyle
Overview: Exercise 2 Solve second OrderODEs using Euler
"""
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

#==============================================================================
def makePlot(x,y,name):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,label = name)
    plt.title("y(t) vs t Exercise 2")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
    plt.show()
#==============================================================================

#==============================================================================
def exerciseTwo():
    """
    Overview: Solve the ODE dy/dx = x + y in the interval [0,1] with initial 
    condition y0 = 1 using the euler method.
    """
    tRange = list(np.linspace(0,20,100))
    dt = tRange[1] - tRange[0]
    z = 1 
    yl = []
    zl = []
    y = 0
    yl.append(0)
    zl.append(1)
    for i in range(0,len(tRange) - 1):
        zold = z
        y += (zold  * dt)
        yl.append(y)
        z += (((-1) * y) * dt) #-1 as k/m defined as -1 in exercise
        zl.append(z)
    makePlot(tRange,zl,"Euler")
#==============================================================================
exerciseTwo()