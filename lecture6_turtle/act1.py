import turtle
turtle.Screen().bgcolor("Orange")
sc=turtle.Screen()
sc.setup(500,500)
turtle.title("My First Turtle Program")
board=turtle.Turtle()
for i in range(4):
    board.forward(200)
    board.left(90)
    i += 1

turtle.done()