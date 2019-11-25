# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:33:42 2019

@author: bguilfoyle
Overview: Exercise One Interpolation
"""
import numpy as np #used for access to linspce and sin
import matplotlib.pyplot as plt #used for plotting grpahs

#==============================================================================
def makePlot(x,y):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(x[0],x[len(x)-1])
    plt.grid()
    plt.show()
#==============================================================================

#==============================================================================    
def interpolation(x,j,vals,fx):
    """
    Overview: Performs global interpolation to the jth degree using Lagrange
    """
    p = []
    pj = []
    for a in range(0,j):
        for b in range(0,len(vals)):
            if vals[a] != vals[b]: #used to prevent division by zero
                pj.append((x - vals[b]) / (vals[a] - vals[b]))
        p.append(pj)
        pj = [] #reset pj to an empty list for next iteration
        
    for i in range(0,len(p)):
        p[i] = fx[i] * (np.prod(p[i])) #take product of subsequent values
        
    return np.sum(p)
#==============================================================================

#==============================================================================
def main():
    x = [-4.0,-3.0,-2.0,0.0,2.0,3.0,4.0]
    fx = [1.5,1.5,0.0,-0.5,2.0,2.0,3.0]
    xVals = np.linspace(-4,4,100)
    gx = [] #used to hold predicted values
    j = len(fx)
    
    for i in range(0,len(xVals)):
        gx.append(interpolation(xVals[i],j,x,fx))  
    
    makePlot(xVals,gx)
        
    #redefining xVals with rounding to allow the corresponding y values to be
    #found from the requested x values
    xVals = list(xVals)
    for i in range(0,len(xVals)):
        xVals[i] = round(xVals[i],1)
    reqX = [-2.5,1,3.5]
    #get values at gx[i] such that xVals[i] == reqX[i]
    reqY = [gx[xVals.index(i)] for i in reqX]
    
    plt.scatter(x,fx, color = 'r')
    plt.scatter(reqX,reqY, color = 'g')
    labels = ["Global Interpolation", "Known Values","Requested Values"]
    plt.legend(labels, loc= 'best')
    
#==============================================================================

main()