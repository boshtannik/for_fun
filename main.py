#!/usr/bin/env python3
from math import sin
import time
import os

def get_sin(number, step, wide):
    return int(sin(number*step) * wide * 0.5 + wide * 0.5)

ITERS_COUNT = 5

iters = []
for i in range(1, ITERS_COUNT):
    iters.append(0.1 * i)

while True:
    time.sleep(0.1)
    i = time.time()
    try:
        for n in range(60):
            results = []
            for iterator in iters:
                ni = i + n
                results.append( get_sin(ni, iterator, 100))
            for width_cursor in range(max(results) + 1):
                if width_cursor in results:
                    print("#", end='')
                else:
                    print(" ", end='')
            print('\n')
    except KeyboardInterrupt:
        break

