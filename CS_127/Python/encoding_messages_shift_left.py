#Saurav Hossain
#08/29/18
#Prints coded messages shift left

z = input("put code here")
m = 1
fin = ""

for i in range(len(z)):
  q = (ord(z[i:i+1]))
  if q == 97:
    a = 122
  elif q == 122:
    a = 97
  else:
    a = (q - m)
  str = chr(a)
  fin = fin + str
print(fin)