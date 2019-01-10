#Saurav Hossain
#09/21/18
#Make a turtle walk 100 times; Each "walk" is 10 steps forward and the turtle can turn 0,1,2,...,359 degrees (chosen randomly) at the beginning of each walk

import turtle
import random

t = turtle.Turtle()
t.speed(10)

for i in range(100):
  t.forward(10)
  a = random.randrange(360)
  t.right(a)