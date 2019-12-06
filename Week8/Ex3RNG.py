"""
Author: Ben Guilfoyle - bengfoyle.github.io - github.com/bengfoyle
Overview: A program to simulate a 2D random walk starting at the origin
"""
import numpy as np #sqrt function
import matplotlib.pyplot as plt #make plots
from mpl_toolkits.mplot3d import Axes3D
import random

#===============================================================================
def makePlot(x,y,z,name,col):
    """
    Overview: Make a plot of x vs y
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c = col, marker = ".")
#===============================================================================

#===============================================================================
def rng(n,x0):
    a,c,m = 65, 319, 65537
    prs = []
    xn = x0
    for i in range (n):
        xn = ((a*xn) + c) % m
        prs.append (xn)
    return prs
#===============================================================================

#===============================================================================
def rng2():
    return random.uniform(0,1)
#===============================================================================

#===============================================================================
def exerciseThree():
    x1,y1,z1 = rng(5000,56),rng(5000,100),rng(5000,54)
    x2,y2,z2 = [],[],[]
    for i in range(0,5000):
        x2.append(rng2())
        y2.append(rng2())
        z2.append(rng2())


    makePlot(x1,y1,z1,"RNG Plot","r")
    makePlot(x2,y2,z2,"RNG Plot","b")
    plt.show()
#===============================================================================
exerciseThree()
