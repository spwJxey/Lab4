import turtle 
t = turtle.Turtle()

def square():
  """
  this will draw a square 100*100
  """
  t.pencolor("purple")
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)

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

square()
t_letter()
  
