
import numpy as np

#use numpy to import a text file


#exp_id, temp, pressure, reaction = np.loadtxt("input_data-1.txt", skiprows = 6, unpack=True)

temp, reaction = np.loadtxt("input_data-1.txt", usecols = (1,3),skiprows = 6, unpack = True)

#to load from a csv
#exp_id, temp, pressure, reaction = np.loadtxt("input_data-1.csv", skiprows = 6, delimiter = ',', unpack=True)


#write out to a file

#np.savetxt("output_data.txt", list(zip(temp,reaction)), fmt = "%12.1f")

info = "Data from pretend experiment"
info += "\n 3/7/2025"
info += "\n collected by Matt Welz \n"


#add info as a header for my output file

np.savetxt("output_data.txt", list(zip(temp,reaction)), fmt = "%12.1f", header = info)
np.savetxt("output_data.csv", list(zip(temp,reaction)), fmt = "%12.1f",delimiter = ',', header = info)


