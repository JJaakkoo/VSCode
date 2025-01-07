# j_heap_sort.py

'''
title: heap sort
author: jako zeng
date-created: 2022-02-14
'''

from z_my_functions import *

def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    """move highest value to index 0 (top of the binary tree)

    Args:
        LIST (list): unsorted values
        LEN_ARRAY (int): length of the unsorted values in the array
        ROOT_INDEX (int): (smallest number) starting highest index in the unsorted part of the array
    """

    LARGEST_INDEX = ROOT_INDEX
    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # check if left child is greater than the parent
    if LEFT_INDEX > LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    # check if the right child is greater than the parent
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX
    

    # Change the root/parent if needed

    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX] 
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        heapify(LIST, LEN_ARRAY, ROOT_INDEX)

# The main function to sort an array

def heapSort(LIST):

    LEN_ARRAY = len(LIST)

    # build a max heap
    for i in range(LEN_ARRAY, -1, -1):
        heapify(LIST, LEN_ARRAY, 1)
        # extract highest value
    
    for i in range(LEN_ARRAY-1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i] # swaps vairables
        heapify(LIST, 1, 0)


if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        heapSort(NUMBERS)
        END = getTime()
        TIMES.append(END-START)
        print(i)
    print(getAverage(TIMES))



