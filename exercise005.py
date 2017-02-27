"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def test_answer(p):
    for x in range(1,20):
        if (p % x) != 0:
            return False
    return True

n = 1

answer = False

while not answer:
    n += 1
    if n % 100000 == 0:
        print "\nAbout to test " + str(n)
    answer = test_answer(n)

print "Answer to problem 5 is: " + str(n)