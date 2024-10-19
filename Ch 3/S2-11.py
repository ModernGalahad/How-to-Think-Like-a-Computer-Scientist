import turtle
window = turtle.Screen()
legolas = turtle.Turtle()
legolas.shape("turtle")

legolas.color("red")
legolas.stamp()

legolas.color("green")

for _ in range(12):
    legolas.left(30)
    legolas.penup()
    legolas.forward(80)
    legolas.pendown()
    legolas.forward(10)
    legolas.penup()
    legolas.forward(10)
    legolas.stamp()
    legolas.backward(100)
    
window.mainloop()