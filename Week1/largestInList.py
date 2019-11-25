# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:01:09 2019
@author: bguilfoyle, github.com/bengfoyle
Overview: Exercise 1.4 - Loop through list and find largest value, and its position
"""

def findLargest(ax):
    """
    Overview: Returns first occuring, largest value in list. 
    """
    largest = ax[0] #initally set 1st value to largest default value
    for i in range(1,len(ax)): #iterate over all other values
        if ax[i] > largest: #compare largest to current element of ax
            largest = ax[i] #if true set largest equal to current element
    return largest

L = [5,7,18,9,0,1,3,7,7,2]
largest = findLargest(L)

#print statement with some formatting, add +1 as lists start indexing at zero 
print("The largest in L is", largest, "item", L.index(largest) + 1)

