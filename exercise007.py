"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from exercise003 import count_factors

primes = [2 , 3]
c = 10001
n = 2

while len(primes) < c:
    if count_factors(n) == 0:
        primes.append(n)
        print n
    n += 1

print "The primes list is: " + str(len(primes)) + " long"
print "The first prime is %d" % primes[0]
print "10,001 prime is: " + str(primes[-1])