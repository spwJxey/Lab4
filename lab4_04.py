import turtle 
t = turtle.Turtle()


def position_turtle(x, y):
  """
  possitions the start possition of the turtle to (x, y)
  """
  t.hideturtle()
  t.penup()
  t.goto(x, y)
  t.showturtle()
  t.pendown()
  

def stair_down(x, s):
  """
  draws 's' amount of decending stairs with the length x
  """
  for i in range(s):
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)

position_turtle(-100, 100)
stair_down(50, 2)