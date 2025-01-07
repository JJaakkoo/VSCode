# h_merge_sort.py
'''
title: merge sort
author: jako zeng
date-created: 2022-02-10
'''

from z_my_functions import *

def mergeSort(LIST):
    """Recursive split of the list

    Args:
        LIST (list): unsorted numbers
    """
    # base case
    if len(LIST) <= 1:
        return LIST
    else:
        # recursive case
        MIDPOINT = len(LIST) // 2
        LEFT = LIST[:MIDPOINT]
        RIGHT = LIST[MIDPOINT:]
        return mergeSortedLists(mergeSort(LEFT), mergeSort(RIGHT))

def mergeSortedLists(LIST_LEFT, LIST_RIGHT):
    """merge 2 sorted lists together

    Args:
        LIST_LEFT (list): sorted numbers
        LIST_RIGHT (list): sorted numbers
    """

    # Special case: one or both of the lists are empty
    # i.e LEFT = [1, 5, 7, 20] RIGHT = [3, 9, 44, 50, 60]
    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    # General Cases 
    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGED = [] # build the list to return
    LIST_LEN_TOTAL = (len(LIST_LEFT) + len(LIST_RIGHT))
    while len(LIST_MERGED) < LIST_LEN_TOTAL:
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]:
            # If the value on the left is smaller or equal to the value of the right list.
            LIST_MERGED.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT += 1
        else: 
            LIST_MERGED.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT += 1

        # if we are at the end of one of the lists, we can take a shortcut
        if INDEX_RIGHT == len(LIST_RIGHT):
            # reached the end of the right list
            # append the remainder of the left list and break
            LIST_MERGED = LIST_MERGED + LIST_LEFT[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LIST_LEFT):
            LIST_MERGED = LIST_MERGED + LIST_RIGHT[INDEX_RIGHT:]
            break
    return LIST_MERGED

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        NUMBERS = mergeSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))