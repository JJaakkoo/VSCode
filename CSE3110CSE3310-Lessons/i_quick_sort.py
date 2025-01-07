# i_quick_sort.py
'''
title: quick sort
author: jako zeng
date-created: 2022-02-11
'''

from z_my_functions import *

def quickSort(LIST, FIRST_INDEX, LAST_INDEX):
    """Uses a pivot value to recursively sort through the list

    Args:
        LIST (list): unsorted list
        FIRST_INDEX (int): LEFT most index value
        LAST_INDEX (int): RIGHT most index value
    """

    if FIRST_INDEX < LAST_INDEX:
        PIVOT_VALUE = LIST[FIRST_INDEX]
        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX
        
        DONE = False

        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE:
                LEFT_INDEX = LEFT_INDEX + 1
            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE:
                RIGHT_INDEX = RIGHT_INDEX - 1

            if RIGHT_INDEX < LEFT_INDEX:
                DONE = True
            else:
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP

        TEMP = LIST[FIRST_INDEX] # PIVOT VALUE
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        # Recursive part
        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX - 1) # Continues down left branch 
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX) # Continues down right branch

# MAIN PROGRAM CODE

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        quickSort(NUMBERS, 0, len(NUMBERS) - 1)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))