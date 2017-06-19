"""In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?"""

import copy

input = """\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""


# tokenLine takes a block of string and returns a list in which each list item is a line from the text
def tokenLine(block):
    return block.split('\n')

# tokenNumbers takes a string of numbers separated by spaces and returns a list of those numbers
def tokenNumbers(line):
    return map(int, line.split(' '))


# Takes a list and returns the largest product of 4 adjacent values on that list
def biggestProducts(numbers):
    if type(numbers) == int:
        return 0
    elif len(numbers) < 4:
        return 0
    fourNumbers = []
    fourNumbers.append(numbers.pop())
    fourNumbers.append(numbers.pop())
    fourNumbers.append(numbers.pop())
    fourNumbers.append(numbers.pop())
    bigProduct = 0
    while len(numbers) > 0:
        product = 1
        for x in fourNumbers:
            product *= x
        if product > bigProduct:
            bigProduct = product
        fourNumbers.pop(0)
        fourNumbers.append(numbers.pop())
    return bigProduct

def hasDiagonalRightDownNeighbor(x, y, numbers):
    # Perform some bound checking based on x and y based on the size of each list
    if (x + 1) >= len(numbers):
        return False
    elif (y + 1) >= len(numbers[x]):
        return False
    return True

def hasDiagonalLeftDownNeighbor(x, y, numbers):
    # Perform some bound checking based on x and y based on the size of each list
    if (x + 1) >= len(numbers):
        return False
    elif y <= 0:
        return False
    return True

listInput = []

for i in tokenLine(input):
    listInput.append(tokenNumbers(i))

maxProduct = 0

print "Checking horizontal products"
# Check horizontal products
for n in listInput:
    p = biggestProducts(n)
    if p > maxProduct:
        maxProduct = p

print "Found the maxProduct is currently: " + str(maxProduct)

print "Reset list!"
listInput = []
for i in tokenLine(input):
    listInput.append(tokenNumbers(i))

print "Checking vertical products"
# Create lists with vertical slices
verticalSlices = []
for v in range(len(listInput)):
    verticalSlices.append([])

for v in range(len(listInput)):
    for x in range(len(listInput[0])):
        verticalSlices[v].append(listInput[x].pop())

for v in verticalSlices:
    verticalProduct = biggestProducts(v)
    if verticalProduct > maxProduct:
        maxProduct = verticalProduct

print "Found the maxProduct is currently: " + str(maxProduct)

print "Reset list!"
listInput = []
for i in tokenLine(input):
    listInput.append(tokenNumbers(i))

x1 = 0
y1 = 0

# Create lists of all the diagonal slices. We can get all diagonal slices with diagonal left down and diagonal left
# down.

# Create list with diagonal right down slices
diagonalRightSlices = []
for n in range(len(listInput)):
    diagonalRightSlice = []
    x = n
    y = 0
    while hasDiagonalRightDownNeighbor(x,y,listInput):
        diagonalRightSlice.append(listInput[x][y])
        x += 1
        y += 1
    diagonalRightSlice.append(listInput[x][y])
    diagonalRightSlices.append(diagonalRightSlice)

for n in range(len(listInput)):
    diagonalRightSlice = []
    x = 0
    y = n
    while hasDiagonalRightDownNeighbor(x,y,listInput):
        diagonalRightSlice.append(listInput[x][y])
        x += 1
        y += 1
    diagonalRightSlice.append(listInput[x][y])
    diagonalRightSlices.append(diagonalRightSlice)

# Create list with diagonal left down slices
diagonalLeftSlices = []
for n in range(len(listInput)):
    diagonalLeftSlice = []
    x = n
    y = len(listInput) - 1
    while hasDiagonalLeftDownNeighbor(x,y,listInput):
        diagonalLeftSlice.append(listInput[x][y])
        x += 1
        y -= 1
    diagonalLeftSlice.append(listInput[x][y])
    diagonalLeftSlices.append(diagonalLeftSlice)

for n in range(len(listInput)):
    diagonalLeftSlice = []
    x = 0
    y = n
    while hasDiagonalLeftDownNeighbor(x,y,listInput):
        diagonalLeftSlice.append(listInput[x][y])
        x += 1
        y -= 1
    diagonalLeftSlice.append(listInput[x][y])
    diagonalLeftSlices.append(diagonalLeftSlice)

# Find the largest product of the diagonal right slices
for dr in diagonalRightSlices:
    diagonalProduct = biggestProducts(dr)
    if diagonalProduct > maxProduct:
        maxProduct = diagonalProduct

# Find the largest product of the diagonal right slices
for dr in diagonalLeftSlices:
    diagonalProduct = biggestProducts(dr)
    if diagonalProduct > maxProduct:
        maxProduct = diagonalProduct

print "Max product is: " + str(maxProduct)