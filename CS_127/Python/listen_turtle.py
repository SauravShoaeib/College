#Saurav Hossain 
#09/08/18 
#A program that asks the user for 5 whole (integer) numbers then turn the turtle left the degrees entered and then the turtle should move forward 100

#Import turt and name
import turtle
t = turtle.Turtle()
#make it perrrrrrty
#t.color("violetred2", "hotpink")
#t.shape("turtle")
#WHY WONT GRADESCOPE LET ME MAKE IT PRETTY, RETURNS IT AS WRONG WHEN THE TURTLE IS CUSTOMIZED (T~T)

nums = []

for i in range (5):	
	x = input("Put number here")
	nums.append(x)	


for items in nums:
	t.left(int(items))
	t.forward(100)

