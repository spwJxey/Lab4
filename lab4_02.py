import turtle 
t = turtle.Turtle()

def stair_down(x):
  #1 stair
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  #2 stair
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  #3 stair
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  #4 stair
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)

stair_down(50)