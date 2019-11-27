"""
Author: Ben Guilfoyle - bengfoyle.github.io
Overview: Solve an example ODE using RK2 and RK4
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
grav = 9.81
k = 2

#==============================================================================
def makePlot(x,y,name):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,label = name)
    plt.title("Exercise 2")
    plt.xlabel("")
    plt.ylabel("")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
#==============================================================================

#==============================================================================
def f(t,y,z):
    return grav - (k * y / m)
#==============================================================================

#==============================================================================
def g(t,y,z):
    return z
#==============================================================================

#==============================================================================
def exerciseTwo():
    start = 0
    end = 10
    steps = 1000
    tRange = np.linspace(start,end,steps)
    dt = tRange[1] - tRange[0]
    yRange = []
    zRange = []
    tExtra = []
    y = 2
    z = 10
    for t in tRange:
        yRange.append(y)
        zRange.append(z)

        kf1 = f(t,y,z) * dt
        kg1 = g(t,y,z) * dt

        kf2 = dt * f(t + (dt / 2), y + (kf1 / 2), z + (kg1/2))
        kg2 = dt * g(t + (dt / 2), y + (kf1 / 2), z + (kg1/2))

        kf3 = dt * f(t + (dt / 2), y + (kf2 / 2), z + (kg2/2))
        kg3 = dt * g(t + (dt / 2), y + (kf2 / 2), z + (kg2/2))

        kf4 = dt * f(t + dt, y + kf3, z + kg3)
        kg4 = dt * g(t + dt, y + kf3, z + kg3)

        z +=  (kf1 / 6) + (kf2 / 3) + (kf3 / 3) + (kf4 / 6)
        y += (kg1 / 6) + (kg2 / 3) + (kg3 / 3) + (kg4 / 6)

    makePlot(tRange,yRange,"RK4")

    plt.show()
#==============================================================================
exerciseTwo()
