#Saurav Hossain 
#09/08/18 
#A program that asks the user for a list of nouns (separated by spaces) and approximates the fraction that are plural by counting the fraction that end in "s"

x = input()

y = x.split()
c = len(y)
d = 0

for i in y:
  if i[-1:] == "s":
    d = d + 1

print (c, d/c)