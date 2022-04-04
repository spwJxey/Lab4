import turtle 
t = turtle.Turtle()
t.pencolor("purple")

def square(x):
  """
  this will draw a square x by x
  """
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  t.forward(x)

def t_letter():
  """
  this will draw the letter T 
  """
  t.left(180)
  t.forward(90)
  t.right(90)
  t.forward(1)
  t.pencolor("white")
  t.forward(9)
  t.pencolor("purple")
  t.forward(40)
  t.right(90)
  t.forward(80)
  t.left(180)
  t.forward(80)
  t.right(90)
  t.forward(40)

square(100)
t_letter()
  
