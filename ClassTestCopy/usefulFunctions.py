# -*- coding: utf-8 -*-
"""
Created on Fri 8 November 2019
 
@author: bguilfoyle
Overview: A selection of useful functions for EP408
"""
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

#==============================================================================
def f(x):
    eq = eval(input("Enter an equation dependant on x."))
    return eq
#==============================================================================
 
"""
PLOTTING
"""    

#==============================================================================
def makePlot(x,y):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.grid()
    plt.legend(loc = "best")
    plt.show()
#==============================================================================

"""
INTERGRATION
"""

#==============================================================================
def simpson(x0,xn,steps):
    """
    Overview: Perform integration using Simpsons method
    """
    if (steps % 2 == 0):
        x = np.linspace(x0,xn,steps)
        h = x[1] - x[0]
        prod = 4
        integral = (f(x0) + f(xn))
        for i in range(1,len(x)-1):
            integral += (prod * f(x[i]))
            if(i % 2 == 0):
                prod = 4
            else:
                prod = 2
        integral *= (h / 3)
        return integral
    else:
        print("x0 and xn must be even numbers for Simson rule, try again")
    
#==============================================================================
    
#==============================================================================
def trapezoid(x0,xn,steps):
    """
    Overview: Perform integration using trapezoidal method
    """
    x = np.linspace(x0,xn,steps)
    h = x[1] - x[0]
    integral = (f(x0) + f(xn)) / 2
    for i in range(1,len(x)-1):
        integral += f(x[i])
    integral *= h
    return integral
        
#==============================================================================
  
"""
INTERPOLATION
"""

#==============================================================================
def interLinear(x,x0,x1,f0,f1):
    return (f0 * ((x - x1) / (x0 - x1))) + ((x - x0) / (x1 - x0)) 
#==============================================================================

#==============================================================================
def interQuadratic(x,x0,x1,x2,f0,f1,f2):
    gx1 = (f0 * ((x - x1) * (x - x2))) / ((x0 - x1) * (x0 - x2))
    gx2 = (f1 * ((x - x0) * (x - x2))) / ((x1 - x0) * (x1 - x2))
    gx3 = (f2 * ((x - x0) * (x - x1))) / ((x2 - x0) * (x2 - x1))
    return gx1 + gx2 + gx3
#==============================================================================
    
"""
DIFFERENTIATION
"""    

H = 0.1
#==============================================================================
def ThreePointDerivative(x):
    """
    Overview: Return the 3 point derivate of x using f(x)
    """
    return (f(x + H) - f(x - H)) / (2 * H) 
#==============================================================================

#==============================================================================
def FivePointDerivative(x):
    """
    Overview: Return 5 point derivative of x using f(x)
    """
    return (1 / (12 * H)) * (f(x - (2 * H )) - (8 * f(x - H))\
            + (8 * f(x + H)) - f(x + (2 * H)))  
#==============================================================================
 