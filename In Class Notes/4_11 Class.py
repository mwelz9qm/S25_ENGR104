# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 11:25:59 2025

@author: mwelz
"""

class Person:
    '''
    This class will model a person with their name and age while including a greeting method
    '''
    #the init function is a "constructor" which sets the rules for creating a new person
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def nameChange(self,newName):
        self.name = newName
        print(f"Successfully changed to {self.name}.")

person1 = Person("Langston", 25)
person1.greeting()
print(person1.age)

person2 = Person("Shannon", 19)
person2.greeting()

person1.nameChange("Tommy")
print(person1.name)

class Resistor:
    '''
    a basic class to represent a resistor
    Attributes: resistance
    Methods: getCurrent returns current through resistor for a given voltage
    '''
    def __init__(self, resistance):
        if resistance <= 0: #check for valid values
            print("Invalid resistance. Default set to 100 ohms")
            self.resistance = 100
        else:
            self.resistance = resistance

    def getCurrent(self, voltage):
        return voltage/self.resistance


r1 = Resistor(50)
r2 = Resistor(100)

print(f"For a volage of 10 volts, the current through r1 is {r1.getCurrent(10)} amps.")
r2.getCurrent(20)

person1.nameChange("Tommy")
print(person1.name)

#write a product class that will be inherited later

class Product:
    def __init__(self,name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
    
    def display_info(self):
        print(f"Product name: {self.name}")
        print(f"Product price: ${self.price}")
        print(f"Product sku: {self.sku}")

p1 = Product("Hoodie", 45, "yfs87d87ftdt87tn")
p1.display_info()

#create a derived class for books that inherits from product

class Book(Product):  #inherits from products
    def __init__(self, name, price, sku, author, isbn, pubYear):
       super().__init__(name, price, sku) #super means use product class function
       self.author = author
       self.isbn = isbn
       self.pubYear = pubYear
       
    def display_info(self):
        print("**************************")
        super().display_info() #use the product class to display name, price, sku
        print(f"Author name: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Year of Publication: {self.pubYear}")
        print("**************************")
    
    def is_public_domain(self, currYear): #returns true/false
        return (currYear - self.pubYear > 95)

#create a book, display it's info, and determine if in public domain

myBook = Book("The Trial", 9.95, "fdhuhkjdhfj", "Franz Kafka", "978-1612931036", 1924)


myBook.display_info()
print(myBook.is_public_domain(2025))
    
