
# assignment 17

# import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# get output filename from user
#outFile = input('Enter output file name: ')
outFile = 'shape_t.png'

# create yellow img, where yellow = red + green
img = np.zeros( (30, 30, 3) )
img[:, :, 0:2] = 1

blueVertical = range(5, 8)
blueHorizontal = range(5, 25)
for y in blueVertical:
	for x in blueHorizontal:
		img[y, x, 0:2] = 0      # set red and green channels to 0
		img[y, x, 2] = 1        # set blue channel to 1

greenVertical = range(8, 25)
greenHorizontal = range(13, 16)
for y in greenVertical:
	for x in greenHorizontal:
		img[y, x, 0] = 0        # set red channel to 0

# load img into pyplot and show it until closed by user
plt.imshow(img)
plt.show()

# save image we created as the file entered by user
plt.imsave(outFile, img)
