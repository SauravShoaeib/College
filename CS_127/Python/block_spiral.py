#Saurav Hossain
#08/29/18
'''
Write a program that implements the pseudocode below:

    For i = 10, 20, 30,... ,250:
        Walk forward i steps
        Turn left 90 degrees
'''

#Import turt and name
import turtle
t = turtle.Turtle()

#make it perrrrrrty
t.color("violetred2", "hotpink")
t.shape("turtle")

i = 0

while (i < 250): 
	t.forward(i)
	t.left(90)
	i = i + 10