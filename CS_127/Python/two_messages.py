#Saurav Hossain
#09/04/18
#A program that asks the user for a message and then prints the message out, two copies of each character per line.

x = input()

for i in range(len(x)):
  print(x[i:i+1] + " " + x[i:i+1]) 