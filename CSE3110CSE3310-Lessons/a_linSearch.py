# a_linSerach.py
'''
title: Linear Search
author: Jako Zeng
date-created: 2022-02-02
'''

import time, random, statistics

# Make a large data set
NUMBERS = []
START_TIME = time.perf_counter()
for i in range(200000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)
END_TIME = time.perf_counter()
TOTAL_TIME = END_TIME - START_TIME
print(len(NUMBERS), TOTAL_TIME)

TIMES = []

for i in range(30):
    # Choose a number in the list
    NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
    print(NUMBER)

    # Linear Search
    START_TIME = time.perf_counter()
    for i in range(len(NUMBERS)):
        if NUMBERS[i] == NUMBER:
            break
    END_TIME = time.perf_counter()
    TOTAL_TIME = END_TIME - START_TIME
    print(TOTAL_TIME)

print(statistics.mean(TIMES))