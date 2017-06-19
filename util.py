"""Utility functions used in at least 2 exercises"""

import math

def count_factors(number):
    x = int(math.sqrt(number)) + 2
    factor_count = 0
    while x > 1:
        if (number % x) == 0:
            factor_count += 1
        x -= 1
    return factor_count

def is_prime(number):
    if number == 2:
        return True
    elif number == 3:
        return True
    elif number == 1:
        return False
    x = int(math.sqrt(number)) + 2
    if x > number:
        x = number
    n = 2
    while n < x:
        if (number % n) == 0:
            return False
        n += 1
    return True