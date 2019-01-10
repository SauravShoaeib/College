#Saurav Hossain
#09/21/18
#A program that computes the average and maximum population over time for a borough (entered by the user)

import matplotlib.pyplot as plt
import pandas as pd

x = input()

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print("Average Population", pop[x].mean())
print("Max Population", pop[x].max())
