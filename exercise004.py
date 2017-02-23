"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

x = 999
y = 999
p = 0

while x > 100:
    while y > 100:
        y -= 1
        test = str(x * y)
        if test == test[::-1] and (int(test) > p):
            p = int(test)
            break
    test = str(x * y)
    if (test == test[::-1]) and (int(test) > p):
        p = int(test)
    x -= 1
    y = x

print "Larget palindrone from multiplying 3 digit numbers is " + str(p)