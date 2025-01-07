#g_recursive_binary_search.py
'''
title: Recrusive bianry search
author: jako zeng
date-created: 2022-02-09
'''

from z_my_functions import *
from random import randrange

def recurBinarySearch(LIST, VALUE):
    """Recursive search through a sorted list

    Args:
        LIST (list): list of integers
        VALUE (integers): 
    """

    MIDPOINT = len(LIST) // 2
    print(MIDPOINT)
    # base case
    if LIST[MIDPOINT] == VALUE:
        return
    else:
        # recursive process
        if VALUE < LIST[MIDPOINT]:
            return recurBinarySearch(LIST[:MIDPOINT], VALUE)
        else:
            return recurBinarySearch(LIST[MIDPOINT + 1:], VALUE)

if __name__ == "__main__":
    NUMBERS = getList(10000)
    NUMBER = NUMBERS[randrange(len(NUMBERS))]
    START = getTime()
    recurBinarySearch(NUMBERS, NUMBER)
    END = getTime()
    print(END - START)
