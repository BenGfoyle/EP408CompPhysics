# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:06:07 2019

@author: bguilfoyle - github.com/bengfoyle
Overview: Perform first and secodn order differenciation
"""
import numpy as np
import random as rn
import matplotlib.pyplot as plt

#Defines the amount by which Taylor looks ahead and behind
H = 1

def makePlot(x,y1,y2,y3,y4,y5):
    plt.plot(x,y1,"g--",label = "sin(x)")
    plt.plot(x,y2,"r",label = "First Order 3 Point")
    plt.plot(x,y3,"b",label = "First Order 5 Point")
    plt.plot(x,y4,"c",label = "Second Order 3 Point")
    plt.plot(x,y5,"k",label = "Second Order 5 Point")
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
    secondOrder3Point = ThreePointDerivative(point3)
    secondOrder5Point = FivePointDerivative(point5)
        
    makePlot(x,y,point3,point5,secondOrder3Point,secondOrder5Point)
        
main()
    