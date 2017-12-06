# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:21:31 2016

@author: Rishabh Lakhotia
"""

acc = 0.001
increment = 0.0001
guess = 0
count = 0
cube = int(input("Enter the number whose cube root is required: "))

while abs(guess**3 - cube) >= acc and guess < cube:
    guess += increment;
    count += 1
print("number of guesses required is " + str(count))
if abs(guess**3 - cube) >= acc:
    print("FAILED")
else:
    print("The cube root of " + str(cube) + " is near to " + str(guess))
    
print("The cube of " + str(guess) + " is " + str(guess**3))