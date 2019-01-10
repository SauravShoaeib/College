#Saurav Hossain
#09/21/18
#A program that prompts the user to enter a list of names; Each person's name is separated from the next by a semi-colon and a space ('; ') and the names are entered lastName, firstName 

y = input()
f = str(y)
x = f.split(";")

for i in x:
  c = str(i)
  z = c.split(",")
  for i in range(1):
    print(z[1] + z[0])