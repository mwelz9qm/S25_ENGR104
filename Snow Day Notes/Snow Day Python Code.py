#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:09:12 2025

@author: mwelz
"""

import numpy as np
import scipy.linalg as slin

# solving a linear system
A =np.array([[1,-2,9,13],[-5,1,6,-7],[4,8,-4,2],[8,5,-7,1]])
b = np.array([1,-3,-2,5])

ans = slin.solve(A,b)
print(ans)

#solve electrical network problem

A = np.array([[11,-3,0],[-3,6,-1],[0,-1,3]])
b = np.array([30,5,-25])

ans = slin.solve(A,b)
print(ans)


#intro to user defined functions

def calculate_area(length, width):  #function to calculate rectangle area
    area = length * width
    return area


l = 5
w = 18

print(calculate_area(l,w))


# function to concatenate strings

def concatenate_strings(string1, string2):
    result = string1 + " " + string2
    return result

    
myOutput = concatenate_strings("Hello", "World")
print(myOutput)
    
firstName = "Matt"
lastName = "Welz"

print(concatenate_strings(firstName,lastName))


#function that takes array of degrees and computes the singes


def find_sines(angles_deg):
    angles_rad = np.radians(angles_deg)
    sines = np.round(np.sin(angles_rad),2)
    return sines


degrees = np.arange(0,361,15)
print(find_sines(degrees))


#function that returns two values

def rectangle_info(length, width):
    area = length * width
    perimeter = 2*length + 2*width
    return area, perimeter


a, p = rectangle_info(12,10)

#function that returns no values

def nada():
    print("Just printing stuff!")
    
    
    
    
nada()


    