
# assignment 21

# import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# get image's file name and threshold from user:
#fileName = input('Enter file name: ')
fileName = 'caDrought2014.png'
t = float(input('Enter threshold: '))

# read in image from file name provided by user:
ca = plt.imread(fileName)

# initiate counts:
#countTotal = 0   # total number of pixels
countSnow = 0     # number of pixels that are almost white

# for every pixel:
for i in range(ca.shape[0]):
	for j in range(ca.shape[1]):
		# add 1 to countTotal:
		#countTotal = countTotal + 1

		# check if red, green, and blue are > t:
		if (ca[i, j, 0] > t) and (ca[i, j, 1] > t) and (ca[i, j, 2] > t):
			countSnow = countSnow + 1

# calculate percentage:
countTotal = ca.shape[0] * ca.shape[1]
percent = round((countSnow / countTotal * 100), 2)

# print results to user:
print('number of white pixels:', countSnow)
print('percent of white pixels:', percent, '%')
#print('test:', countSnow)
