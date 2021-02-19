#!/usr/bin/env python3
from math import sin
import time
import os

def get_sin(number, step, wide):
    return int(sin(number*step) * wide * 0.5 + wide * 0.5)

ITERS_COUNT = 6
NUM_WAWES = 3
SCREEN_HEIGHT = 80
SCREEN_WIDTH = 120

SINGLE_STEP = 13

iters = []
for i in range(1, ITERS_COUNT):
    iters.append(0.1 * i)

screen = [ [x for x in range(SCREEN_WIDTH)] for y in range(SCREEN_HEIGHT) ]

def draw_screen(x, y):
    global screen
    if x > SCREEN_WIDTH or y > SCREEN_HEIGHT: return
    screen[x][y] = 1

def clear_screen():
    global screen
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            screen[y][x] = 0

def print_screen():
    global screen
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            if screen[y][x] == 1:
                print("#", end='')
            else:
                print(' ', end='')
        print(end='\n')

def make_iteration(got_shift):
    for y in range(SCREEN_HEIGHT):
        results = []
        for iterator in iters:
            ni = y + got_shift
            results.append( get_sin(ni, iterator, SINGLE_STEP))

        draw_screen(y, sum(results))

i = 0
while True:
    time.sleep(0.05)
    try:
        i+=0.1
        clear_screen();
        for n in range(1, NUM_WAWES + 1):
            make_iteration(i * n * 1.618)
        print_screen()

    except KeyboardInterrupt:
        break

