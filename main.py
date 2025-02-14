import turtle


class Person(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.speed(0)
        self.color = color
        self.xcor = x
        self.ycor = y
        self.lives = 3
        self.penup()

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)

    def move_left(self):
        self.setheading(180)
        self.forward(20)

    def move_right(self):
        self.setheading(0)
        self.forward(20)


class Bullet(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("trianlge")
        self.color(color)
        self.speed(0)
        self.xcor = x
        self.ycor = y

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


def create_window(windowWidth: int, windowHeight: int, bgcolor: str):
    window = turtle.Screen()
    window.setup(windowWidth, windowHeight)
    window.bgcolor(bgcolor)
    return window


player1 = Person("red", -180, 0)
player2 = Person("blue", 180, 0)


def update():
    print("running in the update function")


window = create_window(1000, 1000, "white")

window.listen()
window.onkeypress(player1.move_up, "w")
window.onkeypress(player1.move_down, "s")
window.onkeypress(player1.move_left, "a")
window.onkeypress(player1.move_right, "d")

window.onkeypress(player2.move_up, "Up")
window.onkeypress(player2.move_down, "Down")
window.onkeypress(player2.move_left, "Left")
window.onkeypress(player2.move_right, "Right")

bullets = []


def shoot(player):
    if player.color == "red":
        bullet = Bullet("red", player.xcor(), player.ycor())
        bullets.append(bullet)


print(player1.shapesize())
window.mainloop()
