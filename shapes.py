import turtle 
t = turtle.Turtle()

def draw_square(color):
  """
  Draws square 20*20, pencolor set so white squares are visible when fill 'color'
  """
  t.color(color)
  t.pencolor("black")
  t.begin_fill()
  for i in range(4):
    t.forward(20)
    t.right(90)
  t.end_fill()

def position_turtle(x, y):
  """
  possitions the start possition of the turtle to (x, y)
  """
  t.hideturtle()
  t.penup()
  t.goto(x, y)
  t.showturtle()
  t.pendown()
 
def draw_row_type_1(x, y):
  """
  draws row type one of checkerboard starting with black
  """
  for i in range (4):
    x = x + 20
    position_turtle(x, y)
    draw_square("black")
    x = x + 20
    position_turtle(x, y)
    draw_square("white")

def draw_row_type_2(x, y):
  """
  draws row type two of checkerboard starting with white 
  """
  for i in range (4):
    x = x + 20
    position_turtle(x, y)
    draw_square("white")
    x = x + 20
    position_turtle(x, y)
    draw_square("black")

def board(x, y):
  """
  draws whole board relative to position of (x, y)
  """
  for i in range(4):
    draw_row_type_1(x, y)
    y = y - 20
    draw_row_type_2(x, y)
    y = y - 20


  
  