# c_bubble_sort.py
'''
title: bubble sort
author: Jako Zeng
date-created: 2022-02-04
'''

from z_my_functions import *

def bubbleSort(LIST):
    """Compares two adjacent values and moves the highest on to the end of the list.

    Args:
        LIST (list): unosrted numbers

    Returns:
        list: sorted numbers
    """
    for i in range(len(LIST)-1, -1, -1): #going backwards from the last value to the second value.
        for j in range(i): #start from the first value and move to the highest value
            if LIST[j] > LIST[j+1]:
                TEMP = LIST[j]
                LIST[j] = LIST[j+1]
                LIST[j+1] = TEMP
        #print(LIST)
    return LIST

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        #print(NUMBERS)
        START = getTime()
        NUMBERS = bubbleSort(NUMBERS)
        END = getTime()
        #print(NUMBERS)
        TIMES.append(END-START)
        print(i)
    print(getAverage(TIMES))
