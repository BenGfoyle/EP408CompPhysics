"""
Author: Ben Guilfoyle - bengfoyle.github.io - github.com/bengfoyle
Overview: A program to simulate a 2D random walk starting at the origin
"""
import numpy as np #sqrt function
import matplotlib.pyplot as plt #make plots
import random


#===============================================================================
def makePlot(x,y,name):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,label = name)
    plt.title("Random Walk")
    plt.xlabel("Steps")
    plt.ylabel("Distance")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
    plt.show()
#===============================================================================

#===============================================================================
STEPS = 10000
numSteps = np.linspace(0,STEPS,STEPS)
xVals,yVals = [],[]
x,y = 0,0
for i in numSteps:
    xVals.append(x)
    yVals.append(y)
    x += random.uniform(-np.sqrt(2),np.sqrt(2))
    y += random.uniform(-np.sqrt(2),np.sqrt(2))

#plt.scatter(xVals,yVals)
distance = [np.sqrt((x**2 + y**2)) for x, y in zip(xVals, yVals)]
makePlot(numSteps,distance,"Exercise 1 Random walk")
#===============================================================================
