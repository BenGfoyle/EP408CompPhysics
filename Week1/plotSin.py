# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:46:58 2019

@author: bguilfoyle github.com/bengfoyle
Overview: Exercise 1.5 - 1.8 Plot f(x) = sin(x) for 0 <= x <= 2 Pi
"""

import numpy as np
import matplotlib.pyplot as plt

def makePlot(xAxis,yAxis):
    plt.plot(xAxis,yAxis,"g--",label = "sin(x)")
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(xAxis[0],xAxis[len(xAxis) -1])
    plt.ylim(min(yAxis),max(yAxis))
    plt.grid()
    plt.legend(loc = "best")
    plt.show()
    
x = np.linspace(0,2 * np.pi, 100) #linspace generates values between 2 values
y = np.sin(x) #perform sin operaton on all elements of x
makePlot(x,y)