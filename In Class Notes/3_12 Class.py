# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 11:20:09 2025

@author: mwelz
"""

import numpy as np
import matplotlib.pyplot as plt

#set up 2 x 2 plots on our figure
# fig, ax = plt.subplots()  this makes just one plot

fig, ax = plt.subplots(2,2, sharex = True)

x = np.linspace(-5,5,300)
#upper left plot
y1 = np.arctan(x)  #using arctan
ax[0,0].plot(x,y1, color = 'magenta', linewidth = 2, linestyle = 'dashed')
ax[0,0].set_title('Plot 1')
ax[0,0].set_ylabel(r'$f(x) = \arctan(x)$')  #r ' ' makes it a "raw" string
#upper right plot
ax[0,1].scatter(x,y1, color = 'black', marker = '*')
ax[0,1].set_title('Plot 2')
ax[0,1].set_ylabel(r'$f(x) = \arctan(x)$')  #r ' ' makes it a "raw" string


#lower left plot
y2 = np.exp(-x**2)  #using e^-x^2
ax[1,0].plot(x,y2, color = 'red', linewidth = 2)
ax[1,0].set_title('Plot 3')
ax[1,0].set_ylabel(r'$f(x) = e^{-x^2}$')  #r ' ' makes it a "raw" string
#lower right plot
ax[1,1].scatter(x,y2, color = 'cyan', marker = '<')
ax[1,1].set_title('Plot 4')
ax[1,1].set_ylabel(r'$f(x) = e^{-x^2}$')  #r ' ' makes it a "raw" string
fig.tight_layout()  #sometimes cleans up the figure spacing

plt.savefig('myFig.pdf', dpi=300)

#make a histogram based on random dice rolls
fig, ax = plt.subplots()
bins = np.arange(0.5, 7, 1)
sampleSize = 10000
rolls = np.ceil(np.random.rand(sampleSize)*6)  #generates sampleSize many numbers between 1 and 6
ax.hist(rolls, color = 'green', edgecolor = 'black', bins = bins)
ax.set_xlabel('Die Value')
ax.set_ylabel('Fequency')
ax.set_title(f"Distribution of {sampleSize} die rolls")
fig.tight_layout()

#make a polar coordinate plot

r = np.linspace(0,10,5000)
theta = np.cos(r**2)

fig, ax = plt.subplots(subplot_kw = {'projection':'polar'})
ax.plot(theta,r)





