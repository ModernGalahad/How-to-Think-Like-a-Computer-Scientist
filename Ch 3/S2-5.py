import turtle
window = turtle.Screen()
legolas = turtle.Turtle()



#Triangle
for _ in range(3):
    legolas.forward(100)
    legolas.left(120)


#Square
for _ in range(4):
    legolas.forward(100)
    legolas.left(90)

#Hexagon
for _ in range(6):
    legolas.forward(100)
    legolas.left(60)

#Octagon
for _ in range(8):
    legolas.forward(100)
    legolas.left(45)

window.mainloop()