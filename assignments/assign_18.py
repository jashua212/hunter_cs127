
# assignment 18

# import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# get size from user
# size = input('Enter the size: ')
size = '50'
integer = int(size)

# get output filename from user
#outFile = input('Enter output file name: ')
outFile = 'stripes10.png'

# create black img
img = np.zeros((integer, integer, 3))

# create alternating stripes
# remm: slicing is from and including, and to but EXCLUDING
img[:, 0::2, 1:2] = 1      # set green channel to 1
img[:, 1::2, 2:3] = 1      # set blue channel to 1

# test
# img = np.zeros( (8,8,3) )
# img[::2, 1::2, 0] = 1

# load img into pyplot and show it until closed by user
plt.imshow(img)
plt.show()

# save image we created as the file entered by user
plt.imsave(outFile, img)
