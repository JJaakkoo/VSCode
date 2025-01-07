# a_diceroll.py
'''
title: Dice Roll
author: jako 
date-created: Feb 25, 2022
'''

from sys import exit

class Die:
    """Create a die to roll for random numbers

    :attributes:
    - DIE_MAX
    - DIE_NUM
    display
    :methods:
    - rollNum()
    - setDie()
    - getEven()
    - display()
int
    """

    from random import randint

    def __init__(self):
        """Constructs a die
        """
        self.DIE_MAX = 6
        self.DIE_NUM = None

    def rollNum(self):
        """Updates DIE_NUM with a new number
        """
        self.DIE_NUM = Die.randint(1,self.DIE_MAX)

### Accessor

    def getEven(self):
        """Determine whether the DIE_NUM is even
        :return: (bool)
        """
        if self.DIE_NUM % 2 == 0:
            return True
        else:
            return False

    def display(self):
        """prints out the die number
        """
        print(self.DIE_NUM)

def checkInt(VALUE,LOW,HIGH):
    try:
        VALUE = int(VALUE)
        if VALUE > HIGH or VALUE < LOW:
            print("This number is not an option")
            return checkInt(input("> "),LOW,HIGH)
        else:
            return VALUE
    except TypeError:
        print("This is not a number!")
        return checkInt(input("> "),LOW,HIGH)
    except ValueError:
        print("This is not a number!")
        return checkInt(input("> "),LOW,HIGH)


if __name__ == "__main__":
### VARIABLES ###
    SCORE = 0
    DIE1 = Die()
    DIE2 = Die()

    print('''
Welcome to Dice Roll
Get points by correctly choosing both odd, both even, or odd and even!DIE_MAX
Lose points if you are wrong.''')

    while True:
### INPUTS ###
        print('''
1. Guess dice will be odd
2. Guess dice will be even
3. Guess one die will be odd and one die will be even''')

        CHOICE = checkInt(input("> "),1,3)

### PROCESSING ###

        DIE1.rollNum()
        DIE2.rollNum()

        if DIE1.getEven() and DIE2.getEven():
            RESULT = 2
        elif not DIE2.getEven() and not DIE1.getEven():
            RESULT = 1
        else:
            RESULT = 3

        if CHOICE == RESULT:
            SCORE += 10
        else:
            SCORE -= 5

### OUTPUTS ###

        print(f"Die 1 = {int(DIE1.DIE_NUM)}")
        print(f"Die 2 = {int(DIE2.DIE_NUM)}")

        if CHOICE == RESULT:
            print("Right on!")
        else:
            print("Better luck next time")

        print(f"SCORE: {SCORE}")

        AGAIN = input("Keep going?> (Y/n) ")
        if AGAIN == "Y" or AGAIN == "y":
            pass
        else:
            exit()
