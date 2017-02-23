"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

# Initial approach was to find all prime numbers up to n and then attempt to factor n with each number, but that was
# waaay too inefficient.
import math

def count_factors(number):
    x = int(math.sqrt(number)) + 2
    factor_count = 0
    while x > 1:
        if (number % x) == 0:
            factor_count += 1
        x -= 1
    return factor_count

n = 600851475143
factors = []
x = int(math.sqrt(n)) + 2

while x > 1:
    if (n % x) == 0:
        print "Found a factor! I found " + str(x) + " all by myself!\n"
        factors.append(x)
    x -= 1

primefactors = []
biggestprime = 0

for f in factors:
    if count_factors(f) == 0 and f > biggestprime:
        biggestprime = f

print "Drum roll.... The biggest prime factor of " + str(n) + " is : " + str(biggestprime)
