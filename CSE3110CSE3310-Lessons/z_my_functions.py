# z_my_functions.py
'''
title: common functions for testing
author: Jako Zeng
date-created: 2022-02-04
'''

import random, statistics, time

def getList(SIZE):
    """return a SORTED list of approximately size Size

    Args:
        SIZE (int): 

    Returns:
        list: 
    """
    NUMBERS = []
    for i in range(SIZE * 2):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS

def getRandomList(SIZE):
    """return a RANDOMIZED list of approximately size SIZE

    Args:
        SIZE (int): 

    Returns:
        list: 
    """
    ORDERED_LIST = getList(SIZE)
    NUMBERS = []
    for i in range(len(ORDERED_LIST)):
        NUMBERS.append(ORDERED_LIST.pop(random.randrange(len(ORDERED_LIST))))
    return NUMBERS

def getAverage(LIST):
    """Averages alll values in the list

    Args:
        LIST (list): containing integers

    Returns:
        float: average
    """
    return statistics.mean(LIST)

def getTime():
    """returns the performance time

    Returns:
        float: 
    """
    return time.perf_counter()

if __name__ == "__main__":
    A_LIST = getRandomList(10)
    print(A_LIST)
    TIME = getTime()
    print(TIME)
    AVERAGE = getAverage([3,4,5])
    print(AVERAGE)