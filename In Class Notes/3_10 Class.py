# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:18:57 2025
3/10/25 Class Notes
@author: mwelz
"""

import numpy as np
import matplotlib.pyplot as plt

#our first scatter plot
x = range(1,6)  #x values
y = [5,2,1,4,3] #y values
plt.figure(1) #label our first figure

plt.scatter(x,y) #make a scatter plot
plt.plot(x,y) #connects the dots

#choose colors, markers, sttyle

plt.figure(2)

plt.scatter(x,y, marker='P', color = "green", s = 200)
plt.plot(x,y, linewidth = 2, color = "black")

#for more options see https://www.w3schools.com/python/matplotlib_markers.asp

#plot cosine from 0 to 4pi

x= np.linspace(0,4*np.pi,1000) #x values
y = np.cos(x) #y values

plt.figure(3)
#adding legend, and lavels to the plot
plt.scatter(x,y, marker = 'd', color = 'cyan', s = 50)
plt.plot(x,y, linewidth =2, color = 'magenta')
plt.legend(['$y = cos(x)$'], loc = "lower left")  # stuff inside $ is math using latex
plt.xlabel('x (radians)', fontsize = 13)
plt.ylabel('f(x)', fontsize = 13)

#another approach to plotting that allows multiple plots in a figure
# 2 rows, 1 column of 1 plots, that share same x axis values
fig, (ax1,ax2) = plt.subplots(2,1, sharex = True)

x = np.linspace(-10,10,30)
y1 = np.exp(x/10) + 2
y2 = np.exp(-x/10) + 4
ax1.scatter(x,y1, marker = '+', color = 'green', s = 50)
ax2.scatter(x,y2, marker = '*', color = 'magenta', s = 50)
ax1.plot(x,y1, linewidth = 2, color = 'black')
ax2.plot(x,y2, linewidth =2 , color = 'orange')

#we use "set" for seeing labels and titles, but not legen
ax1.set_title('Plot 1', loc = 'left')
ax2.set_title('Plot 2', loc = 'left')
ax1.set_xlabel('x - values', fontsize = 12)
ax1.set_ylabel('y = f(x)', fontsize = 12)
ax2.set_xlabel('x - values', fontsize = 12)
ax2.set_ylabel('y = g(x)', fontsize = 12)
ax1.legend(['$f(x)=e^{x/10} + 2$'])
ax2.legend(['$f(x)=e^{-x/10} + 4$'])

#error bars

ax1.errorbar(x,y1, yerr =1, elinewidth = 0.5, ecolor = 'red', capsize = 3, capthick =1)






