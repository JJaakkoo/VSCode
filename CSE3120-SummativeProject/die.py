# die.py
'''
Title: Die Class
Author: Jako 
Date-created: March 11, 2022
'''

from random import randint

class Die:
    """class that holds the die
    """
    def __init__(self): # The variables for the highest numer a dice can roll
        self.DIEMAX = 6
        self.DIENUM = None

    def rollDie(self): # Rolls the dice
        self.DIENUM = randint(1,self.DIEMAX)

# --- Accessors --- #

    def showDie(self): # prints the number on the die
        print(self.DIENUM)

    def returnDie(self): # returns the number of the die
        return(self.DIENUM)

# --- Modifiers --- #

if __name__ == "__main__":
    """print("hi")"""
    