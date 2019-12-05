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
def RNG():
    return random.random()
#===============================================================================

#===============================================================================
def exerciseTwo():
    x = []
    y = []
    z = []
    for i in range(0,1000):
        x.append(RNG())
        y.append(RNG())
        z.append(RNG())

    makePlot(x,y,z,"RNG Plot")
    plt.show()
#===============================================================================
exerciseTwo()
