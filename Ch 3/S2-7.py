import turtle
window = turtle.Screen()
legolas = turtle.Turtle()

angles = [160, -43, 270, -97, -43, 200, -940, 17]

for i in angles:
    legolas.left(i)
    legolas.forward(100)

final_heading = sum(angles)%360
print("The pirate's heading is: ", final_heading)


window.mainloop()
