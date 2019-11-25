# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:47:39 2019

@author: bguilfoyle
Overview: Exercise 5 Solve second OrderODEs Euler Cromer
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
    plt.title("Theta(t) vs t Exercise 5")
    plt.xlabel("t")
    plt.ylabel("Thetea(t)")
    plt.legend(loc = "best")
    plt.grid()
    plt.show()
#==============================================================================

#==============================================================================
def exerciseThree():
    """
    Overview: Solve the ODE for a pendulumn using Euler, and Euler Cromer
    """
    tRange = list(np.linspace(0,20,1000))
    dt = tRange[1] - tRange[0]
    zAns = []
    zDampAns = []
    angle = []
    z = 1
    zDamp = 1
    G = 9.8
    L = 1
    dampFactor = -0.1
    theta = 0
    for i in range(0,1000):
        angle.append(theta)
        zAns.append(z)
        zDampAns.append(zDamp)
        z += ((-G/L) * np.sin(theta) * dt)
        zDamp += ((-G/L) * np.sin(theta) * dt) * np.exp(dampFactor * tRange[i])
        print(theta)
        theta += (z * dt) 
    makePlot(tRange,zAns,"Non-Damped Oscilator")
    makePlot(tRange,zDampAns,"Damped Oscilator")
#==============================================================================
exerciseThree()