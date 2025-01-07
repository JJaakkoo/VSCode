# d_selection_sort.py
'''
title: selection sort
author: Jako Zeng
date-created: 2022-02-07
'''

from z_my_functions import *

def selectionSort(LIST):
    """Comapres the curretn index value with the rest of the set. It will fidn the lowest value and switch it with the current index value.

    Args:
        LIST (list): list of random integers
    """
    for i in range(len(LIST)-1): # for each numer up to the second last number.
        MINIMUM = LIST[i] # Assume the first number is the smallest number.
        for j in range(i+1, len(LIST)): # test each subsequent number
            if LIST[j] < MINIMUM: # test if the curretn number is smaller than the saved minimum
                MINIMUM = LIST[j] # update the minimum with the new smallest value.
                PLACE = j # save the index of the smallest value
        if MINIMUM < LIST[i]: # test if first number is smallest
            TEMP = LIST[i] # save the first number value
            LIST[i] = LIST[PLACE] # update first number value with smallest value.
            LIST[PLACE] = TEMP # update index of smallest value with the first value.
        #print(LIST)

# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        selectionSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))