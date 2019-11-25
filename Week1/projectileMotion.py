import math
import numpy
import matplotlib.pyplot as plt
from matplotlib import cm
from tkinter import *

#find max distance traveled by a body in the x plane
#v^2 = u^2 + 2as
#v = u + at
#s = ut + 0.5*at^2
#Assume no air resistance
#Assume body remains stationary when it impacts the ground

def plotGraph(yAxis,xAxis,timeAxis):
    """
    Overview: Plot graph vased on x y and time axis
    """
    print(xAxis)
    print("##############################################")
    print(yAxis)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #ax2 = ax1.twiny() #creates 2 x axis both relative to shared y axis
    ax1.set_xlabel("Horizontal Displacement(Meters)")
    ax1.set_ylabel("Vertical Displacement(Meters)")
    ax1.grid()
    ax1.plot(xAxis,yAxis)

def getHeight(u,t,a,h):
    """
    Overview: Calculate height of object based on running parameters
    """
    s = (u*t) - (0.5*abs(a))*(t**2) + h
    return s
    
    
def heightLength(h,angle,u,a,lowerT,upperT):
    """
    Overview: Calculate range of projectile over a time range
    """
    
    #parse inputs to floats for calcualtions
    h,angle = float(h),math.radians(float(angle))
    u,a,lowerT,upperT = float(u),float(a),float(lowerT),float(upperT)
    
    #finding cartesian components of inital and final velocity 
    #(final velocity not currently used for anything)
    if angle != 1.5707963267948966:
        uy = u*math.sin(angle)
        ux = u*math.cos(angle)
        #vy = v*math.sin(angle)
        #vx = v*math.cos(angle) 
    else:
        #if angle is 90 degrees then all velocity is in y direction
        uy = u
        ux = 0
        
    #Lists used to track time, height and x displacement
    height = []
    time = []
    xdis = []
    currentTime = lowerT
    currentHeight = getHeight(uy,currentTime,a,h) #get height at t = 0
    #run simulation for as long as y displacement is > 0
    #while(currentHeight >= 0 ):
    while(currentTime <= upperT):
        #append height/x displacemtnt/current time to respective lists
        time.append(currentTime)
        if currentHeight >= 0:
            height.append(currentHeight) 
            xdis.append(ux*currentTime)
        else:
            height.append(height[len(height)-1])
            xdis.append(xdis[len(xdis)-1])
        #incriment current time by 1/10th of a second, feel free to change this
        currentTime += 0.1 
        #new current height calculated
        currentHeight = getHeight(uy,currentTime,a,h) 
        
    print(xdis)
    
    return max(height), max(xdis),height,xdis,time
    
def clicked(): #perform opertion on button click
    height = txt1.get()
    angle = txt2.get()
    initial_velocity = txt3.get()
    acceleration = txt4.get()
    upperT = txt6.get()
    lowerT = txt5.get()
    
    maxHeight, maxDistance,height_list, xdis_list,time_list = \
    heightLength(height, angle,initial_velocity, acceleration,lowerT,upperT)
    
    #Create label based off the returned values for max distance/height
    maxHeight = "Max Height: ", round(maxHeight,5)
    maxDistance = "Max Distance: ", round(maxDistance,5)
    print(maxHeight, maxDistance)
    lbl7= Label(window,text = maxHeight)
    lbl7.grid(column = 0, row = 5)
    lbl8= Label(window,text = maxDistance)
    lbl8.grid(column = 0, row = 6)
    #create plot based on returened lists
    plotGraph(height_list,xdis_list,time_list)

#Define window, name, and parameters
window = Tk()
window.title("Projectile Motion")
window.geometry('450x200')

#Insert text with user input text field. 
lbl1 = Label(window, text="Enter a value for initial height (m)")
lbl1.grid(column=0, row=0)

txt1 = Entry(window, width = 10)
txt1.grid(column = 1, row = 0)

lbl2 = Label(window, text="Enter a value for angle of trajectory (Deg)")
lbl2.grid(column=0, row=1)

txt2 = Entry(window, width = 10)
txt2.grid(column = 1, row = 1)

lbl3 = Label(window, text="Enter a value for initial velocity of the particle (m/s)")
lbl3.grid(column=0, row=2)

txt3 = Entry(window, width = 10)
txt3.grid(column = 1, row = 2)

lbl4 = Label(window, text="Enter a value for acceleration due to gravity (m/s^2)")
lbl4.grid(column=0, row=3)

txt4 = Entry(window, width = 10)
txt4.grid(column = 1, row = 3)

lbl5 = Label(window, text="Enter a value for time interval (s)")
lbl5.grid(column=0, row=4)

txt5 = Entry(window, width = 10)
txt5.grid(column = 1, row = 4)

txt6 = Entry(window, width = 10)
txt6.grid(column = 2, row = 4)

#button that runs "clicked" function on click
btn = Button(window, text="Submit Values", command = clicked)
btn.grid(column=1, row=5)

#loop until closed
window.mainloop()