# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 11:28:03 2025

@author: mwelz
"""

#a while loop that prints all Fibonacci numbers up to a point
x,y = 0,1

while (x < 100):
    print(x)
    x,y = y,x+y
    
#ask a user their name
name = input("What's your name? ")
print(f"Hi! Nice to meet you {name}.")    
    
    
# ask a user to repeatedly give their quiz scores that we store in a list
scores = []
choice = "Y"
while (choice == "Y"):
    score = float(input("Enter a quiz score "))
    scores.append(score)
    choice = input("Do you want to enter another score (Y/N) ")
    
print(f"{name}, you entered the following scores {scores}.")


def find_prime():
    """
    
    Returns
    -------
    Smallest prime dividing a user's integer

    """
    n = int(input("Enter a positive integer greater than 1. "))
    i = 2
    while (n % i != 0 ):
        i += 1 #i = i + 1
    print(f"The smallest prime divisor is {i}.")


find_prime()

