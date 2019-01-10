#Saurav Hossain 
#09/08/18 
#Flood Map

import numpy as np
import matplotlib.pyplot as plt

#Taken from the lab
#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0: 
            #Below sea level
           floodMap[row,col,2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <= 6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%
     
#Save the image:
plt.imsave('floodMap.png', floodMap)


#addition
for row in range(mapShape[0]):
	for col in range(mapShape[1]):
		if elevations[row, col] <= 20 and elevations[row, col] > 6:
			floodMap[row,col,0] = 0.5
			floodMap[row,col,1] = 0.5
			floodMap[row,col,2] = 0.5

plt.imsave('floodMap.png', floodMap)