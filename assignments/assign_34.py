
# assignment 34

# since manipulating an image, which is a 3-dimensional array,
# import numpy instead of pandas:
import numpy as np

# import library for processing images:
import matplotlib.pyplot as plt

# get user inputs:
print('Enter 1 to get upper right corner')
print('Enter 2 to get middle portion')
choice = input('Your choice: ')
inFile = input('Enter input file name: ')
outFile = input('Enter output file name: ')

# for testing only - set user inputs (overwriting above):
choice = '2'
inFile = 'magic_logo.png'
outFile = 'magic_logo_middle.png'

# use matplotlib to read image file and to store it as 'img':
img = plt.imread(inFile)

# get img's dimensions (in pixels):
height = img.shape[0]
width = img.shape[1]
print('pixels:', width, 'by', height)  # for debugging only

# crop per user's choices and save cropped image as 'img2':
if choice == '1':
	# create new img2 by grouping all the shape's pixels into a
	# 2 by 2 grid, and slicing out the upper right corner:
	img2 = img[:height//2, width//2:]

elif choice == '2':
	# create new img2 by grouping all the shape's pixels into a
	# 4 by 4 grid, and slicing out the middle portion:
	quarterHeight = height//4
	quarterWidth = width//4
	img2 = img[quarterHeight:quarterHeight*3, quarterWidth:quarterWidth*3]

else:
	print('wrong choice')
	quit()

# load img2 into matplotlib and show it:
plt.imshow(img2)
plt.show()

# save img2:
plt.imsave(outFile, img2)
