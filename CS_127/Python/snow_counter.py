#Saurav Hossain
#09/18/18
#A program that asks the user for the name of a png file and print the number of pixels that are nearly white 

import matplotlib.pyplot as plt
import numpy as np

img = plt.imread(input())
sc = 0

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if(img[i,j,0] > 0.75) and (img[i,j,1] > 0.75) and (img[i,j,2] > 0.75):
			sc = sc + 1

print("The snow count is", sc)