# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:09:36 2019

@author: bguilfoyle
Overview: Exercise One Differenciation
"""
import numpy as np #used for access to linspce and sin
import matplotlib.pyplot as plt #used for plotting grpahs

#==============================================================================
def f(x):
    return np.sin(x) / x
#==============================================================================

#==============================================================================
def makePlot(x,y):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    #x is sorted in ascending order, can use 1st and last elements as limits
    plt.xlim(x[0],x[len(x) - 1]) 
    plt.ylim(-0.5,1.0)
    plt.show()
#==============================================================================

#==============================================================================
def threePointDerivative(x,H):
    """
    Overview: Return the 3 point derivate of x using f(x)
    """
    return (f(x + H) - f(x - H)) / (2 * H) 
#==============================================================================
    
#==============================================================================
def secondOrder(x,H):
    """
    Overview: Calculate second order derivative using known formual
    """
    return (f(x + H) - (2 * f(x)) + f(x - H)) / H**2
#==============================================================================


#==============================================================================
def main():
    H = 0.1 #Step soze used in differenciation
    x = np.linspace(-20, 20, 1000) #list of 1000 x values from -20, 20 
    y = f(x) #calcualte y using formual in f(x)
    labels = ["f(x)","d(f)/dx","d^2(f)/dx^2"]
    dx = threePointDerivative(x,H)
    dx2 = secondOrder(x,H)
    makePlot(x,y)
    makePlot(x,dx)
    makePlot(x,dx2)
    plt.grid()
    plt.legend(labels,loc = "best")
    plt.show()
#==============================================================================

main()