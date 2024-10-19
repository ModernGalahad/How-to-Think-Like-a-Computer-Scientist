#Draws a five-pointed star
import turtle
window = turtle.Screen()
legolas = turtle.Turtle() 
legolas.color("red")

for _ in range(5):
    legolas.right(144)
    legolas.forward(100)

window.mainloop()