"""
Monte Carlo simulation for calculating pi.

Author: Ross <ross dot warren at pm dot me>
"""


import random
import math

def circleHit(x, y):
    '''Takes random x, y and checks if it falls in a unit circle.'''
    if (x**2 + y**2) <= 1:
        return True
    else:
        return False
    
# MC sim
def main():
    circle = 0
    sq = 0
    iterations = 100000
    
    for i in range(0, iterations):
        x = random.random()
        y = random.random()
        if circleHit(x, y) is True:
            circle = circle + 1
        sq = sq + 1
    
    pi = 4 * (circle / sq)
    
    print("MC pi \t : ", pi)
    print("Diff \t : ", (pi - math.pi)/math.pi * 100, " %")
    
main()

    