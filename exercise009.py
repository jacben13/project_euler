"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

n = 1000

def sum_of_squares(a,b):
    return a ** 2 + b ** 2

def check_answer(a,b):
    c_squared = sum_of_squares(a,b)
    c = c_squared ** 0.5
    if float(c - int(c_squared ** 0.5)) == 0:
        print "Found a triplet with %d, %d, %d" % (a,b,c)
        if (a + b + c) == n:
            return True
    return False

def main():
    for a in range(1,n):
        # print "Outer loop %d" % (a)
        for b in range(1,n):
            if check_answer(a,b):
                c = sum_of_squares(a,b) ** 0.5
                product = long(a * b * c)
                print "Found the triplet at %d, %d, %d" % (a, b, c)
                print "Product is %d" % (product)
                return 1
            b += 1
        a += 1

if __name__ == "__main__":
    main()