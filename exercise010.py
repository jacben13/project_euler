"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from exercise003 import count_factors

primes = [2 , 3]
c = 2000000
n = 2

while n < c:
    if count_factors(n) == 0:
        primes.append(n)
        # print n
    if (n % 100000) == 0:
        print n
    n += 1

sum = 0

for x in primes:
    sum += x

print "The primes list is: " + str(len(primes)) + " long"
print "The first prime is %d" % primes[0]
print "The last in the list of primes is: " + str(primes[-1])
print "The sum of the list of primes is %d" % (sum)