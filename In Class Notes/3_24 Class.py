# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 11:11:37 2025

@author: mwelz
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd


#quick intro to 3-d surface and contour plots

x = np.linspace(-5,5,50)
y = np.linspace(-5,5,50)


X,Y = np.meshgrid(x,y)

Z = np.exp(-(X**2 + Y**2))

fig, ax = plt.subplots(subplot_kw = {'projection':'3d'})

ax.plot_surface(X,Y,Z, cmap = cm.ocean, alpha = 0.8, linewidth = 0.25, cstride = 1, rstride =1)


fig, ax = plt.subplots()
ax.contour(X,Y,Z,12, cmap = cm.ocean)

#working with out first dataframes and pandas

#reading a csv into a dataframe
df = pd.read_csv('sensor_data.csv')

print(df.head())    #first five rows of df
print(df.info())    #returns info about the dataframe

print(df['Temperature_C'])  #print the temperature column
print(df.Temperature_C)     #alternate way to print the temperature column

#reload and skip the current column names and rename them
# df = pd.read_csv('sensor_data.csv', names = ['A','B','C','D','E','F'], skiprows =1)

#accessing row index 5 element from humidity column
print(df.Humidity[5])
print(df[df.Humidity>45])  #prints all rows with humidity > 45

#now let's plot columns from our df


fig, ax = plt.subplots()
ax.scatter(df.Temperature_C,df.Humidity)
ax.set_xlabel('Temperature in Celsius')
ax.set_ylabel('% Humidity')
ax.set_title('Temperature vs Humidity')


#filter into two separate dfs based on location

dfA = df[df.Location == 'Location_A'] 
dfB = df[df.Location == 'Location_B'] 

# make the same plot as above, but for locations A and B separately in the same figure
fig, ax = plt.subplots(2,1, sharex=True)

ax[0].scatter(dfA.Temperature_C,dfA.Humidity)
ax[0].set_xlabel('Temperature in Celsius')
ax[0].set_ylabel('% Humidity')
ax[0].set_title('Location A')

ax[1].scatter(dfB.Temperature_C,dfB.Humidity)
ax[1].set_xlabel('Temperature in Celsius')
ax[1].set_ylabel('% Humidity')
ax[1].set_title('Location B')

fig.tight_layout()


