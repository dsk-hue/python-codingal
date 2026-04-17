import turtle
def second_triangle(r, f):
    board.right(r)
    board.forward(f)
turtle.Screen().bgcolor("Orange")
board=turtle.Turtle()
board.forward(100)
for i in range(2):
    board.left(120)
    board.forward(100)
    i += 1
board.penup()
second_triangle(150, 50)
board.pendown()
second_triangle(90, 100)
for i in range(2):
    second_triangle(120, 100)
    i += 1
turtle.done()