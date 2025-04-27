# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 11:31:44 2025

@author: mwelz
"""
'''
name = input("What's your name? ")

print(f"Nice to meet you, {name}.")

#function that asks for favorite number and squares it
def squareNum():
    favNum = int(input("What's your favorite number? ")) #read in as an integer
    print(f"Your favorite number square is {favNum**2}")
    return favNum**2

# run the function
favNumSquared = squareNum()
'''
import numpy as np

def getArea(name,radius):
    circleArea = np.pi * radius * radius
    print(f"Hi, {name}, the area of your circle is {circleArea}.")
    return circleArea


myArea = getArea("Matt",6)



myGrades = []

response =  'y'
while response == "y" or response == 'Y' or response == "yes":
    grade = float(input("Enter your next grade: "))
    myGrades.append(grade)
    response = input("Do you want to enter another grade? (y/n) ")
    
print(myGrades)


#build a student class with 3 data/instance variables and 2 methods/functions
class studentType:
    
    #constructor function that intializes students
    def __init__(self,name, gpa, year):
        self.name = name
        self.gpa =gpa
        self.year = year
        
    def greeting(self):
        print(f"Hi {self.name}, nice to meet you. Your GPA is {self.gpa} and class year is {self.year}")
        
    def changeGPA(self, newGPA):
        self.gpa = newGPA
        
    
    
#create an instance of studentType

student1 = studentType("Matt Welz", 3.8, "Junior")

student1.greeting()

student1.changeGPA(3.65)

student1.greeting()
    
    
    
    



