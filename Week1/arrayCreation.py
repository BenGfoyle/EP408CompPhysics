# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:08:01 2019
@author: bguilfoyle, github.com/bengfoyle
Overview: Exercise 1.5 - Generating arrays based off values from other arrays
"""
import numpy as np

x = np.linspace(0,2 * np.pi, 100) #linspace generates values between 2 values
y = np.sin(x) #perform sin operaton on all elements of x
print(x)
print(y)