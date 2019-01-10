#Saurav Hossain
#09/24/18
#Ask the user for the borough, an name for the output file, and then display the fraction of the population that has lived in that borough, over time.

#Taken from lab and modified     

import matplotlib.pyplot as plt
import pandas as pd

x = input()
y = input()


#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[x]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file: 
fig = plt.gcf()
fig.savefig(y)