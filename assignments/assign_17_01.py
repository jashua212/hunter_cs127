
# assignment 17

import matplotlib.pyplot as plt
import numpy as np

outFile = input('Enter output file name: ')

# create all BLACK img of 30 by 30 pixels
img = np.zeros( (30, 30, 3) )

# change img to be all yellow (red + green)
img[:, :, 0:2] = 1       # [height, width, rgb layers]

# create blue bar
img[5:8, 5:25, 0:2] = 0  # set red && green layers to 0
img[5:8, 5:25, 2] = 1    # set blue layer to 1

# create green bar
img[8:25, 13:16, 0] = 0  # set red layer to 0

# load img into pyplot and show it until closed by user
plt.imshow(img)
plt.show()

# save image we created as the file entered by user
plt.imsave(outFile, img)
