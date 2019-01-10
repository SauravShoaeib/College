#Saurav Hossain
#09/21/18
#A program that asks the user for the hour of the day (in 24 hour time), and prints a greeting 

z = input()
x = int(z)
if x < 12:
  print("Good Morning")
elif x >= 12 and x < 17:
  print("Good Afternoon")
else:
  print("Good Evening")