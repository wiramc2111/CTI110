# Chad Wiram
# 3/18/2026
# P4LAB1
# This program uses a for loop to create a triangle on top of a square to draw a house

import turtle

# Create a window to draw in
window = turtle.Screen()
window.bgcolor("gray") 

# Create turtle drawing option
asa = turtle.Turtle()
asa.shape("turtle")
asa.pensize(3)
asa.pencolor("red")

# Draw the square
for i in range(4):
    asa.forward(200)
    asa.right(90)
    
# Draw the triangle
for i in range(3):
    asa.forward(200)
    asa.left(120)
    

#Keep  window open
window.mainloop()
