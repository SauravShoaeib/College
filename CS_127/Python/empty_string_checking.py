#Saurav Hossain
#09/21/18
#A program that asks the user to enter a string; if the user enters an empty string program prompts the user for a new string until they enter a non-empty string

x = (input('Enter something'))
while len(x) < 1:
    print('ENTER SOMETHING')
    x = (input())
print(x)