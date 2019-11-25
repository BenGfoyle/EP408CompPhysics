# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:06:42 2019

@author: bguilfoyle - github.com/bengfoyle
Overview: Ex 3.3 Estimate f(x) on any point using global interpolation and 
local linear interpolation
"""
import numpy as np
import matplotlib.pyplot as plt

def makePlot(x,y,name):
    """
    Overview: Construct a plot based on a x and y axis list of points
    """
    plt.plot(x,y,label = name)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.legend(loc = "best")
    plt.show()
    
def interpolation(x,j,vals,fx):
    """
    Overview: Performs global interpolation to the jth degree
    """
    p = [] #* j
    pj = [] #* len(vals)
    for a in range(0,j):
        for b in range(0,len(vals)):
            if vals[a] != vals[b]:
                pj.append((x - vals[b]) / (vals[a] - vals[b]))
        p.append(pj)
        pj = []
        
    for i in range(0,len(p)):
        p[i] = fx[i] * (np.prod(p[i]))
        
    return np.sum(p)

def interLinear(x,x0,x1,f0,f1):
    """
    Overview: Retrun the linear interpolation for a given x
    """
    return (f0 * ((x - x1) / (x0 - x1))) + (f1 * ((x - x0) / (x1 - x0))) 

def main():
    x = [0,0.2,0.4,0.6,0.8]
    fx = [0.5,2,4,6,4]
    xVals = np.linspace(0,0.8,100)
    xValsLinear = np.linspace(0,0.8,len(x) - 1)
    gx = []
    j = len(fx)
    hx = []
    
    for i in range(0,len(xVals)):
        gx.append(interpolation(xVals[i],j,x,fx))
        
    for i in range(0,len(xValsLinear)):
        hx.append(interpolation(xValsLinear[i],j,x,fx))
        
    
    makePlot(x,fx,"f(x)")
    makePlot(xVals,gx,"Global N Order Interpolation")
    makePlot(xValsLinear,hx, "Local Linear Interpolation")

main()