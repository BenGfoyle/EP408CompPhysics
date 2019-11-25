# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:08:46 2019

@author: bguilfoyle
Overview: Perform integration using the trapezoid and Simpson's rule
"""
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

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

#==============================================================================
def f(x):
    """
    Overview: function to be integrated
    """
    return np.sin(x)
#==============================================================================

#==============================================================================
def analytical(x):
    """
    Overview: Return analytical solution to f(x)
    """
    return np.cos(x)
#==============================================================================
    
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
    
#==============================================================================
def main():
    trap = trapezoid(0, np.pi,100)
    print(trap)
    simp = simpson(0, np.pi,100)
    print(simp)
#==============================================================================
    
main()