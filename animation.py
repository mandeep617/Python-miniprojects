import turtle
turtle.bgcolor("cyan")
turtle.pensize(1.6)
turtle.speed(0.25)
color = ["magenta", "red", "purple", "orange", "lightgreen", "yellow", "blue"]
for i in range(11):
    for j in color:
        turtle.color(j)
        turtle.circle(150)    #turtle.circle(150, steps = 5)
        turtle.left(12)
turtle.mainloop()
