
# assignment 14

# import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# get input filename from user
#inFile = input('Enter name of the input file: ')
inFile = 'csBridge.png'

# get output filename from user
#outFile = input('Enter name of the output file: ')
outFile = 'csBridge_wo_red.png'

# read in image from csBridge.png
img = plt.imread(inFile)

# load image into pyplot and show it until closed by user
plt.imshow(img)
plt.show()

# use pyplot to make copy of image and change its colors
img2 = img.copy()      # make a copy of our image
img2[::,::,0] = 0      # set the red channel to 0

# load copied image into pyplot and show it until closed by user
plt.imshow(img2)
plt.show()

# save the image we created to the file: reds.png
plt.imsave(outFile, img2)
