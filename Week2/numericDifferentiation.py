# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:06:07 2019

@author: bguilfoyle - github.com/bengfoyle
Overview: Perform numeric differenciation using Taylor expansion
"""
import numpy as np
import random as rn
import matplotlib.pyplot as plt

#Defines the amount by which Taylor looks ahead and behind
H = 1

def makePlot(xAxis,yAxis,secondary,tertiary,nYAxis,nSecondary,nTertiary):
    plt.plot(xAxis,yAxis,"g--",label = "sin(x)")
    plt.plot(xAxis,secondary,"r",label = "3 Point")
    plt.plot(xAxis,tertiary,"b",label = "5 Point")
    plt.plot(xAxis,nYAxis,"y--",label = "Noisy sin(x)")
    plt.plot(xAxis,nSecondary,"p",label = "Noisy 3 Point")
    plt.plot(xAxis,nTertiary,"o",label = "Noisy 5 Point")
    plt.title("f(x), 3 Point, and 5 Point Derivative")
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

def addNoise(x):
    return x + rn.uniform(-1,1)

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

    
def main():
    x = np.linspace(- 2 * np.pi, 2 * np.pi, 50)
    y = f(x)
    point3 = ThreePointDerivative(x)
    point5 = FivePointDerivative(x)

    randY = []
    randPoint3 = []
    randPoint5 = []
    for i in range(0,len(x)):
        randY.append(addNoise(y[i]))
        randPoint3.append(ThreePointDerivative(randY[i]))
        randPoint5.append(FivePointDerivative(randY[i]))
        
    makePlot(x,y,point3,point5,randY,randPoint3,randPoint5)
        
main()
    