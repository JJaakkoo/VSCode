#f_factorials.py
'''
title: factorials example
author: jako zeng
date-created: 2022-02-09
'''

def factorial(NUMBER):
    """Determines the factorial of the given number

    Args:
        NUMBER (int): 

    Returns: 
        NUMBER (int): total
    """
    # base case
    if NUMBER == 1:
        return NUMBER
    else:
        # recursive case
        return NUMBER * factorial(NUMBER - 1)
    return

if __name__ == "__main__":
    NUM = int(input("Enter a number: "))

    print(f'The factorial of {NUM} is {factorial(NUM)}')

    