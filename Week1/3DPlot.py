# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:37:37 2019
Author: bguilfoyle -github.com/bengfoyle
Overview: Contour 3D Plot using some sample data
"""

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 

xx,yy = np.mgrid[-2:2:81j, -3:3:91J]

zz = np.exp(-2*xx**2-yy**2)*np.cos(2*xx)*np.cos(3*yy)

plt.ion()
fig = plt.figure()
ax = Axes3D(fig)
            
c = ax.plot_surface(xx,yy,zz, rstride = 4, cstride = 3, \
cmap = cm.jet, alpha = 0.9)

ax.contour(xx,yy,zz, zdir = 'x', offset = -3.0, colors = "black")
ax.contour(xx,yy,zz, zdir = 'y', offset = 4.0, colors = "blue")
ax.contour(xx,yy,zz, zdir = 'z', offset = -2.0)

ax.set_xlim3d(-3.0,2.0)
ax.set_ylim3d(-3.0,4.0)
ax.set_zlim3d(-2.0,1.0)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.colorbar(c, orientation = "vertical")
ax.set_title("surface plot with contours", weight = "bold", size = 18)