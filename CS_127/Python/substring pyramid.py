#Saurav Hossain 
#09/04/18 
#Prints word pyramid

x = input() 
for i in range (len(x) - 1): 
	print (x[0:i]) 
for i in range (len(x)): 
	print (x[i:len(x)]) 
print ("Stuff")