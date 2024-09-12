import turtle 

background = input("What color do you want the background to be?\n")
turtle_color = input("What color do you want the pen to be?\n")

window = turtle.Screen()
window.bgcolor(background)
window.title("Hello, Alex!")

alex = turtle.Turtle()
alex.color(turtle_color)
alex.pensize(5)

alex.forward(120)
alex.left(90)
alex.forward(50)

window.mainloop()