# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:25:11 2025

@author: mwelz

for loops stuff

"""


#a for loop that prints the first 100 squares
for num in range(1,101):
    print(f"{num} squared is {num * num}.")
    

#a for loop that sums the first 50000 integers
totalSum = 0
for num in range(1,51):
    totalSum = totalSum + num


print(f"The sum is {totalSum}.")


#a for loop across a list of strings
friendList = ["Rafa","Shelly","Max","Alex","Shannon"]
for friend in friendList:
    print(friend)

#a for loop through the characters in a string
name = "Quentin"
for letter in name:
    print(letter)

#Fibonacci number finder

back2 = 1
back1 = 1

for num in range(3,101):
    fibNum = back1 + back2
    back2 = back1
    back1 = fibNum
    print(fibNum)

#loop through dictionaries

D = {"Colorado":8,"New Mexico":5,"Utah":13,"Arizona":6}

#loop through keys 

for state in D.keys():
    print(state)

#loop through values 

for rank in D.values():
    print(rank)

#track position while looping
counter = 0
for letter in name:
    print(f"Letter {counter} in the name is {letter}")
    counter +=1

#alternate approach to the same thing, tracks index for us

for counter,letter in enumerate(name):
    print(f"Letter {counter} in the name is {letter}")

listA = list(range(1,101))
newList = [num**2 for num in listA]

