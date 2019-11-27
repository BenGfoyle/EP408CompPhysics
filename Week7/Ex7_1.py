"""
Author: Ben Guilfoyle - bengfoyle.github.io
Overview: Solve an example ODE using RK2 and RK4
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
def makePlot(x,y,name):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,label = name)
    plt.title("f(x) vs x Exercise 1")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
#==============================================================================

#==============================================================================
def analyticalExerciseOne(x):
    """
    Overview: Analytical solution to exercise one
    """
    return (2 * np.exp(x)) - x - 1
#==============================================================================

#==============================================================================
def f(x,y):
    """
    Overview: Return the result of the function x + y
    """
    return x + y
#==============================================================================

#==============================================================================
def exerciseOne():
    start = 0
    end = 1
    steps = 1000
    xRange = np.linspace(start,end,steps)
    h = xRange[1] - xRange[0]
    yRange = []
    anliY = []
    y = 1

    for x in xRange:
        if x == 0:
            yRange.append(1)
        else:
            k1 = h * f(x,y)
            k2 = h * f(x + (h / 2), y + (k1/2))
            y += k2
            yRange.append(y)
        anliY.append(analyticalExerciseOne(x))
    print(xRange,yRange,anliY)
    makePlot(xRange,yRange,"RK2")
    makePlot(xRange,anliY,"Analytical")
    plt.show()
#==============================================================================
exerciseOne()
