# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:06:42 2019

@author: bguilfoyle - github.com/bengfoyle
Overview: Exercise 3.1 - estimate f(x) on any point using interpolation
on given arrays.
"""
import numpy as np
import matplotlib.pyplot as plt

def makePlot(x,y):
    plt.plot(x,y)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.grid()
    plt.legend(loc = "best")
    plt.show()

def interLinear(x,x0,x1,f0,f1):
    return (f0 * ((x - x1) / (x0 - x1))) + ( f1 * (x - x0) / (x1 - x0)) 

def interQuadratic(x,x0,x1,x2,f0,f1,f2):
    gx1 = (f0 * ((x - x1) * (x - x2))) / ((x0 - x1) * (x0 - x2))
    gx2 = (f1 * ((x - x0) * (x - x2))) / ((x1 - x0) * (x1 - x2))
    gx3 = (f2 * ((x - x0) * (x - x1))) / ((x2 - x0) * (x2 - x1))
    return gx1 + gx2 + gx3

def main():
    xVals = np.linspace(0,0.8,100)
    x = [0,0.2,0.4,0.6,0.8]
    fx = [0.5,2,4,6,4]
    iLin = []
    iQuad = []
    for i in range(0,len(xVals)):
        iLin.append(interLinear(xVals[i],x[0],x[1],fx[0],fx[1]))
        iQuad.append(interQuadratic(xVals[i],x[0],x[1],x[2],fx[0],fx[1],fx[2]))
    makePlot(x,fx)
    makePlot(xVals,iLin)
    makePlot(xVals,iQuad)
main()