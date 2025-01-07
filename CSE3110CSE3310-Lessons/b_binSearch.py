# b_binSearch.py
'''
title: Binary Search
author: Jako Zeng
date: 2022-02-03
'''

import time, random, statistics

# --- FUNCTIONS --- #
def binarySearch(LIST, VALUE):
    """Perform a binary search fo VALUE on LIST

    Args:
        LIST (list): ordered intergers
        VALUE (int): value to be found

    Returns:
        LIST (list): Updated List
    """
    START = 0
    END = len(LIST) - 1 # Max index Number

    while START <= END:
        MIDPOINT = (START + END) // 2
        """print(LIST[MIDPOINT])"""
        if LIST[MIDPOINT] == VALUE:
            return
        elif VALUE > LIST[MIDPOINT]:
            START = MIDPOINT + 1
        else:
            END = MIDPOINT - 1 # Max index Number
    return

# --- MAIN PROGRAM CODE --- #


if __name__ == "__main__":
    # Make a large data set
    NUMBERS = []
    for i in range(200000):
        if random.randrange(2) == 1:
            NUMBERS.append(i)

    # TEST binary search

    TIMES = []

    for i in range(30):

        NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
        print(NUMBER)
        START_TIME = time.perf_counter()
        binarySearch(NUMBERS, NUMBER)
        END_TIME = time.perf_counter()
        TOTAL_TIME = END_TIME - START_TIME
        print(TOTAL_TIME)
        TIMES.append(TOTAL_TIME)
    print(statistics.mean(TIMES))
