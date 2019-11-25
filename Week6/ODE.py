# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:47:39 2019

@author: bguilfoyle
Overview: Solve ODEs using Euler, and Eurler-Cromer 
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
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
    plt.show()
#==============================================================================

#==============================================================================
def analyticalExerciseOne(x):
    """
    Overview: Analytical solution to exercise one
    """
    return (2 * np.exp(x)) - x - 1
#==============================================================================

#==============================================================================
def f1(x,y):
    """
    Overview: function with respect to x and y, represents dx/dy
    """
    return x + y
#==============================================================================

#==============================================================================
def getYi(x,y,h):
    return y + (h * f1(x,y))
#==============================================================================

#==============================================================================
def exerciseOne():
    """
    Overview: Solve the ODE dy/dx = x + y in the interval [0,1] with initial 
    condition y0 = 1 using the euler method.
    """
    xRange = list(np.linspace(0,1,100))
    anly = analyticalExerciseOne(xRange)
    
    y = []
    y.append(1)
    
    for i in range(0,len(xRange)-1):
        y.append(getYi(xRange[i],y[i],0.01))
    
    makePlot(xRange,y,"Euler")
    makePlot(xRange,anly,"Analytical")
#==============================================================================

#==============================================================================
def exerciseTwo():
    """
    Overview: Solve the ODE d^2y/dt^2 + ky/m = 0 using the Eurler method
    """

#==============================================================================

exerciseOne()
exerciseTwo()