"""The sum of the squares of the first ten natural numbers is,

385
The square of the sum of the first ten natural numbers is,

3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

n = 100

sum_counting = 0
sum_squares = 0

for x in range(1, n + 1):
    sum_counting += x
    sum_squares += x ** 2

sum_counting **= 2

print "The difference is: " + str(sum_counting - sum_squares)