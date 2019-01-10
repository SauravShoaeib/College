#Saurav Hossain
#10/10/18
#A program that asks the user for a CSV of collision data  then lists the top three contributing factors for the primary vehichle of collisions 

import pandas as pd

x = input()         

r = pd.read_csv(x)     

print("Top three contributing factors for collisions:")
print(r["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])