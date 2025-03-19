import turtle


def inside_window(x, y):
  if ((x > 1000 or x < -1000) and (y > 1000 or y < -1000)):
    return False
  else:
    return True


class Bullet(turtle.Turtle):

  def __init__(self, color: str, x, y, direction: str):
    super().__init__()
    self.penup()
    self.goto(x, y)
    self.shape("arrow")
    self.color(color)
    self.speed(0)

    if (direction == "up"):
      self.setheading(90)
    elif (direction == "down"):
      self.setheading(270)
    elif (direction == "left"):
      self.setheading(180)
    elif (direction == "right"):
      self.setheading(0)
    (x, y) = self.pos()
    while (inside_window(x, y)):
      self.forward(10)

  def get_x(self):
    (x, y) = self.pos()
    return x

  def get_y(self):
    (x, y) = self.pos()
    return y

  def shoot(self, direction):
    (x, y) = self.pos()
    if direction == "up":
      self.setheading(90)
      while y < 200:
        self.forward(10)
    elif direction == "down":
      self.setheading(270)
      while y > -200:
        self.forward(10)
    elif direction == "left":
      self.setheading(180)
      while x > -200:
        self.forward(10)
    elif direction == "right":
      self.setheading(0)
      while x < 200:
        self.forward(10)
    else:
      print("ERROR: Invalid direction")

  def is_inside_window(self):
    (x, y) = self.pos()
    return inside_window(x, y)


class Person(turtle.Turtle):

  def __init__(self, color: str, x, y):
    super().__init__()
    self.penup()

    self.shape("circle")
    self.color(color)
    self.speed(0)
    self.playerColor = color
    self.bullets = []

    # must add setpos to move the turtle to the correct position
    self.setpos(x, y)
    self.lives = 3

  def get_x(self):
    (x, y) = self.pos()
    return x

  def get_y(self):
    (x, y) = self.pos()
    return y

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

  def is_touching(self, x, y):
    (x, y) = self.pos()
    heightMax = self.ycor() + 50
    widthMax = self.xcor() + 50
    heightMin = self.ycor() - 50
    widthMin = self.xcor() - 50
    if ((heightMax > x or x < heightMin) and (widthMax > y or y < widthMin)):
      self.lives -= 1
      return True
    else:
      return False

  def lauch_bullet(self):
    (x, y) = self.pos()
    print("x: + " + str(x) + ", y: " + str(y))
    self.bullets.append(Bullet(self.playerColor, x, y, "right"))


def update():
  if (player1.is_touching(player2.get_x(), player2.get_y())):
    player1.lives -= 1
    player2.lives -= 1
  if (player1.lives == 0):
    print("Player 2 wins!")
  elif (player2.lives == 0):
    print("Player 1 wins!")

  for bullet in player1.bullets:
    if not (bullet.is_inside_window()):
      player1.bullets.remove(bullet)

  for bullet in player2.bullets:
    if not (bullet.is_inside_window()):
      player1.bullets.remove(bullet)

  for bullet in player1.bullets:
    if player1.is_touching(bullet.get_x(), bullet.get_y()):
      player1.bullets.remove(bullet)
      player2.lives -= 1

  for bullet in player2.bullets:
    if player1.is_touching(bullet.get_x(), bullet.get_y()):
      player2.bullets.remove(bullet)
      player1.lives -= 1


def create_window(windowWidth: int, windowHeight: int, bgcolor: str):
  window = turtle.Screen()
  window.setup(windowWidth, windowHeight)
  window.bgcolor(bgcolor)
  return window


player1 = Person("red", -180, 100)
player2 = Person("blue", 180, 0)

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
