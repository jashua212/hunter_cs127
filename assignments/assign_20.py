
# assignment 20

# import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

# load the array into matplotlib.pyplot:
plt.imshow(elevations)

# display the original plot:
#plt.show()


# take the shape (dimensions) of the elevations
# and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

print('mapShape[0]:', mapShape[0])
print('mapShape[1]:', mapShape[1])


# create a new blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
	for col in range(mapShape[1]):

        ## elevations[row, col] returns a VALUE stored at POSITION [row, col]
        ## this is just like how array[1] returns a value stored at index 1 !!!

        ## here, we've stored another placeholder (i.e., the 3 color channels) at
        ## that same position [row, col]

		if elevations[row, col] <= 0:
			# below sea level
			floodMap[row, col, 2] = 1.0     # set blue channel to 100%

		elif elevations[row, col] <= 6:
			# below 6 foot storm surge (flooding likely)
			floodMap[row, col, 0:2] = 1.0   # set red & green channels to 100%

		elif elevations[row, col] <= 20:
			# above 6 foot storm surge (flooding is less likely but possible)
			floodMap[row, col, 0:3] = .5    # set all channels to 50%

		else:
			# >20 ft - thus well above 6 foot storm surge and did not flood
			floodMap[row, col, 1] = 1.0     # set green channel to 100%

# load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

# display the plot:
plt.show()

# save image:
plt.imsave('floodMap.png', floodMap)
