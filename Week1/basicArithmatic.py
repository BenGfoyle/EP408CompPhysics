# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:52:17 2019
@author: bguilfoyle, github.com/bengfoyle
Overview: Exercise 1.2 - Add subtract multiply and divide 2 complex numbers
"""

def add(a,b):
    """
    Overview: Return the sum of a + b
    """
    return a + b

def subtract(a,b):
    """
    Overview: Return the value of a - b
    """
    return a - b

def multiply(a,b):
    """
    Overview: Return the value of a * b
    """
    return a * b

def divide(a,b):
    """
    Overview: Return the value of a / b
    """
    return a / b

#define complex numbers. First value is real part, second arguement is complex
x = complex(2,3)
y = complex(3,-7)
z = complex(-3,4)

#print statements with function calls for relivent operations
print(x, "+", y, "=", add(x,y))
print(x, "-", y, "=", subtract(x,y))
print(x, "*", y, "=", multiply(x,y))
print(x, "/", y, "=", divide(x,y))
print(z, "-", 2, "=", subtract(z,2))