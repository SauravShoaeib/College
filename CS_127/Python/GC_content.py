#Saurav Hossain
#08/29/18
#A program that prompts the user for a DNA string, and then prints the length and GC-content (percent of the string that is C or G, written as a decimal).

z = input()

c = 0

for i in range(len(z)):
 if(z[i] == "G" or z[i] == "C"):
 	c = c + 1 
print (len(z))
print (c / len(z))