#Saurav Hossain
#08/27/18
#Draws a octogon, using turtle

#Importing turtle
import turtle

#Creating turtle
t = turtle.Turtle()

#make it perrrrrrty
t.color("violetred2", "hotpink")
t.shape("turtle")

#Makin octogon
for i in range(8):
    t.forward(150)   # moving forward
    t.left(45)       # turn 90
