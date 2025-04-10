# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 11:22:55 2025

@author: mwelz
"""
#quick intro to classes/objects
import numpy as np

a = np.array([[1,2,3],[4,5,6]])

#class definitions are blue prints for new object types
class Person:
    #initializer
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}!")

friend = Person("Langston", 25)

friend.greeting()


friend1 = Person("Susan", 22)
friend1.greeting()
print(f"Susan's age is {friend1.age}")

friends = [friend, friend1]

#random test review stuff (mostly looked at old quizzes)


temperatures = [2, 15, 20, 30, -5, 25, 28]

for temp in temperatures:
    if (temp > 25):
        print(f"{temp} degrees is hot!")
    elif (temp >= 10):
        print(f"{temp} degrees is moderate!")
    else:
        print(f"{temp} degrees is cold!")


temp = 30
humidity = 80

if (temp > 25 and humidity > 70):
    print("It's muggy outside!")
else:
    print("It's not muggy outside!")








