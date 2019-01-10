#Saurav Hossain
#08/29/18
#Shades a shape blue

import turtle				#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
t = turtle.Turtle()		#Create a turtle
t.shape("turtle")		#Make it turtle shaped
t.backward(100)			#Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
     t.forward(10)		#Move forward
     t.pensize(i)		#Set the drawing size to be i (larger each time)
     t.color(0,0,i)		#Set the red channel to be i (brighter each time)
