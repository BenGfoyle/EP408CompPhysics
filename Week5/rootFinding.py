# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:08:22 2019

@author: bguilfoyle
Overview: Finding the roots of equations using Half Interval Search, Bisection,
Newtons, and Secant methods.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as opt

#==============================================================================
def makePlot(x,y):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,'r')
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
#==============================================================================

#==============================================================================
def f1(x):
    """
    Overview: Equation used for exercise one and two and five
    """
    return (x ** 4) - (19 * (x ** 3))+ (117 * (x ** 2)) - (261 * x) + 162 
#==============================================================================
    
#==============================================================================
def f2(x):
    """
    Overview: Equation used for exercise three and four
    """
    return np.sin(x) + (4 * (x ** 2)) - (13 * x) - 5
#==============================================================================

#==============================================================================
def halfInterval(x,d):
    """
    Overview: Calculate the roots using the half interval method
    """
    ans = f1(x) * f1(x + d)
    if d <= 1e-3: #if step size has become too small return x
        return x
    elif ans == 0: #if result of ans is exactly zero return x
        return x
    elif ans > 0: #if ans > 0 adjust x by step
        return halfInterval(x + d,d) 
    elif ans < 0: #if ans < 0 adjust step
        return halfInterval(x, d/2)
#==============================================================================

#==============================================================================
def bisection(xl,xh,n):
    """
    Overview: Calculate the roots usingbisection method
    """
    xm = (xl + xh) / 2
    accuracy = abs(xh - xl) / (2**n)
    ans = f1(xl) * f1(xm)
    if accuracy <= 1e-3: #if accuracy is to this precision
        return xm
    elif ans == 0:
        return xm
    elif ans < 0: #set xh to xm for next run
        return bisection(xl, xm, n + 1)
    elif ans > 0: #set xl to xm for next run
        return bisection(xm, xh, n + 1)
#==============================================================================

#==============================================================================
def newton(x):
    """
    Overview: Calculate the roots using the newton method
    """
    xn = x - (f2(x)/diff(x))
    if abs(xn - x) <= 1e-3: #return xn when reached acceptable accuracy
        return xn
    else:
        return newton(xn)#call newton on xn
#==============================================================================

#==============================================================================
def diff(x):
    """
    Overview: Return the 3 point derivate of x using f(x)
    """
    H = 0.1
    return (f2(x + H) - f2(x - H)) / (2 * H)
#==============================================================================

#==============================================================================
def secant(xl,x):
    """
    Overview: Calculate the roots using the secant method
    """
    #same as newton but doesnt use differentiation function
    xn = x - ((f2(x) * (xl - x)) / (f2(xl) - f2(x)))
    if abs(xn - x) <= 1e-3:
        return xn
    else:
        return secant(xl,xn)
#==============================================================================

#==============================================================================
def exerciseOne(numRoots):
    x =  np.linspace(0,15,100)
    fx = []
    hiRoots = []
    y = [0] * numRoots
    
    for i in x:
        fx.append(f1(i))
        
    hiParam = input("Half Interval: Enter X start, and step size(eg: 1,1)")
    xStart, hiStep  = hiParam.split(',')
    xStart, hiStep  = float(xStart), float(hiStep)
    for i in range(0,numRoots):
        if i == 0:
            hiRoots.append(halfInterval(xStart,hiStep))
        else:
            hiRoots.append(halfInterval(hiRoots[i - 1] + hiStep, hiStep))
            
    makePlot(x,fx)
    plt.scatter(hiRoots,y)

#==============================================================================
            
#==============================================================================
def exerciseTwo(numRoots):
    x =  np.linspace(0,15,100)
    fx = []
    biRoots = []
    y = [0] * numRoots
    
    for i in x:
        fx.append(f1(i))
    biParam = input("Bisection: Enter an X start, end, and step(eh:5,10,1)")
    xl, xh, biStep = biParam.split(',')
    xl, xh, biStep = float(xl), float(xh), float(biStep)
    
    for i in range(0,numRoots):
        biRoots.append(bisection(xl,xh,1))
        xl = xh
        xh += biStep
    
    makePlot(x,fx)
    plt.scatter(biRoots,y)
#==============================================================================
            
#==============================================================================
def exerciseThree(numRoots):
    x =  np.linspace(-5,5,100)
    fx = []
    ntRoots = []
    y = [0] * numRoots
    
    for i in x:
        fx.append(f2(i))
    ntParam = "1,4"
    ntX,ntStep = ntParam.split(',')
    ntX, ntStep = float(ntX), float(ntStep)
    
    for i in range(0,numRoots):
        ntRoots.append(newton(ntX))
        ntX += ntStep
    
    makePlot(x,fx)
    plt.scatter(ntRoots,y)
#==============================================================================
            
#==============================================================================
def exerciseFour(numRoots):
    x =  np.linspace(-5,5,100)
    fx = []
    scRoots = []
    y = [0] * numRoots
    
    for i in x:
        fx.append(f2(i))
    scParam = "1,4,1"
    scl, sch, scStep = scParam.split(',')
    scl, sch, scStep = float(scl), float(sch), float(scStep)
    
    for i in range(0,numRoots):
        scRoots.append(secant(scl,sch))
        scl = sch
        sch += scStep
    
    makePlot(x,fx)
    plt.scatter(scRoots,y)

#==============================================================================

#==============================================================================
def exerciseFive():
    x =  np.linspace(-5,5,100)
    fx = []
    y = [0] * 2
    for i in x:
        fx.append(f1(i))
    
    libRoots = opt.fsolve(f1,[1,3])

    print(libRoots)
    makePlot(x,fx)
    plt.scatter(libRoots,y)

#==============================================================================

ex = int(input("Which exercise would you like to run?1, 2, 3, 4, or 5:"))
numRoots = int(input("How many roots would you like to find?"))
if ex == 1:
    exerciseOne(numRoots)
elif ex == 2:
    exerciseTwo(numRoots)
elif ex == 3:
    exerciseThree(numRoots)
elif ex == 4:
    exerciseFour(numRoots)
elif ex == 5:
    exerciseFive()
else:
    print("Invalid Input")