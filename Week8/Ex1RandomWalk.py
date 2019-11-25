"""
Author: Ben Guilfoyle - bengfoyle.github.io - github.com/bengfoyle
Overview: A program to simulate a 2D random walk starting at the origin
"""
import numpy as np #sqrt function
import matplotlib.pyplot as plt #make plots
import random
#===============================================================================
STEPS = 10000
xVals,yVals = [],[]
x,y = 0,0
seed = random.seed(a = None)
for i in range(0,STEPS):
    print(x,y)
    xVals.append(x)
    yVals.append(y)
    x += random.uniform(-np.sqrt(2),np.sqrt(2))
    y += random.uniform(-np.sqrt(2),np.sqrt(2))

plt.scatter(xVals,yVals)
plt.show()
#===============================================================================
