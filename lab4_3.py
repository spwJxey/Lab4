import turtle 
t = turtle.Turtle()


def position_turtle(x, y):
  t.hideturtle()
  t.penup()
  t.goto(x, y)
  t.showturtle()
  t.pendown()
  

def stair_down(x):
  for i in range(4):
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)

position_turtle(-100, 100)
stair_down(50)