#!/usr/bin/env python3

"""
solution to parts C and D of problem 42 from Intro to Probability 2nd Ed
"""

import sys
import random
from math import pi, cos, sin

def bernoulli_points(test_condition):
    # track sum of bernoulli trials
    b_sum = 0
    for i in range(n):
        # create points between (0,0) and (1,1)
        x = random.random()
        y = random.random()

        if test_condition(x, y):
            b_sum += 1

    # average trials
    return b_sum/n

def part_c(r, n):
    # place circle flush to point (0,0) on unit square
    center = (r, r)

    # trial succeeds if
    # distance between random point and circle center is less than radius
    def condition(x, y):
        return ((abs(x - center[0])**2 + abs(y - center[1])**2)**(0.5) < r)
    return bernoulli_points(condition)

def part_d(n):
    # trial succeeds if
    # coordinates satisfy condition given by part d
    def condition(x, y):
        val = cos(pi*x) + sin(pi*y)
        return (val >= 0 and val <= 1)
    return bernoulli_points(condition)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('(using default radius 0.5 and 10000 trials)\n')
        r = 0.5
        n = 10000
    else:
        # first two arguments given to program are radius and number of trials
        r = float(sys.argv[1])
        if r < 0 or r > 1:
            raise ValueError('Radius must fall within range [0, 1].')
        n = int(sys.argv[2])
        if n < 1:
            raise ValueError('Must perform at least one trial.')

    # PART C #
    area = part_c(r, n)
    # algebraically calculate pi based on formula for area of a circle
    calculated_pi = area / r**2

    # PART D #
    d_area = part_d(n)

    # display part c
    print('Radius: ' + str(r) + '\t' + 'Trials: ' + str(n))
    print('Estimated area of circle: ' + str(area))
    print('Estimated value of pi: ' + str(calculated_pi))
    print('Actual value of pi: ' + str(pi) + '\n')

    # display part d
    print('Trials: ' + str(n))
    print('Estimated area described in part (d): ' + str(d_area))
