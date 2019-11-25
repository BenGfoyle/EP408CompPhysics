# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:47:39 2019

@author: bguilfoyle
Overview: Exercise 4 Solve second OrderODEs using Euler adn Euler Cromer
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#==============================================================================
def makePlot(x,y,name):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,label = name)
    plt.title("Theta(t) vs t Exercise 4")
    plt.xlabel("t")
    plt.ylabel("Thetea(t)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
    plt.show()
#==============================================================================

#==============================================================================
def f(x,y):
    """
    Overview: function with respect to x and y, represents dx/dy
    """
    return x + y
#==============================================================================


#==============================================================================
def exerciseFour():
    """
    Overview: Solving an ODE using scipy.integrate.odient
    """
    t = np.linspace(0,1,100)
    dydx = odeint(f,1,t)
    makePlot(t,dydx,"ODE Solution with Scipy")
#==============================================================================
exerciseFour()