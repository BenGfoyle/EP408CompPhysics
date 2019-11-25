"""
Created on Mon Oct  7 11:06:42 2019

@author: bguilfoyle - github.com/bengfoyle
Overview:EX3.4 - Estimate f(x) on any point using cubic spline
"""
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

def makePlot(x,y):
    plt.plot(x,y)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
#    plt.xlim(x[0],x[len(x) -1])
#    plt.ylim(min(y),max(y))  
#    plt.legend(loc = "best")
    

def main():
    xVals = [0.3,0.5,0.9]
    x = [0,0.2,0.4,0.6,0.8,1.0,1.2,1.4]
    fx = [0.5,2,4,6,4,4,5.2,0]
    gx = []
    for i in range(0,len(xVals)):
        splineCo = splrep(x,fx)
        gx.append(splev(xVals[i],splineCo))
        
    makePlot(x,fx)
    plt.scatter(xVals,gx)
    plt.grid()
    plt.show()
    
main()