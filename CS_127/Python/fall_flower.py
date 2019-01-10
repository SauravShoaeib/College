#Saurav Hossain
#08/28/18
'''
A program that implements the pseudocode
    Repeat 36 times:
        Walk forward 100 steps
        Turn left 145 degrees
        Walk forward 10 steps
        Turn right 90 degrees
        Walk forward 10 steps
        Turn left 135 degrees
        Walk forward 100 steps
'''

#Import turt and name
import turtle
t = turtle.Turtle()

#make it perrrrrrty
t.color("violetred2", "hotpink")
t.shape("turtle")


#Repeat 4 times:
for i in range(36):
  t.forward(100) 
  t.left(145)
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.left(135)
  t.forward(100)