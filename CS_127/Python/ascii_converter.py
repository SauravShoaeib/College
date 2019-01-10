#Saurav Hossain
#08/29/18
#Prints inserted messages in ASCII

print("WRITE SOEMTHING DUDE")
z = input()

for i in range(len(z)):
  print(ord(z[i:i+1])) #ord converts ascii to num vals of characters
