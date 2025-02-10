# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:20:24 2025
ENGR 104 Class Notes
@author: mwelz
"""

import numpy as np

#manually create a numpy array
array1 = np.array([4,5,2.3,9,12.3,5])

#fill with linspace
array2 = np.linspace(0,30,11) #start with 0, end with 30, 11 points

#fill with arange which just behaves like "range"
array3 = np.arange(0,16,3)

#fill with ones
array4 = np.ones(12)

array4 = np.ones(12,dtype=int)  #makes 1s ints instead of floats

#fill with zeros

array5 = np.zeros(42)

#doing math on a numpy array
a = np.array([4,7,8,12])
print(a+2)
print(a**2)
print((a-3)**2)
print(np.sin(a))

angles_deg = np.arange(0,91,5)  #angles in degrees
angles_rad = np.radians(angles_deg) #convert degs to rads
final = np.sin(angles_rad)  #find sin
final = np.round(final,3) #round final to 3 places

#build an array with 10 6's

sixes = np.ones(10, dtype = int) + 5





