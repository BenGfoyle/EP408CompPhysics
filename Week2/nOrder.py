# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:06:07 2019

@author: bguilfoyle - github.com/bengfoyle
Overview: Perform N order Differentials
"""
import numpy as np
import random as rn
import matplotlib.pyplot as plt

#Defines the amount by which Taylor looks ahead and behind
H = 0.0001

def makePlot(x,y1,y2,y3):
    plt.plot(x,y1,"g--",label = "sin(x)")
    plt.plot(x,y2,"r",label = "N Order 3 Point")
    plt.plot(x,y3,"b",label = "N Order 5 Point")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    #plt.xlim(xAxis[0],xAxis[len(xAxis) -1])
    plt.grid()
    plt.legend(loc = "best")
    plt.show()

def f(x):
    """
    Overview: Return result of some function f(x)
    """
    return np.sin(x)

def ThreePointDerivative(x):
    """
    Overview: Return the 3 point derivate of x using f(x)
    """
    return (f(x + H) - f(x - H)) / (2 * H)
 
def FivePointDerivative(x):
    """
    Overview: Return 5 point derivative of x using f(x)
    """
    return (1 / (12 * H)) * (f(x - (2 * H )) - (8 * f(x - H)) + (8 * f(x + H)) - f(x + (2 * H)))

def nOrderThree(ax,n):
    for i in range(0,n):
        ax = ThreePointDerivative(ax)
    return ax

def nOrderFive(ax,n):
    for i in range(0,n):
        ax = FivePointDerivative(ax)
    return ax
        
def main():
    x = np.linspace(- 2 * np.pi, 2 * np.pi, 10000)
    y = f(x)
    n = 4
    point3 = nOrderThree(x,n)
    point5 = nOrderFive(x,n)
    
    
    makePlot(x,y,point3,point5)
        
main()
    