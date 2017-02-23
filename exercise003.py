"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

# This method doesn't work because lists of this size are frowny face, need to chunk the list into many chunks
# and then append each lists prime numbers to another list.

import math

n = 600851475143
primes = range(2,int(math.sqrt(n))+2)
c = 2
p = 0
x = 2

print "Starting loop"
while c < (n / 2):
    while p < n:
        p = c * x
        x += 1
        try:
            primes.remove(p)
        except ValueError:
            pass
    p = 0
    c += 1
    x = 2

primefactors = []

for y in primes:
    if (n % y) == 0:
        print "Found a prime factor! I found " + str(y) + " all by myself!\n"
        primefactors.append(y)

print "Prime factors are: " + str(primefactors)
print "\nLargest prime factor is: " + str(primefactors[-1])