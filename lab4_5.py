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
  

def stair_down(h, v, s):
  """
  draws 's' amount of decending stairs with lengths horozontal = h and vertical = v
  """
  for i in range(s):
    t.forward(h)
    t.right(90)
    t.forward(v)
    t.left(90)

position_turtle(-100, 100)
stair_down(10, 50, 5)