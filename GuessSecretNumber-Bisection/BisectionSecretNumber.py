# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:53:10 2016

@author: Rishabh Lakhotia
"""

epsilon = 0.01
low = 0
high = 100
guess = False

print("Please think of a number between 0 and 100!")

while guess == False:
    ans = int((high+low)/2)
    print("Is your secret number " + str(ans) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if x == "h":
        high = round(ans,0)
    elif x == "l":
        low = round(ans,0)
    elif x == "c":
        guess = True
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(round(ans,0)))