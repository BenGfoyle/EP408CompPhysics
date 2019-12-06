"""
Author: Ben Guilfoyle - bengfoyle.github.io - github.com/bengfoyle
Overview: A program to simulate a 2D random walk starting at the origin
"""
import numpy as np #sqrt function
import matplotlib.pyplot as plt #make plots
from mpl_toolkits.mplot3d import Axes3D
import random

#===============================================================================
def makePlot(x,y,z,name):
    """
    Overview: Make a plot of x vs y
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    fig.show()
#===============================================================================

#===============================================================================
def RNG(i):
    a,c,m,seed = 65, 319, 65537, 3434
    if i == 0:
        return seed
    else:
        return ((a * RNG(i - 1) + c) % m)
#===============================================================================

#===============================================================================
def exerciseThree():
    x = []
    y = []
    z = []
    for i in range(1,100):
        x.append(RNG(i))
        y.append(RNG(i))
        z.append(RNG(i))

    print(x,y,z)

    makePlot(x,y,z,"RNG Plot")
    plt.show()
#===============================================================================
exerciseThree()
