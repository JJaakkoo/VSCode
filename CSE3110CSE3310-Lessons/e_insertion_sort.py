# e _insertion_sort.py
'''
title: insertion sort
author: jako zeng
date-created: 2022-02-08
'''

from z_my_functions import *

def insertionSort(LIST):
    """Splits the list into a sorted and unsorted section and then takes the left-most value from the unsorted section and inserts it into the sorted section

    Args:
        LIST (list): list of integer
    """
    for i in range(1, len(LIST)):
        
        INDEX_VALUE = LIST[i] # current value to be inserted.
        
        SORTED_INDEX = i - 1

        # Traverse through the sorted section of the list
        while SORTED_INDEX >= 0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            # Move sorted values up one (to make space)
            LIST[SORTED_INDEX + 1] = LIST[SORTED_INDEX]
            SORTED_INDEX -= 1 
        # place value in the space created above
        LIST[SORTED_INDEX + 1] = INDEX_VALUE
        # NOTE: The + 1 adjusts for the -1 that occurs at the end fo the while loop.
        #print(LIST)

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        insertionSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))
