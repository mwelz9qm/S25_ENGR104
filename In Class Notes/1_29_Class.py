"""
ENGR 104
Class work and notes for 1/29/25
"""

print("Hello world!")

name = "Maria"
print(f"Hello {name}, nice to meet you!")  #f string printing

distance = 400  #in miles
mpg = 30 #gas mileage per gallon
averageSpeed = 60 #miles per hour
costPerGallon = 3.10 # gas price in dollars

#calculations

time = distance / averageSpeed   #hours
gallons = distance / mpg 
cost = gallons * costPerGallon #dollars

#print results

print("Calculation Results: ")
print(f"Time of Trip: {round(time,1)} hours")
print(f"Number of Gallons used: {round(gallons,1)}")
print(f"Total cost of trip: ${round(cost,2)} ")


#importing new modules

import numpy as np
import math as m

print(np.sin(12))    #use np before the function we want from numpy
print(m.sin(12))
print(np.log(9))
print(np.sqrt(169))

dist = np.sqrt((1+2.5)**2 + (3 - 7.6)**2)
print(f"The distance between our points is {round(dist,2)}.")

from numpy import sin   #what not to do!!

a = sin(3)


#formatting for homework assignments

"""
Your Name
Assignment #3 
ENGR104
2.3.2025
"""
#Problem 7.1
print("--- Problem 7.1 ---")
h_0 = 1.6 #initial height m
v_0 = 15.2 #initial velocity m/s
t = 1.5 #time of flight (s)
g = 9.81 # gravitational acceleration m/s^2








