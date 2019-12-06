"""
Author: Ben Guilfoyle - bengfoyle.github.io - github.com/bengfoyle
Overview: A program to simulate a 2D random walk starting at the origin
"""
import numpy as np #sqrt function
import matplotlib.pyplot as plt #make plots
import random
from tkinter import *

#===============================================================================
def makePlot(x,y,name):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y,label = name)
    plt.title("Nuclear Decay - Number of Nuclei vs Time")
    plt.xlabel("Time")
    plt.ylabel("Number of Nuclei")
    # plt.xlim(x[0],x[len(x) -1])
    # plt.ylim(min(y),max(y))
    plt.legend(loc = "best")
    plt.grid()
#===============================================================================

#===============================================================================
def decay(N0,lam,t):
    """
    Overview: number of particles as a function of time
    """
    return N0 * np.exp(-lam * t)
#===============================================================================

#===============================================================================
def exerciseTwo():
    N0 = int(txt1.get()) #initial number of nuclei
    lam = float(txt2.get()) #decay constant
    dt = float(txt3.get()) #time step

    nuke, nukeAnli, timeEx = [],[],[]
    N = N0
    t = 0
    nuke.append(N)
    timeEx.append(t)
    while N > 1:
        print(N)
        N = len([i for i in range(0,N) if random.random() < lam])
        nuke.append(N)
        t += dt
        timeEx.append(t)

    time = np.linspace(0,timeEx[len(timeEx) - 1],1000)
    for t in time:
        nukeAnli.append(decay(N0,lam,t))
        
    makePlot(timeEx,nuke,"Estimate")
    makePlot(time,nukeAnli,"Analytical")
    plt.show()
#===============================================================================

#===============================================================================
"""
GUI
"""
#Define window, name, and parameters
window = Tk()
window.title("Nuclear Decay")
window.geometry('450x300')

#Insert text with user input text field.
lbl1 = Label(window, text = "Initial Number of Nuclei")
lbl1.grid(column = 0, row = 0)

txt1 = Entry(window, width = 20)
txt1.grid(column = 1, row = 0)

lbl2 = Label(window, text = "Decay Constant between 0 and 1")
lbl2.grid(column = 0, row = 1)

txt2 = Entry(window, width = 10)
txt2.grid(column = 1, row = 1)

lbl3 = Label(window, text = "Time Step")
lbl3.grid(column = 0, row = 2)

txt3 = Entry(window, width = 10)
txt3.grid(column = 1, row = 2)

#button that runs "clicked" function on click
btn1 = Button(window, text = "Make Plot", command = exerciseTwo)
btn1.grid(column = 0, row = 3)

#loop until closed
window.mainloop()
#===============================================================================
