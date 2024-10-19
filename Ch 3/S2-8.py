import turtle
window = turtle.Screen()
legolas = turtle.Turtle()
legolas.shape("turtle")
legolas.color("green")


for _ in range(18):
    legolas.forward(100)
    legolas.left(20)

window.mainloop()

#20 degrees