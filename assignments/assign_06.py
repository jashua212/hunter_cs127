
# assignment 6

## USING 3 METHODS


# method 1: using a for-loop
def printNumberSequenceForLoop(n):

    # range function effectively generates a LIST of the INDICES
    myRange = range(n)

    for i in myRange:
        print(n)             # printing n, instead of i
        n = n - 1

    print('WOW')

# here, myRange = [0,1,2,3,4,5,6,7,8,9,10,11] -- excl 12 !!
printNumberSequenceForLoop(12)


# method 2: using a while-loop
def printNumberSequenceWhileLoop(n):
    while n >= 1:
        print(n)            # printing n, instead of i
        n = n - 1

    print('WOW')

#printNumberSequenceWhileLoop(12)


# method 3: using a REVERSED RANGE in a for-loop
def printReverseRange(n):
    rng = range(n, 0, -1)

# here, rng = [12,11,10,9,8,7,6,5,4,3,2,1] -- incl 12 !!

    for i in rng:
        print(i)

    print('WOW')

#printReverseRange(12)
