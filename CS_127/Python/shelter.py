#Saurav Hossain
#09/21/18
'''
Displays shelter population over time to:
-ask the user to specify the input file,
-ask the user to specify the output file,
-make a plot of the fraction of the total population that are children over time from the data in input file, and
-store the plot in the output file the user specified.
'''

import matplotlib.pyplot as plt
import pandas as pd

x = input()
y = input()

fcg = pd.read_csv(x)
fcg['Fraction Children'] = fcg['Total Children in Shelter']/fcg['Total Individuals in Shelter']
fcg.plot(x = 'Date of Census', y = 'Fraction Children')
fig = plt.gcf()
fig.savefig(y)