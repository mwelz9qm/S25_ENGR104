"""
ENGR 104
Class on 2/7/2025
"""

#tuples are lists that are constant/ummutable
tup = (4,9,"dog",7,"cat")

print(tup[3])
# tup[3] = 90 is illegal because we can't change

# intro to python dictionaries 
favNum = {"Matt":17, "Shannon":3, "Jesse":101}
print("Matt's favorite number is",favNum["Matt"])
favNum["Erin"] = 23

rando = {} #empty dictionary, build a dictionary from there
rando[5]= "horse"
rando["coffee"] = 7
rando[(3,5)] = 72.4
rando[-99.9] = [1,2,3]
print(rando)

#nested dictionary example
pops = {}
pops[1997] = {"Springfield":12000,"Bristol":20000,"Lafayette":4800}
pops[1998] = {"Springfield":13500,"Bristol":20000,"Lafayette":5000}
pops[1999] = {"Springfield":14000,"Bristol":18000,"Lafayette":5200,"Richmond":72000}

#population of Springfield in 1998
print(pops[1998]["Springfield"])
# change the population of Richmond in 1999
pops[1999]["Richmond"] = 100000




