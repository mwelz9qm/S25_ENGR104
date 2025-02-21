# -*- coding: utf-8 -*-
"""
class examples for 2/21/25

@author: mwelz
"""

#user defined function
#function to get distance between two points (x1,y1), (x2,y2)
#if no second point, defaults to origin -- put default parameters at the end
#docstring for professional documentation
def distance(x1,y1,x2 = 0,y2 = 0):
    """
    

    Parameters
    ----------
    x1 : float
        x coordinate.
    y1 : float
        y coordinate.
    x2 : float, optional
        x coordinate. The default is 0.
    y2 : float, optional
        y coordinate. The default is 0.

    Returns
    -------
    d : float
        distance between two points.

    """
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return d


dist = distance(3,5,-8,7)   
print(f"The distance between (3,5) and (-8,7) is {round(dist,2)} units.")


dist = distance(3,4)
print(f"The distance between (3,4) and the origin is {dist}  units.")


#scope example
import numpy as np

def scope_test(s,n,t,l,a,d):
    s = "something something"
    n = 17
    t = (11.4,8.6)
    l[0] = "day"
    a[-1] = 999.9
    d["dog"] = "Ziggy"


s1 ="stuff"
n1 = 99
t1 = (5,5)
l1 = [5,6,7,"cow"]
a1 = np.arange(4,23,3)
d1 = {"city":"Durango", "state":"Colorado"}

scope_test(s1,n1,t1,l1,a1,d1)
print(s1,n1,t1,l1,a1,d1)


#example of lambda function
#takes two inputs, squares them, adds them up 

g = lambda a,b: a**2 + b**2

print(g(3,4))


#function to estimate the derivative
def deriv(f,x):    #differentiate f at point x
    return (f(x+.000001) - f(x))/.000001


f = lambda x: x**2

print(f"The derivate of x^2 at x=5 is roughly {deriv(f,5)}")

