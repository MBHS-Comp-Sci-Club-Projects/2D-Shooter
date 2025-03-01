import turtle


def inside_window(x, y):
  if ((x > 200 or x < -200) and (y > 200 or y < -200)):
    return False
  else:
    return True

class Bullet(turtle.Turtle):

  def __init__(self, color: str, x, y, direction: str):
    super().__init__()
    print("bullet Direction " + direction)
    self.shape("arrow")
    self.color(color)
    self.speed(0)
    self.penup()
    self.xcor = x
    self.ycor = y
    print("my pos is " + str(self.xcor) + " " + str(self.ycor))

    if (direction == "up"):
      self.setheading(90)
    elif (direction == "down"):
      self.setheading(270)
    elif (direction == "left"):
      self.setheading(180)
    elif (direction == "right"):
      self.setheading(0)

    while (inside_window(self.xcor, self.ycor)):
      self.forward(10)

  def shoot(self, direction):
    if direction == "up":
      self.setheading(90)
      while self.ycor() < 200:
        self.forward(10)
    elif direction == "down":
      self.setheading(270)
      while self.ycor() > -200:
        self.forward(10)
    elif direction == "left":
      self.setheading(180)
      while self.xcor() > -200:
        self.forward(10)
    elif direction == "right":
      self.setheading(0)
      while self.xcor() < 200:
        self.forward(10)
    else:
      print("ERROR: Invalid direction")



class Person(turtle.Turtle):

  def __init__(self, color : str, x, y):
    super().__init__()
    self.shape("circle")
    self.color(color)
    self.speed(0)
    self.playerColor = color

    #must add setpos to move the turtle to the correct position
    self.xcor = x
    self.ycor = y
    self.lives = 3
    self.penup()

  def move_up(self):
    self.setheading(90)
    self.forward(10)

  def move_down(self):
    self.setheading(270)
    self.forward(20)

  def move_left(self):
    self.setheading(180)
    self.forward(20)

  def move_right(self):
    self.setheading(0)
    self.forward(20)

  def lauch_bullet(self):
    Bullet(self.playerColor, self.xcor, self.ycor, "right") # must replace self.xcor with self.xcor()




def create_window(windowWidth: int, windowHeight: int, bgcolor: str):
  window = turtle.Screen()
  window.setup(windowWidth, windowHeight)
  window.bgcolor(bgcolor)
  return window


player1 = Person("red", -180, 100)
player2 = Person("blue", 180, 0)


def update():
  print("running in the update function")


window = create_window(1000, 1000, "white")

window.listen()
window.onkeypress(player1.move_up, "w")
window.onkeypress(player1.move_down, "s")
window.onkeypress(player1.move_left, "a")
window.onkeypress(player1.move_right, "d")
window.onkeypress(player1.lauch_bullet, "Return")

window.onkeypress(player2.move_up, "Up")
window.onkeypress(player2.move_down, "Down")
window.onkeypress(player2.move_left, "Left")
window.onkeypress(player2.move_right, "Right")
window.onkeypress(player2.lauch_bullet, "space")


window.mainloop()
