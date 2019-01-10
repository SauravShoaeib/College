#Saurav Hossain
#09/21/18
#The program takes a string as input and uses that string to control what the turtle draws on the screen 

x = input()
#Importing turtle
import turtle
#Creating turtle
t = turtle.Turtle()
#make it perrrrrrty
#fucking not allowed to make it pretty ffss - t.color("violetred2", "hotpink")
t.shape("turtle")
for m in x:
  if(m == "F"):
    t.forward(50)
  elif(m == "L"):
    t.left(90)
  elif(m == "R"):
    t.right(90)
  elif(m == "^"):
    t.penup()
  elif(m == "v"):
    t.pendown()
  elif(m == "B"):
    t.backward(50)
  elif(m == "S"):
    t.stamp()
  elif(m == "l"):
    t.left(45)
  elif(m == "r"):
    t.right(45)
  elif(m == "p"):
    t.color("purple")