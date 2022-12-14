
# assignment 9

# get input string from user
inputString = input('Enter an all-small-letter string: ').lower()

# get integer from user
integer = int(input('Enter a non-negative integer to shift: '))

# set constants
ASCII_OFFSET = 96
NUM_OF_LETTERS = 26

# create output string
cipher = ''
for char in inputString:

    net = ord(char) - 96
    print('net:', net)

    #breakpoint()

    netPlus = net + integer
    print('netPlus:', netPlus)

    remainder = netPlus % 26
    print('remainder:', remainder)

    if remainder == 0:
        remainder = 26
    print('post-if remainder:', remainder)

    fullNetPlus = remainder + 96
    print('fullNetPlus:', fullNetPlus)

    shiftedChar = chr(fullNetPlus)
    cipher = cipher + shiftedChar

# print output string
print('ciphered string:', cipher)
